"""
This file contains the function to get the latest block from the PeerPlays blockchain.
"""
from peerplays.blockchain import Blockchain
from peerplays_instance import peerplays


def get_latest_block():
    """
    This function returns the latest block from the PeerPlays blockchain.
    """
    chain = Blockchain(blockchain_instance=peerplays)

    latest_block = None
    for block in chain.blocks():
        latest_block = block
        break

    return latest_block
