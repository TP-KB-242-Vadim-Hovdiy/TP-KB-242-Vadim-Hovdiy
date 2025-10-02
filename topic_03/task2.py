def test():
    my_list = [1, 2, 3]
    print("Початковий список:", my_list)

    my_list.append(4)
    print("append(4):", my_list)

    my_list.extend([5, 6])
    print("extend([5, 6]):", my_list)

    my_list.insert(2, 99)
    print("insert(2, 99):", my_list)

    my_list.remove(99)
    print("remove(99):", my_list)

    copy_list = my_list.copy()
    print("copy():", copy_list)

    my_list.sort(reverse=True)
    print("sort(reverse=True):", my_list)

    my_list.reverse()
    print("reverse():", my_list)

    my_list.clear()
    print("clear():", my_list)

test()
