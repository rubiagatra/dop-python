from pyrsistent import m
my_data = m(num=42);
your_data = my_data.set('num', 43)

print(my_data) # pmap({'num': 42})
print(your_data) # pmap({'num': 43})
