# Next Word Predictor 

A deep learning project that implements **Next Word Prediction** using **LSTM** and **GRU** models. This project demonstrates how **recurrent neural networks (RNNs)** can learn language patterns and predict the next probable word in a sequence.

---

## Features

- Utilizes **LSTM (Long Short-Term Memory)** networks for sequential text prediction.
- Supports **GRU (Gated Recurrent Unit)** as an alternative model.
- Provides a **web-based user interface** to input phrases and get predicted next words.
- Backend built with **Django** serving the prediction API and frontend input form.
- Includes **pre-trained model files** for immediate usage and further training.

---

## Project Structure

| File/Directory | Description |
| :--- | :--- |
| `predictor/` | Django app containing views, utils, templates, and models. |
| `model_next_word_LSTM.h5` | The pre-trained LSTM model file. |
| `tokenizer.pickle` | Tokenizer object used for text preprocessing. |
| `utils.py` | Contains the prediction logic using the loaded model and tokenizer. |
| `templates/predictor/index.html` | The user input frontend template. |
| `nextwordpredictor/` | Django project configuration files. |

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/puttavijaykumar/lstm-next-word-predictor.git](https://github.com/puttavijaykumar/lstm-next-word-predictor.git)
    cd lstm-next-word-predictor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    # On Windows: .venv\Scripts\activate
    ```

3.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the migrations and start the server:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000/` to access the input form.

---

## Usage

- Enter a phrase in the input box on the web interface.
- Click **“Predict”**.
- The application returns the **most likely next word** based on the trained model.

---

## Model Training (Optional)

You can retrain or fine-tune the LSTM or GRU models using your own text dataset by modifying the training scripts (note: the training scripts themselves are not explicitly included in this repository's structure but are assumed to be part of the development process).

---

## Deployment

This project can be deployed to cloud platforms supporting Django, such as **Render** . Make sure to configure necessary **environment variables** (e.g., `SECRET_KEY`, database settings) and ensure proper setup for **serving static files** accordingly.

---

## Contributing

Feel free to open issues or create pull requests to improve the project! Your contributions are welcome.

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgments

- **TensorFlow** and **Keras** for the deep learning framework.
- **Django community** for web framework support.
- Inspiration from various **NLP and machine learning tutorials**.
