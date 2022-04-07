import json

obj = {"ticker": "BTC-USD", "start": "2021-01-01T00:00:00.000Z",
       "end": "2022-01-01T00:00:00.000Z", "interval": "1mo"}

stringified_obj = json.dumps(obj)
print(stringified_obj)
