from peerplays.blockchain import Blockchain
from peerplays import PeerPlays

def get_latest_block():
    # Connect to a PeerPlays node
    peerplays = PeerPlays("wss://ca.peerplays.info/api")
    chain = Blockchain(blockchain_instance=peerplays)

    # Get the latest block
    latest_block = None
    for block in chain.blocks():
        latest_block = block
        break  # Exit the loop after getting the first block

    return latest_block