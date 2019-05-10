# blockstream
A python wrapper class for blockstream.info's Bitcoin block explorer API

written in Python 3

Block explorer: https://blockstream.info

API Reference: https://github.com/Blockstream/esplora/blob/master/API.md

## Install
```
pip install blockstream
```
or sometimes
```
pip3 install blockstream
```

### Usage
```python
from blockstream import BlockExplorer

explorer = BlockExplorer()

# get transaction by id
tx_id = '3NukJ6fYZJ5Kk8bPjycAnruZkE5Q7UW7i8'
tx = explorer.get_transaction(tx_id)
```

### Examples
Reference examples.py to see each method in use
