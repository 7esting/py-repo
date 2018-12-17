"""
MongoEngine is a Document-Object Mapper (think Object-Relational Mapping (ORM)
for RDBMS DBs, but for document databases) for working with MongoDB from Python.

It uses a simple declarative API, similar to the Django ORM.

Documentation available at docs.mongoengine.org - there is currently a tutorial,
 a user guide and API reference.

http://docs.mongoengine.org/tutorial.html
"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
import datetime, pytz
import mongoengine
from config_settings import db_config as db_conn

# --------------------------- Function Definitions ----------------------------

def time_stamp():
    """Returns timestamp in ISO-8601 form '2016-11-16T14:31:18.130822-08:00'
    Requires import datetime, pytz"""
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
    #return utc_now.isoformat()
    return pst_now.isoformat()

"""
MongoEngine database connection registration
--------------------------------------------
Option 1: mongoengine.register_connection(alias='directory', name='library_members')
Option 2: Use the mongoengine.connect(...)
          This option allows you to specify bin, user, password, uri, auth..
          connect(bin=client[dbname],
                host=db_conn.DATABASE_CONFIG['MONGO_URI'],
                username='webapp',
                password='pwd123',
                authentication_source='admin')
                
If database does not exist it will get created!!!
"""

# MongoEngine database connection
def global_init():
    mongoengine.register_connection(alias='directory', name='library_members')

# ------------------------- MongoDB Connection Str ----------------------------
# If database does not exist it will get created
dbname = db_conn.DATABASE_CONFIG['MONGO_DB2']
print(f"{dbname} : {type(dbname)}")
print(type(db_conn.DATABASE_CONFIG['MONGO_URI']))

# MongoEngine.connect bin connection string registration
#connect(bin=client[dbname], host=db_conn.DATABASE_CONFIG['MONGO_URI'],
#           username='webapp', password='pwd123', authentication_source='admin')
mongoengine.connect(db=dbname, host=db_conn.DATABASE_CONFIG['MONGO_URI'])

# Class name ==> Collection name.  Overridden by meta {..}
class Members(mongoengine.Document):
    username = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    create_date = mongoengine.DateTimeField(default=time_stamp)
    active_account = mongoengine.BooleanField(default=True)

    # TODO: Implement this later
    # Login status
    #logged = mongoengine.EmbeddedDocument(logged_status)

    # Uncomment if not using mongoengine.connect(...)
    # meta = {
    #     'db_alias': 'directory',
    #     'collection': 'members'
    # }

# ------------------------------- Main Function -------------------------------
def main():
    # User dictionary
    usrList = {
        "username": "jmontana",
        "email": "jmontana@49rs.com",
        "username": "tbrady",
        "email": "tbrady@pats.com",
        "username": "arogers",
        "email": "arogers@grnbay.com"
    }

    # MongoEngine database connection registration
    # Option 1:
    #global_init()
    # Option 2: Use the mongoengine.connect(...) see above
    #           This option allows you to specify bin, user, password, uri, auth...

    # Instantiate Users objects
    # usr1: <type hint>
    usr1: object = Members(username = 'jplunkett', email = 'jplunkett@raiders.com').save()
    usr2 = Members(username = 'msanchez', email = 'msanchez@jets.com')
    usr2.save()

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()

