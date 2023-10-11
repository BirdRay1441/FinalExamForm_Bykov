#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def it_is_a_palindrome(string):
    return string == string[::-1]
string = "радар"
print(f"Является ли '{string}' палиндромом? {it_is_a_palindrome(string)}")
