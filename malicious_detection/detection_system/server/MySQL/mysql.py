#!coding=utf8

import pymysql

class MySQL(object):
	def __init__(self, host, user, passwd, db, port=3306, charset='utf8'):
		self.conn = pymysql.connect(
						host = host, 
						port = port, 
						user = user,
						passwd = passwd,
						db = db,
						charset = charset
						)
		self.cursor = self.conn.cursor()

	async def get(self, sql):
		self.cursor.execute(sql)
		return self.cursor.fetchone()

	async def query(self, sql):
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	async def execute(self, sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()

	def close(self):
		self.cursor.close()
		self.conn.close()