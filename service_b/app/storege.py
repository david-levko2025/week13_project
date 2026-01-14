import redis 
from schema import IPData
import os 
from dotenv import load_dotenv 

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance 
  

class DBConnection(SingletonClass):
    _connection = None 

    @staticmethod
    def get_connection():
        load_dotenv()
        host=os.getenv("REDIS_HOST")
        port=os.getenv("REDIS_PORT")
        connection = redis.Redis(host=host, port=port, decode_responses=True)
        return connection

    @staticmethod
    def close_connection():
        if DBConnection._connection:
            DBConnection._connection.close() 


class DBCrud:
    _connection = DBConnection.get_connection()
    
    @staticmethod
    def add_data(data: IPData) -> bool:    # type: ignore
        "add the data to redis db return bool response"
        ip = data.ip
        data_json = data.model_dump_json()
        if DBCrud._connection:
            try:
                DBCrud._connection.set(ip, data_json)
                return True 
            except:
                return False
    @staticmethod
    def get_data() -> list:  # type: ignore
        "get all data from db "
        list_all_data: list = []
        conn = DBCrud._connection
        if DBCrud._connection:
            try:
                data = conn.keys()
                if isinstance(data, list):
                    for k in data:
                        data_dict = conn.get(k)
                        list_all_data.append({k : data_dict})
                    return list_all_data
            except:
                print("Error: can't get the data to db")