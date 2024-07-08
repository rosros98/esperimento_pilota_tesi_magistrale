import pandas as pd
import matplotlib.pyplot as plt

# Carica il nuovo dataset filtrato
df_filtered = pd.read_csv("df_emotion_sentiment_final.csv")

# Seleziona solo le righe con sentimento "POSITIVE" o "NEGATIVE"
df_positive = df_filtered[df_filtered['Dominant_Sentiment'] == 'POSITIVE']
df_negative = df_filtered[df_filtered['Dominant_Sentiment'] == 'NEGATIVE']

# Calcola le frequenze dei valori nella colonna "Dominant_Emotion" per i sentimenti positivi
positive_emotion_freq = df_positive['Dominant_Emotion'].value_counts(normalize=True)

# Calcola le frequenze dei valori nella colonna "Dominant_Emotion" per i sentimenti negativi
negative_emotion_freq = df_negative['Dominant_Emotion'].value_counts(normalize=True)

# Plot
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot per sentimenti positivi
axs[0].bar(positive_emotion_freq.index, positive_emotion_freq.values)
axs[0].set_title('Frequenza delle emozioni per sentimenti positivi')
axs[0].set_xlabel('Dominant_Emotion')
axs[0].set_ylabel('Frequenza')

# Plot per sentimenti negativi
axs[1].bar(negative_emotion_freq.index, negative_emotion_freq.values)
axs[1].set_title('Frequenza delle emozioni per sentimenti negativi')
axs[1].set_xlabel('Dominant_Emotion')
axs[1].set_ylabel('Frequenza')

plt.tight_layout()
plt.show()
