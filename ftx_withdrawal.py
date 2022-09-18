import os
import sys
from pprint import pprint
import requests

from dotenv import load_dotenv

load_dotenv()

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


print('CCXT Version:', ccxt.__version__)

exchange = ccxt.ftx({
    'apiKey': os.getenv('API'),
    'secret': os.getenv('API_SECRET'),
})

# pprint(dir(exchange))  # uncomment to print all available methods

markets = exchange.load_markets()

exchange.verbose = True  # uncomment for debugging

# response = exchange.fetch_balance()
# pprint(response)

response = requests.get("/wallet/balances")