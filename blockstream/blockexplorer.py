from . import util


def get_transaction(tx_id):
    """
    Request information about a transaction by ID
    :param str tx_id: transaction ID 
    :return: an instance of :class:`Transaction` class
    """
    resource = f'tx/{tx_id}'
    tx_data = util.call_api(resource)
    return Transaction(tx_data)


def get_transaction_status(tx_id):
    """
    Request the transaction confirmation status
    :param str tx_id: transaction ID
    :return: an instance of :class:`TransactionStatus` class
    """
    resource = f'tx/{tx_id}/status'
    response = util.call_api(resource)
    return TransactionStatus(response)


def get_transaction_hex(tx_id):
    """
    Request the raw transaction in hex
    :param str tx_id: transaction ID
    :return: dictionary containing tx hex
    """
    resource = f'tx/{tx_id}/hex'
    response = util.call_api(resource)
    return response  # figure this better maybe


def get_transaction_merkle_proof(tx_id):
    """
    Request the merkle intrusion proof of a transaction
    :param str tx_id: transaction ID
    :return: an instance of :class:`TransactionMerkle` class
    """
    resource = f'tx/{tx_id}/merkle-proof'
    response = util.call_api(resource)
    return TransactionMerkleProof(response)


def get_transaction_output_status(tx_id, vout):
    """
    Request the spending status of a transaction output
    :param str tx_id: transaction ID
    :param str vout: transaction output
    :return: an instance of :class:`TransactionOutput` class
    """
    resource = f'tx/{tx_id}/outspend/{vout}'
    response = util.call_api(resource)
    return TransactionOutput(response)


def get_all_transaction_outputs_statuses(tx_id):
    """
    Request the spending status of all transaction outputs
    :param str tx_id: transaction ID
    :return list: a list of :class:`TransactionOutput` objects
    """
    resource = f'tx/{tx_id}/outspends'
    response = util.call_api(resource)
    outspends = []
    for output in response:
        outspends.append(TransactionOutput(output))
    return outspends


def post_transaction():
    """
    Broadcast a raw transaction to the network
    """
    pass


def get_address(address):
    """
    Request address information
    :param str address: a bitcoin address/scripthash
    :return: an instance of :class:`Address` class
    """
    resource = f'address/{address}'
    response = util.call_api(resource)
    return Address(response)


def get_address_transactions(address):
    """
    Request all transactions for an address, newest first
    """
    resource = f'address/{address}/txs'
    response = util.call_api(resource)
    transactions = []
    for tx in response:
        transactions.append(Transaction(tx))
    return transactions


def get_confirmed_transaction_history(address, ls_tx_id=''):
    """
    Request confirmed transaction history for an address, newest first
    25 per page
    :param str address: a bitcoin address
    :param str ls_tx_id: last transaction ID
    :return list: 
    """
    resource = f'address/{address}/txs/chain/{ls_tx_id}'
    response = util.call_api(resource)
    confirmed_transactions = []
    for tx in response:
        confirmed_transactions.append(Transaction(tx))
    return confirmed_transactions


def get_address_mempool(address):
    """
    Request unconfirmed transaction history of an address, newest first
    up to 50 transactions no paging
    :param str address: a bitcoin address
    :return list: a list of :class:`Transaction` objects
    """
    resource = f'address/{address}/txs/mempool'
    response = util.call_api(resource)
    mempool_transactions = []
    for tx in response:
        mempool_transactions.append(Transaction(tx))
    return mempool_transactions


def get_address_utxo(address):
    """
    Request the list of unspent transaction outputs associated with
    an address
    :param str address: a bitcoin address
    :return list: a list of :class:`UTXO` objects
    """
    resource = f'address/{address}/utxo'
    response = util.call_api(resource)
    utxo_list = []
    for utxo in response:
        utxo_list.append(UTXO(utxo))
    return utxo_list


def get_block_by_hash(block_hash):
    """
    Request a given block by hash
    :param str block_hash: a bitcoin block hash
    :return: an instance of :class:`Block` class
    """
    resource = f'block/{block_hash}'
    response = util.call_api(resource)
    return Block(response)


def get_block_by_height(height):
    """
    Request a given block by height
    :param str height: a bitcoin block height
    :return: an instance of :class:`Block` class
    """
    block_hash = get_block_hash_from_height(height)
    resource = f'block/{block_hash}'
    response = util.call_api(resource)
    return Block(response)


def get_block_hash_from_height(height):
    """
    Request a block hash by specifying the height
    :param str height: a bitcoin block height
    :return: a bitcoin block address
    """
    resource = f'block-height/{height}'
    return util.call_api(resource)


def get_block_status(block_hash):
    """
    Request the block status
    :param str block_hash: a bitcoin block hash
    :return: an instance of :class:`BlockStatus` class
    """
    resource = f'block/{block_hash}/status'
    response = util.call_api(resource)
    return BlockStatus(response)


def get_block_transactions(block_hash, start_index='0'):
    """
    Request a list of transactions in a block (up to 25)
    :param str block_hash: a bitcoin block hash
    :param str start_index: index of transaction list to start from
    """
    resource = f'block/{block_hash}/txs/{start_index}'
    response = util.call_api(resource)
    transactions = []
    for tx in response:
        transactions.append(Transaction(tx))
    return transactions


def get_transaction_ids(block_hash):
    """
    Request a list of all transaction IDs in a block
    :param str block_hash: a bitcoin block hash
    :return: a list of transaction IDs in the block
    """
    resource = f'block/{block_hash}/txids'
    response = util.call_api(resource)
    return response


