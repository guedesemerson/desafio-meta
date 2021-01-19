def max_water(arr, arr_size):
    n = 0
    list_to_append = []
    water = 0

    while n < arr_size:
        if len(list_to_append) == 0 or arr[list_to_append[-1]] >= arr[n]:
            list_to_append.append(n)
            n += 1
        else:
            x = list_to_append[-1]
            list_to_append.pop()
            if len(list_to_append) != 0:
                temp = min(arr[list_to_append[-1]], arr[n])
                dist = n - list_to_append[-1] - 1
                water += dist * (temp - arr[x])
    return water


def main():
    arr = [0, 1, 0, 2, 1, 0,
           1, 3, 2, 1, 2, 1]
    arr_size = len(arr)

    print(max_water(arr, arr_size))


if __name__ == "__main__":
    main()



