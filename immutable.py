# tuples are immutable
x = ( 1, 2, 3)
#del x[1]  # This will raise an error because tuples are immutable
print(x)

# list inside a tuple is mutable
y = ([1, 2], 3)
del y[0][1]
print(y)