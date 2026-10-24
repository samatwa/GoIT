def check_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return "Asymmetrical"
            stack.pop()

    if not stack:
        return "Symmetrical"
    else:
        return "Asymmetrical"

# Приклади використання:
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(f"{expr}: {check_balanced(expr)}")
