#enviando mensaje whatsapp

import pywhatkit

numero = input("introduzca el numero del telefono:")
mensaje = input("introduzca el mensaje")
hora = int(input("hora de envio"))
minuto = int(input("minuto de envio"))

pywhatkit.sendwhatmsg(numero,mensaje,hora,minuto)