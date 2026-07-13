def TaylorSeriesSin(data):
    newValue = -1
    tempValue = 0
    absError = abs(newValue - tempValue)
    while(absError > 1.0 *pow(10,-3)):
        i = 1
        timer = 0
        if(timer %2 == 0):
            newValue = pow(data,i)
            timer+=1
            i +=2
        else:
            newValue = -pow(data,i)
            timer+=1
            i+=2
        absError = abs(newValue - tempValue)
        tempValue = newValue
    return newValue
