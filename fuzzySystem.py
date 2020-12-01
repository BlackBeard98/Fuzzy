from Nodes import RuleNode
from LinguisticVar import LinguisticVar
import numpy as np
from scipy.integrate import trapz
class FuzzySystem:

    def __init__ (self ,rules, input_variables , output_variables):
        self.rules = rules
        self.input_variables = {var.name:var for var in input_variables}
        self.output_variables = {var.name:var for var in output_variables}


    def add_rule(self, antecedent, consecuence):
        self.rules.append(RuleNode(antecedent, consecuence))

    def mamdani_inference(self, values):
        functions = {rule.consequent.var:[] for rule in self.rules}
        for rule in self.rules:
            strenght = rule.antecedent.evaluate(self.input_variables, values)
            functions[rule.consequent.var].append(Min(strenght,self.output_variables[rule.consequent.var][rule.consequent.adj]))
        return {name: Agregate(functions[name]) for name in functions}

    def larsen_inference(self , values):
        functions = {rule.consequent.var:[] for rule in self.rules}
        for rule in self.rules:
            strenght = rule.antecedent.evaluate(self.input_variables, values)
            functions[rule.consequent.var].append(Star(strenght,self.output_variables[rule.consequent.var][rule.consequent.adj]))
        return {name: Agregate(functions[name]) for name in functions}
    
    def defuzzication_mom(self,function, variable:str , step):
        l = self.output_variables[variable].min
        r = self.output_variables[variable].max

        mx = 0
        mxs = []
        while l <= r:
            ev = function(l)
            if ev > mx:
                mx = ev
                mxs = [l]
            elif ev == mx:
                mxs.append(l)
            l+= step
        return sum(mxs)/len(mxs)

    def defuzzication_coa(self, function,variable,step):
        l = self.output_variables[variable].min
        r = self.output_variables[variable].max
        suma_n = 0
        suma_d = 0
        while l <= r:
            suma_n += function(l)*l
            suma_d += function(l)
            l+= step
        return suma_n /suma_d

    def defuzzication_boa(self, function,variable,step):
        l = self.output_variables[variable].min
        r = self.output_variables[variable].max
        def _integrate(f, a, b, dx = 1):
            y = [f(x) for x in np.arange(a, b, dx)]
            return trapz(y, dx=dx)
        
        area = _integrate(function,l,r,step)

        ans = 0
        x= r
        while x>1e-5:
            while _integrate(function,l,ans+x,step)<area/2:
                ans+=x
            x= x/2
        return ans
        
    
class Min:
    def __init__(self , value, function):
        self.value = value
        self.function = function

    def __call__(self,x ):
        return  min(self.value , self.function(x))
class Star:
    def __init__(self , value, function):
        self.value = value
        self.function = function

    def __call__(self,x ):
        return  self.value * self.function(x)

class Agregate:
    def __init__(self ,functions):
        self.functions = functions

    def __call__(self,x):
        return max([func(x) for func in self.functions])
