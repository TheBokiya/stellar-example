# stellar-sdk >= 2.0.0 required
# create a completely new and unique pair of keys
# see more about KeyPair objects: https://stellar-sdk.readthedocs.io/en/latest/api.html#keypair
from stellar_sdk.keypair import Keypair

pair = Keypair.random()
print(f"Secret: {pair.secret}")
print(f"Public Key: {pair.public_key}")


####### Account 1 #############
###############################
###############################
# Public Key: GBJ5BW3YUFXQSHH6QAF3EZ653CHZGT5MMAWNTBP4S4L5RTOXFNANHZOV
# Secret: SCVGZOIVVG3C27MZNNSJGSOLSNONYOP6JDWDFJFUZNFCURMUO43FI3PA


####### Account 2 #############
###############################
###############################
# Public Key: GDJNTEOKKOU6QNS6WEP7Z6SVR3ORB3DQ3V4NAUSNPDZ7WFGMN4ZUCXIT
# Secret: SBTG2WEE6AUHMK4ON7DGLZNIGRUH2Y3WPJ4GLDO5PRKFAGCMWBWQETZQ
