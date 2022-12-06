## autor:
# Michel silva

# data: 06/12/2022

# enviar mensagem para uma lista de números pelo WhatsApp


import pywhatkit as kit #  pip install pywhatkit ou pip3 install pywhatkit
import time #  pip install time ou pip3 install time
from datetime import datetime as dt # pip install datetime ou pip3 install datetime

quantidade = int(input("informe a quantidade: "))  # quantidade de contatos que serão enviados a mensagem
msg = input("informe a mensagem: ") # mensagem que será enviada

contatos = ['+5583982173126']  # lista de contatos que serão enviados a mensagem

i = 0  # contador
while i < quantidade: # enquanto o contador for menor que a quantidade de contatos
  kit.sendwhatmsg(contatos[0], msg, dt.now().hour, dt.now().minute + 1) # envia a mensagem para o primeiro contato da lista e aguarda 1 minuto para enviar a próxima mensagem
  # kit.sendwhatmsg(contatos[0], msg, 1, 30) # 1:30 da manhã  
  time.sleep(5) # aguarda 5 segundos para enviar a próxima mensagem 
  contatos.pop(0) # remove o primeiro contato da lista para enviar a próxima mensagem