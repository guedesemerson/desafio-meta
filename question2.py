def balanced_brackets(bracket_string):
    brackets_patterns = ['()', '{}', '[]']
    while any(x in bracket_string for x in brackets_patterns):
        for value_bracket in brackets_patterns:
            bracket_string = bracket_string.replace(value_bracket, '')
    if bracket_string == '':
        return 'SIM'
    return 'NÃO'


def main():
    ex1 = '{[()]}'
    ex2 = '{[(])}'
    ex3 = '{{[[(())]]}}'

    print(balanced_brackets(ex1))
    print(balanced_brackets(ex2))
    print(balanced_brackets(ex3))


if __name__ == '__main__':
    main()


