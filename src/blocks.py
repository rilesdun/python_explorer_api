"""
Functions related to peerplays blocks
"""

import logging

from peerplays.block import Block
from peerplays.witness import Witness
from peerplays_instance import peerplays

logger = logging.getLogger(__name__)



def get_block_info(block_num=None):
    """
    Fetches and returns information about a specific block in the PeerPlays blockchain.

    If no block number is provided, information about the latest block is returned.

    :param block_num: The number of the block to fetch information about.. 
    If None, fetches the latest block.
    :type block_num: int, optional
    :return: A dictionary containing information about the block, or None if an error occurs.
    :rtype: dict or None
    """
    try:
        # if no block number is given - fetch the latest block
        if block_num is None:
            block_num = peerplays.info()["head_block_number"]

        # grab the block
        block = Block(block_num, blockchain_instance=peerplays)

        witness = Witness(block["witness"], blockchain_instance=peerplays)

        num_transactions = len(block["transactions"])
        # create a dictionary with the block information
        block_info = {
            "Current block number": block_num,
            "Previous block number": block_num - 1,
            "Previous block ID": block["previous"],
            "Witness ID": block["witness"],
            "Witness Name": witness.account["name"],
            "Transactions": block["transactions"],
            "Number of Transactions": num_transactions
        }

        logger.info("Successfully fetched block %s", block_num)
        return block_info

    except Exception as exception: # pylint: disable=broad-except
        logger.error("Error fetching block %s: %s", block_num, exception, exc_info=True)
    return None
    