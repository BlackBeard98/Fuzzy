class Node():
    pass


class ExprNode(Node):
    def evaluate(self,var , adjs):
        pass

class BinaryNode(ExprNode):
    def __init__(self , left, right):
        self.left = left
        self.right = right
    
    
class AndNode(BinaryNode):
    def evaluate(self, var, adjs):
        eva  = min(self.right.evaluate( var , adjs), self.left.evaluate(var, adjs))
        return eva

class ORNode(BinaryNode):
    def evaluate(self, var, adjs):
        eva=  max(self.right.evaluate(var, adjs), self.left.evaluate(var, adjs))
        return eva

class UnaryNode(ExprNode):
    def __init__(self,expr):
        self.expr = expr

    
class NotNode(UnaryNode):
    def evaluate(self, var , adjs):
        eva = 1 - self.expr.evaluate(var,adjs)
        return eva

class Statement(ExprNode):
    def __init__(self,var, adj):
        self.var = var
        self.adj = adj
    
    def evaluate(self , vars , values):
        eva = vars[self.var][self.adj](values[self.var])
        return eva
        
class RuleNode(Node):
    def __init__(self,antecedent,consequent):
        self.antecedent = antecedent
        self.consequent = consequent