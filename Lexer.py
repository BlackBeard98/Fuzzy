import ply.lex as lex
import tokens

class RuleLexer:

    def __init__(self):
        self.tokens =  tokens.tokens
        self.keywords = tokens.keywords
        self.errors = []    #list of errors

    def check_keyword(self, t):
        t_upper = t.value.upper()

        if t_upper in self.keywords:
            t.type = t_upper

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        pass

    def t_ADJ(self, t):
        r'[a-z][0-9A-Za-z_]*'
        self.check_keyword(t)
        return t
    
    def t_VAR(self, t):
        r'[A-Z][0-9A-Za-z_]*'
        self.check_keyword(t)
        return t 

    t_OPAR = r'\('
    t_CPAR = r'\)'
    t_COMA = r','
    t_ignore = ' \t'

    def t_error(self, t):
        print(f"MEh {t.value}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def input(self,data):
        self.build() 
        
        self.data = data
        self.lexer.input(self.data)
    
    
    def tokenize(self, data):
        self.input(data)

        self.tokens_res = []
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            self.tokens_res.append(tok)
            #print(tok)

        self.idx = 0
        return self.errors

    def token(self):
        if self.idx >= len(self.tokens_res):
            return None
        
        self.idx += 1
        return self.tokens_res[self.idx-1]

lexer  = RuleLexer()
lexer.tokenize("IF X is a Not  thEN Y is b \n If not")