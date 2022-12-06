#
import pywhatkit as kit
import time
from datetime import datetime as dt

quantidade = int(input("informe a quantidade: "))
msg = input("informe a mensagem: ")

contatos = ['+5583982173125']

i = 0
while i < quantidade:
  kit.sendwhatmsg(contatos[0], msg, dt.now().hour, dt.now().minute + 1)
  # kit.sendwhatmsg(contatos[0], msg, 1, 30) # 1:30
  time.sleep(5)
  contatos.pop(0)