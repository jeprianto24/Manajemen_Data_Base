from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["wide_column_db"]
collection = db["mahasiswa"]
collection.delete_many({})

data = [
    {
        "nim": "D0222316",
        "nama": "Jeprianto",
        "jurusan": "Informatika",
        "angkatan": "2023",
        "universitas": "Universitas Sulawesi Barat"
    },
    {
        "nim": "D0222317",
        "nama": "Andi",
        "jurusan": "Sistem Informasi",
        "angkatan": "2022"
    },
    {
        "nim": "D0222318",
        "nama": "Budi",
        "jurusan": "Teknik Komputer"
    },
    {
        "nim": "D0222319",
        "nama": "Citra",
        "universitas": "Universitas Sulawesi Barat"
    },
    {
        "nim": "D0222320",
        "nama": "Dewi",
        "ipk": 3.85,
        "beasiswa": True
    }
]

collection.insert_many(data)

print("Data Mahasiswa (Wide-Column Style):")
for mhs in collection.find():
    print(mhs)
