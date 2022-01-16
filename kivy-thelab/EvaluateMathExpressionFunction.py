import operator

StringOfExpression = "7+3*6/3-9^5"
ListOfExpression = []
    

for x in StringOfExpression:
    ListOfExpression.append(x)

"""

#peMDas
i = 0    
while i < len(ListOfExpression):

    if ListOfExpression[i] == '*':
        EvaluatedExpression = operator.mul(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
        ListOfExpression[i-1] = EvaluatedExpression
        ListOfExpression.pop(i)
        ListOfExpression.pop(i)
    
    if ListOfExpression[i] == '/':
        EvaluatedExpression = operator.truediv(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
        ListOfExpression[i-1] = EvaluatedExpression
        ListOfExpression.pop(i)
        ListOfExpression.pop(i)

    i+=1


#pEmdas
i = 0
while i < len(ListOfExpression):

    if ListOfExpression[i] == '^':
        EvaluatedExpression = operator.pow(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
        ListOfExpression[i-1] = EvaluatedExpression
        ListOfExpression.pop(i)
        ListOfExpression.pop(i)
    
    i+=1


#pemdAS
i = 0    
while i < len(ListOfExpression):

    if ListOfExpression[i] == '+':
        EvaluatedExpression = operator.add(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
        ListOfExpression[i-1] = EvaluatedExpression
        ListOfExpression.pop(i)
        ListOfExpression.pop(i)
    
    if ListOfExpression[i] == '-':
        EvaluatedExpression = operator.sub(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
        ListOfExpression[i-1] = EvaluatedExpression
        ListOfExpression.pop(i)
        ListOfExpression.pop(i)

    i+=1
"""

def EvaluateMathExpression(A_List):
    
    #pEmdas
    i = 0
    while i < len(ListOfExpression):
        if ListOfExpression[i] == '^':
            EvaluatedExpression = operator.pow(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
            ListOfExpression[i-1] = EvaluatedExpression
            ListOfExpression.pop(i)
            ListOfExpression.pop(i)
        i+=1

    #peMDas 
    i = 0
    while i < len(ListOfExpression):

        if ListOfExpression[i] == '*':
            EvaluatedExpression = operator.mul(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
            ListOfExpression[i-1] = EvaluatedExpression
            ListOfExpression.pop(i)
            ListOfExpression.pop(i)
        
        if ListOfExpression[i] == '/':
            EvaluatedExpression = operator.truediv(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
            ListOfExpression[i-1] = EvaluatedExpression
            ListOfExpression.pop(i)
            ListOfExpression.pop(i)
        i+=1

    #pemdAS
    i = 0
    while i < len(ListOfExpression):

        if ListOfExpression[i] == '+':
            EvaluatedExpression = operator.add(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
            ListOfExpression[i-1] = EvaluatedExpression
            ListOfExpression.pop(i)
            ListOfExpression.pop(i)
        
        if ListOfExpression[i] == '-':
            EvaluatedExpression = operator.sub(float(ListOfExpression[i-1]), float(ListOfExpression[i+1]))
            ListOfExpression[i-1] = EvaluatedExpression
            ListOfExpression.pop(i)
            ListOfExpression.pop(i)
        i+=1



EvaluateMathExpression(ListOfExpression)
print(ListOfExpression)