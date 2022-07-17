num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
odd_num = []
for i in num:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)

# list comprehensive method which is compact
even_num = [i for i in num if i % 2 == 0]
print(even_num)
odd_num=[i for i in num if i%2 !=0]
print(odd_num)
square_even_num=[i*i for i in even_num]
print("Square of even numbers :",square_even_num)
square_odd_num=[i*i for i in odd_num]
print("Square of odd numbers :",square_odd_num)
square_num=[i*i for i in num]
print("Square of all  numbers :",square_num)


# set
# set remove duplicates
s = set([1, 2, 2, 3, 54, 6, 4, 6, 2, 67, 27, 72, 7, 2])
print(s)
# set comprehension
even_set = {i for i in s if i % 2 == 0}
print(even_set)
odd_set = {i for i in s if i % 2 != 0}
print(odd_set)

# dictionary
city = ["A", "B", "C"]
country = ["D", "E", "F"]
z = zip(city, country)
print(z)
for amit in z:
    print(amit)

# dictionary comprehension
d= {city : country for city, country in zip(city,country)}
print(d)
