# Return Statements - get information back from a called function. function execute then return values, info, etc
def cube(num):                          # can return a str, bool, array, int etc.
    return num*num*num                  # return a value back to the caller *4* from the function; return also breaks the function, no further lines in function will be called
result = cube(4)
print(result)


