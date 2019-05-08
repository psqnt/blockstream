"""
A python wrapper for blockstream.info API

reference:
https://github.com/Blockstream/esplora/blob/master/API.md
"""

import requests


class BlockExplorer:
    """
    Interact with blockstream's block explorer
    """

    def __init__(self):
        self.base_url = 'https://blockstream.info/api/'
    
    def get_block_by_hash(self, block_hash):
        """
        Request a given block by hash
        """
        method = 'block/'
        url = self.base_url + method + block_hash
        return requests.get(url).content.decode('utf-8')
    
    def get_block_by_height(self, height):
        """
        Request a given block by height
        """
        method = 'block-height/'
        url = self.base_url + method + height
        block_hash = requests.get(url).content.decode('utf-8')
        return self.get_block_by_hash(block_hash)

    def get_block_hash_from_height(self, height):
        """
        Request a block hash by specifying the height
        """
        method = 'block-height/'
        url = self.base_url + method + height
        return requests.get(url).content.decode('utf-8')
    
    def get_block_status(self, block_hash):
        """
        Request the block status
        """
        method = f'block/{block_hash}/status'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def get_block_transactions(self, block_hash, start_index='0'):
        """
        Request a list of transactions in a block (up to 25)
        """
        method = f'block/{block_hash}/txs/{start_index}'
        url = self.base_url + method
        print(url)
        return requests.get(url).content.decode('utf-8')
    
    def get_transaction_ids(self, block_hash):
        """
        Request a list of all transaction IDs in a block
        """
        method = f'block/{block_hash}/txids'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def get_blocks(self, start_height=None):
        """
        Request the 10 newest blocks starting at tip (most recent)
        or at start_height
        """
        if start_height is None:
            method = 'blocks/'
        else:
            method = 'blocks/{start_height}'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def get_last_block_height(self):
        """
        Request the height of the last block
        """
        method = 'blocks/tip/height'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def get_last_block_hash(self):
        """
        Request the hash of the last block
        """
        method = 'blocks/tip/hash'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    

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
