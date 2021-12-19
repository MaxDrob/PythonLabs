
string1 = "This is a string."
string2 = " This is another string."
print(string1)
print(string2)
newstring = string1 + string2
print(newstring)

# Примените к любой строке следующие функции

print("длина строки составляет", len(newstring), "знак(а)")
print("Up we go!", newstring.title())
print("Get low()", newstring.lower())
print("Up()", newstring.upper())
print("no space 1()", newstring.rstrip())
print("no space 2()", newstring.lstrip())
print("no space 3()", newstring.strip())
print("Delete something('0')", newstring.strip('0'))

print("task4")
d = "qwerty"
ch = d[2] # извлекается символ ‘e’
print("ch", ch)
chm = d[1:3]
print("chm", chm)
print("other options")
print(d[1:], d[:3], d[:], d[1:5:2])