# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
import psycopg2

class DbManager(QtCore.QObject):
    def __init__(self,DatabaseName:str,DbUser:str,DbPassword:str):
        try:
            self.DatabaseName = DatabaseName
            self.DbUser = DbUser
            self.DbPassword = DbPassword
        except Exception() as e:
            print(f"{e} : all parameters are required!")
            return False
        
    def connect(self):
        try:
            psycopg2.connect("dbname={self.DatabaseName} username={self.DbUser} password={self.DbPassword}")
            print("connected ..")
            return True
            
        
