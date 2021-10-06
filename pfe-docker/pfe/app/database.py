from logging import FATAL
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://192.168.1.105:27018"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.mlops

user_collection = database.get_collection("users_collection")
file_collection = database.get_collection("files_collection")

# helpers


def file_helper(file) -> dict:
    return {
        "id": str(file["_id"]),
        "name": file["name"],
        "date": file["date"],
        "type": file["type"],
        "service": file["service"],
        "inputLink": file["inputLink"],
        "outputLink": file["outputLink"],
        "user_id": file["user_id"],
    }

async def retrieve_all_files():
    files = []
    async for file in file_collection.find():
        files.append(file_helper(file))
    return files


# Retrieve all files present in the database
async def retrieve_files(user_id: str):
    print(user_id)
    files = []
    async for file in file_collection.find({"user_id" : user_id }):
        files.append(file_helper(file))
    return files

# Add a new file into to the database
async def add_file(file_data: dict) -> dict:
    file = await file_collection.insert_one(file_data)
    new_file = await file_collection.find_one({"_id": file.inserted_id})
    return file_helper(new_file)



# Retrieve a file with a matching ID
async def retrieve_file(id: str) -> dict:
    file = await file_collection.find_one({"_id": ObjectId(id)})
    if file:
        return file_helper(file)



# Update a file with a matching ID
async def update_file(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    file = await file_collection.find_one({"_id": ObjectId(id)})
    if file:
        updated_file = await file_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_file:
            return True
        return False


# Delete a file from the database
async def delete_file(id: str):
    file = await file_collection.find_one({"_id": ObjectId(id)})
    if file:
        await file_collection.delete_one({"_id": ObjectId(id)})
        return True



# ----------------------- user --------------------

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "password": user["password"],

    }

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user_data.update({'password': get_password_hash(user_data['password']) })
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve a user with a matching ID
async def retrieve_user(user_data: dict) -> dict:
    user = await user_collection.find_one({"email": user_data["email"]})
    if user:
        if  verify_password(user_data['password'], user['password']):
            return user_helper(user)
    else:
        print("batata")



async def is_admin(user_id: dict)-> dict:
    print(user_id)
    admin = await user_collection.find_one({"_id": ObjectId(user_id), "role": "admin"})
    if admin:
            return True
    else:
        return False
