import json
from peerplays import PeerPlays
from peerplays.block import Block
from peerplays.witness import Witness

# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

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

        return block_info
    except Exception as e:
        print(f"Error fetching block {block_num}: {e}")
        return None