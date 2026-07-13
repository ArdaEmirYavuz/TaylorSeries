import math
import ModuleTaylor as Taylor
def TaylorSeriesE(x):
    tempValue = 1
    timer = 1
    newValue = 0
    absError = 1 
    if(x <= -9):
        return 0
    elif(x >= 710):
        return "Overflow"
    while(True):
        newValue = tempValue + (Taylor.Pow(x,timer)/Taylor.Fact(timer))
        absError = abs(newValue - tempValue)
        tempValue = newValue
        if(absError < 1.0*pow(10,-3)):
            return newValue
        else:
            timer +=1
            continue
concl = TaylorSeriesE(710)
concl2 = TaylorSeriesE(3) / Taylor.TaylorSeriesSin(3)
print(concl)
print(concl2)
