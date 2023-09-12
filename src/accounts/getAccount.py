from peerplays.account import Account
from peerplays import PeerPlays
from config import api_url

peerplays = PeerPlays(api_url)

def get_account_info(account_name):
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