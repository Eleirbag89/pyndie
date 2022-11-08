# Pyndie
Un linguaggio di programmazione ispirato alle canzoni indie italiane

## Filosofia
Pyndie è un linguaggio di programmazione ispirato ai testi delle canzoni indie italiane.   


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
* Esegui `pyndie /path/to/ruspy/file`
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

Operatori Logici:
* `non` not booleano
* `o`  or booleano
* `e` and booleano
* `COMPARATOR` operatore di uguaglianza
* `minore` indica `più piccolo di`
* `maggiore` indica `più grande di`
COMPARATOR può assumere i seguenti valori: `sembra|sembri|sembriamo|sembrate|sembro`

Variabili:
* Puoi usare tutti gli spazi che vuoi per il nome delle tue variabili
* vai a capo per differenziare due variabili consecutive
* Puoi effettuare un assegnamento così: `variabile EQUALS espressione` 
* Le stringhe sono racchiuse da doppi apici `"Stringa"`   
EQUALS può assumere i seguenti valori: `è|sono|sei|siete|siamo|ero|eri|era|eravamo|eravate`

Controllo del flusso
* Per creare un costrutto IF: `variabile OPERATORE espressione ? istruzioni [ELSE istruzioni] HEY.` Oppure usa `minore` o `maggiore`
OPERATORE è uno qualunque degli operatori logici. mentre ELSE può assumere i valori `invece|altrimenti`

Funzioni
* Definire una funzione usando: `SAI CHE EQUALS variable AS params HEY statements OH`
* Richiamare una funzione usando: `CALL variable CHE EQUALS params_actual !`
* Far ritornare un valore ad una funzione: `dammi valore`

Input/Output
* Stampare sullo schermo; `PRINT espressione`   
PRINT può assumere i seguenti valori: `sussurra|gridavate|gridava|gridavi|gridavano|grido|grida|sussurravate|sussurravi|sussurrava|sussurra|sussurro`


Infine:   
A noi Padani non piace parlare dei propri errori, per cui molte volte il codice fallirà senza segnalare nulla.   
Pensate al debug come a un piccolo gioco fra di noi.

## Esempi
`Attenzione padani ! Gli Africani tornino a casa loro`   
`milioni sono 0 tutti sono 1`   
`gli Africani sono milioni? Espellili tutti.`    
`espelli gli Africani * Ricordate padani! Gli Africani-Tutti a casa loro`    
`Basta`   
`Urla ricordate padani! Bingo bongo a casa loro`   
`PadaniaLibera`   
Questo codice definisce una funzione chiamata "padani" che calcola il fattoriale in maniera ricorsiva.   

Di seguito la lista con tutti gli script creati fino ad ora e come utilizzarli
* Fattoriale: Calcola il fattoriale di un numero in input.   
Fattoriale di 5: `RusPython examples/Fattoriale.ruspy 5`
* Fibonacci: Calcola i primi n valori della sequenza di Fibonacci in base al numero in input.   
Primi 8: `RusPython examples/Fibonacci.ruspy 8`
* Hello world: Semplice programma di esempio.   
Lancialo con `RusPython examples/Hello_World.ruspy`
* Or(d)inamento: Ordina la sequenza in input.   
Esempio `RusPython examples/Ordinamento.ruspy 75 5 1 9 104 32`
* ParamList: stampa sullo schermo tutti i parametri in input.   
Esempio `RusPython examples/ParamList.ruspy 5 Borghezio 3.14`
* RitualeDelPo: gioca a indovinare il numero magico per ultimare il rituale.   
Esempio `RusPython examples/RitualeDelPo.ruspy`
* Matrimonio: Controlla se due parametri di input possono sposarsi.   
Esempio `RusPython examples/Matrimonio.ruspy 5 5`
* ServerWeb: Avvia un server web. Il primo parametro è il percorso dove sono salvati i file del sito, il secondo è l'host e il terzo la porta.       
Esempio `RusPython examples/ServerWeb.ruspy /var/wwww/ localhost 8080`
* 99 bottiglie: Canta la canzone 99 bottiglie di birra.       
Esempio `RusPython examples/99 bottiglie.ruspy`
* Tris: Gioca una partita a Tris contro la migliore simulazione di Matteo.
Esempio `RusPython examples/Tris.ruspy`

## Attivati
Sentiti libero di contribuire al progetto con commit, idee, suggerimenti.   
Puoi creare fork e spinoff senza chiedere il permesso a nessuno (ok, però magari un piccolo link mettilo).   
Puoi contribuire anche scrivendo del codice RusPython e arricchendo la nostra galleria di esempi.