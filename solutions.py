#1 Write a function named isnegative. It should accept a number and return a boolean value based on whether the input is negative.
def isnegative(number):
    if number < 0:
        return True
    else:
        return False


#2 Write a function named count_evens. It should accept a list and return the number of odd numbers in the list.
def count_evens(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


#3 Write a function named increment_odds. It should accept a list of numbers and return a new list with the odd numbers from the original list incremented.
def increment_odds(numbers):
    new_list = []
    for number in numbers:
        if number % 2 != 0:
            new_list.append(number + 1)
        else:
            new_list.append(number)
    return new_list


#4 Write a function named average. It should accept a list of numbers and return the mean of the numbers.
def average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


#5 Create a function named name_to_dict. It should accept a string
#  that is a first name and last name separated by a space, and return
#  a dictionary with first_name and last_name keys.
def name_to_dict(first_and_last):
    new_dict = {
        'first_name': '',
        'last_name': '',
    }
    names = first_and_last.split(' ')
    new_dict['first_name'] = names[0]
    new_dict['last_name'] = names[1]
    return new_dict


#6 Write a function named capitalize_names. It should accept a list of
#  dictionaries where each dictionary represents a person and has keys
#  first_name and last_name. It should return a list of dictionaries
#  with each person's name capitalized.
def capitalize_names(dicts):
    for dict in dicts:
        for x in dict:
            dict[x] = dict[x].capitalize()
    return dicts



#7 Write a function named count_vowels. It should accept a word and
#  return a number that is the number of vowels in the given word. "y"
#  should not count as a vowel.
def count_vowels(word):
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count += 1
    return count


#8 Write a function named analyze_word. It should accept a string that
#  is a word and return a dictionary with information about the word,
#  the total number of characters in the word, the original word, and
#  the number of vowels in the word.
def analyze_word(word):
    n_letters = len(word)
    n_vowels = count_vowels(word)
    new_dict = {
        'word': '',
        'n_letters': 0,
        'n_vowels': 0
    }
    new_dict['word'] = word
    new_dict['n_letters'] = n_letters
    new_dict['n_vowels'] = n_vowels
    return new_dict


print(type(isnegative(0)))
print(isnegative(4))
print(isnegative(0))
print(isnegative(-6))

print()

print(type(count_evens([1,2,3])))
print(count_evens([1,2,3]))
print(count_evens([4, 6, 8, 10, 12]))
print(count_evens([1, 3, 5, 7, 9]))
print(count_evens([]))
print(count_evens([3, 2]))

print()

print(type(increment_odds([1, 2, 3])))
print(increment_odds([1, 2, 3]))
print(increment_odds([2, 2, 1, 4, 5]))
print(increment_odds([]))
print(increment_odds([0, 1]))

print()

print(type(average([1, 2, 3])))
print(average([1, 2, 3]))
print(average([4, 6, 8, 10, 12]))
print(average([1, 2]))

print()

print(type(name_to_dict('Ada Lovelace')))
print(name_to_dict('Ada Lovelace'))
print(name_to_dict('Marie Curie'))

print()

names = []
names.append({'first_name': 'ada', 'last_name': 'lovelace'})
names.append({'first_name': 'marie', 'last_name': 'curie'})
print(names)

print()

print(type(names))
print(capitalize_names(names))
print(type(capitalize_names(names)))

print()

print(type(count_vowels('codeup')))
print(count_vowels('codeup'))
print(count_vowels('abcde'))
print(count_vowels('why'))

print()

print(type(analyze_word('codeup')))
print(analyze_word('codeup'))
print(analyze_word('abcde'))
print(analyze_word('why'))