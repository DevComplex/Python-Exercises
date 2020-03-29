def flatten_list_v1(elements):
    flattened_list = []

    for el in elements:
        if isinstance(el, list):
            flattened_list += flatten_list_v1(el)
        else:
            flattened_list.append(el)

    return flattened_list

def flatten_list_v2(elements):
    from collections import deque

    elements.reverse()
    stack = deque(elements)
    flattened_list = []

    while(len(stack) > 0):
        top = stack.pop()

        if isinstance(top, list):
            top.reverse()
            stack += top
        else:
            flattened_list.append(top)

    return flattened_list

def test_func(name, func, test_cases):
    print(f"Testing {name}...")

    for (test_case, values) in test_cases.items():
        input_values = values["input"]
        expected_values = values["expected"]

        output_values = func(input_values)

        did_test_pass = output_values == expected_values
        test_state = "Passed" if did_test_pass else "Failed"

        print(f"{test_case}... {test_state}")

def main():
    functions_to_test = {
        "Recursive Flatten List": flatten_list_v1,
        "Iterative Flatten List": flatten_list_v2
    }

    test_cases = {
        "test_case_1": {
            "input": [1, [2, [3, [4, 5, 6, 7, [8, [9, 10]]]]]],
            "expected": list(range(1, 11))
        },
        "test_case_2": {
            "input": [1, [[[[[[[10]]]]]]]],
            "expected": [1, 10]
        }
    }

    for (name, func) in functions_to_test.items():
        test_func(name, func, test_cases)


if __name__ == "__main__":
    main()