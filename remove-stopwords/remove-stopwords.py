def remove_stopwords(tokens: list, stopwords: list) -> list:
    block = set(stopwords)
    return [token for token in tokens if token not in block]