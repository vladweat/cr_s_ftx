import ftx
import os
import json
from dotenv import load_dotenv

load_dotenv()


client = ftx.FtxClient()

client = ftx.FtxClient(api_key=os.getenv('API'), api_secret=os.getenv('API_SECRET'))

# subaccounts = client.get_subaccounts()
# responce_get_subaccs = json.dumps(subaccounts, indent=2)
# print(responce_get_subaccs)

# # var = client.create_subaccounts("sub2")
# # delete = client. delete_subaccounts("sub2")

# # responce_create_subacc = json.dumps(var, indent=2)

# subaccounts = client.get_subaccounts()
# responce_get_subaccs = json.dumps(subaccounts, indent=2)
# print(responce_get_subaccs)

# balance = client.get_subaccounts_balance("FTXApp")
# print(json.dumps(balance, indent=2))

account = client.get_account_info()
print(json.dumps(account, indent=2))