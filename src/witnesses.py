from peerplays import PeerPlays
from peerplays.witness import Witnesses
from peerplays.account import Account

# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

def list_active_witnesses():
    witnesses = Witnesses(blockchain_instance=peerplays)
    witness_info = []

    # grab attributes of each witness
    for witness in witnesses:
        account = Account(witness["witness_account"], blockchain_instance=peerplays)
        witness_info.append({
            "account_name": account['name'],
        
            "witness_data": {key: value for key, value in witness.items()}
        })
        
        witness_info = sorted(witness_info, key=lambda x: x['witness_data']['total_votes'], reverse=True)

    return witness_info