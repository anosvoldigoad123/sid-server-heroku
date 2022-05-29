import json
import urllib.request
from fastapi import FastAPI, Request
import json
from fastapi.responses import JSONResponse
import uvicorn
import random
import os
import sys
from time import time as timestamp
from time import sleep
import names
from hashlib import sha1
from functools import reduce
from base64 import b85decode, b64decode
import random
import aiohttp
import asyncio
import heroku3
import requests
import requests_random_user_agent
import hmac
import platform,socket,re,uuid
import base64
import  threading
from uuid import uuid4
import aminos
api="https://service.narvii.com/api/v1"
key=""
name=""
def res():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[name]
    botapp.restart()

def r():
    s = requests.Session()
    return s.headers['User-Agent']
def sig(data):
        key='f8e7a61ac3f725941e3ac7cae2d688be97f30b93'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("42") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='02b258c63559d8804321c5d5065af320358d366f'
    mac = hmac.new(bytes.fromhex(key), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()

def reset(l):
  #data.subClient.send_message(data.chatId,"done")
  #sleep(1)
  sys.argv
  sys.executable
  print("restart now")
  os.execv(sys.executable, ['python'] + sys.argv)

def login_custom(email: str, password: str,device:str):
        headers = {
            #"NDCDEVICEID": '223B063D54BEB7463B92A073735DB6F26EFD413010CCF78271F5953F8BB9010FCFF94D3FF917CB98DE',
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": r(),
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }
        data = json.dumps({
            "email": email,
            # "phoneNumber":email,
            "v": 2,
            "secret":f"0 {password}",
            "deviceID": device,
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })
        headers["NDC-MSG-SIG"]=sig(data)
        headers["NDCDEVICEID"]=dev()
        response = requests.post(f"{api}/g/s/auth/login", headers=headers, data=data)
        if response.status_code == 403:
        	error=json.dumps({"api:statuscode":69,"api:message":"wait ip is changing"})
        	res()
        	return error
        else:
            resp=response.json()
            if resp["api:statuscode"]==110:
                res()
                return resp
            return resp
        
app = FastAPI()

@app.get('/')
async def get_webpage():
    return "Sid server"
    
@app.get('/reset')
async def ress():
    res()
    return "restarted"



@app.post("/login")
async def submit_report(request: Request):
    body = await request.json()
    email=body["email"]
    password=body["password"]
    device=body["device"]
    data=login_custom(email, password, device)
    return data
