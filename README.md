# Credit Risk Assessment & Default Prediction

## 🎯 Obiettivo del Progetto
Questo progetto ha l'obiettivo di sviluppare un modello predittivo in Python capace di calcolare la probabilità che un nuovo richiedente non restituisca un prestito bancario. L'analisi si basa su dataset storici reali, come il **German Credit Data** (focalizzato su dati demografici e finanziari essenziali) e l'**Home Credit Default Risk** (orientato al credito al consumo).

Il progetto non si limita alla pura accuratezza statistica, ma adotta una prospettiva di ingegneria gestionale: le metriche tecniche del modello vengono tradotte in un'analisi diretta dell'impatto economico e dei costi operativi per l'istituto di credito.

## 🛠️ Stack Tecnologico e Metodologia
L'intera pipeline di Data Science è stata costruita utilizzando le librerie standard del settore:
*   **Pandas & NumPy:** Utilizzati per la Data Exploration, l'identificazione dei valori mancanti (NaN) e il trattamento degli outlier (es. anomalie nei redditi dichiarati) per garantire l'affidabilità del modello. I valori continui (come il patrimonio) sono stati normalizzati per ottimizzare le prestazioni degli algoritmi.
*   **Matplotlib & Seaborn:** Impiegati per la visualizzazione dei dati, permettendo di generare grafici chiari che mostrano l'andamento del tasso di insolvenza in relazione a variabili chiave come le fasce d'età o i livelli di reddito.
*   **Scikit-Learn:** Utilizzato per l'addestramento del modello di classificazione vero e proprio, implementando algoritmi solidi come la **Logistic Regression** e il **Random Forest**.

## 📊 Variabile Target e Profilazione Storica
Il modello si basa sull'assunto fondamentale che lo storico creditizio (prestiti passati, rimborsi, ritardi) sia il miglior predittore del comportamento futuro. 

La variabile da prevedere ("Rischio Credito") è stata codificata in modo binario:
*   **1 = Buon Pagatore (Non-Default):** Cliente a basso rischio che rispetta gli obblighi finanziari.
*   **0 = Cattivo Pagatore (Default):** Cliente insolvente o con ritardi significativi.

## 🔍 Variabili Predittive (Features)
L'algoritmo valuta diverse categorie di attributi per definire il profilo di rischio:
*   **Dati Demografici:** Valuta l'interazione tra età, stato civile e anzianità lavorativa. Ad esempio, l'anzianità aziendale funge da indicatore primario per la stabilità del reddito, mentre i clienti molto giovani presentano generalmente un rischio fisiologico maggiore.
*   **Attributi di Liquidità:** Analizza i fondi immediatamente disponibili tramite il conto corrente (Checking Account) e la capacità di assorbire imprevisti tramite il conto di risparmio (Savings Account).
*   **Attributi Patrimoniali (Property/Assets):** Il possesso di un'abitazione, di veicoli o investimenti indica stabilità a lungo termine. La presenza di un patrimonio diversificato fornisce alla banca una garanzia tangibile (collaterale) in caso di insolvenza.

## 💼 Impatto di Business: La Matrice di Confusione
Il valore reale di questo modello risiede nella sua capacità di ottimizzare le decisioni di erogazione, bilanciando due tipologie di errore statistico che hanno un peso economico radicalmente diverso per la banca:

| Esito Modello | Il cliente paga (Realtà) | Il cliente NON paga (Realtà) |
| :--- | :--- | :--- |
| **Prestito Erogato** (Modello: Sicuro) | Vero Positivo (Guadagno standard) | **Falso Positivo (Danno enorme)** |
| **Prestito Rifiutato** (Modello: A Rischio) | **Falso Negativo (Mancato guadagno)** | Vero Negativo (Perdita evitata) |

*   **Il Falso Positivo (Il Rischio Maggiore):** Si verifica quando il modello classifica erroneamente un cliente come sicuro, spingendo la banca a erogare il prestito a un soggetto che si rivelerà insolvente. Questo rappresenta un **danno economico enorme** dovuto alla perdita diretta del capitale prestato. (Nota: l'impatto di questo errore è mitigato se il cliente possiede un patrimonio solido che funge da garanzia).
*   **Il Falso Negativo (Il Costo Opportunità):** Si verifica quando il modello è eccessivamente prudente e classifica a rischio un cliente affidabile. Questo si traduce in un **mancato guadagno** (interessi persi) per l'istituto di credito.

**Conclusione:** L'algoritmo è stato progettato e tarato con l'obiettivo primario di minimizzare i Falsi Positivi, accettando un lieve incremento fisiologico dei Falsi Negativi al fine di proteggere la liquidità e i bilanci dell'istituto bancario.
