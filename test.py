from requests import Request, Session
import hmac
import json
import time
import os
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API')
API_SECRET = os.getenv('API_SECRET')
SUBACCOUNT = "FTXApp"


def create_subaccount(name):
    endpoint = "https://ftx.com/api/subaccounts"

    ts = int(time.time() * 1000)
    s = Session()
    params = json.dumps({
        "nickname": name
    })
    request = Request("POST", endpoint, params=params)
    prepared = request.prepare()
    signature_payload = f"{ts}{prepared.method}{prepared.path_url}".encode()
    if prepared.body:
        signature_payload += prepared.body

    signature = hmac.new(API_SECRET.encode(), signature_payload, "sha256").hexdigest()

    prepared.headers["FTX-KEY"] = API_KEY
    prepared.headers["FTX-SIGN"] = signature
    prepared.headers["FTX-TS"] = str(ts)
    prepared.headers["FTX-SUBACCOUNT"] = SUBACCOUNT

    response = s.send(prepared)
    data = response.json()
    pprint(data)
    return data

create_subaccount("sub2")