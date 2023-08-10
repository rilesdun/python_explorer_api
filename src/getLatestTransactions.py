from peerplays import PeerPlays
from peerplays.block import Block
from collections import deque

# connect to a peerplays1 node
peerplays = PeerPlays("wss://ca.peerplays.info/api")

# storing the latest blocks that contain transactions
blocks_with_transactions = deque(maxlen=1000)

def update_blocks_with_transactions():
    latest_block_num = peerplays.info()["head_block_number"]

    # If the deque is empty, start from the latest block
    # Otherwise, start from the next block after the latest block in the deque
    start_block_num = blocks_with_transactions[-1]["block_num"] + 1 if blocks_with_transactions else latest_block_num

    # Go through each block from start_block_num to latest_block_num
    for block_num in range(start_block_num, latest_block_num + 1):
        block = Block(block_num, blockchain_instance=peerplays)

        # If the block contains transactions, add it to the deque
        if block["transactions"]:
            blocks_with_transactions.append({
                "block_num": block_num,
                "transactions": block["transactions"]
            })

def get_latest_transactions(num_transactions=10):
    
    update_blocks_with_transactions()
    transactions = []
    for block in reversed(blocks_with_transactions):
        # add the transactions from this block to the list
        transactions.extend(block["transactions"])

        if len(transactions) >= num_transactions:
            return transactions[:num_transactions]

    # If we've gone through all blocks in the deque and still haven't found enough transactions,
    # just return what we have
    return transactions