# coding: utf-8
import pymysql
from log import logger
from config import Config

CONFIG = Config()
DB_HOST = CONFIG.get('db', 'host')
DB_PORT = CONFIG.getint('db', 'port')
DB_DATABASE = CONFIG.get('db', 'database')
DB_USERNAME = CONFIG.get('db', 'username')
DB_PASSWORD = CONFIG.get('db', 'password')
DB_CHARSET = CONFIG.get('db', 'charset')


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host=DB_HOST,
                                    port=DB_PORT,
                                    user=DB_USERNAME,
                                    password=DB_PASSWORD,
                                    db=DB_DATABASE,
                                    charset=DB_CHARSET,
                                    cursorclass=pymysql.cursors.DictCursor)

    def get_conn(self):
        return self.conn

    def close(self):
        self.conn.close()

    def execute(self, sql, param_tuple):
        logger.info(sql % param_tuple)
        with self.conn.cursor() as cursor:
            result = cursor.execute(sql, param_tuple)
        self.conn.commit()
        return result

    def query(self, sql, param_tuple):
        logger.info(sql % param_tuple)
        with self.conn.cursor() as cursor:
            cursor.execute(sql, param_tuple)
            result = cursor.fetchall()
        return result


if __name__ == '__main__':
    db = DB()
    re = db.execute('update ra_user set tel= %s where username = %s', ('18012345678', 'phtest'))
    print re
    re = db.query('SELECT * FROM ra_user where username = %s', '哈哈哈哈')
    print re
    db.close()
