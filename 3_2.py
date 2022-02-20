words_num = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def num_translate(word):
    if word.istitle:
        return str(words_num.get(word.lower())).title()
    return words_num.get(word)

print(num_translate(input("Введите слово: ")))