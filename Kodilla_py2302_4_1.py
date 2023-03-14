def palindrome(word):
    return word == word[::-1]

word = input ("Podaj słowo które chcesz sprawdzić: ")

print(palindrome(word))
