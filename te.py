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