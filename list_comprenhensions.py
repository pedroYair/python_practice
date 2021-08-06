"""
Key Points to Remember:

List comprehension is an elegant way to define and create lists based on existing lists.

List comprehension is generally more compact and faster than normal functions and loops for creatinglist.

However, we should avoid writing very long list comprehensions in one line to ensure that code is
user-friendly.

Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten
 in the form of list comprehension.




"""

# generar nueva lista con aquellos nombres que tengan la letra "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# pasar los nombres de la lista a mayusculas
newlist = [x.upper() for x in fruits]
print(newlist)

# lista con los numeros del 0 al 19
newlist2 = [x for x in range(20)]
print(newlist2)

newlist3 = [x for x in range(21) if x % 2 == 0]
print(newlist3)

# retorna el valor si es par, caso contrario retorna el string "impar"
newlist4 = [x if x % 2 == 0 else "impar" for x in range(21)]
print(newlist4)

newlist5 = [x for x in range(21) if x % 2 == 0 if x % 3 == 0]
print(newlist5)
