import re
import operator

#ListOfOperators = ['+', '-', '*', '/']

StringOfExpression = "7+3*6/3-9.5"

#StringOfExpression_ListOfNumbers = re.split(pattern = r"[\+\-\*\/]",
#         string = StringOfExpression)


"""StringOfExpression_ListOfOperators = []

for x in StringOfExpression:
    for op in ListOfOperators:
        if x == op:
            StringOfExpression_ListOfOperators.append(x)
        else:
            pass

print(StringOfExpression_ListOfOperators)
print(StringOfExpression_ListOfNumbers)

for op in StringOfExpression_ListOfOperators:
    if op == '*' or op == '/':
        print(StringOfExpression_ListOfOperators.index(op))
        print("The " + str(op) + " occured at: " + str(StringOfExpression_ListOfOperators.index(op)))
    else:
        pass
"""

ListOfExpression = []

for x in StringOfExpression:
    ListOfExpression.append(x)

print(ListOfExpression)


ListOfExpression2 = ListOfExpression.copy()

print(len(ListOfExpression2))

for i in range(len(ListOfExpression2)):
    if ListOfExpression2[i-1] == '*':
        EvaluatedExpression = operator.mul(float(ListOfExpression2[i-2]), float(ListOfExpression2[i]))
        ListOfExpression2[i-2] = EvaluatedExpression
        
        
    else:
        pass 
    
    #else:
    #    EvaluatedExpression = operator.truediv(float(ListOfExpression2[index-1]), float(ListOfExpression2[index+1]))
    #    ListOfExpression2[index-1] = EvaluatedExpression
    #    ListOfExpression2.pop(index)
    #    ListOfExpression2.pop(index+1)

print(ListOfExpression2)
#"7+3*6/3-9.5" -> 7+6-9.5

#StringOfExpression2 = StringOfExpression[:3]            [:2] prints indeces 0,1 not 2


