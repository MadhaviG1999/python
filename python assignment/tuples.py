thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
print(thistuple[1])
x = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
