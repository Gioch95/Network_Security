# Network_Security

In questo progetto viene utilizzata la libreria disponibile per python riguardante il procotollo QUIC aioquic. 

$ pip install aioquic
$ choco install openssl

In questo script, si utilizzerà la libreria per implementare una Gestione degli eventi basata su QUIC utilizzando un client e un server. Si avrà un evento trigger (numeri negativi o lo zero in un vettore di array) che attiverà il client, che invierà dei dati dinamicamente al server, in modalità 0-RTT o in modalità 1-RTT a seconda dello status del ticket. La durata del ticket è stata portata a 60 secondi. E' stato implementato un contatore che quando è allo stato di partenza (uguale a zero) e l'evento trigger è stato rilevati, il client invierà i dati al server in modalità 1-RTT, quando invece il contatore verrà incrementato di 1 secondo fino ad arrivare a 60 secondi, il client in questi 60 secondi invierà i dati al server in modalità 0-RTT. Una volta che finirà il conteggio di 60 secondi, il contatore ripartirà dallo stato di partenza e il client invierà di nuovo i dati in modalità 1-RTT, e così via.

