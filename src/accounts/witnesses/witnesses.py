"""
This module contains functions to fetch the list of active witnesses.
"""
import logging
from peerplays import PeerPlays
from peerplays.witness import Witnesses
from peerplays.account import Account
from cache_config import cache



# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

logger = logging.getLogger(__name__)

@cache.cached(timeout=1200)
def list_active_witnesses():
    """
    This function returns the list of active witnesses.
    """
    witnesses = Witnesses(blockchain_instance=peerplays)
    witness_info = []

    # grab attributes of each witness
    for witness in witnesses:
        account = Account(witness["witness_account"], blockchain_instance=peerplays)
        witness_info.append({
            "account_name": account['name'],
            "witness_data": {key: value for key, value in witness.items()}
        })

    witness_info = sorted(witness_info, key=lambda x: x['witness_data']['total_votes'], 
                          reverse=True)

    logger.info("Successfully fetched %s active witnesses", len(witness_info))
    return witness_info
