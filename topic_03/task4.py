def find(sorted_list, element):
    for i, val in enumerate(sorted_list):
        if element < val:
            return i
    return len(sorted_list)  # вставка в кінець

nums = [1, 3, 5, 7, 9]
print("Список:", nums)
x = 6
pos = find(nums, x)
print(f"Елемент {x} слід вставити на позицію {pos}")
 
nums.insert(find(nums, x), x)
print(nums)