#!/usr/bin/python
vowel=('a','e','i','o','u')
Vowels=('A','E','I','O','U')
string=raw_input("Enter the string")
ans=""
for letter in string:
	if letter not in vowel and letter not in Vowels:
		ans=ans+letter
print ans
