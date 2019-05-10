# documentation
# BlockExplorer
## import
``` python
from blockstream import BlockExplorer
```
## Initialize BlockExplorer Object
```python
explorer = BlockExplorer()
```
## get transaction
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
transaction = explorer.get_transaction(tx_id)
```
## get transaction status
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_status = explorer.get_transaction_status(tx_id)
```
## get transaction hex
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_hex = explorer.get_transaction_hex(tx_id)
```
## get transaction merkle proof
```python
tx_merkle_proof = explorer.get_transaction_merkle_proof(tx_id)
```
## get transaction output status
```python
vout = '1B2fFAimxLTDgvtLPs212pa3f7ymHdVQmV'
tx_output_status = explorer.get_transaction_output_status(tx_id, vout)
```
## get all transaction outputs statuses
```python
all_outspends = explorer.get_all_transaction_outputs_statuses(tx_id)
```

# post a transaction
```python
# not added yet
```

## get information about an address
```python
address = 'bc1qw6lwxz3lxtg969hx7g0qnxfnm7608m3nxu7far'
addr_info = explorer.get_address(address)
```
## get address transactions
```python
txs = explorer.get_address_transactions(address)
```
## get confirmed transaction history
```python
confirmed_tx_hist = explorer.get_confirmed_transaction_history(address)
```
## get address mempool
```python
addr_mempool = explorer.get_address_mempool(address)
```
## get address utxo
```python
addr_utxo = explorer.get_address_utxo(address)
```
## get mempool
```python
mempool = explorer.get_mempool()
```
## get mempool transactions IDs
```python
mempool_tx_ids = explorer.get_mempool_transaction_ids()
```
## get mempool recent transactions 
```python
recent_mempool_txs = explorer.get_mempool_transaction_ids()
```
## get fee estimates
```python
fee_estimates = explorer.get_fee_estimates()
```
## get hash from height
```python
block_hash = explorer.get_block_hash_from_height('575165')
```
## get block from hash
```python
block_hash = '0000000000000000000cf9b9dd7bb882d825f4e3830dc9391425c40c56e82d7f'
block = explorer.get_block_by_hash(block_hash)
```
## get block from height
```python
block = explorer.get_block_by_height('575165')
```
## get block status by hash
```python
block_status = explorer.get_block_status(block_hash)
```
## get block transactions by block hash
```python
transactions = explorer.get_block_transactions(block_hash)
```
## get block transaction IDs by block hash
```python
txids = explorer.get_transaction_ids(block_hash)
```
## get 10 most recent blocks
```python
recents = explorer.get_blocks()
```
## get 10 blocks starting at specified height
```python
height_of_interest = '575135'
ten_blocks = explorer.get_blocks(height_of_interest)
```
## get last block height
```python
tip_height = explorer.get_last_block_height()
```
## get last block hash
```python
tip_hash = explorer.get_last_block_hash()
```