def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    intval = int(input("Enter a value:"))
    while 0 >= intval or intval > 100:
        intval = int(input("Enter a value:"))
        
    number = intval
        
    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
