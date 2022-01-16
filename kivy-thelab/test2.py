"""

import re
import operator

class SolveMathExpression():
    StringOfExpression = "7+3*6/3-9.5"
    ListOfExpression = []
    i=0
    

    for x in StringOfExpression:
        ListOfExpression.append(x)

    def EvaluateMathExpression(self):
        while self.i < len(self.ListOfExpression):
            if self.ListOfExpression[self.i] == '*':
                EvaluatedExpression = operator.mul(float(self.ListOfExpression[self.i-1]), float(self.ListOfExpression[self.i+1]))
                self.ListOfExpression[self.i-1] = EvaluatedExpression
                del self.ListOfExpression[self.i-1:self.i+1]
            else:
                pass
            self.i+=1




s = SolveMathExpression()
s.EvaluateMathExpression()
print(s.ListOfExpression)


"""