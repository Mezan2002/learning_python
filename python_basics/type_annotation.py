""" Type annotation """

AGE = 21
AGE = "Python"
print(AGE)

# that is a valid case of python but if we came at python from any other language then we didn't like it so for that also we have an type annotation

AGE: int = 21
AGE = "Python"
print(AGE)  # that is a case that we can define a type of a variable now I am using the pylint for my linting that's why that is not giving any error but if we use mypy then it will give us an error when we are giving a string instead of our number variable
