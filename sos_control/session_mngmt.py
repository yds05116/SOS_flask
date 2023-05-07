from db_model.mongodb import conn_mongodb
from datetime import datetime

class sosSession():
    sos_page = {'A': 'sos.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")  # https://strftime.org/

        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'user_email': user_email,
            'page': webpage_name,
            'access_time': now_time
        })

    @staticmethod
    def get_sos_page(sos_id=None):
        if sos_id == None:
                return sosSession.blog_page['A']
        else:
            return sosSession.blog_page[sos_id]
