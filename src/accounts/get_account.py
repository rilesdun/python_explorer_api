"""
This module contains the function to get account information.
"""
from peerplays.account import Account
from peerplays_instance import peerplays

def get_account_info(account_name):
    """
    This function returns the account information for the given account name.
    """
    account = Account(account_name, blockchain_instance=peerplays)
    account_info = {
        "id": account["id"],
        "name": account["name"],
        "owner": account["owner"],
        "active": account["active"],
        "options": account["options"],
        "balances": account.balances,
    }
    return account_info
