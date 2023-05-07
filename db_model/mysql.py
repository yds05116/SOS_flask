import pymysql
MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='lsh',
    passwd='8617',
    db='kiosk_db',
    charset='utf8'
) # mySQL에 연결

def conn_mysqldb():
    if not MYSQL_CONN.open: # 커넥션이 끊어져 있다면
        MYSQL_CONN.ping(reconnect=True) # 다시 접속
    return MYSQL_CONN