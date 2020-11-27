# blockstream
A python 3 wrapper and CLI for blockstream.info's Bitcoin block explorer API

Written in Python 3

Docs: https://github.com/psqnt/blockstream/blob/master/docs.md

Block explorer: https://blockstream.info

API Reference: https://github.com/Blockstream/esplora/blob/master/API.md

## Install
```
pip install blockstream
```

if not in a python3 virtualenv make sure to use python3
```
pip3 install blockstream
```

## Usage
This will install a command line tool called `bsapi` or 
you can import into a python project

#### Command Line Tool Help
```
Usage: bsapi [OPTIONS] [INFILE] [OUTFILE] COMMAND [ARGS]...

Options:
  -v, --verbose
  --help         Show this message and exit.

Commands:
  request  Makes a request to blockstream info api and echos response
```

```python
from blockstream import blockexplorer

# get transaction by id
tx_id = '56a5b477182cddb6edb460b39135a3dc785eaf7ea88a572052a761d6983e26a2'
tx = blockexplorer.get_transaction(tx_id)

# get address data
address = '3ADPkym6mQ2HyP7uASh5g3VYauhCWZpczF'
addr_info = blockexplorer.get_address(address)
```

## Examples
Reference examples.py to see each method in use

#### Command Line Tool Examples:
```
echo -n "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f" | bsapi - - request --param_type transaction
```
```
echo -n "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f" | bsapi - - request --param_type hash
{
  "id": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
  "height": 0,
  "version": 1,
  "timestamp": 1231006505,
  "tx_count": 1,
  "size": 285,
  "weight": 816,
  "merkle_root": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
  "previous_block_hash": null,
  "nonce": 2083236893,
  "bits": 486604799
}
```
bsapi - - request 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f --param_type hash
{
  "id": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
  "height": 0,
  "version": 1,
  "timestamp": 1231006505,
  "tx_count": 1,
  "size": 285,
  "weight": 816,
  "merkle_root": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
  "previous_block_hash": null,
  "nonce": 2083236893,
  "bits": 486604799
}
```

## Issues
the `scripthash` endpoint seems to be broken, however you can get data about a scripthash address by calling the `address` endpoint. I have decided to remove the functions to hit the `scripthash` endpoint for now.

Also the broadcast transaction api endpoint has not been implemented yet
