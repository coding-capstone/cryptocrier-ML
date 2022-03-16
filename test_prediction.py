import requests

prediction_request = '{"ticker": "BTC-USD","start":"2021-01-01T00:00:00.000Z","end": "2022-01-01T00:00:00.000Z","interval": "1h", "model": "lr"}'

result = requests.post('http://127.0.0.1:5000/prediction', json=prediction_request)
if result.ok:
    print(result.json())
