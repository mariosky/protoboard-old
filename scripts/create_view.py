__author__ = 'mariosky'

import psycopg2
from django.conf import settings

if __name__ == "__main__":
    import django
    django.setup()
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")

con = psycopg2.connect(database=settings.DATABASES['default']['NAME'],user=settings.DATABASES['default']['USER'],
                       host=settings.DATABASES['default']['HOST'],password=settings.DATABASES['default']['PASSWORD'],
                       )
print con

cur = con.cursor()

cur.execute("""CREATE OR REPLACE VIEW activitytree_ula_vw AS
 SELECT ul.user_id, ul.learning_activity_id, ul.pre_condition, ul.progress_status, ul.objective_status, ul.objective_measure, la.parent_id, la.rollup_objective, la.rollup_progress, la.name
   FROM activitytree_learningactivity la
   JOIN activitytree_userlearningactivity ul ON la.id = ul.learning_activity_id;""")

alter = """ALTER TABLE activitytree_ula_vw OWNER TO %s;""" % settings.DATABASES['default']['USER']

cur.execute( """ALTER TABLE activitytree_ula_vw OWNER TO %s;""" % settings.DATABASES['default']['USER'])
con.commit()

cur.close()
con.close()