from peerplays import PeerPlays
from peerplays.account import Account

# Connect to PeerPlays network
peerplays = PeerPlays("wss://ca.peerplays.info/api")

def get_account_history(account_name):
    # Get the account
    account = Account(account_name, blockchain_instance=peerplays)

    # Retrieve account history
    account_history = [op for op in account.history()]

    return account_history