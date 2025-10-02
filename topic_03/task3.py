def test_dict_functions():
    first_function = {"a": 1, "b": 2, "c": 3}
    print("Початковий словник:", first_function)

    first_function.update({"d": 4})
    print("update({'d': 4}):", first_function)

    del first_function["a"]
    print("del first_function['a']:", first_function)

    print("keys():", list(first_function.keys()))
    print("values():", list(first_function.values()))
    print("items():", list(first_function.items()))

    first_function.clear()
    print("clear():", first_function)

test_dict_functions()
