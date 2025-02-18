



def is_valid(braces: str) -> bool:
    # define a map with closing braces as key and openning braces as value
    # create a stack
    # put each bracket in the string into the stack
    # if the closing bracket doesnt match with the topmost in the stack return false
    # pop the stack
    braces_map = { '}': '}', '[': ']', '(': ')'}
    braces_stack = []

    for brace in braces:
        if brace in braces_map:
            if not braces_stack or braces_stack[-1] != braces_map[brace]:
                return False
            braces_stack.pop()
        else:
            braces_stack.append(brace)
    return len(braces_stack) == 0