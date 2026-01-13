import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)


from pydantic import BaseModel 
list_all_data = []
class IPData(BaseModel):
    ip: str 
    lat: str 
    lon: str 

def add_data(data: IPData) -> bool:    # type: ignore
    "add the data to redis db return bool response"
    ip = data.ip
    data_json = data.model_dump_json()
    try:
        r.set(ip, data_json)
        return True 
    except:
        return False 
            
def get_data():
    "get all data from db "

    if r:
        try:
            data = r.keys()
            if isinstance(data, list):
                for k in data:
                    data_dict = r.get(k)
                    list_all_data.append({k : data_dict})
        except:
            print("Error: can't get the data to db")


print(list_all_data)
get_data()
print(list_all_data)