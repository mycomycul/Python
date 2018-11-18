
#Doc strings are executable code, Comments are not

class sampleClass:
    """
    Sample of a class docstring that can be accessed via help(sampleClass)
    or printing the __doc__ 

    """
    classvar = "Taco"

def theFunction():
    '''
    By placing docstring style comments after object declarations 
    you can access the function's docstring property "__doc__"

    To Access from the Shell you can type help(function_name) to get the docstring
    '''
    print("Python docstrings are not comments.")

print("\nJust printing the docstring value...")
print(theFunction.__doc__)
print(sampleClass.__doc__)
theFunction()
