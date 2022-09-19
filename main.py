from pydoc import cli
from urllib import response
import ftx
import os
import json
from dotenv import load_dotenv

load_dotenv()

# for PROD
# API = str(input("Input FTX API key: "))
# API_SECRET = str(input("Input FTX SECRET_API key: "))
# client = ftx.FtxClient()
# client = ftx.FtxClient(api_key=API, api_secret=API_SECRET)

# for DEBUG
client = ftx.FtxClient()
client = ftx.FtxClient(
    api_key=os.getenv('API'), 
    api_secret=os.getenv('API_SECRET'))

# for PROD
# wallet_file = str(input("Input wallet file: "))
# if os.path.exists(wallet_file) == True:
#     with open(wallet_file) as file:
#         wallet_array = [row.strip() for row in file]
# else:
#     raise Exception("File.net, pizdabol!")

# for DEBUG
with open("wallet.txt") as file:
    # with open("ftx/wallet.txt") as file:
    wallet_array = [row.strip() for row in file]
##


# ## for MAIN ACCOUNT
# check_balance = client.get_balances()

# coin_array = []

# print("Coin - Available For Withdrawal")
# for i in range(len(check_balance)):
#     coin_array.append(check_balance[i]['coin'])
#     print(f"{check_balance[i]['coin']} - {check_balance[i]['availableForWithdrawal']}")

# coin_to_transfer = str(input("Input coin to transfer: "))
# value_to_one_transfer = str(input("Input value to 1 transfer: " ))

# for SUB ACCOUNT
users_subaccounts = client.get_subaccounts()
name_of_subaccounts = []

for i in range(len(users_subaccounts)):
    name_of_subaccounts.append(users_subaccounts[i]['nickname'])

print(f"Ur subaccounts: {' '.join(name_of_subaccounts)}")
subaccount = str(input("Chose subaccount: "))

if subaccount in name_of_subaccounts:
    check_sub_balance = client.get_subaccounts_balance(subaccount)

    if len(check_sub_balance) == 0:
        raise Exception("Pusto, chose drugoy!")

    else:
        coin_dict = {}

        for i in range(len(check_sub_balance)):
            coin_dict[check_sub_balance[i]['coin']] = check_sub_balance[i]['availableForWithdrawal']
else:
    raise Exception("Wrong subaccount, peredelivay!")

print("Coin - Available For Withdrawal")
for key, value in coin_dict.items():
        print(f"{key} - {value}")

coin_to_transfer = str(input("Input coin to transfer (example - BTC): ")).upper()
check_coin_in_dict = coin_to_transfer in coin_dict

if check_coin_in_dict == True:
    value_to_one_transfer = float(input("Input value to 1 transfer (example - 0.45): "))

    if value_to_one_transfer == 0:
        raise Exception("Malo!")
    
    if value_to_one_transfer >= coin_dict[coin_to_transfer]:
        raise Exception("Mnoga!")
else:
    raise Exception("Ti kogo hochesh naebat? Net takoy moneti!")

chains = ["erc20", "trx", "sol", "omni", "bep2", "bsc", "ftm", "avax", "matic"]

print(f"Chains: {' '.join(chains).upper()}")

transfer_chain = str(input("Input chain: ")).lower()

if transfer_chain in chains:
    print(f"U sure u want to transfer {value_to_one_transfer} {coin_to_transfer} to {len(wallet_array)} wallets?")

else:
    raise Exception("Net takoy seti!")

## TO-DO перевод внутри сети

# print(chains)
# # chain_for_transfer =

# print(f"U sure u want to transfer {value_to_one_transfer} {coin_to_transfer} to {len(wallet_array)} wallets?")
