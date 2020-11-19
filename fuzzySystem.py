from Nodes import RuleNode
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
        functions = []
        for rule in self.rules:
            strenght = rule.antecedent.evaluate({var.name:var for var in self.input_variables}, values)
            functions.append( Min(strenght,self.output_variables[rule.consequent.adj](x)))
        return lambda x : max([g(x) for g in functions])


class Min:
    def __init__(self , value, function):
        self.value = value
        self.function = function

    def __call__(self,x ):
        return  (self.value * self.function(x))

class Agregate:
    def __init__(self ,functions):
        self.functions = functions

    def __call__(self,x):
        return max([func(x) for func in self.functions])