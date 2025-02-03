from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import ssl

# url
uri = "mongodb+srv://vinayak2:vinayak@cluster0.vkpkc.mongodb.net/?retryWrites=true&w=majority"

# create a new client and connect to server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("/Users/vinayakgupta/Documents/sensorproject/notebooks/wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

try:
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("Data inserted successfully!")
except Exception as e:
    print(f"Error inserting data: {e}")




