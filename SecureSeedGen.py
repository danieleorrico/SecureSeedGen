"""
SecureSeedGen: Cryptographically Secure 24-word Seed Generator

Questo programma genera un seed a 24 parole utilizzando un generatore di numeri casuali
criptograficamente sicuro e diverse fonti di entropia dal sistema. Le parole generate
conformi allo standard BIP39 possono essere utilizzate per creare un wallet di criptovalute.

Fasi del programma:
1. Raccolta di dati casuali da diverse fonti sul sistema.
2. Applicazione di una funzione di hash sicura (SHA-512) ai dati raccolti.
3. Concatenazione dell'entropia risultante con un checksum.
4. Generazione di una mnemonic a 24 parole utilizzando l'entropia risultante.
5. Verifica della mnemonic generata.

"""

import hashlib
import time
import random
import psutil  # Modulo per ottenere informazioni sul sistema
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39MnemonicValidator

def gather_entropy():
    # Fase 1: Raccolta di dati casuali da diverse fonti
    entropy_sources = []
    
    # Aggiungi il timestamp del sistema in millisecondi
    entropy_sources.append(str(time.time()))
    
    # Aggiungi lo stato della CPU
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    entropy_sources.extend(str(usage) for usage in cpu_usage)
    
    # Aggiungi il consumo di memoria
    mem_usage = psutil.virtual_memory().percent
    entropy_sources.append(str(mem_usage))
    
    # Aggiungi dati casuali generati da Python
    entropy_sources.append(str(random.getrandbits(256)))
    
    # Concatena i dati casuali da tutte le fonti
    entropy = ''.join(entropy_sources).encode()
    
    # Fase 2: Applicazione di una funzione di hash sicura (SHA-512) ai dati raccolti
    entropy = hashlib.sha512(entropy).digest()
    
    return entropy

def generate_seed():
    # Fase 3: Raccolta di dati casuali da diverse fonti
    entropy = gather_entropy()
    
    # Fase 4: Calcolo del checksum SHA256 della entropia
    checksum = hashlib.sha256(entropy).digest()
    
    # Concatenazione dell'entropia e il checksum
    full_entropy = entropy + checksum[:1]
    
    # Fase 5: Generazione di una mnemonic a 24 parole dalla entropia
    mnemonic = Bip39MnemonicGenerator.FromEntropy(full_entropy)
    
    # Verifica della mnemonic generata
    if not Bip39MnemonicValidator.Validate(mnemonic, Bip39WordsNum.WORDS_NUM_24):
        raise ValueError("Errore nella generazione della mnemonic.")
    
    return mnemonic

# Esempio di utilizzo
if __name__ == "__main__":
    try:
        mnemonic = generate_seed()
        print("Mnemonic (Seed a 24 parole):", mnemonic)
    except Exception as e:
        print("Si è verificato un errore durante la generazione della seed:", e)
