# -*- coding: utf-8 -*-

from pymysql import connect
import pymysql.err


class MySQLHelper():
    
    def __init__(self):
        self.host = ''
        self.user = ''
        self.password = ''
        self.database = ''
        self.port = 3306
    
    def getconnect(self):
        conn = connect(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port)
        return conn
    
    def getcursor(self):
        conn = self.getconnect()
        cursor = conn.cursor()
        return cursor
    
    def select(self,sql,types,number=1):
        cursor = self.getcursor()
        cursor.execute(sql)
        try:
            if types=='all':
                result = cursor.fetchall()
            elif types=='one':
                result = cursor.fetchone() 
            elif types=='many':
                result = cursor.fetchmany(number)
            else:
                pass
            return result
        except Exception:
            print('对不起,只能输all,one,many中的其中一个')
        

    
    def dml(self,sql):
        cursor = self.getcursor()
        try:
            result = cursor.execute(sql)
            if result:
                print('执行成功')
            else:
                print('执行失败,请检查sql')
        except pymysql.err.ProgrammingError:
            print('请检查sql语句')
        except pymysql.err.OperationalError:
            print('字段找不到')
            

        
    def close(self):
        self.getcursor().close()
        self.getconnect().close()


# msh = MySQLHelper()
# msh.host = 'localhost'
# msh.user = 'root'
# msh.password = 'root'
# msh.database = 'sharkshop'
# #rs = msh.select('select * from dept','caichang')
# #print(rs)
# #msh.dml("insert into dept(deptno,dname,loc) values (50,'caichang','包包')")
# msh.close()