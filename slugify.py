def slugify(text):
    letter_list = []
    for letter in text.strip():
        if letter == " ":
            letter_list.append("_" if letter_list[-1] != "_" else "")
        elif letter == "-":
            letter_list.append("_")
        elif letter.isalnum():
            letter_list.append(letter.lower())
    return "".join(letter_list)

print(slugify(""))