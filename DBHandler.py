import pymysql
import smtplib, os


class DBHandler:

    def __init__(self, DATABASE_IP, DB_USER, DB_PASSWORD, DATABASE):
        self.DATABASE_IP = DATABASE_IP
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DATABASE = DATABASE

    def __del__(self):
        print("Destructor")

    def getStockQty(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select itemQuantity from stock'
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)

    def insertFeedback(self, id, subject, message):
        db = None
        cur = None
        insert = False
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update patient set subject=%s, message=%s where patientID=%s'
            args = (subject, message, id)
            print("Before SQL")
            cur.execute(sql, args)
            db.commit()
            insert = True
            print("After SQL")
        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert

    def insertStock(self):
        db = None
        cur = None
        insert = False
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'update stock set itemQuantity =40 '
            cur.execute(sql)
            insert = True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
        return insert

    def getPatientID(self, id):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select patientID from patient where patientID = %s'
            cur.execute(sql, (id,))
            result = cur.fetchone()
            return result[0]
        except Exception as e:
            print(e, "tu banda banja getPatientId")
        finally:
            db.commit()
        return[0]

    def getPatientID2(self, name, email):
        db = None
        cur = None
        try:
            db = pymysql.connect(host='localhost', port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select patientID from patient where pName=%s AND pEmail=%s'
            args = (name, email)
            cur.execute(sql, args)
            result = cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            db.commit()
            return result[0]

    def getStaffID(self, id, cnic):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3307, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select * from staff where staffID=%s AND sCNIC=%s'
            args = (id, cnic)
            cur.execute(sql, args)
            result = cur.fetchone()

        except Exception as e:
            print(e)
        finally:
            import mysql.connector
            from mysql.connector import Error

            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='python_db',
                                                     user='pynative',
                                                     password='pynative@#29')

                cursor = connection.cursor(prepared=True)
                sql_update_query = """UPDATE Employee set Salary = %s where Id = %s"""

                data_tuple = (12000, 1)
                cursor.execute(sql_update_query, data_tuple)
                connection.commit()
                print("Employee table updated using the prepared statement")

            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

    def deleteStaff(self, id):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'Delete from staff where staffID = %s'
            result = cur.execute(sql, (id,))
            db.commit()
            if (result == False):
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            db.commit()
            return result

    def deletePatient(self, id):
        db = None
        cur = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'DELETE FROM patient WHERE patientID = %s'
            result = cur.execute(sql, (id,))
            if (result == False):
                return False
            else:
                return True
        except Exception as e:
            print(e, "tu banda banja deletepatient")
            return False
        finally:
            db.commit()
            return result
        
    def showFeedBack(self):
        db = None
        cursor = None
        try:

            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select pName, pEmail, subject, message from patient'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def showStockView(self):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=DATABASE_IP, port=3306, user=self.DB_USER, passwd=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            print("here")
            sql = 'Select * from stock'
            cur.execute(sql)
            result = cur.fetchall()

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if (db != None):
                db.commit()
            return result

    def validateStaff(self, id, password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select sPassword from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            passwd = tuple[0]
            if done:
                if password == passwd:
                    valid = True
        except Exception as e:
            print(e)
            print('error in validate staff')
        finally:
            if db != None:
                db.commit()
        return valid

    def validatePatient(self, id, password):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select pPassword from patient where patientID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            if tuple:
                passwd = tuple[0]
            if done:
                if password == passwd:
                    valid = True
        except Exception as e:
            print(e)
            print('error in validate patient')
        finally:
            if db != None:
                db.commit()
        return valid

    def checkAdmin(self, id):
        db = None
        valid = False
        try:
            db = pymysql.connect(host=self.DATABASE_IP, port=3306, user=self.DB_USER, password=self.DB_PASSWORD,
                                 database=self.DATABASE)
            cur = db.cursor()
            sql = 'select designation from staff where staffID=%s'
            args = (id)
            done = cur.execute(sql, args)
            tuple = cur.fetchone()
            designation = tuple[0]
            if done:
                if designation == 'admin':
                    valid = True
        except Exception as e:
            print(e)
            print('error in check admin')
        finally:
            if db != None:
                db.commit()
        return valid
