"""
Example uses for blockstream.info api wrapper class
"""
import datetime

from blockstream import blockexplorer


# get transaction
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
transaction = blockexplorer.get_transaction(tx_id)
print(transaction)

# get transaction status
tx_status = blockexplorer.get_transaction_status(tx_id)
print(tx_status)

# get transaction hex
tx_hex = blockexplorer.get_transaction_hex(tx_id)
print(tx_hex)

# get transaction merkle proof
tx_merkle_proof = blockexplorer.get_transaction_merkle_proof(tx_id)
print(tx_merkle_proof)

# get transaction output status
vout = '0'
tx_output_status = blockexplorer.get_transaction_output_status(tx_id, vout)
print(tx_output_status)

# get all transaction outputs statuses
all_outspends = blockexplorer.get_all_transaction_outputs_statuses(tx_id)
print(all_outspends)

# post a transaction


# get information about an address
address = 'bc1qw6lwxz3lxtg969hx7g0qnxfnm7608m3nxu7far'
addr_info = blockexplorer.get_address(address)
print(addr_info)

# get address transactions
txs = blockexplorer.get_address_transactions(address)
print(txs)

# get confirmed transaction history
confirmed_tx_hist = blockexplorer.get_confirmed_transaction_history(address)
print(confirmed_tx_hist)

# get address mempool
addr_mempool = blockexplorer.get_address_mempool(address)
print(addr_mempool)

# get address utxo
addr_utxo = blockexplorer.get_address_utxo(address)
print(addr_utxo)

# get mempool
mempool = blockexplorer.get_mempool()
print(mempool)

# get mempool transactions IDs
mempool_tx_ids = blockexplorer.get_mempool_transaction_ids()
#print(mempool_tx_ids)

# get mempool recent transactions 
recent_mempool_txs = blockexplorer.get_mempool_transaction_ids()
#print(recent_mempool_txs)

# get fee estimates
fee_estimates = blockexplorer.get_fee_estimates()

# get hash from height
block_hash = blockexplorer.get_block_hash_from_height('575165')
print(block_hash)

# get block from hash
block = blockexplorer.get_block_by_hash(block_hash)
print(block)

# get block from height
block = blockexplorer.get_block_by_height('575165')
print(block)

# get block status by hash
block_status = blockexplorer.get_block_status(block_hash)
print(block_status)

# get block transactions by block hash
transactions = blockexplorer.get_block_transactions(block_hash)
print(transactions)

# get block transaction IDs by block hash
txids = blockexplorer.get_transaction_ids(block_hash)
print(txids)

# get 10 most recent blocks
recents = blockexplorer.get_blocks()
print(recents)

# get 10 blocks starting at specified height
height_of_interest = '575135'
ten_blocks = blockexplorer.get_blocks(height_of_interest)
print(ten_blocks)

# get last block height
tip_height = blockexplorer.get_last_block_height()
print(tip_height)

# get last block hash
tip_hash = blockexplorer.get_last_block_hash()
print(tip_hash)
