def is_balanced(expression):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_mapping.values():
            stack.append(char)
        elif char in bracket_mapping and (not stack or stack.pop() != bracket_mapping[char]):
            return False

    return not stack

# Test the function
expression1 = "([]{})"
expression2 = "([)]"
expression3 = "({[]})"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
print(is_balanced(expression3))  # Output: True