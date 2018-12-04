def is_unique(input_string):
    exists_map = []

    for i in range(128):
        exists_map.append(False)

    for c in input_string.lower():
        if exists_map[ord(c)]:  # ord(<char>) gets ASCII value of the char
            return False
        exists_map[ord(c)] = True

    return True


print(is_unique("test"))
print(is_unique("Test"))
print(is_unique("tub"))
