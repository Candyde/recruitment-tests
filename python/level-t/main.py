
def is_palindrome(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
     
    string = input("Enter the string: ")
    status= is_palindrome(string)
    if(status):
        return("It is a palindrome ")
    else:
        return("Sorry! Try again")