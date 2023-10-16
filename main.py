
import os
import time
import random

#durata del ticket
ticket_lifetime = 60



#server = "python http3_server.py --certificate ../tests/ssl_cert.pem --private-key ../tests/ssl_key.pem"

event = [-1, 0, 1, 2, 3, 4, 5, 6]
contatore = 0


while True:

    client_0RTT = "python http3_client.py --ca-certs tests/pycacert.pem --session-ticket tests/ticket.bin wss://localhost:4433/ws"
    client_1RTT = "python http3_client.py --ca-certs tests/pycacert.pem wss://localhost:4433/ws"

    #se l'evento trigger è stato rilevato e allo stesso tempo il contatore va da 1 a 60
    if (random.choice(event) == -1 or 0) and contatore <= 60:
        print("l'evento è stato rilevato")
        print("Il dato verrà trasmesso con modalità 0-RTT")
        os.system(client_0RTT)
        contatore += 1
        time.sleep(1)
        print(contatore)

    #se l'evento trigger è stato rilevato e allo stesso tempo il contatore è uguale a 0
    if (random.choice(event) == -1 or 0) and contatore == 0:
        print("l'evento è stato rilevato")
        print("il dato verrà trasmesso con modalità 1-RTT")
        os.system(client_1RTT)
        contatore += 1
        time.sleep(1)
        print(contatore)

    #se invece il contatore è maggiore di 61, ossia ha superato 1 minuto, il conteggio riparte da zero
    if contatore >= 61:
        contatore = 0
        print("Ripartito da zero!")











