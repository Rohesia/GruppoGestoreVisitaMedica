Gestione Pazienti e Visite

Questo progetto permette di gestire una lista di pazienti e di registrare le loro visite mediche (check-up).
L’obiettivo è avere un piccolo gestionale che lavori con due file CSV: uno per i pazienti e uno per le visite.
Il programma funziona tramite un menù semplice, dove si possono creare pazienti, aggiungere visite e visualizzare i dati già memorizzati.

Struttura del progetto

Il programma è composto da alcuni file principali:

1. funzioni.py

Contiene tutte le funzioni operative del sistema.
Gestisce:

il caricamento dei pazienti dal file CSV

la creazione di un nuovo paziente

la selezione del paziente

l’inserimento di una nuova visita

la stampa di pazienti e visite

il menù principale che l’utente utilizza per muoversi nel programma

2. utente.py

Definisce la classe Paziente, cioè l’oggetto che rappresenta ogni persona registrata nel programma.
Contiene attributi come nome, cognome, codice fiscale e data di nascita.

3. CheckUp.py

Contiene la classe CheckUp, che serve per creare e memorizzare ogni visita.
Si occupa anche di scriverla nel file CSV e di mostrare tutte le visite associate a un paziente.

4. pazienti.csv

File che memorizza l’elenco di tutti i pazienti.
Viene aggiornato automaticamente quando si aggiunge un nuovo paziente.

5. visite.csv

File che contiene tutte le visite registrate.
Ogni riga rappresenta un check-up di un paziente.

Come funziona il programma

Quando si avvia il programma, vengono caricati automaticamente tutti i pazienti esistenti dal file pazienti.csv.
Dopo il caricamento, compare il menù principale con cinque opzioni fondamentali:

Creare un nuovo paziente

Registrare una nuova visita a un paziente

Visualizzare l’elenco dei pazienti

Mostrare tutte le visite di un paziente

Uscire dal programma

Ogni voce del menù guida l’utente passo passo, richiedendo soltanto le informazioni essenziali (come nome, cognome, data, descrizione della visita, ecc.).

Flusso tipico di utilizzo

L’utente avvia il programma.

Il sistema carica i pazienti salvati in precedenza.

L’utente crea un paziente oppure ne seleziona uno già esistente.

Si possono aggiungere una o più visite, che verranno salvate nel file CSV delle visite.

In qualunque momento si può rivedere l’elenco delle visite di quel paziente.

I dati rimangono salvati nei file anche quando il programma viene chiuso.

Obiettivo del progetto

L’idea è creare un piccolo gestionale semplice ma strutturato, utile per esercitarsi con:

programmazione a oggetti (classi Paziente e CheckUp)

gestione di file CSV

organizzazione di un software tramite moduli separati

utilizzo di liste globali, menù e selezione degli elementi

L’intero progetto è pensato per essere chiaro, leggibile e facilmente estendibile.
Ad esempio, si potrebbero aggiungere funzioni per modificare un paziente, cancellare una visita, filtrare i dati o generare report.