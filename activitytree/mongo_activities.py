__author__ = 'mario'



from pymongo import MongoClient

_client = MongoClient()
_db = _client.protoboard_database
_activities_collection = _db.activities_collection

class Activity:
    @staticmethod
    def get(uri):
        return _activities_collection.find_one({'_id':uri})




if __name__ == "__main__":
    print  Activity.get('/programPPP/1')