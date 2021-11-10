def strings_construction(a, b):
    """
    :param a: string - first string
    :param b: string - second string
    :return: integer - count of a occurs in b
    """
    b_letters = {}
    minor_occurs_letter = count = 0
    a_unique = sorted(set(a))
    for letter in a_unique:
        b_letters.update({letter: b.count(letter)})
    for k, v in b_letters.items():
        if count == 0:
            minor_occurs_letter = v
        else:
            if minor_occurs_letter < v:
                minor_occurs_letter = v
    return minor_occurs_letter


print(strings_construction('abc', 'abccba'))
print(strings_construction('aaabbcc', 'acvsdbc'))
print(strings_construction('ovo', 'ano novo'))
