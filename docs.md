# block explorer

## import
``` python
from blockstream import blockexplorer
```

## get transaction
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
transaction = blockexplorer.get_transaction(tx_id)
```
## get transaction status
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_status = blockexplorer.get_transaction_status(tx_id)
```
## get transaction hex
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_hex = blockexplorer.get_transaction_hex(tx_id)
```
## get transaction merkle proof
```python
tx_merkle_proof = blockexplorer.get_transaction_merkle_proof(tx_id)
```
## get transaction output status
```python
vout = '1B2fFAimxLTDgvtLPs212pa3f7ymHdVQmV'
tx_output_status = blockexplorer.get_transaction_output_status(tx_id, vout)
```
## get all transaction outputs statuses
```python
all_outspends = blockexplorer.get_all_transaction_outputs_statuses(tx_id)
```

# post a transaction
```python
# not added yet
```

## get information about an address
```python
address = 'bc1qw6lwxz3lxtg969hx7g0qnxfnm7608m3nxu7far'
addr_info = blockexplorer.get_address(address)
```
## get address transactions
```python
txs = blockexplorer.get_address_transactions(address)
```
## get confirmed transaction history
```python
confirmed_tx_hist = blockexplorer.get_confirmed_transaction_history(address)
```
## get address mempool
```python
addr_mempool = blockexplorer.get_address_mempool(address)
```
## get address utxo
```python
addr_utxo = blockexplorer.get_address_utxo(address)
```
## get mempool
```python
mempool = blockexplorer.get_mempool()
```
## get mempool transactions IDs
```python
mempool_tx_ids = blockexplorer.get_mempool_transaction_ids()
```
## get mempool recent transactions 
```python
recent_mempool_txs = blockexplorer.get_mempool_transaction_ids()
```
## get fee estimates
```python
fee_estimates = blockexplorer.get_fee_estimates()
```
## get hash from height
```python
block_hash = blockexplorer.get_block_hash_from_height('575165')
```
## get block from hash
```python
block_hash = '0000000000000000000cf9b9dd7bb882d825f4e3830dc9391425c40c56e82d7f'
block = blockexplorer.get_block_by_hash(block_hash)
```
## get block from height
```python
block = blockexplorer.get_block_by_height('575165')
```
## get block status by hash
```python
block_status = blockexplorer.get_block_status(block_hash)
```
## get block transactions by block hash
```python
transactions = blockexplorer.get_block_transactions(block_hash)
```
## get block transaction IDs by block hash
```python
txids = blockexplorer.get_transaction_ids(block_hash)
```
## get 10 most recent blocks
```python
recents = blockexplorer.get_blocks()
```
## get 10 blocks starting at specified height
```python
height_of_interest = '575135'
ten_blocks = blockexplorer.get_blocks(height_of_interest)
```
## get last block height
```python
tip_height = blockexplorer.get_last_block_height()
```
## get last block hash
```python
tip_hash = blockexplorer.get_last_block_hash()
```