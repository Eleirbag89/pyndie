# Pyndie
Un linguaggio di programmazione ispirato alle canzoni indie italiane

## Installazione
Pyndie è progettato per funzionare su Python 3.8.10.   
Per usarlo scarica ed estrai il file .zip  oppure clona il repository digitando

```bash
git clone https://github.com/Eleirbag89/Pyndie.git
```

Aggiungi la cartella di Pyndie al `PATH` usando uno dei due comandi seguenti (su Linux)

1. Temporaneo: Scrivi `export PATH=$PATH:/path/to/RusPython` nel terminale.
2. Permanente: Aggiungi `export PATH=$PATH:/path/to/RusPython` alla fine del tuo file `~/.bashrc`.

## Utilizzo
* Scrivi un file pyndie usando l'opportuna sintassi.
* Esegui `pyndie /path/to/pyndie/file`
* PROFIT!

## Funzionalità
Pyndie include diverse funzionalità perfette per ogni aspirante cantane indie:
* Ogni programma deve contenere il nome di una città.
* Le istruzioni sono progettate per essere dei tormentoni orecchiabili.
* Il linguaggio è case insensitive per permettere la massima libertà.

## Grammatica
La grammatica del linguaggio è un pò complessa, abbiamo distillato l'essenza dell'indie italiano. Ecco come puoi essere anche tu l'idolo degli hipster alternativi

Operatori Aritmetici:
* `più` fa la somma
* `meno` fa la sottrazione
* `per` fa la moltiplicazione
* `diviso` fa la divisione
* `MODULE` fa il modulo    
MODULE può assumere i seguenti valori: `divisibile|resto|resta`    

Operatori Logici:
* `non` not booleano
* `o`  or booleano
* `e` and booleano
* `COMPARATOR` operatore di uguaglianza
* `minore` indica `più piccolo di`
* `maggiore` indica `più grande di`
COMPARATOR può assumere i seguenti valori: `sembra|sembri|sembriamo|sembrate|sembro`

Numeri
* Farmacologici: DRUG NUMBER     
dove DRUG è un farmaco fra  `paracetamolo|tachipirina|aulin|oki` e NUMBER un numero intero
* Poetici: formati da una sequenza di parole.     
Il numero risultante è la concatenazione della lunghezza modulo 10 di ogni parola, gli articoli sono ignorati    

Variabili:
* Puoi usare tutti gli spazi che vuoi per il nome delle tue variabili
* vai a capo per differenziare due variabili consecutive
* Puoi effettuare un assegnamento così: `variabile EQUALS espressione` 
* Le stringhe sono racchiuse da doppi apici `"Stringa"`   
EQUALS può assumere i seguenti valori: `è|sono|sei|siete|siamo|ero|eri|era|eravamo|eravate`

Controllo del flusso
* Per creare un costrutto IF: `variabile OPERATORE espressione ? istruzioni [ELSE istruzioni] HEY`    
OPERATORE è uno qualunque degli operatori logici. mentre ELSE può assumere i valori `invece|altrimenti`
* Per un ciclo while: `WHILE boolean_expression DO statements HEY`    
WHILE può assumere i valori `finché|finchè` mentre DO `faccio|fate|facciamo`


Funzioni
* Definire una funzione usando: `SAI CHE EQUALS variable AS params HEY statements OH`
* Richiamare una funzione usando: `CALL variable CHE EQUALS params_actual !`
* Far ritornare un valore ad una funzione: `dammi valore`

Input/Output
* Stampare sullo schermo; `PRINT espressione`   
PRINT può assumere i seguenti valori: `sussurra|gridavate|gridava|gridavi|gridavano|grido|grida|sussurravate|sussurravi|sussurrava|sussurra|sussurro`


## Esempi
```sai che sei bella come l'aria hey l'aria sembra abbacinata?
dammi una abbindolata hey
dammi l'aria per ricordare bella che è l'aria meno Albuquerque! oh
mi sussurrava ricorda la bella che è sparita!
```   
Questo codice definisce una funzione chiamata "bella" che calcola il fattoriale di 7 in maniera ricorsiva.   


## Attivati
Sentiti libero di contribuire al progetto con commit, idee, suggerimenti.   
Puoi creare fork e spinoff senza chiedere il permesso a nessuno (ok, però magari un piccolo link mettilo).   
Puoi contribuire anche scrivendo del codice Pyndie e arricchendo la nostra galleria di esempi.