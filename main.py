#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word[0:2] == word[-2:][::-1]:
        return True
    else:
        return False

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE  
    print(palindrome(word))
