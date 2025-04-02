import pandas as pd
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def train_and_save_model():
    dataset = pd.read_csv("./spam_assassin.csv")
    data, target = dataset.text, dataset.target

    stop_words = stopwords.words("english")
    tfidf = TfidfVectorizer(
        stop_words=stop_words, token_pattern=r"(?u)\b([a-zA-Z]{4,12})\b"
    )
    train_X = tfidf.fit_transform(data)

    rf_clf = RandomForestClassifier(random_state=0)
    param_grid = {"n_estimators": range(100, 351, 50), "bootstrap": [True, False]}
    grid_search = GridSearchCV(rf_clf, param_grid, cv=3, n_jobs=-1, scoring="accuracy")
    grid_search.fit(train_X, target)

    model = grid_search.best_estimator_
    model.fit(train_X, target)

    with open("spam_classifier.pkl", "wb") as model_file:
        pickle.dump((model, tfidf), model_file)

    print("Modelo entrenado y guardado como 'spam_classifier.pkl'")


if __name__ == "__main__":
    train_and_save_model()
