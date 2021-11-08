from stellar_sdk.server import Server

server = Server("https://horizon-testnet.stellar.org")
public_key = "GBJ5BW3YUFXQSHH6QAF3EZ653CHZGT5MMAWNTBP4S4L5RTOXFNANHZOV"
account = server.accounts().account_id(public_key).call()
for balance in account['balances']:
    print(f"Type: {balance['asset_type']}, Balance: {balance['balance']}")
