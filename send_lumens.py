from stellar_sdk.keypair import Keypair
from stellar_sdk.network import Network
from stellar_sdk.server import Server
from stellar_sdk.transaction_builder import TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError
from stellar_sdk import Asset

server = Server("https://horizon-testnet.stellar.org")
source_key = Keypair.from_secret(
    "SCVGZOIVVG3C27MZNNSJGSOLSNONYOP6JDWDFJFUZNFCURMUO43FI3PA")
destination_id = "GDJNTEOKKOU6QNS6WEP7Z6SVR3ORB3DQ3V4NAUSNPDZ7WFGMN4ZUCXIT"

# First, check to make sure that the destination account exists.
# You could skip this, but if the account does not exist, you will be charged
# the transaction fee when the transaction fails.
try:
    server.load_account(destination_id)
except NotFoundError:
    # If the account is not found, surface an error message for logging.
    raise Exception("The destination account does not exist!")

# If there was no error, load up-to-date information on your account.
source_account = server.load_account(source_key.public_key)

# Let's fetch base_fee from network
base_fee = server.fetch_base_fee()

# Start building the transaction.
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    # Because Stellar allows transaction in many currencies, you must specify the asset type.
    # Here we are sending Lumens.
    .append_payment_op(destination=destination_id, amount="10", asset_code="XLM")
    # A memo allows you to add your own metadata to a transaction. It's
    # optional and does not affect how Stellar treats the transaction.
    .add_text_memo("Test Transaction")
    # Wait a maximum of three minutes for the transaction
    .set_timeout(10)
    .build()
)

# Sign the transaction to prove you are actually the person sending it.
transaction.sign(source_key)

try:
    # And finally, send it off to Stellar!
    response = server.submit_transaction(transaction)
    print(f"Response: {response}")
except (BadRequestError, BadResponseError) as err:
    print(f"Something went wrong!\n{err}")
