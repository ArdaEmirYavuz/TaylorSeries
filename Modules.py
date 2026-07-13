def Pow(data,power):
    total = 1
    for i in range(0,power):
        total *= data
    return total
def Fact(data):
    total = 1
    if(data == 0):
        return 1
    elif(data <0):
        for i in range(data,-1):
            total *= i
    else:
        for i in range(data,1,-1):
            total *= i
    return total

def TaylorSeriesSin(data):
    newValue = -1
    tempValue = 0
    absError = 1
    timer = 0
    i = 1
    values = []
    while(absError > 1.0 *pow(10,-3)):
        if(timer %2 == 0):
            newValue = pow(data,i) / Fact(i)
            values.append(newValue)
            timer+=1
            i +=2
        else:
            newValue = -1 * (pow(data,i) / Fact(i))
            values.append(newValue)
            timer+=1
            i+=2
        absError = abs(newValue - tempValue)
        tempValue = newValue
    return sum(values)
