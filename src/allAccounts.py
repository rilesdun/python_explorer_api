from peerplays import PeerPlays
from peerplays.witness import Witnesses
from peerplays.account import Account

# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

def list_all_accounts():
    # list of active witnesses
    witnesses = Witnesses(blockchain_instance=peerplays)

    # list to hold the witness information
    witness_info = []

    # grabbing attributes of each active witness to the list
    for witness in witnesses:
        account = Account(witness["witness_account"], blockchain_instance=peerplays)
        witness_info.append({
            "account_name": account['name'],
            "witness_data": {key: value for key, value in witness.items()}
        })

    return witness_info