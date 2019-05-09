def find(_str):
    for i, ltr in enumerate(_str):
        if ltr in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            yield i


def calculate_ans(_question):
    int_index = list(find(_question))
    for i in range(0, len(int_index)):
        if i + 1 < len(int_index) and _question[int_index[i] + 1:int_index[i + 1]].count('?') > 2 and int(
                _question[int_index[i]]) + int(_question[int_index[i + 1]]) is 10:
            return True
    return False


question = "asde1a5?dse?se?s5fsad"
print(calculate_ans(question))
