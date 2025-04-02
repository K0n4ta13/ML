# Email Classifier

This project is an email classifier that uses the `spam_assassin.csv` dataset to detect spam and non-spam emails.

## Installation

To run this project, follow these steps:

1. Install dependencies with:
   ```sh
   uv sync
   ```

2. Activate the virtual environment:
   ```sh
   source .venv/bin/activate
   ```
## Model Training

To train the model, run:
   ```sh
   uv run train_model.py
   ```

To train the model and evaluate its accuracy, use:
   ```sh
   uv run train_test_model.py
   ```
## Model Usage

To run the model, use:
   ```sh
   streamlit run app.py
   ```
This command will launch an interactive interface where you can enter emails and determine whether they are spam or not.
