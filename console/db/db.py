import pymongo
import os

mongoCon = os.environ.get("DATABASE_URL", "localhost:30001")
client = pymongo.MongoClient(f"mongodb://{mongoCon}/")
databaseName = "furniture"

dblist = client.list_database_names()
if databaseName in dblist:
    print(f"The database {databaseName} exists.")
else:
    print(f"The database {databaseName} created.")

db = client[databaseName]
