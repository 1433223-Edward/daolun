def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

user_input = input("请输入数组：")
unsorted_array = list(map(int, user_input.split()))

insertion_sort(unsorted_array)

print("排序后为：", unsorted_array)
