from stack import Stack


def check_if_nested(s):
    action = Stack()

    for x in s:
        if x in ['(', '{', '[']:
            action.push(x)
        elif x in [')', '}', ']']:
            if action.size() == 0:
                return 0
            y = action.pop()
            if x == ')' and y != '(':
                return 0
            elif x == ']' and y != '[':
                return 0
            elif x == '}' and y != '{':
                return 0
    return 1


if __name__ == '__main__':
    # testing our code - unit tests are shown separately
    test_cases = {
        "([)()]": 0,
        "{[()()]}": 1,
        "": 1,
        "{}": 1,
        "()[}": 0,
        "[]()": 1,
        ")(": 0,
        "}{()": 0,

    }

    for test_element in test_cases.keys():
        assert test_cases[test_element] == check_if_nested(test_element), "The following test " + test_element + "Failed "

    print("Everything is OK")