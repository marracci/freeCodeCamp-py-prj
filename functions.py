# using functions = collections of code to perform a specific task
def ciao():                             # defines that a function is being described. all code after this line will be inside the function
    print("Ciao paesano")               # functions must have indented code in order to remain of function
ciao()                                  # executes code inside function

def ciaobella(name, age):               # parameter is a piece of information given to a function. name, age are two parameters given here
    print("Ciao " + name + "your " + str(age) + "years of living treat you well")   #pass in str, int, bool, arrays
ciaobella("Jenna", 29)                  # runs function, gets parameter name as str, and age as int--converting int to str


