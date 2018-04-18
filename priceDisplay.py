from sense_hat import SenseHat
sense = SenseHat()
from urllib2 import urlopen
import json
import time

sense.set_rotation(180)
while True:
  #try:
    url = urlopen('https://poloniex.com/public?command=returnTicker').read()
    result = json.loads(url)
    ETH = result['BTC_ETH']['last']
    BTC = result['USDT_BTC']['last']
    BTC = round(float(BTC),2)
    print('BTC: $'+ str(BTC));
    ETH_USD = float(BTC) * float(ETH)
    ETH_USD = round(float(ETH_USD),2)
    print('ETH: $'+ str(ETH_USD));
    #Steem = result['BTC_STEEM']['last']
    #SBD_USD = float(SBD) * float(BTC)
    #STEEMUSD = float(Steem) * float(BTC)
    #sense.show_message("BTC " + '{0:.2f}'.format(BTC), text_colour=[255, 215, 0])
    sense.show_message("ETH: $" + str(ETH_USD), text_colour=[7, 24, 138])
    sense.show_message("BTC: $" + str(BTC), text_colour=[4, 112, 22])
    time.sleep(3)
 # except:
  #  sense.show_message("failed to retrieve feed")
   # time.sleep(3)