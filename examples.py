"""
Example uses for blockstream.info api wrapper class
"""
import datetime

from blockstream import BlockExplorer, Block, Address, Transaction, Mempool


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


# get transaction
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
transaction = explorer.get_transaction(tx_id)
print(transaction)

# get transaction status
tx_status = explorer.get_transaction_status(tx_id)
print(tx_status)

# get transaction hex
tx_hex = explorer.get_transaction_hex(tx_id)
print(tx_hex)

# get transaction merkle proof
tx_merkle_proof = explorer.get_transaction_merkle_proof(tx_id)
print(tx_merkle_proof)

# get transaction output status
vout = '1B2fFAimxLTDgvtLPs212pa3f7ymHdVQmV'
tx_output_status = explorer.get_transaction_output_status(tx_id, vout)
print(tx_output_status)

# get all transaction outputs statuses
all_outspends = explorer.get_all_transaction_outputs_statuses(tx_id)
print(all_outspends)

# post a transaction


# get information about an address
address = 'bc1qw6lwxz3lxtg969hx7g0qnxfnm7608m3nxu7far'
addr_info = explorer.get_address(address)
print(addr_info)

# get address transactions
txs = explorer.get_address_transactions(address)
print(txs)

# get confirmed transaction history
confirmed_tx_hist = explorer.get_confirmed_transaction_history(address)
print(confirmed_tx_hist)

# get address mempool
addr_mempool = explorer.get_address_mempool(address)
print(addr_mempool)

# get address utxo
addr_utxo = explorer.get_address_utxo(address)
print(addr_utxo)

# get script has mempool
#sh_mempool = explorer.get_script_hash_mempool(script_hash)
#print(sh_mempool)

# get information about a scripthash
#script_hash = '3NukJ6fYZJ5Kk8bPjycAnruZkE5Q7UW7i8'
#sh_info = explorer.get_script_hash(script_hash)
#print(sh_info)

# get script hash transactions
#sh_txs = explorer.get_script_hash_transactions(script_hash)
#print(sh_txs)

# get confirmed script_hash transaction history
#sh_tx_hist = explorer.get_confirmed_script_hash_transaction_history(script_hash)
#print(sh_tx_hist)

# get script hash utxo
#sh_utxo = explorer.get_script_hash_utxo(script_hash)
#print(sh_utxo)

# get mempool
mempool = explorer.get_mempool()
print(mempool)

# get mempool transactions IDs
mempool_tx_ids = explorer.get_mempool_transaction_ids()
print(mempool_tx_ids)

# get mempool recent transactions 
recent_mempool_txs = explorer.get_mempool_transaction_ids()
print(recent_mempool_txs)

# get fee estimates
fee_estimates = explorer.get_fee_estimates()

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

blocks = []
for b in ten_blocks:
    block = Block(b['id'], b['height'], b['version'], b['timestamp'], 
            b['tx_count'], b['size'], b['weight'], b['merkle_root'], 
            b['previousblockhash'], b['nonce'], b['bits'])
    blocks.append(block)

for block in blocks:
    print(block.id, block.tx_count, block.timestamp)