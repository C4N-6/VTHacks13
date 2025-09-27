import os
from typing import List, Tuple
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

download("stopwords", quiet=True)
download("punkt_tab", quiet=True)


def findFiles(directory: str) -> List[str]:
    return os.listdir("path/to/directory")


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
                print(word)
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
        with open(file, "r") as f:
            text = f.read()
        fileRanking.append((file, findNumberOfKeywordsInText(text, keywords)))

    fileRanking.sort(key=lambda x: x[1])

    if fileRanking.__sizeof__() > numberOfFiles:
        fileRanking = fileRanking[:10]

    return fileRanking


if __name__ == "__main__":
    prompt = "Get keywords out of a prompt using Python."
    answer = """ Well, a good keywords set is a good method. But, the key is how to build it. There are many way to do it.

Firstly, the simplest one is searching open keywords set in the web. It's depend on your luck and your knowledge. Your keywords (likes "python, java, machine learing") are common tags in Stackoverflow, Recruitment websites. Don't break the law!

The second one is IR(Information Extraction), it's more complex than the last one. There are many algorithms, likes "TextRank", "Entropy", "Apriori", "HMM", "Tf-IDF", "Conditional Random Fields", and so on.

Good lucky.

For matching keywords/phases, Trie Tree is more faster. """
    keywords = extract_keywords(prompt)
    print(keywords)
    print(findNumberOfKeywordsInText(answer, keywords))
