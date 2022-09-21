from colorama import init, Fore, Back, Style
import time
import secrets
from random import randint

continuing = True

btcval = 23099.10

for i in range(100000000):
  if continuing == True:
      time.sleep(0.01)
      ranInt = randint(0,2500)
      if ranInt <= 1:
        randomBTC = randint(1,100) / 100
        if randomBTC % 1 == 2:
          print(Fore.WHITE + "> 0x" + secrets.token_hex(randint(17,22)) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(btcval * randomBTC)) + "0)")
        else:
           print(Fore.WHITE + "> 0x" + secrets.token_hex(randint(17,22)) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(btcval * randomBTC)) + ")")
        answer = input("> Would you like to continue? (Y/N) ")
        if answer == "y" or answer == "Y":
          continuing = True
        else:
          continuing = False
      else:
        print(Fore.WHITE + "> 0x" + secrets.token_hex(randint(17,22)) + Fore.RED + " > 0.00 BTC ($0.00)")
  else:
    break
