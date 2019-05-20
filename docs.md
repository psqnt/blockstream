# blockstream block explorer documentation
A python 3 api-wrapper for https://blockstream.info bitcoin blockchain explorer

# Usage
## Install
Any of the following will work.

If In a python3 virtual environment use:
```
pip install blockstream
```
Otherwise use one of the following
```
pip3 install blockstream
```
```
python3 -m pip install blockstream
```
## import
``` python
from blockstream import blockexplorer
```

## API Rate Limits
There is nothing formal in the documentation but this works
```python
sleep_time = .25  # don't overstep rate limits
```

# Transactions
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#transactions

Example JSON response for transaction:
https://blockstream.info/api/tx/546681da510fcdd4b6712b96a791ca5084005f7276f235767c28f91ef0141c9e

## `Transaction` Class
```
+ id: str
+ version: int
+ locktime: int
+ vin: list
+ vout: list
+ size: int
+ weight: int
+ fee: int
+ status: dict
```

## get transaction
Returns an instance of `Transaction` class
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
transaction = blockexplorer.get_transaction(tx_id)
```

## `TransactionStatus` Class
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-txtxidstatus

```
+ confirmed
+ block_height
+ block_hash
+ block_time
```
## get transaction status
Returns an instance of `TransactionStatus` class
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_status = blockexplorer.get_transaction_status(tx_id)
```
## get transaction hex
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-txtxidhex

Returns a string
```python
tx_id = '73236c12b8595c85dc629e1e01e4a0938376fb6c219632a97429ab59d6c0fac3'
tx_hex = blockexplorer.get_transaction_hex(tx_id)
```

## `TransactionMerkleProof` Class
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-txtxidmerkle-proof

```
+ block_height
+ merkle
+ pos
```
## get transaction merkle proof
Returns an instance of `TransactionMerkleProof` class
```python
tx_merkle_proof = blockexplorer.get_transaction_merkle_proof(tx_id)
```

## `TransactionOutput` Class
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-txtxidoutspendvout

```
+ spend
+ tx_id
+ vin
+ status
```

## get transaction output status
Returns an instance of `TransactionOutput` class
```python
vout = '1B2fFAimxLTDgvtLPs212pa3f7ymHdVQmV'
tx_output_status = blockexplorer.get_transaction_output_status(tx_id, vout)
```
## get all transaction outputs statuses
Returns a list of `TransactionOutput` objects
```python
all_outspends = blockexplorer.get_all_transaction_outputs_statuses(tx_id)
```

# post a transaction
```python
# not added yet
```

# Addresses
Example JSON response for Address:
https://blockstream.info/api/address/3ADPkym6mQ2HyP7uASh5g3VYauhCWZpczF

## `Address` class
```
+ address: str
+ chain_stats: dict
+ mempool_stats: dict
```
## get an address
Get information about an address

Returns an instance of `Address` class
```python
address = 'bc1qw6lwxz3lxtg969hx7g0qnxfnm7608m3nxu7far'
addr_info = blockexplorer.get_address(address)
```
## get address transactions
Get transactions that an address has taken part in

Returns a list of `Transaction` objects
```python
txs = blockexplorer.get_address_transactions(address)
```
## get confirmed transaction history
Returns a list of `Transaction` objects
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

# Mempool
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#mempool

Example JSON response: https://blockstream.info/api/mempool

## `Mempool` Class

```
+ count
+ vsize
+ total_fee
+ fee_histogram
```
## get mempool
Returns an instance of `Mempool` class
```python
mempool = blockexplorer.get_mempool()
```
## get mempool transactions IDs
Returns a list of of type `str` (Transaction hashes/IDs)
```python
mempool_tx_ids = blockexplorer.get_mempool_transaction_ids()
```
## `MempoolRecent` Class
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-mempoolrecent

Example JSON Response: https://blockstream.info/api/mempool/recent
```
+ tx_id: str
+ fee: int
+ vsize: int
+ value: int
```

## get mempool recent transactions
Returns an instance of `MempoolRecent` class

```python
recent_mempool_txs = blockexplorer.get_mempool_transaction_ids()
```
# FeeEstimates
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#fee-estimates

Example JSON Response: https://blockstream.info/api/fee-estimates
## `FeeEstimates` class
```
+ two_blocks: float
+ three_blocks: float
+ four_blocks: float
+ six_blocks: float
+ ten_blocks: float
+ twenty_blocks: float
+ onefourfour_blocks: float
+ fivezerofour_blocks: float
+ tenzeroeight_blocks: float
```
## get fee estimates
Returns an instance of `FeeEstimates` class
```python
fee_estimates = blockexplorer.get_fee_estimates()
```

# Blocks
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#blocks

Example JSON Response: https://blockstream.info/api/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f

## get hash from height
Returns a block hash. Return type: `str`
```python
block_hash = blockexplorer.get_block_hash_from_height('575165')
```

## `Block` Class
```
+ id: str
+ height: int
+ version: int
+ timestamp: int
+ tx_count: int
+ size: int
+ weight: int
+ merkle_root: str
+ previous_block_hash: str
+ nonce: int
+ bits: int
```

## get block from hash
Returns an instance of `Block` Class
```python
block_hash = '0000000000000000000cf9b9dd7bb882d825f4e3830dc9391425c40c56e82d7f'
block = blockexplorer.get_block_by_hash(block_hash)
```
## get block from height
Returns an instance of `Block` Class
```python
block = blockexplorer.get_block_by_height('575165')
```

## `BlockStatus` Class
API Docs: https://github.com/Blockstream/esplora/blob/master/API.md#get-blockhashstatus

Example JSON response: https://blockstream.info/api/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f/status

```
+ in_best_chain: boolean
+ height: int
+ next_best: str
```

## get block status by hash
Returns an intance of `BlockStatus` class

```python
block_status = blockexplorer.get_block_status(block_hash)
```
## get block transactions by block hash
Get a list of transactions in a specific block

Returns a list of `Transaction` objects
```python
transactions = blockexplorer.get_block_transactions(block_hash)
```
## get block transaction IDs by block hash
Get a list of transaction hashes/IDs

Returns a list of type: `str`

```python
txids = blockexplorer.get_transaction_ids(block_hash)
```
## get 10 most recent blocks
Returns a list of `Block` objects

```python
recents = blockexplorer.get_blocks()
```
## get 10 blocks starting at specified height
Returns a list of `Block` objects

```python
height_of_interest = '575135'
ten_blocks = blockexplorer.get_blocks(height_of_interest)
```
## get last block height
Get the most recent block height

Return type: `int`
```python
tip_height = blockexplorer.get_last_block_height()
```
## get last block hash
Get the most recent block hash

Return type: `str`
```python
tip_hash = blockexplorer.get_last_block_hash()
```
