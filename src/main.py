from AI import AI


if __name__ == "__main__":
    ai = AI()

    print(ai.askAI("hello how are you doing"))


def getURL(filename):
    if str(filename).count(".") > 1:
        return "hidden files dont work"
    name_without_extension = filename.rsplit(".", 1)[0]
    return f"https://piazza.com/class/m63z5y05jgj3f6/post/{name_without_extension}"