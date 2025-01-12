import random
LETTER_SCORES = {
'А':1,'Б':3,'В':1,'Г':3,'Д':2,'Е':1,'Ё':3,'Ж':5,'Ж':5,'И':1,
'Й':4,'К':2,'Л':2,'М':2,'Н':1,'О':1,'П':2,'Р':1,'С':1,'Т':1,
'У':2,'Ф':10,'Х':5,'Ц':5,'Ч':5,'Ш':8,'Щ':10,'Ъ':10,'Ы':4,'Ь':3,
'Э':8,'Ю':8,'Я':3
}
def get_random_letter():
    dict_keys = LETTER_SCORES.keys()
    converted_dictionary = list(dict_keys)
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(letter):
    while True:
        player_word = input(f"Введите слово на букву {letter}: ")
        if player_word[0].upper() == letter:
            return player_word
        else:
            print(f"Нужно слово на букву {letter}")

    
def calculate_score(player_word):
    all_scores = []
    for letter in player_word:
        scores = LETTER_SCORES.get(letter.upper(), 0)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = get_random_letter()
    print('Буква: ', random_letter)
    print('Первый игрок')
    first_player_word = get_word_with_letter(random_letter)
    print('Второй игрок')
    second_player_word = get_word_with_letter(random_letter)
    first_player_score = calculate_score(first_player_word)
    print('Очки первого игрока за слово "', first_player_word, '" :',  first_player_score)
    second_player_score = calculate_score(second_player_word)
    print('Очки второго игрока за слово "', second_player_word, '" :', second_player_score)
    if first_player_score > second_player_score:
        print('Победил первый игрок!1!')
    elif first_player_score < second_player_score:
        print('Победил второй игрок!1!')
    else:
        print('Ничья💀💀')


if __name__ == "__main__":
    main()

