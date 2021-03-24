from __future__ import print_function


russian_number_system = {
    'ноль': 0,
    'нуля': 0,
    'нулю': 0,
    'нулём': 0,
    'нуле': 0,
    'один': 1,
    'единица': 1,
    'одного': 1,
    'одному': 1,
    'первый': 1,
    'первого': 1,
    'первому': 1,
    'первым': 1,
    'первом': 1,
    'два': 2,
    'двух': 2,
    'двумя': 2,
    'две': 2,
    'второй': 2,
    'второго': 2,
    'второму': 2,
    'вторым': 2,
    'втором': 2,
    'три': 3,
    'трёх': 3,
    'трём': 3,
    'тремя': 3,
    'четыре': 4,
    'четырёх': 4,
    'четырём': 4,
    'четырьмя': 4,
    'пять': 5,
    'пяти': 5,
    'пятью': 5,
    'шесть': 6,
    'шести': 6,
    'шестью': 6,
    'семь': 7,
    'семи': 7,
    'восемь': 8,
    'восеми': 8,
    'восьмью': 8,
    'девять': 9,
    'девяти': 9,
    'девятью': 9,
    'десять': 10,
    'десяти': 10,
    'десятью': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
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
