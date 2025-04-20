def slugify(text):
    return "_".join(word.lower()
                    for word in text.split(" "))


print(slugify(""))