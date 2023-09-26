"""
This module contains functions to interact with the PeerPlays blockchain,
specifically to retrieve account history.
"""
from peerplays.account import Account
from peerplays_instance import peerplays

def get_account_history(account_name):
    """
    retrieve account history
    """
    account = Account(account_name, blockchain_instance=peerplays)

    account_history = list(account.history())

    return account_history