def get_blocks(start_height=''):
    """
    Request the 10 newest blocks starting at tip (most recent)
    or at start_height (optional)
    :param str start_height: block height
    :return: a list of :class:`Block` objects
    """
    resource = f'blocks/{start_height}'
    response = util.call_api(resource)
    blocks = []
    for block in response:
        blocks.append(Block(block))
    return blocks


def get_last_block_height():
    """
    Request the height of the last block
    :return dict: most recent block height in bitcoin
    """
    resource = 'blocks/tip/height'
    return util.call_api(resource)


def get_last_block_hash():
    """
    Request the hash of the last block
    """
    resource = 'blocks/tip/hash'
    return util.call_api(resource)


def get_mempool():
    """
    Request mempool backlog statistics
    """
    response = util.call_api('mempool')
    return Mempool(response)


def get_mempool_transaction_ids():
    """
    Request the full list of transactions IDs currently in the mempool,
    as an array
    :return list: a list of transaction IDs
    """
    resource = 'mempool/txids'
    return util.call_api(resource)


def get_mempool_recent_transactions():
    """
    Request a list of the last 10 transactions to enter the mempool
    :return list: a list of transaction IDs
    """
    resource = 'mempool/recent'
    response = util.call_api(resource)
    transactions = []
    for tx in response:
        transactions.append(MempoolRecent(tx))
    return transactions


def get_fee_estimates():
    """
    Request an object where the key is the confirmation target (in number
    of blocks) and the value is estimated fee rate (in sat/vB)
    :return: an instance of :class:`FeeEstimate` class
    """
    response = util.call_api('fee-estimates')
    return FeeEstimates(response)


class BlockStatus:
    """Bitcoin block status utility."""
    def __init__(self, status):
        self.in_best_chain = status['in_best_chain']
        self.height = status['height']
        self.next_best = status['next_best']

    def __str__(self):
        return str(vars(self))


class Block:
    """Bitcoin block utility class"""
    def __init__(self, block):
        self.id = block['id']
        self.height = block['height']
        self.version = block['version']
        self.timestamp = block['timestamp']
        self.tx_count = block['tx_count']
        self.size = block['size']
        self.weight = block['weight']
        self.merkle_root = block['merkle_root']
        self.previous_block_hash = block['previousblockhash']
        self.nonce = block['nonce']
        self.bits = block['bits']

    def __str__(self):
        return str(vars(self))


class Address:
    """Bitcoin Address utility class."""
    def __init__(self, address):
        self.address = address['address']  # str
        self.chain_stats = address['chain_stats']  # dict
        self.mempool_stats = address['mempool_stats']  # dict

    def __str__(self):
        return str(vars(self))


class UTXO:
    """Bitcoin UTXO utility class."""
    def __init__(self, utxo):
        self.tx_id = utxo['txid']
        self.vout = utxo['vout']
        self.status = TransactionStatus(utxo['status'])
        self.value = utxo['value']

    def __str__(self):
        return str(vars(self))


class TransactionStatus:
    """Transaction status utility."""
    def __init__(self, status):
        self.confirmed = status.get('confirmed')
        self.block_height = status.get('block_height')
        self.block_hash = status.get('block_hash')
        self.block_time = status.get('block_time')

    def __str__(self):
        return str(vars(self))


class TransactionMerkleProof:
    """Tx Merkle proof utility."""
    def __init__(self, merkle):
        self.block_height = merkle['block_height']
        self.merkle = merkle['merkle']
        self.pos = merkle['pos']

    def __str__(self):
        return str(vars(self))


class TransactionOutput:
    """Tx Output utility."""
    def __init__(self, output):
        self.spend = output['spent']
        self.tx_id = output['txid']
        self.vin = output['vin']
        self.status = TransactionStatus(output['status'])

    def __str__(self):
        return str(vars(self))


class Transaction:
    """Bitcoin Transaction utility class."""
    def __init__(self, transaction):
        print(transaction)
        self.id = transaction['txid']
        self.version = transaction['version']
        self.locktime = transaction['locktime']
        self.vin = transaction['vin']
        self.vout = transaction['vout']
        self.size = transaction['size']
        self.weight = transaction['weight']
        self.fee = transaction['fee']
        self.status = TransactionStatus(transaction['status'])

    def __str__(self):
        return str(vars(self))


class Mempool:
    """Bitcoin Mempool utility class."""
    def __init__(self, mempool):
        self.count = mempool['count']
        self.vsize = mempool['vsize']
        self.total_fee = mempool['total_fee']
        self.fee_histogram = mempool['fee_histogram']

    def __str__(self):
        return str(vars(self))


class MempoolRecent:
    """Recent TXs in mempool utility."""
    def __init__(self, info):
        self.tx_id = info['txid']
        self.fee = info['fee']
        self.vsize = info['vsize']
        self.value = info['value']

    def __str__(self):
        return str(vars(self))


class FeeEstimates:
    """Fee Estimates utility class."""
    def __init__(self, data):
        self.two_blocks = data['2']
        self.three_blocks = data['3']
        self.four_blocks = data['4']
        self.six_blocks = data['6']
        self.ten_blocks = data['10']
        self.twenty_blocks = data['20']
        self.onefourfour_blocks = data['144']
        self.fivezerofour_blocks = data['504']
        self.tenzeroeight_blocks = data['1008']

    def __str__(self):
        return str(vars(self))
