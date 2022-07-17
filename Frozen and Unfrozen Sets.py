# set is an unordered unique elements
# set can't be called by indexing but list can be called
# set allow duplicate elements but set don't allow it
number = [1, 2, 34, 57, 8, 23, 6, 78, 22, 12, 2, 24, 211, 1, 1]
s = set(number)
print(s)
s.add(5)
s.add(7)
s.add(6)
print(s)
# frozen set
fs = frozenset(number)
print(fs)
# fs.add(78) {frozen set don't allow modification}


# set operations
A = {"ami", "tmi", "se"}
B = {"AMI", "tmi", "SE"}
print("ami" in A)
print("tumi" in B)
print("Intersections of Two sets: ", A & B)
print("Difference of two sets: ", A - B)
# subset check
AA = {1, 2, 2, 3}
BB = {1, 2}
print(AA < BB)
print(AA > BB)
