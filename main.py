import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# FASE 1: Caricamento e Preparazione Dati
# 1. Carichiamo il dataset Excel
df = pd.read_excel('german_credit_data.xlsx')

# 2. Data Exploration: Gestiamo i valori mancanti
df = df.dropna()

# 3. Definiamo le features usando i NOMI ESATTI del tuo file Excel
features_cols = ['età', 'conto corrente', 'patrimonio', 'anzianità lavorativa']
target_col = 'credito'

X = df[features_cols]
y = df[target_col]

# Trasformiamo eventuali variabili categoriche in numeri (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True)

# FASE 2: Addestramento del Modello
# Dividiamo i dati: 70% per addestrare, 30% per testare
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inizializziamo l'algoritmo
modello = RandomForestClassifier(random_state=42)

# Addestriamo il modello
modello.fit(X_train, y_train)

# CALCOLO PROBABILITÀ E RAGGRUPPAMENTO A FASCE
# Otteniamo le percentuali di rischio dal modello per il set di test
percentuali = modello.predict_proba(X_test)

# Estraiamo la probabilità di default (Classe 0)
prob_insolvenza_predetta = percentuali[:, 0]

# Creiamo un DataFrame con i risultati
risultati = X_test.copy()
risultati['prob_insolvenza'] = prob_insolvenza_predetta

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
