import os

import websocket
import threading
from time import sleep
import json

Instruments={1:'BTCCAD',2:'BCHCAD',3:'ETHCAD',4:'XRPCAD',5:'LTCCAD',74:'BTCUSD',75:'EOSCAD',76:'XLMCAD',77:'DOGECAD',78:'ADACAD'}
def on_message(ws, message):
    price = json.loads(message)
    d = json.loads(price['o'])
    id = d['InstrumentId']
    currency = Instruments[id]
    buy = d['BestOffer']
    sell = d['BestBid']
    print("Real Time - ","id - "+str(id), "Currency-" + str(currency), "buy - " + str(buy), "Sell - " + str(sell))
    if id==78:
        print('------------')
def on_close(ws):
    print ("### closed ###")
    # f = open("log.txt", "a")
    # f.write("closed\n")
    # f.close()
    os.system('python phase.py')

try:
    if __name__=='__main__':
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp("wss://api.ndax.io/WSGateway/", on_message = on_message, on_close = on_close)
        wst = threading.Thread(target=ws.run_forever)
        wst.daemon = True
        wst.start()
        conn_timeout = 5
        print('bbbb')
        while not ws.sock.connected and conn_timeout:
            print('ccccc')
            sleep(1)
            conn_timeout -= 1
        while ws.sock.connected:
            print('dddddd')
            for id in Instruments:
                payload = {"OMSId": 1,
                             "InstrumentId": id}
                message = {"m": 0,
                             "i": 1,
                             "n": "GetLevel1",
                             "o": json.dumps(payload)
                             }
                ws.send(json.dumps(message))
                if id==78:
                    sleep(2)
except Exception as e:
    # f = open("log.txt", "a")
    # f.write(str(e)+"\n")
    # f.close()
    os.system('python phase1.py')