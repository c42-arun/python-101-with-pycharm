def urlify(input_str, length):
    char_arr = []
    for i in range(len(input_str)):
        char_arr.append(input_str[i])

    for i in range(length):
        if char_arr[i] == ' ':
            shift_chars(char_arr, i, 2)

            char_arr[i] = '%'
            char_arr[i + 1] = '2'
            char_arr[i + 2] = '0'

    return ''.join(char_arr)


def shift_chars(char_arr, start_index, no_of_moves):
    for i in range(len(char_arr) - 1, start_index + no_of_moves, -1):
        char_arr[i] = char_arr[i - no_of_moves]


print(urlify('Mr John  ', 9))
