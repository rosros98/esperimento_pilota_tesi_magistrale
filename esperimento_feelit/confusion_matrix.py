from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from esperimento_feelit.valutazione_sentiment import df_previsioni_modello_misto, df_etichette_effettive_misto

#from esperimento_feelit.valutazione_sentiment import df_etichette_effettive_positivi, df_previsioni_modello_positivi
#from esperimento_feelit.valutazione_sentiment import df_etichette_effettive_negativi, df_previsioni_modello_negativi

# Calcola la matrice di confusione
conf_matrix = confusion_matrix(df_etichette_effettive_misto['sentiment'], df_previsioni_modello_misto['sentiment'])

# Visualizza la matrice di confusione utilizzando Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['negative', 'positive'], yticklabels=['negative', 'positive'])
plt.xlabel('Previsioni')
plt.ylabel('Etichette effettive')
plt.title('Matrice di Confusione')
plt.show()
