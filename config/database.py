from pymongo import MongoClient

client = MongoClient("mongodb+srv://yasminkhan2014yk:Mongo654321!@cluster0.xetvj.mongodb.net/?appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]