def merge_func(lst, starting_index, mid_index, last_index):
    len1 = mid_index - starting_index + 1
    len2 = last_index - mid_index

    list1 = []
    list2 = []

    for i in range(starting_index, mid_index + 1):
        list1.append(lst[i])
    for i in range(mid_index + 1, last_index + 1):
        list2.append(lst[i])

    # # With while loop:
    # itr = starting_index
    # itr1 = 0
    # while itr1 < len1:
    #     list1.append(lst[itr])
    #     itr1 += 1
    #     itr += 1
    #
    # itr = mid_index + 1
    # itr2 = 0
    # while itr2 < len2:
    #     list2.append(lst[itr])
    #     itr2 += 1
    #     itr += 1

    itr = starting_index
    itr1, itr2 = 0, 0

    while itr1 < len1 and itr2 < len2:
        if list1[itr1] <= list2[itr2]:
            lst[itr] = list1[itr1]
            itr1 += 1
        else:
            lst[itr] = list2[itr2]
            itr2 += 1
        itr += 1

    while itr1 < len1:
        lst[itr] = list1[itr1]
        itr += 1
        itr1 += 1

    while itr2 < len2:
        lst[itr] = list2[itr2]
        itr += 1
        itr2 += 1


def merge_sort_func(lst, starting_index, last_index):
    if starting_index >= last_index:
        return

    mid_index = (starting_index + last_index) // 2

    merge_sort_func(lst, starting_index, mid_index)
    merge_sort_func(lst, mid_index + 1, last_index)

    merge_func(lst, starting_index, mid_index, last_index)


if __name__ == "__main__":
    # input_list = [3, 2, 9, 0, 2, -1, 343]

    input_list = list(map(int, input().split(",")))
    merge_sort_func(input_list, 0, len(input_list) - 1)
    print(input_list)
