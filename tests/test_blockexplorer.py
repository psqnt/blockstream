import unittest

from blockstream import blockexplorer, util
from blockstream.blockexplorer import (
    Block, BlockStatus, Transaction, Mempool, MempoolRecent, Mempool,
    Address, TransactionMerkleProof, TransactionOutput, TransactionStatus
)

class UtilTests(unittest.TestCase):
    """
    Tests for util.py
    """

    def server_response(self):
        response = util.call_api('blocks/')
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def server_error(self):
        response = util.call_api('doesntexist')
        self.assertEqual(response, 404)


class BlockExplorerTests(unittest.TestCase):
    """
    Tests for blockexplorer.py
    """
    TX_ID = '847b7d587541ef51e8dd50030affac416aa8d96a64470249cf847944f5198e6b'

    def test_get_transaction(self):
        tx = blockexplorer.get_transaction(self.TX_ID)
        self.assertIsInstance(tx, Transaction)
    
    def test_get_transaction_status(self):
        tx_status = blockexplorer.get_transaction_status(self.TX_ID)
        self.assertIsInstance(tx_status, TransactionStatus)
    
    def test_get_transaction_hex(self):
        tx_hex = blockexplorer.get_transaction_hex(self.TX_ID)
        self.assertIsInstance(tx_hex, str)

    def test_genesis_block_data(self):
        bh = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
        block = blockexplorer.get_block_by_hash(bh)
        self.assertEqual(block.id, bh)
        self.assertEqual(block.height, 0)
        self.assertEqual(block.version, 1)
        self.assertEqual(block.timestamp, 1231006505)
        self.assertEqual(block.tx_count, 1)
        self.assertEqual(block.size, 285)
        self.assertEqual(block.weight, 816)
        mr = '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
        self.assertEqual(block.merkle_root, mr)
        self.assertEqual(block.previous_block_hash, None)
        self.assertEqual(block.nonce, 2083236893)
        self.assertEqual(block.bits, 486604799)


if __name__ == "__main__":
    unittest.main()
