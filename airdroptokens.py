#! /usr/bin/python3
from datetime import datetime

from solathon import Client, PublicKey
from solathon.utils import sol_to_lamport

client = Client("https://api.devnet.solana.com")

# Change your PublicKey here to where you want your tokens to airdrop
public_key = PublicKey("7dDc9rEvoHzcNA6ywgS3hNeSvAD4ovVFoCob9JcDwbKS")
amount = sol_to_lamport(1)

date = datetime.now().isoformat()


response = client.request_airdrop(public_key, amount)

response["timestamp"] = datetime.now().isoformat()
print(response)
