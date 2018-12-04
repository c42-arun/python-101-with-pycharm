def is_permutation(input_str1, input_str2):
    if len(input_str1) != len(input_str2):
        print('Strings of different lengths cannot be permutations of one another')
        return False

    ascii_sum1 = 0
    ascii_sum2 = 0

    '''
    for c in input_str1.lower():
        ascii_sum1 = ascii_sum1 + ord(c)

    for c in input_str2.lower():
        ascii_sum2 += ord(c)
    '''

    for i in range(len(input_str1)):
        ascii_sum1 += ord(input_str1[i])
        ascii_sum2 += ord(input_str2[i])

    '''
    print('String 1 =' + str(ascii_sum1))
    print('String 2 =' + str(ascii_sum2))
    '''

    if ascii_sum1 == ascii_sum2:
        print('They are permutations')
        return True
    else:
        print('They are NOT permutations')
        return False


is_permutation('dog', 'god')
is_permutation('chair', 'hair')
is_permutation('chair', 'stair')
