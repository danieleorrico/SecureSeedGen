# SecureSeedGen: Generatore di Seed Sicuro Criptograficamente

SecureSeedGen è un programma Python che genera un seed criptograficamente sicuro composto da 24 parole utilizzando un generatore di numeri casuali e diverse fonti di entropia dal sistema. Le parole generate sono conformi allo standard BIP39 e possono essere utilizzate per creare un wallet di criptovalute.

## Caratteristiche principali
- Utilizza diverse fonti di entropia, inclusi timestamp del sistema, stato della CPU, consumo di memoria e dati casuali generati da Python.
- Applica una funzione di hash sicura (SHA-512) per ottenere un'entropia risultante.
- Genera un seed a 24 parole conforme allo standard BIP39.
- Verifica la validità della mnemonic generata.

## Fasi del programma
1. Raccolta di dati casuali da diverse fonti sul sistema.
2. Applicazione di una funzione di hash sicura (SHA-512) ai dati raccolti.
3. Calcolo del checksum SHA256 dell'entropia risultante.
4. Generazione di una mnemonic a 24 parole utilizzando l'entropia risultante.
5. Verifica della mnemonic generata.

## Utilizzo
Assicurati di avere Python installato sul tuo sistema. Esegui il programma eseguendo il file `secure_seed_gen.py`. Il programma genererà un seed a 24 parole e lo stamperà a schermo.

## Modifiche nella nuova versione (V2):
Nella nuova versione del programma sono state apportate le seguenti modifiche per aumentare ulteriormente l'entropia e migliorare la sicurezza del seed generato:
- Implementazione di algoritmi di mescolamento più complessi e iterazione del processo di mixing per aumentare la casualità dei dati raccolti.
- Aggiunta di un ciclo che itera il processo di mixing per 10 volte, applicando algoritmi di permutazione casuale e l'operazione XOR tra i byte dell'entropia.

---

# SecureSeedGen: Cryptographically Secure 24-word Seed Generator

SecureSeedGen is a Python program that generates a cryptographically secure 24-word seed using a random number generator and various sources of entropy from the system. The generated words are compliant with the BIP39 standard and can be used to create a cryptocurrency wallet.

## Key Features
- Utilizes various sources of entropy, including system timestamps, CPU status, memory consumption, and randomly generated data from Python.
- Applies a secure hash function (SHA-512) to obtain resulting entropy.
- Generates a 24-word seed compliant with the BIP39 standard.
- Validates the generated mnemonic.

## Program Phases
1. Gathering random data from various sources on the system.
2. Applying a secure hash function (SHA-512) to the collected data.
3. Calculating the SHA256 checksum of the resulting entropy.
4. Generating a 24-word mnemonic using the resulting entropy.
5. Verifying the generated mnemonic.

## Usage
Ensure you have Python installed on your system. Run the program by executing the `secure_seed_gen.py` file. The program will generate a 24-word seed and print it to the screen.

## Changes in the New Version (V2):

In the new version of the program, the following changes have been made to further increase entropy and enhance the security of the generated seed:

- Implementation of more complex mixing algorithms and iteration of the mixing process to increase the randomness of the collected data.
- Addition of a loop that iterates the mixing process 10 times, applying random permutation algorithms and the XOR operation between the entropy bytes.
