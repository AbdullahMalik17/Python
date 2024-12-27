name="Abdullah Malik "
print(name)
print(type(name))
print(dir(name)) #  tells the methods used in it .
print(id(name))  # tells the physical address .
print([i for i in dir(name)if "_" not in i])     # tells the attributes .


