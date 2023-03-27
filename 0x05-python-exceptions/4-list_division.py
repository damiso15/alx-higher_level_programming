#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for element in range(list_length):
        try:
            res = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result.append(res)
    return result
