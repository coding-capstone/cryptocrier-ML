import requests

history_request = '{"ticker": "BTC-USD","start":"2021-01-01T00:00:00.000Z","end": "2022-01-01T00:00:00.000Z","interval": "1mo"}'

history_result = requests.get('http://127.0.0.1:5000/history', json=history_request)
if history_result.ok:
    print(history_result.json())
