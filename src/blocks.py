import json
import logging
from peerplays import PeerPlays
from peerplays.block import Block
from peerplays.witness import Witness
from config import api_url

logger = logging.getLogger(__name__)



peerplays = PeerPlays(api_url)


def get_block_info(block_num=None):
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

        logger.info(f"Successfully fetched block {block_num}")
        return block_info
    
    except Exception as e:
        logger.error(f"Error fetching block {block_num}: {e}", exc_info=True)
        return None