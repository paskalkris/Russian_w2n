from __future__ import print_function


russian_number_system = {
    'ноль': 0,
    'нуля': 0,
    'нулю': 0,
    'нулём': 0,
    'нуле': 0,
    'нулевая': 0,
    'нулевого': 0,
    'нулевое': 0,
    'нулевой': 0,
    'нулевом': 0,
    'нулевому': 0,
    'нулевою': 0,
    'нулевую': 0,
    'нулевые': 0,
    'нулевым': 0,
    'нулевыми': 0,
    'нулевых': 0,
    'один': 1,
    'единица': 1,
    'одного': 1,
    'одному': 1,
    'первого': 1,
    'первое': 1,
    'первой': 1,
    'первом': 1,
    'первому': 1,
    'первою': 1,
    'первую': 1,
    'первые': 1,
    'первый': 1,
    'первым': 1,
    'первыми': 1,
    'первых': 1,
    'два': 2,
    'двух': 2,
    'двумя': 2,
    'две': 2,
    'вторая': 2,
    'второго': 2,
    'второе': 2,
    'второй': 2,
    'втором': 2,
    'второму': 2,
    'вторую': 2,
    'вторые': 2,
    'вторым': 2,
    'вторыми': 2,
    'вторых': 2,
    'три': 3,
    'трёх': 3,
    'трём': 3,
    'тремя': 3,
    'третий': 3,
    'третье': 3,
    'третьего': 3,
    'третьей': 3,
    'третьем': 3,
    'третьему': 3,
    'третьею': 3,
    'третьи': 3,
    'третьим': 3,
    'третьими': 3,
    'третьих': 3,
    'третью': 3,
    'третья': 3,
    'четыре': 4,
    'четырёх': 4,
    'четырём': 4,
    'четырьмя': 4,
    'четвёртого': 4,
    'четвёртое': 4,
    'четвёртой': 4,
    'четвёртом': 4,
    'четвёртому': 4,
    'четвёртую': 4,
    'четвёртые': 4,
    'четвёртый': 4,
    'четвёртым': 4,
    'четвёртыми': 4,
    'четвёртых': 4,
    'пять': 5,
    'пяти': 5,
    'пятью': 5,
    'пятого': 5,
    'пятое': 5,
    'пятой': 5,
    'пятом': 5,
    'пятому': 5,
    'пятую': 5,
    'пятые': 5,
    'пятый': 5,
    'пятым': 5,
    'пятыми': 5,
    'пятых': 5,
    'шесть': 6,
    'шести': 6,
    'шестью': 6,
    'шестая': 6,
    'шестого': 6,
    'шестое': 6,
    'шестой': 6,
    'шестом': 6,
    'шестому': 6,
    'шестую': 6,
    'шестые': 6,
    'шестым': 6,
    'шестыми': 6,
    'шестых': 6,
    'семь': 7,
    'семи': 7,
    'седьмая': 7,
    'седьмого': 7,
    'седьмое': 7,
    'седьмой': 7,
    'седьмом': 7,
    'седьмому': 7,
    'седьмую': 7,
    'седьмые': 7,
    'седьмым': 7,
    'седьмыми': 7,
    'седьмых': 7,
    'восемь': 8,
    'восеми': 8,
    'восьмью': 8,
    'восьмая': 8,
    'восьмого': 8,
    'восьмое': 8,
    'восьмой': 8,
    'восьмом': 8,
    'восьмому': 8,
    'восьмую': 8,
    'восьмые': 8,
    'восьмым': 8,
    'восьмыми': 8,
    'восьмых': 8,
    'девять': 9,
    'девяти': 9,
    'девятью': 9,
    'девятая': 9,
    'девятого': 9,
    'девятое': 9,
    'девятой': 9,
    'девятом': 9,
    'девятому': 9,
    'девятую': 9,
    'девятые': 9,
    'девятый': 9,
    'девятым': 9,
    'девятыми': 9,
    'девятых': 9,
    'десять': 10,
    'десяти': 10,
    'десятью': 10,
    'десятая': 10,
    'десятого': 10,
    'десятое': 10,
    'десятой': 10,
    'десятом': 10,
    'десятому': 10,
    'десятую': 10,
    'десятые': 10,
    'десятый': 10,
    'десятым': 10,
    'десятыми': 10,
    'десятых': 10,
    'одиннадцать': 11,
    'одиннадцатая': 11,
    'одиннадцатого': 11,
    'одиннадцатое': 11,
    'одиннадцатой': 11,
    'одиннадцатом': 11,
    'одиннадцатому': 11,
    'одиннадцатую': 11,
    'одиннадцатые': 11,
    'одиннадцатый': 11,
    'одиннадцатым': 11,
    'одиннадцатыми': 11,
    'одиннадцатых': 11,
    'двенадцать': 12,
    'двенадцатая': 12,
    'двенадцатого': 12,
    'двенадцатое': 12,
    'двенадцатой': 12,
    'двенадцатом': 12,
    'двенадцатому': 12,
    'двенадцатую': 12,
    'двенадцатые': 12,
    'двенадцатый': 12,
    'двенадцатым': 12,
    'двенадцатыми': 12,
    'двенадцатых': 12,
    'тринадцать': 13,
    'тринадцатая': 13,
    'тринадцатого': 13,
    'тринадцатое': 13,
    'тринадцатой': 13,
    'тринадцатом': 13,
    'тринадцатому': 13,
    'тринадцатую': 13,
    'тринадцатые': 13,
    'тринадцатый': 13,
    'тринадцатым': 13,
    'тринадцатыми': 13,
    'тринадцатых': 13,
    'четырнадцать': 14,
    'четырнадцатая': 14,
    'четырнадцатого': 14,
    'четырнадцатое': 14,
    'четырнадцатой': 14,
    'четырнадцатом': 14,
    'четырнадцатому': 14,
    'четырнадцатую': 14,
    'четырнадцатые': 14,
    'четырнадцатый': 14,
    'четырнадцатым': 14,
    'четырнадцатыми': 14,
    'четырнадцатых': 14,
    'пятнадцать': 15,
    'пятнадцатая': 15,
    'пятнадцатого': 15,
    'пятнадцатое': 15,
    'пятнадцатой': 15,
    'пятнадцатом': 15,
    'пятнадцатому': 15,
    'пятнадцатую': 15,
    'пятнадцатые': 15,
    'пятнадцатый': 15,
    'пятнадцатым': 15,
    'пятнадцатыми': 15,
    'пятнадцатых': 15,
    'шестнадцать': 16,
    'шестнадцатая': 16,
    'шестнадцатого': 16,
    'шестнадцатое': 16,
    'шестнадцатой': 16,
    'шестнадцатом': 16,
    'шестнадцатому': 16,
    'шестнадцатую': 16,
    'шестнадцатые': 16,
    'шестнадцатый': 16,
    'шестнадцатым': 16,
    'шестнадцатыми': 16,
    'шестнадцатых': 16,
    'семнадцать': 17,
    'семнадцатая': 17,
    'семнадцатого': 17,
    'семнадцатое': 17,
    'семнадцатой': 17,
    'семнадцатом': 17,
    'семнадцатому': 17,
    'семнадцатую': 17,
    'семнадцатые': 17,
    'семнадцатый': 17,
    'семнадцатым': 17,
    'семнадцатыми': 17,
    'семнадцатых': 17,
    'восемнадцать': 18,
    'восемнадцатая': 18,
    'восемнадцатого': 18,
    'восемнадцатое': 18,
    'восемнадцатой': 18,
    'восемнадцатом': 18,
    'восемнадцатому': 18,
    'восемнадцатую': 18,
    'восемнадцатые': 18,
    'восемнадцатый': 18,
    'восемнадцатым': 18,
    'восемнадцатыми': 18,
    'восемнадцатых': 18,
    'девятнадцать': 19,
    'девятнадцатая': 19,
    'девятнадцатого': 19,
    'девятнадцатое': 19,
    'девятнадцатой': 19,
    'девятнадцатом': 19,
    'девятнадцатому': 19,
    'девятнадцатую': 19,
    'девятнадцатые': 19,
    'девятнадцатый': 19,
    'девятнадцатым': 19,
    'девятнадцатыми': 19,
    'девятнадцатых': 19,
    'двадцать': 20,
    'двадцатая': 20,
    'двадцатого': 20,
    'двадцатое': 20,
    'двадцатой': 20,
    'двадцатом': 20,
    'двадцатому': 20,
    'двадцатую': 20,
    'двадцатые': 20,
    'двадцатый': 20,
    'двадцатым': 20,
    'двадцатыми': 20,
    'двадцатых': 20,
    'тридцать': 30,
    'тридцатая': 30,
    'тридцатого': 30,
    'тридцатое': 30,
    'тридцатой': 30,
    'тридцатом': 30,
    'тридцатому': 30,
    'тридцатую': 30,
    'тридцатые': 30,
    'тридцатый': 30,
    'тридцатым': 30,
    'тридцатыми': 30,
    'тридцатых': 30,
    'сорок': 40,
    'сороковая': 40,
    'сорокового': 40,
    'сороковое': 40,
    'сороковой': 40,
    'сороковом': 40,
    'сороковому': 40,
    'сороковую': 40,
    'сороковые': 40,
    'сороковым': 40,
    'сороковыми': 40,
    'сороковых': 40,
    'пятьдесят': 50,
    'пятидесятая': 50,
    'пятидесятого': 50,
    'пятидесятое': 50,
    'пятидесятой': 50,
    'пятидесятом': 50,
    'пятидесятому': 50,
    'пятидесятую': 50,
    'пятидесятые': 50,
    'пятидесятый': 50,
    'пятидесятым': 50,
    'пятидесятыми': 50,
    'пятидесятых': 50,
    'шестьдесят': 60,
    'шестидесятая': 60,
    'шестидесятого': 60,
    'шестидесятое': 60,
    'шестидесятой': 60,
    'шестидесятом': 60,
    'шестидесятому': 60,
    'шестидесятую': 60,
    'шестидесятые': 60,
    'шестидесятый': 60,
    'шестидесятым': 60,
    'шестидесятыми': 60,
    'шестидесятых': 60,
    'семьдесят': 70,
    'семидесятая': 70,
    'семидесятого': 70,
    'семидесятое': 70,
    'семидесятой': 70,
    'семидесятом': 70,
    'семидесятому': 70,
    'семидесятую': 70,
    'семидесятые': 70,
    'семидесятый': 70,
    'семидесятым': 70,
    'семидесятыми': 70,
    'семидесятых': 70,
    'восемьдесят': 80,
    'восьмидесятая': 80,
    'восьмидесятого': 80,
    'восьмидесятое': 80,
    'восьмидесятой': 80,
    'восьмидесятом': 80,
    'восьмидесятому': 80,
    'восьмидесятую': 80,
    'восьмидесятые': 80,
    'восьмидесятый': 80,
    'восьмидесятым': 80,
    'восьмидесятыми': 80,
    'восьмидесятых': 80,
    'девяносто': 90,
    'девяностая': 90,
    'девяностого': 90,
    'девяностое': 90,
    'девяностой': 90,
    'девяностом': 90,
    'девяностому': 90,
    'девяностую': 90,
    'девяностые': 90,
    'девяностый': 90,
    'девяностым': 90,
    'девяностыми': 90,
    'девяностых': 90,
    'сто': 100,
    'сотая': 100,
    'сотого': 100,
    'сотое': 100,
    'сотой': 100,
    'сотом': 100,
    'сотому': 100,
    'сотую': 100,
    'сотые': 100,
    'сотый': 100,
    'сотым': 100,
    'сотыми': 100,
    'сотых': 100,
    "двести": 200,
    'двухсотая': 200,
    'двухсотого': 200,
    'двухсотое': 200,
    'двухсотой': 200,
    'двухсотом': 200,
    'двухсотому': 200,
    'двухсотую': 200,
    'двухсотые': 200,
    'двухсотый': 200,
    'двухсотым': 200,
    'двухсотыми': 200,
    'двухсотых': 200,
    "триста": 300,
    'трёхсотая': 300,
    'трёхсотого': 300,
    'трёхсотое': 300,
    'трёхсотой': 300,
    'трёхсотом': 300,
    'трёхсотому': 300,
    'трёхсотую': 300,
    'трёхсотые': 300,
    'трёхсотый': 300,
    'трёхсотым': 300,
    'трёхсотыми': 300,
    'трёхсотых': 300,
    "четыреста": 400,
    'четырёхсотая': 400,
    'четырёхсотого': 400,
    'четырёхсотое': 400,
    'четырёхсотой': 400,
    'четырёхсотом': 400,
    'четырёхсотому': 400,
    'четырёхсотую': 400,
    'четырёхсотые': 400,
    'четырёхсотый': 400,
    'четырёхсотым': 400,
    'четырёхсотыми': 400,
    'четырёхсотых': 400,
    "пятьсот": 500,
    'пятисотая': 500,
    'пятисотого': 500,
    'пятисотое': 500,
    'пятисотой': 500,
    'пятисотом': 500,
    'пятисотому': 500,
    'пятисотую': 500,
    'пятисотые': 500,
    'пятисотый': 500,
    'пятисотым': 500,
    'пятисотыми': 500,
    'пятисотых': 500,
    "шестьсот": 600,
    'шестисотая': 600,
    'шестисотого': 600,
    'шестисотое': 600,
    'шестисотой': 600,
    'шестисотом': 600,
    'шестисотому': 600,
    'шестисотую': 600,
    'шестисотые': 600,
    'шестисотый': 600,
    'шестисотым': 600,
    'шестисотыми': 600,
    'шестисотых': 600,
    "семьсот": 700,
    'семисотая': 700,
    'семисотого': 700,
    'семисотое': 700,
    'семисотой': 700,
    'семисотом': 700,
    'семисотому': 700,
    'семисотую': 700,
    'семисотые': 700,
    'семисотый': 700,
    'семисотым': 700,
    'семисотыми': 700,
    'семисотых': 700,
    "восемьсот": 800,
    'восьмисотая': 800,
    'восьмисотого': 800,
    'восьмисотое': 800,
    'восьмисотой': 800,
    'восьмисотом': 800,
    'восьмисотому': 800,
    'восьмисотую': 800,
    'восьмисотые': 800,
    'восьмисотый': 800,
    'восьмисотым': 800,
    'восьмисотыми': 800,
    'восьмисотых': 800,
    "девятьсот": 900,
    'девятисотая': 900,
    'девятисотого': 900,
    'девятисотое': 900,
    'девятисотой': 900,
    'девятисотом': 900,
    'девятисотому': 900,
    'девятисотую': 900,
    'девятисотые': 900,
    'девятисотый': 900,
    'девятисотым': 900,
    'девятисотыми': 900,
    'девятисотых': 900,
    'тысяча': 1000,
    'тысячи': 1000,
    'тысяче': 1000,
    'тысячу': 1000,
    'тысячей': 1000,
    'тысяч': 1000,
    'миллион': 1000000,
    'миллиона': 1000000,
    'миллиону': 1000000,
    'миллионом': 1000000,
    'миллионе': 1000000,
    'миллионов': 1000000,
    'миллиард': 1000000000,
    'миллиарда': 1000000000,
    'миллиарду': 1000000000,
    'миллиардом': 1000000000,
    'миллиарде': 1000000000,
    'миллиардов': 1000000000,
    'целых': '.',
    'целая': '.'
}

