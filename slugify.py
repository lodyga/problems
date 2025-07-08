def slugify(text):
    letter_list = []
    for letter in text.strip():
        if letter in " -_":
            if letter_list and letter_list[-1] != "_":
                letter_list.append("_")
        elif letter.isalnum():
            letter_list.append(letter.lower())
    return "".join(letter_list)

print(slugify(""))