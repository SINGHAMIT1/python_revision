d={"amit":176551368,"mom":1239999,"dad":3223343212,"brother":2492349}
print(d)
print(d["mom"])
d["gf"]=54983
print(d)
del d["gf"]
print(d)
for key in d:
    print("key :", key,
          "value :", d[key])
for k,v in d.items():
    print("key :", k,
          "value :", v)
print(d)
"amit" in d
"samir" in d
d.clear()
print(d)

