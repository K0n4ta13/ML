import pandas as pd
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


def train_and_evaluate():
    dataset = pd.read_csv("./spam_assassin.csv")
    data, target = dataset.text, dataset.target

    train_X, test_X, train_y, test_y = train_test_split(
        data, target, test_size=0.3, random_state=0, stratify=target
    )

    stop_words = stopwords.words("english")
    tfidf = TfidfVectorizer(
        stop_words=stop_words, token_pattern=r"(?u)\b([a-zA-Z]{4,12})\b"
    )
    train_X = tfidf.fit_transform(train_X)
    test_X = tfidf.transform(test_X)

    rf_clf = RandomForestClassifier(random_state=0)
    param_grid = {"n_estimators": range(100, 351, 50), "bootstrap": [True, False]}
    grid_search = GridSearchCV(rf_clf, param_grid, cv=3, n_jobs=-1, scoring="accuracy")
    grid_search.fit(train_X, train_y)

    model = grid_search.best_estimator_
    model.fit(train_X, train_y)

    predictions = model.predict(test_X)
    accuracy = accuracy_score(predictions, test_y)
    print(f"Precisión del modelo: {accuracy:.4f}")


if __name__ == "__main__":
    train_and_evaluate()
