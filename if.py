key_location= "chair"
locations=["table","closet","bookself", "chair","dining"]
for i in locations:
    if i==key_location:
        print("key is found in :", i)
        break
    else:
        print("key is not found in :", i)