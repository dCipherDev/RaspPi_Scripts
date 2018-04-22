
from sense_hat import SenseHat
sense = SenseHat()
from urllib2 import urlopen
import json
import time

#Low Light Toggle: set your sense-hat's display to low brightness  
sense.low_light = False #True 
#Rotation Toggle
sense.set_rotation(180)
TEMP_ETH = 0
TEMP_BTC = 0
while True:
  try:
  #Connecting to Poloniex's API and geting the last prices
    url = urlopen('https://poloniex.com/public?command=returnTicker').read()
    result = json.loads(url)

  #Setting the last price for our coins for later use 
    ETH = result['BTC_ETH']['last']
    BTC = result['USDT_BTC']['last']

    BTC = round(float(BTC),2)
  
  #Converting ETH price in USD
    ETH_USD = float(BTC) * float(ETH)
    ETH_USD = round(float(ETH_USD),2)
  
  #Storing the price for later use
    ETH_OLD = TEMP_ETH
    BTC_OLD = TEMP_BTC

    print('ETH: $'+ str(ETH_USD))
    print('BTC: $'+ str(BTC))

#Changing the color of the text 
#Green when the price rises, yellow when it stays the same 
#and red when it decreses

#Display the prices on SENSE-HAT for ETH.
    if ETH_USD > ETH_OLD :
      sense.show_message("ETH: $" + str(ETH_USD), text_colour=[0,255,0])
    elif ETH_USD == ETH_OLD :
      sense.show_message("ETH: $" + str(ETH_USD), text_colour=[255, 255, 0])
    else :
      sense.show_message("ETH: $" + str(ETH_USD), text_colour=[255, 51, 51])

#Display the prices on SENSE-HAT for BTC.
    if BTC > BTC_OLD :
          sense.show_message("BTC: $" + str(BTC), text_colour=[0,255,0])
    elif BTC == BTC_OLD :
      sense.show_message("BTC: $" + str(BTC), text_colour=[255, 255, 0])
    else :
      sense.show_message("BTC: $" + str(BTC), text_colour=[255, 51, 51])
  
  #Printing the stored values to console
    print('ETH_OLD: $'+ str(ETH_OLD))
    print('BTC_OLD: $'+ str(BTC_OLD))
    print('--------------------------')

    TEMP_ETH = ETH_USD
    TEMP_BTC = BTC
    time.sleep(3)
  except:
    sense.show_message("failed to retrieve feed")
    time.sleep(3)