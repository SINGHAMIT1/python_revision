# by using json we can convert the data from dict to string format
book = {}
book["tom"] = {
    "name": 'tom',
    "address": '145 new york, usa',
    "phone": 12454411

}
book["john"] = {
    "name": 'john',
    "address": '145 new york, usa',
    "phone": 2454250

}
print(book)
print(type(book))
import json

s = json.dumps(book)
print(s)
print(type(s))
