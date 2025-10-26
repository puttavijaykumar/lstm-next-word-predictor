import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'model', 'model_next_word_LSTM.h5')
tokenizer_path = os.path.join(BASE_DIR, 'model', 'tokenizer.pickle')

model = tf.keras.models.load_model(model_path)

with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)

max_sequence_len = model.input_shape[1] + 1

def predict_next_word(text):
    token_list = tokenizer.texts_to_sequences([text.lower()])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]
    padded = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted_probs = model.predict(padded)
    predicted_index = predicted_probs.argmax(axis=-1)[0]
    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    return ""
