#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def counting_of_the_unanimous(string):
    return sum(1 for char in string if char.lower() in "аеёиоуыэюя")
string = "Привет, мир!"
print(f"В '{string}' {counting_of_the_unanimous(string)} гласных")
