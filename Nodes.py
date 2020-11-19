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
        return min(self.right.evaluate( var , adjs), self.left.evaluate(var, adjs))

class ORNode(BinaryNode):
    def evaluate(self, var, adjs):
        return max(self.right.evaluate(var, adjs), self.left.evaluate(var, adjs))

class UnaryNode(ExprNode):
    def __init__(self,expr):
        self.expr = expr

    def evaluate(self, var , adjs):
        return 1 - self.expr.evaluate(var,adjs)
class NotNode(UnaryNode):
    pass

class Statement(ExprNode):
    def __init__(self,var, adj):
        self.var = var
        self.adj = adj
    
    def evaluate(self , vars , values):
        return vars[self.var][self.adj](values[self.var])
        
        
class RuleNode(Node):
    def __init__(self,antecedent,consequent):
        self.antecedent = antecedent
        self.consequent = consequent