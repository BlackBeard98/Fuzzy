from Lexer import RuleLexer
from Parser import RuleParser
from LinguisticVar import LinguisticVar
from membership_functions import TrapezoidalFuzzyNumber , TriangularFuzzyNumber
from fuzzySystem import FuzzySystem
import matplotlib.pyplot as plt
import numpy as np

file = open ("rules.txt", "r")

rule_lexer = RuleLexer()

errors_lexer = rule_lexer.tokenize(file.read())

if len(errors_lexer) > 0:
    for error in errors_lexer:
        print(error) 
    exit(1)

rule_parser = RuleParser()

rules , errors_parser = rule_parser.parse(rule_lexer)


if len(errors_parser) > 0:
    for error in errors_parser:
        print(error)
        exit(1)

temperatura = LinguisticVar('Temperatura',
                                    frio=TriangularFuzzyNumber(10, 15, 20),
                                    normal=TriangularFuzzyNumber(15, 21, 25), 
                                    caliente=TriangularFuzzyNumber(20, 25, 30))

cielo = LinguisticVar('Cielo',
                                    soleado=TriangularFuzzyNumber(0, 10, 20),
                                    nublado=TriangularFuzzyNumber(10, 20, 30),
                                    lluvioso =  TriangularFuzzyNumber(20,30,40)
                                  )

action = LinguisticVar('Accion',
                                    casa=TriangularFuzzyNumber(0, 50, 100),
                                    cine=TriangularFuzzyNumber(50,100 ,150),
                                    playa = TriangularFuzzyNumber(100,150,200)
                                  )


syst = FuzzySystem(rules,[temperatura,cielo],[action, cielo]) 
a = syst.mamdani_inference({"Temperatura":15, "Cielo":17})


t = np.arange(-0. , 200., 0.2)
k = [a['Accion'](x) for x in t]   
plt.plot(t,k, 'r--')
plt.show()
exit()