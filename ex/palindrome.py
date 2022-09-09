# Return the first letter of a word
def first(word):
    return word[0]

# Return the last letter of a word
def last(word):
    return word[-1]

# Return the middle letters of a word
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    "Return True is a word is a palindrome, return False if not"
    word_middle = middle(word)
    word_first = first(word)
    word_last = last(word)
    # If the first letter is different from the last letter
    # It is not a palindrome
    if word_first != word_last:
        return False
    else:
        # If the final unit of word is an empty string
        # It's a palindrome
        if word_middle == '':
            return True
        else:
            # The first letter is equal to the last letter
            # We check the middle characters of a word
            # by using recursive 
            return is_palindrome(word_middle)

def is_palindrome_book(word):
    "Return True is a word is a palindrome."
    # If a word only has only or none character
    # it must be a palindrome
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    # The word has characters more than one
    # The last letter and the first letter of it is equal
    # So, we repeat palindrome function to find 
    # whether the substring is a palindrome
    return is_palindrome_book(middle(word))

words = ['a', 'ab', 'aba', 'abca', 'abcba']

if __name__ == "__main__":
    for i in words:
        print(f'test word: {i}')
        print(f'first: {first(i)}')
        print(f'last: {last(i)}')
        print(f'middle: {middle(i)}')

    for i in words:
        print('\n Test palindrome')
        print(f'{i}:  {is_palindrome(i)}')