from peerplays.account import Account
from peerplays import PeerPlays

peerplays = PeerPlays("wss://ca.peerplays.info/api")

def get_account_info(account_name):
    account = Account(account_name, blockchain_instance=peerplays)
    account_info = {
        "id": account["id"],
        "name": account["name"],
        "owner": account["owner"],
        "active": account["active"],
        "options": account["options"],
        "balances": account.balances,
        # Add any other attributes you need here
    }
    return account_info