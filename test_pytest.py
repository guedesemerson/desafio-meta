from question1 import sum_two_distinct_index
from question2 import balanced_brackets
from question3 import action_profits
from question4 import max_water

class TestTasks:
    def teste_question1(self):
        array_nums = [2, 7, 11, 15]
        target = 9

        assert sum_two_distinct_index(array_nums, target) == [0, 1]

    def teste_question2(self):
        ex = '{{[[(())]]}}'

        assert balanced_brackets(ex) == 'SIM'


    def teste_question3(self):
        ex1 = [7, 1, 5, 3, 6, 4]

        assert action_profits(ex1) > 0

    def teste_question4(self):
        arr = [0, 1, 0, 2, 1, 0,
               1, 3, 2, 1, 2, 1]
        n = len(arr)

        assert max_water(arr, n) == 6