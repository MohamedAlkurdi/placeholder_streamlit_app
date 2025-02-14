import streamlit as st
import jwt
import time
from dotenv import load_dotenv
import os

load_dotenv()

login_url = os.getenv('LOGIN_URL')

def extract_query(SECRET_KEY):
    query_params = st.query_params
    query = query_params.get("query")
    try:
        payload = jwt.decode(query, SECRET_KEY, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.DecodeError:
        return None 
    return {
        'query':query,
        'decrypted_query':payload['query'],
    }

def validate_extracted_data(data):
    if data:
        expiration = int(data['decrypted_query']['exp'])
        if time.time() > expiration:
            return {"status":False,
                    'error_type':'EXPIRED_TOKEN',
                    "message":"Your session has expired, please log in again.",
                    "markdown":f'<button><a href="{login_url}" target="_blank">Sign in again.</a></button>'}
        else:
            return {'status':True,
                    'message':'Your session is active.',
                    'expires_at':expiration}
    else:
        return {'status':False,
                'error_type':'INVALID_TOKEN',
                'message':'Invalid Token.'}
    

    # def get_from_django():
    # url = "http://127.0.0.1:8000/get_data"
    # response = requests.get(url)
    # if response.status_code == 200:
    #     return response.json()
    # return response.status_code