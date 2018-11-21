__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

from api.parser.grammar.WangVisitor import WangVisitor
from api.parser.grammar.WangParser import WangParser
from pruebas.src.deduction import *
from pruebas.src.formula import *

"""
    Tests Wang Visitor
    See grammar/Wang.g4
    based on jszheng git https://github.com/jszheng/py3antlr4book
    Example calc
"""
class WangPrintVisitor(WangVisitor):
    def __init__(self):
        pass
        
    def visitFormExpr(self, ctx):
        print(f'\nStart Visiting FormExpr (=>) {len(ctx.sequence())} children')
        children = ctx.sequence()
        for ch in children:
            self.visit(ch)
    
    def visitSeqExpr(self, ctx):
        print(f'Visiting SeqExpr (,) with {len(ctx.expr())} children')
        children = ctx.expr()
        for ch in children:
            self.visit(ch)
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        print(f'Visiting Id={name}')

    def visitAndExpr(self, ctx):
        print('Visiting AndExpr (&)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        

    def visitOrExpr(self, ctx):
        print('Visiting OrExpr (|)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
       
    def visitImplyExpr(self, ctx):
        print('Visiting ImplyExpr (->)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        
    def visitBicondExpr(self, ctx):
        print('Visiting BicondExpr (<->)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))

    def visitParens(self, ctx):
        print('Visiting ParenExpr (...)')
        self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        print('Visiting NotExpr (~) ')
        self.visit(ctx.expr())
        
    
class WangCreateDeductionVisitor(WangVisitor):
    def __init__(self):
        pass
        
    def visitDeduction(self, ctx):
        return self.visit(ctx.formula(0))

    def visitFormExpr(self, ctx):
        list_left = self.visit(ctx.sequence(0))
        if (not list_left):
            list_left = []
        list_right = self.visit(ctx.sequence(1))
        if (not list_right):
            list_right = []
        return Deduction(list_left, list_right)
    
    def visitSeqExpr(self, ctx):
        children = ctx.expr()
        return list(map(lambda ch: self.visit(ch), children))
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        return Atom(name)

    def visitAndExpr(self, ctx):
        form_left = self.visit(ctx.expr(0))
        form_right = self.visit(ctx.expr(1))
        return And(form_left, form_right)
        
    def visitOrExpr(self, ctx):
        form_left = self.visit(ctx.expr(0))
        form_right = self.visit(ctx.expr(1))
        return Or(form_left, form_right)
       
    def visitImplyExpr(self, ctx):
        form_left = self.visit(ctx.expr(0))
        form_right = self.visit(ctx.expr(1))
        return Then(form_left, form_right)
        
    def visitBicondExpr(self, ctx):
        form_left = self.visit(ctx.expr(0))
        form_right = self.visit(ctx.expr(1))
        return Bicond(form_left, form_right)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        return Not(self.visit(ctx.expr()))