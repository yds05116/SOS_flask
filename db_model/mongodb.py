import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST)) # localhost로 mongoDB 접속

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        sos_ab = MONGO_CONN.sos_session_db.sos_ab 
    except: 
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        sos_ab = MONGO_CONN.sos_session_db.sos_ab 
    return sos_ab