import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# FASE 1: Caricamento e Preparazione Dati
# 1. Carichiamo il dataset Excel
df = pd.read_excel('german_credit_data.xlsx')
#print(df.T[1]) #stampa la prima riga della tabella T

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
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

# 1. PREDIZIONI E PROBABILITÀ BASE
# Predizioni "secche" (0 o 1) del modello con soglia standard al 50%
y_pred = modello.predict(X_test)

# Otteniamo le percentuali di rischio dal modello per il set di test
# Restituisce un array 2D: [[prob_default, prob_buon_pagatore], ...]
percentuali = modello.predict_proba(X_test)

# Estraiamo la probabilità di default (Classe 0)
prob_insolvenza_predetta = percentuali[:, 0]

# Estraiamo la probabilità che il cliente sia un BUON PAGATORE (Classe 1)
prob_buon_pagatore = percentuali[:, 1]

# 2. METRICHE DI VALUTAZIONE (SOGLIA 50%)
print("\nVALUTAZIONE DEL MODELLO (SOGLIA 50%)")

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Confusion matrix (Il cuore del tuo README)
print("\nMATRICE DI CONFUSIONE (Impatto di Business):")
print(confusion_matrix(y_test, y_pred))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC-AUC (Calcolato sul rischio di default)
# Nota: Di base scikit-learn calcola l'AUC sulla classe positiva (1).
auc = roc_auc_score(y_test, prob_buon_pagatore)
print(f"ROC-AUC: {auc:.2f}")

# 3. OTTIMIZZAZIONE DI BUSINESS (SOGLIA 75%)
# Definiamo la nostra nuova soglia "severa" al 75%
soglia_sicurezza = 0.75

# Creiamo le nuove predizioni: 1 (Eroga) se supera la soglia, altrimenti 0 (Rifiuta)
y_pred_severo = (prob_buon_pagatore >= soglia_sicurezza).astype(int)
# nella tabella risultati è possibile verificare che i clienti a cui è assegnata un tasso di
# insolvenza >= 0.25, allora viene assegnato il default.

# Verifichiamo il nuovo impatto aziendale
print(f"\n MATRICE DI CONFUSIONE (SOGLIA {int(soglia_sicurezza*100)}%)")
print(confusion_matrix(y_test, y_pred_severo))

# Creiamo un DataFrame con i risultati
risultati = X_test.copy()
risultati['prob_insolvenza'] = prob_insolvenza_predetta #Prende la colonna dei numeri decimali appena calcolata
                                                        # dall'algoritmo (la probabilità di default che avevamo estratto con
                                                        # predict_proba) e la affianca come nuova colonna chiamata
                                                        # 'prob_insolvenza' all'interno della nostra tabella risultati;
risultati['decisione_modello_severo'] = y_pred_severo

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
