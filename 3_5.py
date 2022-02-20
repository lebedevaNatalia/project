from random import choice, randrange

nouns = ["автомобирь", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat):
    i = nouns.copy()
    j = adverbs.copy()
    k = adjectives.copy()
    list_jokes = []
    list_min = min(i, j, k)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat > 0:
            list_jokes.append(f'{i.pop(num)} {j.pop(num)} {k.pop(num)}')
        else:
            list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice.adjectives}')
        n -= 1
    return list_jokes

print(get_jokes(n, repeat))


