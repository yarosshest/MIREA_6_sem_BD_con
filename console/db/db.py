import pymongo
import os

mongoCon = os.environ.get("DATABASE_URL", "localhost:30001")
myclient = pymongo.MongoClient(f"mongodb://{mongoCon}/")
databaseName = "furniture"

dblist = myclient.list_database_names()
if databaseName in dblist:
    print(f"The database {databaseName} exists.")
else:
    print(f"The database {databaseName} created.")

db = myclient[databaseName]
