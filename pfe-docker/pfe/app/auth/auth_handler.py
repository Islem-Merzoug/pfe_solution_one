
import time
from typing import Dict

import jwt
from decouple import config
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

import os 


JWT_SECRET = os.environ.get("secret")
JWT_ALGORITHM = os.environ.get("algorithm")


def token_response(token: str, user_id: str, fullname: str, email: str):
    return {
        "user_id": user_id,
        "fullname": fullname,
        "email": email,
        "access_token": token
    }

def signJWT(user_id: str, fullname: str, email: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "fullname": fullname,
        "email": email,
        "expires": time.time() + 6
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token, user_id, fullname, email)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
