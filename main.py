import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# FASE 1: Caricamento e Preparazione Dati
# 1. Carichiamo il dataset Excel
df = pd.read_excel('german_credit_data.xlsx')
print(df.T[1]) #stampa la prima riga della tabella T

# 2. Data Exploration: Gestiamo i valori mancanti
df = df.dropna() #cancella le righe (cioè i clienti) che contengono almeno un valore nullo, es: 'credito' ~ NULL

# 3. Definiamo le features usando i NOMI ESATTI del tuo file Excel
features_cols = ['età', 'conto corrente', 'patrimonio', 'anzianità lavorativa']
target_col = 'credito'

X = df[features_cols] #colonne con features
y = df[target_col] # colonna con il target 0/1
#ad ogni riga di features corrisponde un certo esito (target) 0/1

# Trasformiamo eventuali variabili categoriche in numeri (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True) # conversione superflua perchè il dataset è già numericamente convertito

# FASE 2: Addestramento del Modello
# Dividiamo i dati: 70% per addestrare, 30% per testare
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#NB: il test_size è una percentuale unitaria che indica la quantità di dati da utilizzare per il test (0.3~ 30%);
# il random_state è il seme di casualità, forza Python a eseguire questo mescolamento in modo esattamente identico a ogni avvio del programma;
# in questo caso 42...numero non proprio a caso :)

# Inizializziamo l'algoritmo
modello = RandomForestClassifier(random_state=42)
#abbiamo impostato un seme anche qui, che non deve essere necessariamente uguale a quello per selezionare i dati
# di test e allenamento... per coerenza scegliamo dinuovo il 42...NON NECESSARIO

# Addestriamo il modello
modello.fit(X_train, y_train)

# CALCOLO PROBABILITÀ E RAGGRUPPAMENTO A FASCE
# Otteniamo le percentuali di rischio dal modello per il set di test
percentuali = modello.predict_proba(X_test)
print(percentuali)
# si tratta di una LISTA di liste: [ [prob_default, prob_non_default], ... , [prob_default, prob_non_default]]
# ogni lista della LISTA corrisponde all'esito rispetto una riga (cliente) del test

# Estraiamo la probabilità di default (Classe 0)
prob_insolvenza_predetta = percentuali[:, 0] #estrazione dell'elemento di indice 0 per ogni lista della LISTA. Sintassi valida per array Numpy
print(prob_insolvenza_predetta) #quindi abbiamo una lista di valori di default

# Creiamo un DataFrame con i risultati
risultati = X_test.copy()
risultati['prob_insolvenza'] = prob_insolvenza_predetta #Prende la colonna dei numeri decimali appena calcolata
                                                        # dall'algoritmo (la probabilità di default che avevamo estratto con
                                                        # predict_proba) e la affianca come nuova colonna chiamata
                                                        # 'prob_insolvenza' all'interno della nostra tabella risultati;

# Definiamo i limiti delle fasce e le etichette da mostrare
limiti_eta = [18, 25, 35, 45, 55, 65, 120] # 120 serve a coprire chiunque abbia più di 65 anni
etichette_fasce = ['18-25', '26-35', '36-45', '46-55', '56-65', 'Over 65']

# pd.cut() taglia i valori dell'età esatta assegnandoli alla fascia corrispondente
risultati['fascia_età'] = pd.cut(risultati['età'], bins=limiti_eta, labels=etichette_fasce, right=True)

# Ora raggruppiamo calcolando la media, ma usando la NUOVA colonna 'fascia_età'
prob_media_fascia = risultati.groupby('fascia_età')['prob_insolvenza'].mean().reset_index()

# CREAZIONE GRAFICO A BARRE
plt.figure(figsize=(10, 6))

# Sostituiamo lo scatter plot con un grafico a barre (plt.bar)
plt.bar(prob_media_fascia['fascia_età'], prob_media_fascia['prob_insolvenza'],
        color='steelblue', edgecolor='black', alpha=0.8)

plt.title('Probabilità di Insolvenza Media Predetta per Fascia d\'Età')
plt.xlabel('Fasce d\'Età del Cliente')
plt.ylabel('Probabilità di Default Media (Modello ML)')
plt.grid(axis='y', linestyle='--', alpha=0.5) # Mettiamo la griglia solo in orizzontale per i grafici a barre

plt.show()
