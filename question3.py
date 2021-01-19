def action_profits(arr):
    max_profit = 0
    min_profit = arr[0]
    for action_value in arr:
        min_profit = min(action_value, min_profit)
        max_profit = max(max_profit, action_value - min_profit)

    return max_profit


def main():
    ex1 = [7, 1, 5, 3, 6, 4]
    ex2 = [7, 6, 4, 3, 1]
    print(action_profits(ex1))
    print(action_profits(ex2))


if __name__ == "__main__":
    main()


