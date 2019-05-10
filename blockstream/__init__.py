"""
A python wrapper for blockstream.info API

reference:
https://github.com/Blockstream/esplora/blob/master/API.md
"""
import datetime
import requests


class BlockExplorer:
    """
    Wrapper class for blockstream's block explorer
    """

    def __init__(self):
        self.base_url = 'https://blockstream.info/api/'
    
    def get_transaction(self, tx_id):
        """
        Request information about a transaction by ID
        """
        method = f'tx/{tx_id}'
        return self.make_json_request(method)
    
    def get_transaction_status(self, tx_id):
        """
        Request the transaction confirmation status
        """
        method = f'tx/{tx_id}/status'
        return self.make_json_request(method)
    
    def get_transaction_hex(self, tx_id):
        """
        Request the raw transaction in hex
        """
        method = f'tx/{tx_id}/hex'
        return self.make_request(method)
    
    def get_transaction_merkle_proof(self, tx_id):
        """
        Request the merkle intrusion proof of a transaction
        """
        method = f'tx/{tx_id}/merkle-proof'
        return self.make_json_request(method)
    
    def get_transaction_output_status(self, tx_id, vout):
        """
        Request the spending status of a transaction output
        """
        method = f'tx/{tx_id}/outspend/{vout}'
        return self.make_request(method)
    
    def get_all_transaction_outputs_statuses(self, tx_id):
        """
        Request the spending status of all transaction outputs
        """
        method = f'tx/{tx_id}/outspends'
        return self.make_json_request(method)
    
    def post_transaction(self):
        """
        Broadcast a raw transaction to the network
        """
        pass
    
    def get_address(self, address):
        """
        Request address information
        """
        method = f'address/{address}'
        return self.make_json_request(method)
    
    def get_script_hash(self, script_hash):
        """
        Request information about an address/scripthash
        """
        method = f'scripthash/{script_hash}'
        return self.make_request(method)
    
    def get_address_transactions(self, address):
        """
        Request all transactions for an address, newest first
        """
        method = f'address/{address}/txs'
        return self.make_json_request(method)
    
    def get_script_hash_transactions(self, script_hash):
        """
        Request all transactions for an address or script_hash,
        newest first
        """
        method = f'scripthash/{script_hash}/txs'
        return self.make_request(method)

    def get_confirmed_transaction_history(self, address, ls_tx_id=''):
        """
        Request confirmed transaction history for an address, newest first
        25 per page
        """
        method = f'address/{address}/txs/chain/{ls_tx_id}'
        return self.make_json_request(method)
    
    def get_confirmed_script_hash_transaction_history(self, sh, ls_tx_id=''):
        """
        Request confirmed transaction history for a script_hash, newest first
        25 per page
        """
        method = f'scripthash/{sh}/txs/chain/{ls_tx_id}'
        return self.make_request(method)
    
    def get_address_mempool(self, address):
        """
        Request unconfirmed transaction history of an address, newest first
        up to 50 transactions no paging
        """
        method = f'address/{address}/txs/mempool'
        return self.make_json_request(method)
    
    def get_script_hash_mempool(self, script_hash):
        """
        Request unconfirmed transaction history of a scripthash, newest first
        up to 50 transactions no paging
        """
        method = f'scripthash/{script_hash}/txs/mempool'
        return self.make_json_request(method)

    def get_address_utxo(self, address):
        """
        Request the list of unspent transaction outputs associated with
        an address
        """
        method = f'address/{address}/utxo'
        return self.make_json_request(method)
    
    def get_script_hash_utxo(self, script_hash):
        """
        Request the list of unspent transaction outputs associated with
        a scripthash
        """
        method = f'scripthash/{script_hash}/utxo'
        return self.make_json_request(method)

    def get_block_by_hash(self, block_hash):
        """
        Request a given block by hash
        """
        method = f'block/{block_hash}'
        return self.make_json_request(method)
    
    def get_block_by_height(self, height):
        """
        Request a given block by height
        """
        method = f'block-height/{height}'
        url = self.base_url + method
        block_hash = requests.get(url).content.decode('utf-8')
        return self.get_block_by_hash(block_hash)

    def get_block_hash_from_height(self, height):
        """
        Request a block hash by specifying the height
        """
        method = f'block-height/{height}'
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def get_block_status(self, block_hash):
        """
        Request the block status
        """
        method = f'block/{block_hash}/status'
        return self.make_json_request(method)
    
    def get_block_transactions(self, block_hash, start_index='0'):
        """
        Request a list of transactions in a block (up to 25)
        """
        method = f'block/{block_hash}/txs/{start_index}'
        return self.make_json_request(method)
    
    def get_transaction_ids(self, block_hash):
        """
        Request a list of all transaction IDs in a block
        """
        method = f'block/{block_hash}/txids'
        return self.make_json_request(method)
    
    def get_blocks(self, start_height=None):
        """
        Request the 10 newest blocks starting at tip (most recent)
        or at start_height
        """
        if start_height is None:
            method = 'blocks/'
        else:
            method = f'blocks/{start_height}'
        
        return self.make_json_request(method)
    
    def get_last_block_height(self):
        """
        Request the height of the last block
        """
        method = 'blocks/tip/height'
        return self.make_request(method)
    
    def get_last_block_hash(self):
        """
        Request the hash of the last block
        """
        method = 'blocks/tip/hash'
        return self.make_request(method)
    
    def get_mempool(self):
        """
        Request mempool backlog statistics
        """
        return self.make_request('mempool/')
    
    def get_mempool_transaction_ids(self):
        """
        Request the full list of transactions IDs currently in the mempool,
        as an array
        """
        method = 'mempool/txids'
        return self.make_json_request(method)

    def get_mempool_recent_transactions(self):
        """
        Request a list of the last 10 transactions to enter the mempool
        """
        method = 'mempool/recent'
        return self.make_json_request(method)
    
    def get_fee_estimates(self):
        """
        Request an object where the key is the confirmation target (in number
        of blocks) and the value is estimated fee rate (in sat/vB)
        """
        return self.make_request('fee-estimates/')
    
    def make_request(self, method):
        """
        Build a url and make an api request. use this for calls that don't 
        return in json format
        """
        url = self.base_url + method
        return requests.get(url).content.decode('utf-8')
    
    def make_json_request(self, method):
        """
        Build a url and make an api request for json formatted data
        """
        url = self.base_url + method
        return requests.get(url).json()


class Block:
    """Hold block data."""
    def __init__(self, id, height, version, timestamp, tx_count, size, 
                 weight, merkle_root, previous_block_hash, nonce, bits):
        self.id = id
        self.height = height
        self.version = version
        self.timestamp = timestamp
        self.tx_count = tx_count
        self.size = size
        self.weight = weight
        self.merkle_root = merkle_root
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce
        self.bits = bits


class Address:
    """Hold Address data."""
    def __init__(self, address, chain_stats, mempool_stats):
        self.address = address  # str
        self.chain_stats = chain_stats  # dict
        self.mempool_stats = mempool_stats  # dict


class Transaction:
    """Hold Transaction data."""
    def __init__(self, id, version, locktime, vin, 
                 vout, size, weight, fee, status):
        self.id = id
        self.version = version
        self.locktime = locktime
        self.vin = vin
        self.vout = vout
        self.size = size
        self.weight = weight
        self.fee = fee
        self.status = status


class Mempool:
    """Hold Mempool data."""
    def __init__(self, count, vsize, total_fee, fee_histogram):
        self.count = count
        self.vsize = vsize
        self.total_fee = total_fee
        self.fee_histogram = fee_histogram
