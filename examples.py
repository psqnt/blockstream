"""
Example uses for blockstream.info api wrapper class
"""
import datetime

from wrapper import BlockExplorer


def get_genesis_block(explorer):
    """
    Get genesis block (block 0)
    """
    height = '0'
    return explorer.get_block_by_height(height)


def get_genesis_block_by_hash(explorer):
    """
    Use hash
    """
    tx_hash = explorer.get_block_hash_from_height('0')
    return explorer.get_block_by_hash(tx_hash)


# Testing
explorer = BlockExplorer()

print(get_genesis_block(explorer))
print(get_genesis_block_by_hash(explorer))

# get hash from height
block_hash = explorer.get_block_hash_from_height('575165')
print(block_hash)

# get block from hash
block = explorer.get_block_by_hash(block_hash)
print(block)

# get block from height
block = explorer.get_block_by_height('575165')
print(block)

# get block status by hash
block_status = explorer.get_block_status(block_hash)
print(block_status)

# get block transactions by block hash
transactions = explorer.get_block_transactions(block_hash)
print(transactions)

# get block transaction IDs by block hash
txids = explorer.get_transaction_ids(block_hash)
print(txids)

# get 10 most recent blocks
recents = explorer.get_blocks()
print(recents)

# get 10 blocks starting at specified height
height_of_interest = '575135'
ten_blocks = explorer.get_blocks(height_of_interest)
print(ten_blocks)

# get last block height
tip_height = explorer.get_last_block_height()
print(tip_height)

# get last block hash
tip_hash = explorer.get_last_block_hash()
print(tip_hash)


# good example would be to show total transactions each day over past 10 days

# Look up all blocks in past 10 days

# divide those blocks into each day they occured

# total the number of transactions in all those blocks

# implement a function that gives you all blocks that occured on a certain day

# a function that gives you all transactions that occured on a certain day

# size of mempool given a specific day

# total number of transactions

# average number of transactions per day (since inception, 1 month, 1 year, 3 months, etc)

# average size of block per day ...

# average weight of block per day ...

#### IN A SEPARATE PROGRAM

# pull all that data in and match the data with price at the time (average, high, low)

# build an API wrapper for a price data provider (maybe block stream)