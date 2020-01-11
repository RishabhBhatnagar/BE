from collections import Counter
import re


print = lambda *a, **kwa: __import__('builtins').print(*a, '\n', **kwa)
string = input('Enter a string: ')

# Write a Python program to calculate the length of a string.
print("Length of the string:", len(string))

#Write a Python program to count the number of characters (character frequency) in a string.
print("character and frequencies:", Counter(string))

''' Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. If the string length is less than 2, return instead
of the empty string.'''
print("requested string with first and last 2 chars:", "" if len(string) < 2 else string[:2] + string[-2:])

'''Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to $, except the first char
itself.'''
first_char = string[0]
print('modified string with $:', first_char + string.replace(first_char, '$')[1:])

'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each '''
str1, str2, *_ = input('Enter two spaced strings:').split()
print('words with first chars swapped:', str1[0] + str2[1:], str2[0] + str1[1:])

'''Write a Python program to add &#39;ing&#39; at the end of a given string (length
should be at least 3). If the given string already ends with &#39;ing&#39; then add &#39;ly&#39;
instead. If the string length of the given string is less than 3, leave it
unchanged.'''
print('Ingly modified string:', string if len(string) < 3 else string + ('ing', 'ly')[string.endswith('ing')])

'''Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole
'not'...'poor' substring with 'good'. Return the resulting string.'''
print('not-good-poor:', re.sub('not.+poor', 'good', string))

'''Write a Python function that takes a list of words and returns the length of
the longest one.'''
strings = input("Enter a list of spaced strings: ")
print("maximum length of strings is: ", max(map(len, strings.split())))

'''Write a Python program to remove the nth index character from a nonempty
string.'''
n = int(input("Enter the value of n: "))
print(string[:n] + string[n + 1:])

'''Write a Python program to change a given string to a new string where the
first and last chars have been exchanged.'''
print('First and Last chars swapped:', string[-1] + string[1:-1], string[0])

'''Write a Python program to remove the characters which have odd index
values of a given string.'''
print('String with odd index removed:', string[0::2])

'''Write a Python program to count the occurrences of each word in a given
sentence.'''
sent = input("Enter a sentence: ")
print("Word Frequency:", Counter(sent.split()))

'''Write a Python script that takes input from the user and displays that input
back in upper and lower cases.'''
print("Lower Case:{} \nUpper Case:{}".format(string.lower(), string.upper()))

'''Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).'''
sent = input("Enter a comma separated word list: ")
print("sorted unique words:", sorted(set(sent.split(', '))))

'''Write a Python function to create the HTML string with tags around the
word(s).'''
word = input('enter the tag name: ')
print("HTML based: <{tag}></{tag}>".format(tag=word))



"""
Output:
Enter a string: not everyone is poor in studying
Length of the string: 32 

character and frequencies: Counter({' ': 5, 'n': 4, 'o': 4, 'e': 3, 'i': 3, 't': 2, 'r': 2, 'y': 2, 's': 2, 'v': 1, 'p': 1, 'u': 1, 'd': 1, 'g': 1}) 

requested string with first and last 2 chars: nong 

modified string with $: not everyo$e is poor i$ studyi$g 

Enter two spaced strings:one two
words with first chars swapped: owo tne 

Ingly modified string: not everyone is poor in studyingly 

not-good-poor: good in studying 

Enter a list of spaced stringsaaaa bbb cc d
maximum length of strings is:  4 

Enter the value of n: 3
noteveryone is poor in studying 

First and Last chars swapped: got everyone is poor in studyin n 

String with odd index removed: nteeyn spo nsuyn 

Enter a sentence: the the the of of it for for a a a a
Word Frequency: Counter({'a': 4, 'the': 3, 'of': 2, 'for': 2, 'it': 1}) 

Lower Case:not everyone is poor in studying 
Upper Case:NOT EVERYONE IS POOR IN STUDYING 

Enter a comma separated word list: enter, a, comma, separated, word, list
sorted unique words: ['a', 'comma', 'enter', 'list', 'separated', 'word'] 

enter the tag name: html
HTML based: <html></html> 
"""
