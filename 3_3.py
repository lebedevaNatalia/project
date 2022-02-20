names = ("Иван", "Мария", "Петр", "Илья", "Андрей", "Ольга", "Алексей", "Антон", "Анна")

def thesaurus(names):
    names_dict = {}
    for i in sorted(names):
        letter = i[0]
        if letter in names_dict:
            names_dict[letter] += [i]
        else:
            names_dict[letter] = [i]
    return names_dict

print(thesaurus(names))
    