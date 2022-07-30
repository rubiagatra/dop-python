my_data = {"num": 42};
your_data = my_data;
your_data["num"] = your_data["num"] + 1;

print(my_data) # {'num': 43}
print(your_data) # {'num': 43}
