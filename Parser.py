import ply.yacc as yacc
from tokens import tokens
from Nodes import *
from Lexer import RuleLexer


class RuleParser():
    def __init__(self):
        self.tokens = tokens
        self.errors = []
       

    def p_program(self, p):
        'program : list_rules'
        p[0]=p[1]

    def p_list_rules(self, p):
        'list_rules : list_rules rule'
        p[0] = p[1] + p[2]

    def p_list_rules_2(self, p):
        'list_rules : rule'
        p[0] = p[1]

    def p_rule (self , p):
        'rule : IF exp THEN list_statement'
        p[0] = [RuleNode(p[2],x) for x in p[4]] 

    def p_list_statement_1 (self , p):
        'list_statement : list_statement COMA statement'
        p[0] = p[1] + [p[3]]
    
    def p_list_statement_2 (self , p):
        'list_statement : statement'
        p[0] = [p[1]]

    def p_exp1 (self , p):
        'exp : exp AND term'
        p[0] = AndNode(p[1], p[3])
    
    def p_exp2 (self , p):
        'exp : exp OR term'
        p[0] = ORNode(p[1], p[3])
    
    def p_exp3 (self, p):
        'exp : term'
        p[0] = p[1]
    
    def p_term1 (self , p):
        'term : NOT term'
        p[0] = NotNode(p[2])
    
    def p_term2 (self , p):
        'term : OPAR exp CPAR'
        p[0] = p[2]
    
    def p_term3 (self , p):
        'term : statement'
        p[0] = p[1]

    def p_statement (self, p):
        'statement : VAR IS ADJ'
        p[0] = Statement(p[1],p[3])
        

    # Error rule for syntax errors
    def p_error(self, p):
        self.errors.append(f"({p.lineno}) - SyntacticError: Error near {p.value}")
    
    def build(self):
        self.parser = yacc.yacc(module=self, write_tables=False)

    def parse(self, lexer):
        self.data = lexer.data
        self.lexer = lexer
        self.build()
        result = None

        if len(lexer.tokens_res) == 0:
            self.errors.append(f"(0,0) - SyntacticError: Error near EOF")
        else:               
            result = self.parser.parse(lexer=lexer)
        return (result ,self.errors)
        