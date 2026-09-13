# Credit Risk Assessment & Default Prediction

## Obiettivo del Progetto
Questo progetto implementa un modello predittivo in Python strutturato per calcolare la probabilità che un richiedente risulti insolvente su un prestito bancario[cite: 1]. Utilizzando il dataset storico **German Credit Data**, l'analisi supera la semplice accuratezza statistica per adottare una prospettiva di ingegneria gestionale[cite: 1]. Le probabilità estratte dal modello servono come base per ottimizzare le decisioni di erogazione e quantificare l'impatto sui costi aziendali[cite: 1].

## Struttura del Dataset e Variabili Chiave
L'algoritmo valuta il profilo di rischio incrociando i dati demografici con gli attributi finanziari.

**Variabile Target ('credito'):**
*   **1 (Buon Pagatore):** Cliente a basso rischio che rispetta gli obblighi finanziari[cite: 3].
*   **0 (Default):** Cliente insolvente o con ritardi significativi[cite: 3].

**Features Predittive Utilizzate:**
*   **Età e Anzianità Lavorativa:** L'età permette di isolare il rischio fisiologico maggiore tipico dei clienti più giovani, mentre l'anzianità aziendale funge da indicatore primario di stabilità del reddito[cite: 5].
*   **Conto Corrente:** Misura la liquidità immediata per far fronte agli impegni a breve termine[cite: 4].
*   **Patrimonio:** Rappresenta la solidità a lungo termine. Funge da garanzia (collaterale) in caso di insolvenza, riducendo il rischio effettivo per la banca[cite: 4].

## Stack Tecnologico e Pipeline
La pipeline di Data Science riflette esattamente le operazioni implementate nel codice principale dello script, utilizzando strumenti focalizzati sull'estrazione di valore decisionale:

*   **Pandas:** Motore centrale dell'esplorazione e manipolazione dati[cite: 1]. È stato utilizzato per il caricamento del dataset Excel, la pulizia dei valori mancanti (`dropna`), la trasformazione delle variabili categoriche in numeriche (`get_dummies`) e la segmentazione avanzata delle età in categorie strutturate (`pd.cut`) per l'aggregazione finale.
*   **Scikit-Learn:** Impiegato per l'addestramento del modello di classificazione[cite: 1]. Lo script implementa in modo specifico l'algoritmo **Random Forest Classifier**. Attraverso l'uso della funzione `predict_proba()`, il modello calcola l'esatta percentuale statistica di default per ogni cliente analizzato, fornendo un dato continuo invece di un'etichetta rigida.
*   **Matplotlib:** Utilizzato per la visualizzazione dell'output in ottica di business[cite: 1]. Il codice genera un grafico a barre aggregato che confronta le fasce d'età con la probabilità media di insolvenza prevista dal modello, eliminando il rumore statistico.

## Impatto di Business e Matrice di Confusione
Il risultato in probabilità percentuali permette all'istituto di credito di impostare soglie di tolleranza strategiche, bilanciando due tipologie di errore statistico che presentano pesi economici radicalmente diversi per la banca[cite: 1]:

| Esito Modello | Il cliente paga (Realtà) | Il cliente NON paga (Realtà) |
| :--- | :--- | :--- |
| **Prestito Erogato** (Modello: Sicuro) | Vero Positivo (Guadagno) | **Falso Positivo (Danno economico enorme)** |
| **Prestito Rifiutato** (Modello: A Rischio) | **Falso Negativo (Mancato guadagno)** | Vero Negativo (Perdita evitata) |

*   **Il Falso Positivo (Il Rischio Primario):** Si verifica quando il modello classifica erroneamente il cliente come sicuro e la banca eroga i fondi[cite: 1]. Genera una perdita diretta del capitale prestato[cite: 1].
*   **Il Falso Negativo (Il Costo Opportunità):** Si verifica quando il modello è eccessivamente prudente e rifiuta un cliente affidabile[cite: 1]. Causa alla banca un mancato incasso sui potenziali interessi attivi[cite: 1].

L'utilizzo del Random Forest abbinato all'analisi per fasce d'età offre alla direzione bancaria uno strumento decisionale solido per minimizzare i Falsi Positivi, tutelando la liquidità e i bilanci dell'istituto.
