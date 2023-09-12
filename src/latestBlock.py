from peerplays.blockchain import Blockchain
from peerplays import PeerPlays

from config import api_url

peerplays = PeerPlays(api_url)

def get_latest_block():
    chain = Blockchain(blockchain_instance=peerplays)

    # Get the latest block
    latest_block = None
    for block in chain.blocks():
        latest_block = block
        break 

    return latest_block