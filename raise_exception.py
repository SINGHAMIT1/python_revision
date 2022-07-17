# raise exception
try:
    raise MemoryError("Memory error")
except MemoryError as e:
    print(e)
# user defined exception is basically an object/instance of a class
# finally keyword will execute no matter what exceptions occur
