import websocket
import json
def on_message(ws, message):
    o = json.loads(message)
    returnList = o["o"]
    returnList = json.loads(returnList)
    buy = []
    sell = []
    for data in returnList:
        if data[9] == 0:
            buy.append(data)
        else:
            sell.append(data)
    buy = sorted(buy, key=lambda x: x[6], reverse=True)[:3]
    sell = sorted(sell, key=lambda x: x[6], reverse=True)[:3]
    count = 1
    for data in buy:
        print(f'buy No. - {count}: ', data[6])
        count += 1
    count = 1
    for data in sell:
        # print(f'sell No. - {count}: ',data[6])
        count += 1
    print()
    print("--------------------------------------------------------------------------------")
def on_error(ws, error):
    print(error)
def on_close(ws):
    print("### closed ###")
def on_open(ws):
    print("### STARTING ###")
    payload = {"OMSId": 1,
               "InstrumentId": 78,
               "depth": 10}
    message = {"m": 0,
               "i": 78,
               "n": "SubscribeLevel2",
               "o": json.dumps(payload)
               }
    ws.send(json.dumps(message))
if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://api.ndax.io/WSGateway/", on_message=on_message, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()



