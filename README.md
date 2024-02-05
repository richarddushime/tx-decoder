
# Bitcoin Transaction Decoder

This Python script decodes a raw Bitcoin transaction using the Bitcoin Core's `decoderawtransaction` command. 
The decoded information includes the version, inputs, outputs, and locktime.

## Requirements

- Python 3
- Bitcoin Core installed and running

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/richarddushime/tx-decoder.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tx-decoder
   ```

3. Replace `<raw_transaction_hex>` with the actual raw hex of the Bitcoin transaction you want to decode.

4. Run the script with:

   ```
   python3 decode_transaction.py 
   ```
## Testing

To run the provided test:

```
python3 script_test.py
```

## Notes

- Make sure Bitcoin Core is running and accessible from the command line.
- The script prints the decoded information to the console.