decimal_words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']


"""
function to form numeric multipliers for million, billion, thousand etc.

input: list of strings
return value: integer
"""


def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(russian_number_system[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] + numbers[1] + numbers[2]
    elif len(numbers) == 2:
        return numbers[0] + numbers[1]
    else:
        return numbers[0]


"""
function to convert post decimal digit words to numerial digits
input: list of strings
output: double
"""


def get_decimal_sum(decimal_digit_words):
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in decimal_words):
            return 0
        else:
            decimal_number_str.append(russian_number_system[dec_word])
    final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
    return float(final_decimal_string)


"""
function to return integer for an input `number_sentence` string
input: string
output: int or double or None
"""


def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()  # converting input to lowercase

    if(number_sentence.isdigit()):  # return the number if user enters a number string
        return int(number_sentence)

    split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

    clean_numbers = []
    clean_decimal_numbers = []

    # removing and, & etc.
    for word in split_words:
        if word in russian_number_system:
            clean_numbers.append(word)

    # Error message if the user enters invalid input!
    if len(clean_numbers) == 0:
        raise ValueError("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)") 

    # Error if user enters million,billion, thousand or decimal point twice
    if clean_numbers.count('тысяча') > 1 or clean_numbers.count('миллион') > 1 or clean_numbers.count('миллиард') > 1 or clean_numbers.count('целых') > 1 or clean_numbers.count('целая') > 1:
        raise ValueError("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    # separate decimal part of number (if exists)
    if clean_numbers.count('целых') == 1 or clean_numbers.count('целая') == 1:
        clean_decimal_numbers = clean_numbers[clean_numbers.index('целых')+1:]
        clean_numbers = clean_numbers[:clean_numbers.index('целых')]

    if 'миллиард' in clean_numbers:
        billion_index = clean_numbers.index('миллиард')
    elif 'миллиарда' in clean_numbers:
        billion_index = clean_numbers.index('миллиарда')
    elif 'миллиарду' in clean_numbers:
        billion_index = clean_numbers.index('миллиарду')
    elif 'миллиардом' in clean_numbers:
        billion_index = clean_numbers.index('миллиардом')
    elif 'миллиарде' in clean_numbers:
        billion_index = clean_numbers.index('миллиарде')
    elif 'миллиардов' in clean_numbers:
        billion_index = clean_numbers.index('миллиардов')
    else:
        billion_index = -1
        
    if 'миллион' in clean_numbers:
        million_index = clean_numbers.index('миллион')
    elif 'миллиона' in clean_numbers:
        million_index = clean_numbers.index('миллиона')
    elif 'миллиону' in clean_numbers:
        million_index = clean_numbers.index('миллиону')
    elif 'миллионом' in clean_numbers:
        million_index = clean_numbers.index('миллионом')
    elif 'миллионе' in clean_numbers:
        million_index = clean_numbers.index('миллионе')
    elif 'миллионов' in clean_numbers:
        million_index = clean_numbers.index('миллионов')
    else:
        million_index = -1
    
    if 'тысяча' in clean_numbers:
        thousand_index = clean_numbers.index('тысяча')
    elif 'тысячи' in clean_numbers:
        thousand_index = clean_numbers.index('тысячи')
    elif 'тысяче' in clean_numbers:
        thousand_index = clean_numbers.index('тысяче')
    elif 'тысячу' in clean_numbers:
        thousand_index = clean_numbers.index('тысячу')
    elif 'тысячей' in clean_numbers:
        thousand_index = clean_numbers.index('тысячей')
    elif 'тысяч' in clean_numbers:
        thousand_index = clean_numbers.index('тысяч')
    else:
        thousand_index = -1

    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        raise ValueError("Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    total_sum = 0  # storing the number to be returned

    if len(clean_numbers) > 0:
        # hack for now, better way TODO
        if len(clean_numbers) == 1:
                total_sum += russian_number_system[clean_numbers[0]]

        else:
            if billion_index > -1:
                billion_multiplier = number_formation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * 1000000000

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                        
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                        
                elif thousand_index == 0:
                    thousand_multiplier = 1
                
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index == len(clean_numbers)-1:
                hundreds = 0
            elif thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[thousand_index+1:])
            elif million_index > -1 and million_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[million_index+1:])
            elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[billion_index+1:])
            elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                hundreds = number_formation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds

    # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        decimal_sum = get_decimal_sum(clean_decimal_numbers)
        total_sum += decimal_sum

    return total_sum
