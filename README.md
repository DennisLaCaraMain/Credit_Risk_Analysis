# Credit Risk Assessment & Default Prediction

## Obiettivo del Progetto
Questo progetto implementa un modello predittivo in Python per calcolare la probabilità che un richiedente risulti insolvente su un prestito bancario[cite: 1]. Utilizza il dataset storico **German Credit Data**, focalizzandosi su un'analisi chiara e un'ottimizzazione mirata alla minimizzazione dei rischi aziendali[cite: 1].

## Variabili Chiave del Modello
L'algoritmo incrocia il profilo demografico e finanziario del cliente.

**Variabile Target ('credito'):**
*   **1 (Buon Pagatore):** Cliente a basso rischio che rispetta gli obblighi[cite: 2].
*   **0 (Default):** Cliente insolvente o con ritardi significativi[cite: 2].

**Features Predittive:**
*   **Età e Anzianità Lavorativa:** I clienti molto giovani presentano generalmente un rischio maggiore, mentre l'anzianità aziendale funge da forte indicatore di stabilità del reddito[cite: 4].
*   **Conto Corrente:** Misura la liquidità immediata per far fronte agli impegni a breve termine[cite: 3].
*   **Patrimonio:** Rappresenta la solidità a lungo termine. Immobili, veicoli o investimenti fungono da garanzia (collaterale) in caso di insolvenza[cite: 3].

## Strumenti Utilizzati
La pipeline di analisi è costruita sulle librerie standard di Data Science[cite: 1]:
*   **Pandas:** Utilizzato per l'esplorazione dei dati, la gestione dei valori mancanti (NaN) e l'aggregazione per fasce d'età[cite: 1, 5].
*   **Scikit-Learn:** Impiegato per l'addestramento del **Random Forest Classifier**, generando probabilità di default percentuali al posto di semplici etichette binarie[cite: 1].
*   **Matplotlib:** Utilizzato per la visualizzazione dell'output in un grafico a barre finale[cite: 1].

## Analisi dei Rischi (Matrice di Confusione)
Le probabilità generate dal modello aiutano l'istituto di credito a bilanciare due errori critici[cite: 1]:

| Esito Modello | Il cliente paga (Realtà) | Il cliente NON paga (Realtà) |
| :--- | :--- | :--- |
| **Prestito Erogato** (Modello: Sicuro) | Vero Positivo | **Falso Positivo (Danno economico enorme)** |
| **Prestito Rifiutato** (Modello: A Rischio) | **Falso Negativo (Mancato guadagno)** | Vero Negativo |

L'obiettivo principale del modello è minimizzare i **Falsi Positivi** (erogare il prestito a chi non paga), accettando un lieve incremento dei **Falsi Negativi** (rifiutare un cliente affidabile), poiché la perdita del capitale erogato rappresenta il danno maggiore per la banca[cite: 1].
