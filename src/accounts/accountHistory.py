from peerplays import PeerPlays
from peerplays.account import Account
from config import api_url

peerplays = PeerPlays(api_url)

def get_account_history(account_name):
    account = Account(account_name, blockchain_instance=peerplays)

    account_history = [op for op in account.history()]

    return account_history