from fastapi import APIRouter, Depends
from app.models import Message, MessageCreate
from pymongo import MongoClient
from bson import ObjectId
from typing import List
import redis

router = APIRouter()
client = MongoClient('mongodb://mongo:27017')
db = client.mydatabase
messages_collection = db.messages
cache = redis.StrictRedis(host='redis', port=6379, db=0)

@router.get('/api/v1/messages/', response_model=List[Message])
def get_messages():
    messages = list(messages_collection.find())
    for message in messages:
        message['id'] = str(message['_id'])
    return messages

@router.post('/api/v1/message/')
def create_message(message: MessageCreate):
    new_message = {"author": message.author, "text": message.text}
    result = messages_collection.insert_one(new_message)
    new_message["id"] = str(result.inserted_id)
    cache.delete('messages')
    return new_message