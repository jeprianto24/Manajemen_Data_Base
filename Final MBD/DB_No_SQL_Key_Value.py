from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["key_value_db"]            
collection = db["data_mahasiswa"]        

collection.delete_many({})

data = [
    {"key": "nama", "value": "Jeprianto"},
    {"key": "nim", "value": "D0222316"},
    {"key": "jurusan", "value": "Informatika"},
    {"key": "angkatan", "value": "2023"},
    {"key": "universitas", "value": "Universitas Sulawesi Barat"}
]

collection.insert_many(data)

print("Data di MongoDB (Model Key-Value):")
for item in collection.find():
    print(f"{item['key']} : {item['value']}")
