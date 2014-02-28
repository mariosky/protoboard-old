#!/usr/bin/env python
from FIS import * 

# Variables
service = LinguisticVariable('service')
service.addMF('poor',MF.Gaussian(1.5,0.0))
service.addMF('good',MF.Gaussian(1.5,5.0))
service.addMF('excelent',MF.Gaussian(1.5,10))

food = LinguisticVariable('food')
food.addMF('rancid',MF.Trapezoidal(0.0, 0.0, 1.0, 3.0))
food.addMF('delicious',MF.Trapezoidal(7.0, 9.0, 10.0, 10.0))

tip = LinguisticVariable('tip', type = 'out', range = (0,30))
tip.addMF('cheap',MF.Triangular(0.0,5.0,10.0))
tip.addMF('average',MF.Triangular(10.0,15.0,20.0))
tip.addMF('generous',MF.Triangular(20.0,25.0,30.0)) 

# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('or',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['rancid'])))
r1.consequent.append(FuzzyProposition(tip,tip.mfs['cheap']))

r2 = FuzzyRule()
r2.antecedent.append(FuzzyProposition(service,service.mfs['good']))
r2.consequent.append(FuzzyProposition(tip,tip.mfs['average']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('or',FuzzyProposition(service,service.mfs['excelent']),FuzzyProposition(food,food.mfs['delicious'])))
r3.consequent.append(FuzzyProposition(tip,tip.mfs['generous']))

reglas = [r1,r2,r3]
 
fis = FIS(reglas)
    
def eval(s, f):
    service.current_value = s
    food.current_value = f
 
    return fis.eval()

if __name__ == '__main__':
    eval(5,5)
