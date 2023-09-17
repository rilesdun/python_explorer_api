"""
This module contains functions to interact with the PeerPlays blockchain,
specifically to retrieve account history.
"""
from peerplays import PeerPlays
from peerplays.account import Account
from config import api_url

peerplays = PeerPlays(api_url)


def get_account_history(account_name):
    """
    retrieve account history
    """
    account = Account(account_name, blockchain_instance=peerplays)

    account_history = list(account.history())

    return account_history
