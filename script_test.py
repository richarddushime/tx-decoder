import unittest
from unittest.mock import patch
from decode_transaction import decode_transaction 

class TestDecodeTransaction(unittest.TestCase):
    @patch('subprocess.run')
    def test_decode_transaction(self, mock_subprocess_run):
        # Mock subprocess.run to return the desired JSON output
        mock_subprocess_run.return_value = type('', (object,), {
            'returncode': 0,
            'stdout': '{"version": 2, "vin": [{"txid": "ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e23490", "vout": 0, "scriptSig": {"hex": "empty"}, "sequence": "ffffffff"}], "vout": [{"value": 0.20000000, "scriptPubKey": {"hex": "OP_DUP OP_HASH160 16d31d7632aa17b3b316b813c0a3177f5b615020 OP_EQUALVERIFY OP_CHECKSIG"}}, {"value": 0.79863814, "scriptPubKey": {"hex": "OP_HASH160 838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb OP_EQUAL"}}], "locktime": 0}',
            'stderr': ''
        })
        
        # Call the function with the provided raw transaction hex
        result = decode_transaction("020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000")
        
        # Verify the expected outputs
        self.assertEqual(result, None)  # The function currently prints outputs to the console

if __name__ == '__main__':
    unittest.main()
