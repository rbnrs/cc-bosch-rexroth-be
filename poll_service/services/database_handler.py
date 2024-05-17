import os
from dotenv import load_dotenv
from pymongo import MongoClient, database

load_dotenv()

class DatabaseHandler:

    __mongo_database: database.Database

    def __init__(self):
        
        db_username:str = os.getenv('DB_USER')
        db_password:str = os.getenv('DB_PASSWORD')
        db_port:int = int(os.getenv('DB_PORT'))
        db_name = 'cc-bosch-rexroth'
        
        self.__mongo_client = MongoClient(
            host='localhost',
            port=db_port,
            username=db_username,
            password=db_password
        ) 
        
        self.__mongo_database = self.__mongo_client.get_database(db_name)
        
    
    def get_database(self) -> database.Database:
        return self.__mongo_database
    
    def insert(self, object: any, collection_name: str) -> bool: 
        try:
            result = self.get_database().get_collection(collection_name).insert_one(object)
            return True
        except:
            return False
        
    def get(self, collection_name: str, query: any) -> any:
        return self.get_database().get_collection(collection_name).find_one(query)
        