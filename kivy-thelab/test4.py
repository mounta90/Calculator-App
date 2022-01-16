import re

StringOfExpression = "7+3*6/3-9.5"

StringOfExpression_ListOfNumbers = re.split(pattern = r"[\+\-\*\/]", string = StringOfExpression)

print(StringOfExpression_ListOfNumbers)

