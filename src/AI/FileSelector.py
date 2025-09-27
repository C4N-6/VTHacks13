import os
from sys import argv
from typing import List, Tuple
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

download("stopwords", quiet=True)
download("punkt_tab", quiet=True)


def findFiles(directory: str) -> List[str]:
    return os.listdir(directory)


def extract_keywords(text: str) -> List[str]:
    keywords = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    keywords = [
        word.lower()
        for word in keywords
        if word.isalpha() and word.lower() not in stop_words
    ]
    return keywords


def findNumberOfKeywordsInText(text: str, keywords: List[str]) -> int:
    num: int = 0
    for word in text.split():
        for keyword in keywords:
            if word == keyword:
                num += 1
                continue

    return num


def getFilesForPrompt(
    directory: str, prompt: str, numberOfFiles: int = 10
) -> List[Tuple]:
    files = findFiles(directory)
    fileRanking: List[Tuple[str, int]] = list()
    keywords = extract_keywords(prompt)

    for file in files:
        with open(directory + "/" + file, "r") as f:
            text = f.read()
        fileRanking.append((file, findNumberOfKeywordsInText(text, keywords)))

    fileRanking.sort(key=lambda x: x[1], reverse=True)

    fileRanking = [x for x in fileRanking if x[1] != 0]
    if fileRanking.__sizeof__() > numberOfFiles:
        fileRanking = fileRanking[:numberOfFiles]

    return fileRanking


if __name__ == "__main__":
    prompt = "Get keywords out of a prompt using Python."

    print(
        getFilesForPrompt(
            "/Users/patetoman/Documents/Git/VTHacks13/questions-2114", prompt, 370
        )
    )
