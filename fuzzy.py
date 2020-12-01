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
                                     frio=TrapezoidalFuzzyNumber(0, 0, 10,25),
                                    normal=TriangularFuzzyNumber(15, 25, 30), 
                                    caliente=TrapezoidalFuzzyNumber(25, 30, 40,40))

humedad = LinguisticVar('Humedad',
                                    baja=TrapezoidalFuzzyNumber(0, 0, 40,50),
                                    regular=TriangularFuzzyNumber(40, 55, 70),
                                    alta =  TrapezoidalFuzzyNumber(60,70,100,100)
                                  )

viento = LinguisticVar('Viento',
                                    calmado =TrapezoidalFuzzyNumber(0,0, 10, 20),
                                    moderado =TrapezoidalFuzzyNumber(10,20,40 ,50),
                                    intenso = TrapezoidalFuzzyNumber(40,50,100,100)
                                  )

sensacion = LinguisticVar('Sensacion',
                                    frio=TrapezoidalFuzzyNumber(0, 0, 10,25),
                                    normal=TriangularFuzzyNumber(15, 25, 30), 
                                    caliente=TrapezoidalFuzzyNumber(25, 30, 40,40))

syst = FuzzySystem(rules,[temperatura,humedad,viento],[sensacion]) 
a = syst.mamdani_inference({"Temperatura":23, "Humedad":95, "Viento":15})
b = syst.larsen_inference({"Temperatura":23, "Humedad":95, "Viento":15})


print("Mamdani y MOM")
print(syst.defuzzication_mom(a['Sensacion'], 'Sensacion',2.1))
print("Mamdani y COA")
print(syst.defuzzication_coa(a['Sensacion'], 'Sensacion',2.1))
print("Mamdani y BOA")
print(syst.defuzzication_boa(a['Sensacion'], 'Sensacion',2.1))

print("Larsen y MOM")
print(syst.defuzzication_mom(b['Sensacion'], 'Sensacion',2.1))
print("Larsen y COA")
print(syst.defuzzication_coa(b['Sensacion'], 'Sensacion',2.1))
print("Larsen y BOA")
print(syst.defuzzication_boa(b['Sensacion'], 'Sensacion',2.1))

