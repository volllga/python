assert abs(-42) == 42
# assert abs(-42) == -42, "Should be absolute value of a number"
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# умеет подставлять пользовательские значения в строки с помощью функции .format()

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


#print(test_input_text(8, 5))
print(test_substring("fulltext", "some_value"))

