# :four_leaf_clover: Twilight-Algoritm
My simple string encryption algorithm with data salting.

# :lock: Encrypt:
```bash
python main.py --key "12345" --encrypt "Hello world"

OUTPUT > Encrypted value: VVdWfFpdXkR8fV1XV0MVEVZXfFldRURDUF1XX0NaVBITfFp5EhNDUHlFV1EVXlYTFEdDQFcUWVReVhRR
```

# :unlock: Decrypt:
```bash
python main.py --key "12345" --decrypt "VF5fW1pVRVZ8WnlXREZaXRJfQ1ldQHtGRxFde1BaRnpBWFB5EhNDUBF6exRZXlZXUVFDEntYWV56RFFR"

OUTPUT > Decrypted value: Hello world
```
