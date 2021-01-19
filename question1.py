def sum_two_distinct_index(numbers_by_index, target):

    pos = 0
    dictionary = dict()
    while pos < len(numbers_by_index):
        if (target - numbers_by_index[pos]) not in dictionary:
            dictionary[numbers_by_index[pos]] = pos
            pos += 1
        else:
            return [dictionary[target - numbers_by_index[pos]], pos]


def main():
    array_nums = [2, 7, 11, 15]
    target = 9

    print(sum_two_distinct_index(array_nums, target))


if __name__ == '__main__':
    main()
