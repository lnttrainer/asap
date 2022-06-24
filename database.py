"""This module implements DB related stuff"""
import sqlite3

# DB and Table creation
class Criminal:
    def __init__(self,DBName):
        self.DbName = DBName

    def CreateDBT(self):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.cursor()
        query = f"""CREATE TABLE IF NOT EXISTS CRIMINAL(
                ID INT PRIMARY KEY NOT NULL,
                NAME CHAR(20) NOT NULL, 
                COUNTRY CHAR(20), 
                CCOUNT INT NOT NULL)"""
        cursor.execute(query)
        conn.commit()
        conn.close()

    def InsertCriminal(self,FormData):
        id = int(FormData['criid'])
        name = FormData['criname']
        country = FormData['cricountry']
        count = int(FormData['cricount'])

        conn = sqlite3.connect(self.DbName)
        conn.execute("INSERT INTO CRIMINAL (ID,NAME,COUNTRY,CCOUNT) "
                     f"VALUES ({id}, '{name}', '{country}', {count})")
        conn.commit()
        conn.close()

    def AllCriminals(self):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.execute("SELECT * from CRIMINAL ORDER BY CCOUNT DESC")
        CriminalsData = cursor.fetchall()
        conn.commit()
        conn.close()
        return CriminalsData

    def RetrieveCriminal(self,id):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.execute(f"SELECT * from CRIMINAL WHERE ID={id}")
        CriminalData = cursor.fetchall()
        conn.commit()
        conn.close()
        return CriminalData

    def UpdateCriminal(self,FormData):
        id = FormData['criid']
        name = FormData['criname']
        country = FormData['cricountry']
        count = int(FormData['cricount'])

        conn = sqlite3.connect(self.DbName)
        conn.execute(f"UPDATE CRIMINAL SET ID={id}, NAME='{name}', COUNTRY='{country}', CCOUNT={count} WHERE ID={id}")
        conn.commit()
        conn.close()

    def DeleteCriminalData(self,id):
        conn = sqlite3.connect(self.DbName)
        conn.execute(f"DELETE FROM CRIMINAL WHERE ID={id}")
        conn.commit()
        conn.close()