import subprocess
import json

def decode_transaction(hex_string):
    # Use bitcoin-cli to decode the raw transaction hex
    result = subprocess.run(["bitcoin-cli", "decoderawtransaction", hex_string], capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print("Error decoding transaction:")
        print(result.stderr)
        return
    
    # Parse the JSON output
    decoded_data = json.loads(result.stdout)
    
    # Print the decoded data
    print("Version:", decoded_data["version"])
    
    print("Inputs:")
    for input_data in decoded_data["vin"]:
        print("  Previous Transaction Output (UTXO):", input_data["txid"])
        print("  Index:", input_data["vout"])
        print("  ScriptSig:", input_data["scriptSig"]["hex"])
        print("  Sequence:", input_data["sequence"])
    
    print("Outputs:")
    for output_data in decoded_data["vout"]:
        print("  Value:", output_data["value"], "BTC")
        print("  ScriptPubKey:", output_data["scriptPubKey"]["hex"])
    
    print("Locktime:", decoded_data["locktime"])

# Test the script with the provided raw transaction hex
# raw_transactio_hex ="your hex value "
raw_transaction_hex = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"
decode_transaction(raw_transaction_hex)
