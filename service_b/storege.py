import redis 

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance 
  

class DBConnection(SingletonClass):
    @staticmethod
    def get_connection():
        connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
        # change it to env variables
        return connection


    # def close_connection(self):
    #     if self.connection and self.connection.is_connected():
    #         self.connection.close() 


class DBCrud:
    _connection = DBConnection.get_connection()

    @staticmethod
    def add_data(data: dict) -> bool | None:
        "add the data to redis db return bool response"
        if DBCrud._connection:
            try:
                DBCrud._connection.hset("data", mapping={**data})
                return True 
            except:
                return False
        return None


    @staticmethod
    def get_data():
        "get all data from db "
        if DBCrud._connection:
            try:
                data = DBCrud._connection.hgetall("data")
                return data
            except:
                print("Error: can't add the data to db")