__author__ = 'mariosky'
__author__ = 'mariosky'
import redis

HOST = "96.126.96.132"
PORT = 6379
APP_NAME = 'cola'
WORKER_HEARTBEAT_INTERVAL = 10 #Time a worker waits for a Task before unblocking to send a heartbeat


r = redis.Redis(host=HOST, port=PORT)


class Task:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.method = kwargs.get('method', None)
        self.params = kwargs.get('params', {})
        self.state = kwargs.get('state', 'created')
        self.expire = kwargs.get('expire', None)
        self.result = None
        self.__dict__.update(kwargs)

    def enqueue(self, app_name):
        pipe = r.pipeline()
        if pipe.rpush('%s:task_queue' % app_name, self.id):
            self.state = 'submitted'
            pipe.set(self.id, self.__dict__)
            pipe.execute()
            return True
        else:
            return False

    def put_result(self, worker):
        pipe = r.pipeline()
        if pipe.zrem('%s:pending_set' % worker.cola.app_name, '%s:%s' % (worker.id, self.id)):
            self.state = 'completed'
            pipe.set(self.id, self.__dict__)
            pipe.sadd('%s:result_set' % worker.cola.app_name, self.id)
            pipe.execute()
            return True
        else:
            return None

    def get_result(self, app_name, as_dict = False):
        if r.sismember('%s:result_set' % app_name, self.id):
            _dict = eval(r.get(self.id))
            self.__dict__.update(_dict)
            if as_dict:
                return self.__dict__
            else:
                return self
        else:
            return None

    def __repr__(self):
        return self.id +" method:"+ str(self.method) +", params:" + str(self.params)

    def as_dict(self):
        return self.__dict__


class Cola:
    def __init__(self, name = APP_NAME):
        self.app_name = name
        self.task_counter = self.app_name+':task_counter'
        self.pending_set = self.app_name+':pending_set'
        self.task_queue = self.app_name+':task_queue'
        self.result_set = self.app_name+':result_set'
        self.worker_set = self.app_name+':worker_set'


    def initialize(self):
        r.flushall()
        r.setnx(self.task_counter,0)

    def enqueue(self, **kwargs ):
        if kwargs['id'] is None:
            kwargs['id'] = "%s:task:%s" % (self.app_name, r.incr(self.task_counter))
        t = Task(**kwargs)
        t.enqueue(self.app_name)
        return kwargs['id']

    def get_dead_workers(self):
        workers = r.smembers(self.worker_set)
        dead = []
        for w in workers:
            if r.get(w):
                pass
            else:
                r.srem(self.worker_set,w)
                dead.append(w)
        return dead



class Worker:
    def __init__(self, worker_id, cola):
        self.cola = cola
        self.id = '%s:worker:%s' % (cola.app_name, worker_id)
        r.sadd(self.cola.worker_set, self.id)

    def pull_task(self, time_out=WORKER_HEARTBEAT_INTERVAL):
        #Pop task from queue
        #This is a blocking operation
        #task is a tuple (queue_name, task_id)
        task = r.blpop(self.cola.task_queue, time_out)
        if task:
            #Get Task Details
            _task = r.get(task[1])
            #Get Time_stamp
            time_stamp =r.time()[0]
            #Store task in pending_set ordered by time
            # zadd NOTE: The order of arguments differs from that of the official ZADD command.
            r.zadd(self.cola.pending_set, '%s:%s' % (self.id, task[1]), time_stamp)
            # Return a Task object
            return Task(**eval(_task))
        #If there is no task to do return None
        else:
            return None

    def send_heartbeat(self, timeout = WORKER_HEARTBEAT_INTERVAL+5):
        r.set(self.id, 1)
        r.expire(self.id, timeout)