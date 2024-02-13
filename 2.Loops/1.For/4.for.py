my_dict = {'a': 1, 'b': 2, 'c': 3}

print("keys")
for key in my_dict:
    print(key)

print("values")
for value in my_dict.values():
    print(value)

print("Key Value Pairs")
for key,value in my_dict.items():
    print(f"{key}:{value}")
    