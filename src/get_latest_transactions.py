"""
This module is used to get the latest transactions from the Peerplays blockchain.
"""
from peerplays.block import Block
from peerplays_instance import peerplays

def get_block_with_transactions(block_num):
    """
    This function returns the block information for the given block number.
    """
    block = Block(block_num, blockchain_instance=peerplays)
    if block["transactions"]:
        return {
            "block_num": block_num,
            "transactions": block["transactions"]
        }
    return None

def get_latest_transactions(num_transactions=10):
    """
    This function returns the latest transactions.
    """
    latest_block_num = peerplays.info()["head_block_number"]
    transactions = []

    for block_num in range(latest_block_num, latest_block_num - 50, -1):
        block = get_block_with_transactions(block_num)
        if block:
            transactions.extend(block["transactions"])

        if len(transactions) >= num_transactions:
            return transactions[:num_transactions]

    return transactions
