import os
import time
import hmac
import requests
from pprint import pprint
from requests import Request, Session

import json

from dotenv import load_dotenv

load_dotenv()

s = Session()

ts = int(time.time() * 1000)
request = Request('GET', 'https://ftx.com/api/wallet/saved_addresses')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new(os.getenv('API_SECRET').encode(), signature_payload, 'sha256').hexdigest()

prepared.headers['FTX-KEY'] = os.getenv('API')
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)

answer = s.send(prepared)

json_response = json.loads(answer.text)

print(json.dumps(json_response, indent=2))

# print(json.dumps(answer.text, indent=6))
