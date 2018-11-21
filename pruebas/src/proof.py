"""
Prototipo de modelo de objetos para Wang
loriacarlos@gmail.com
@since II-2018

Modificado por:
-María Álvarez Hernández
-Luis ALonso Calderón Achío
-Enrique Díaz Delgado
-Derian Sibaja Chavarría
"""

from pruebas.src.deduction import *
from pruebas.src.formula import *
from enum import Enum, auto
from abc import ABCMeta, abstractmethod
from pruebas.src.utils import *
from pruebas.src.tree import Tree
from pruebas.models import *

class RuleType(Enum):
    AXIOM = auto()
    OR_LEFT = auto()
    OR_RIGHT = auto()
    AND_LEFT = auto()
    AND_RIGHT = auto()
    EQUIV_IMPLIES_LEFT = auto()
    EQUIV_IMPLIES_RIGHT = auto()
    EQUIV_BICOND_LEFT = auto()
    EQUIV_BICOND_RIGHT = auto()
    NOT_RIGHT = auto()
    NOT_LEFT = auto()

class Just:
    def __init__(self, subject, rule):
        self.subject = subject
        self.rule = rule
        
class Rule(metaclass=ABCMeta):
    def __init__(self, ruletype):
        self.__ruletype = ruletype
    @abstractmethod
    def apply(self, deduction): pass
    @property
    def kind(self):
        return self.__ruletype

    def __call__(self, deduction):
        return self.apply(deduction)

class Axiom(Rule):
    def __init__(self):
        super().__init__(RuleType.AXIOM)
    
    def apply(self, deduction):
        yield from iFirst(((self, (x[0], y[0]), deduction) 
        for x in enumerate(deduction.left)
        for y in enumerate(deduction.right) if x[1] == y[1]))

    def __str__(self):
        return "Axiom"
        

AXIOM_RULE = Axiom()

class AndLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.AND_LEFT)
    def apply(self, deduction):
        ands = (f for f in enumerate(deduction.left) if isinstance(f[1], And))
        yield from iFirst(((self, (f[0], None),
            Deduction(list(replace(deduction.left, f[0], [f[1].left, f[1].right])), deduction.right))
            for f in ands))

    def __str__(self):
        return "And-Left"
            
AND_LEFT_RULE= AndLeft()        
            
class OrRight(Rule):
    def __init__(self):
        super().__init__(RuleType.OR_RIGHT)
    def apply(self, deduction):
        ors = (f for f in enumerate(deduction.right) if isinstance(f[1], Or))
        yield from iFirst(((self, (None, f[0]),
            Deduction(deduction.left, list(replace(deduction.right, f[0], [f[1].left, f[1].right]))))
            for f in ors))

    def __str__(self):
        return "Or-Right"

OR_RIGHT_RULE= OrRight()

            
class OrLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.OR_LEFT)
    def apply(self, deduction):
        firstOr = firstOccurrence(lambda f: isinstance(f[1], Or), enumerate(deduction.left))
        #ors = (f for f in enumerate(deduction.left) if isinstance(f[1], Or))
        #for f in ors:
        if(firstOr != None):
            replaced1 = list(replace(deduction.left, firstOr[0], [firstOr[1].left]))
            replaced2 = list(replace(deduction.left, firstOr[0], [firstOr[1].right]))
            yield (self, (firstOr[0], None), Deduction(replaced1, deduction.right))
            yield (self, (firstOr[0], None), Deduction(replaced2, deduction.right))

    def __str__(self):
        return "Or-Left"
            
OR_LEFT_RULE= OrLeft()  

class AndRight(Rule):
    def __init__(self):
        super().__init__(RuleType.AND_RIGHT)
    def apply(self, deduction):
        firstAnd = firstOccurrence(lambda f: isinstance(f[1], And), enumerate(deduction.right))
        #ands = (f for f in enumerate(deduction.right) if isinstance(f[1], And))
        #for f in ands:
        if(firstAnd != None):
            replaced1 = list(replace(deduction.right, firstAnd[0], [firstAnd[1].left]))
            replaced2 = list(replace(deduction.right, firstAnd[0], [firstAnd[1].right]))
            yield (self, (None, firstAnd[0]), Deduction(deduction.left, replaced1))
            yield (self, (None, firstAnd[0]), Deduction(deduction.left, replaced2))

    def __str__(self):
        return "And-Right"
            
AND_RIGHT_RULE= AndRight()  

class EquivImpliesLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.EQUIV_IMPLIES_LEFT)
    def apply(self, deduction):
        thens = (f for f in enumerate(deduction.left) if isinstance(f[1], Then))
        return iFirst(((self, (f[0], None), 
            Deduction(list(replace(deduction.left, f[0], [f[1].weak_nf()])), deduction.right)) 
            for f in thens))

    def __str__(self):
        return "Equiv.Implies-Left"
            
EQUIV_IMPLIES_LEFT = EquivImpliesLeft() 

class EquivImpliesRight(Rule):
    def __init__(self):
        super().__init__(RuleType.EQUIV_IMPLIES_RIGHT)
    def apply(self, deduction):
        thens = (f for f in enumerate(deduction.right) if isinstance(f[1], Then))
        return iFirst(((self, (None, f[0]), 
            Deduction(deduction.left, list(replace(deduction.right, f[0], [f[1].weak_nf()])))) 
            for f in thens))

    def __str__(self):
        return "Equiv.Implies-Right"
            
EQUIV_IMPLIES_RIGHT = EquivImpliesRight() 

class EquivBicondLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.EQUIV_BICOND_LEFT)
    def apply(self, deduction):
        biconds = (f for f in enumerate(deduction.left) if isinstance(f[1], Bicond))
        return iFirst(((self, (f[0], None), 
            Deduction(list(replace(deduction.left, f[0], [f[1].weak_nf()])), deduction.right)) 
            for f in biconds))

    def __str__(self):
        return "Equiv.Bicond-Left"
            
EQUIV_BICOND_LEFT = EquivBicondLeft() 

class EquivBicondRight(Rule):
    def __init__(self):
        super().__init__(RuleType.EQUIV_BICOND_RIGHT)
    def apply(self, deduction):
        biconds = (f for f in enumerate(deduction.right) if isinstance(f[1], Bicond))
        return iFirst(((self, (None, f[0]), 
            Deduction(deduction.left, list(replace(deduction.right, f[0], [f[1].weak_nf()])))) 
            for f in biconds))

    def __str__(self):
        return "Equiv.Bicond-Right"
            
EQUIV_BICOND_RIGHT = EquivBicondRight()  

class NotLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.NOT_LEFT)
    def apply(self, deduction):
        nots = (f for f in enumerate(deduction.left) if isinstance(f[1], Not))
        for f in nots:
            newLeft, newRight = deduction.left[:], deduction.right[:]
            newRight.insert(0, newLeft.pop(f[0]).left)
            yield (self, (f[0], None), Deduction(newLeft, newRight))
            return

    def __str__(self):
        return "Not-Left"

NOT_LEFT = NotLeft()  

class NotRight(Rule):
    def __init__(self):
        super().__init__(RuleType.NOT_RIGHT)
    def apply(self, deduction):
        nots = (f for f in enumerate(deduction.right) if isinstance(f[1], Not))
        for f in nots:
            newLeft, newRight = deduction.left[:], deduction.right[:]
            newLeft.insert(0, newRight.pop(f[0]).left)
            yield (self, (None, f[0]), Deduction(newLeft, newRight))
            return

    def __str__(self):
        return "Not-Right"

NOT_RIGHT = NotRight()  
        
class Probador():
    def __init__(self, deduction):
        self.afirmacion = deduction
        self.__deducciones = None
        self.__inferencias = None
        self.__arbolPrueba = None
    @property
    def deducciones(self):
        if(not self.__deducciones):
            self.probar()
        return self.__deducciones

    @property
    def inferencias(self):
        if(not self.__inferencias):
            self.__inferencias, self.__deducciones = self.inferenciasDeducciones(self.arbolPrueba)
        return self.__inferencias

    @property
    def arbolPrueba(self):
        if(not self.__arbolPrueba):
            self.__arbolPrueba = Tree(('Initial State', None, self.afirmacion))
            list(map(lambda x:self.__arbolPrueba.addChild(x),self.probar()))
        return self.__arbolPrueba

    def inferenciasDeducciones(self, arbol):
        inferencias = []
        deducciones = []
        for ch in arbol.children:
            inferenciasHijas, deduccionesHijas = self.inferenciasDeducciones(ch)
            inferencias += inferenciasHijas
            deducciones += deduccionesHijas
            deducciones.append({
                "afirmacion": str(arbol.value[2])
            })
            inferencias.append({
                'deduccionVieja': str(arbol.value[2]),
                'deduccionNueva': str(ch.value[2]),
                'regla': str(ch.value[0]),
                'reglaPosIzq': ch.value[1][0] if ch.value[1] else None,
                'reglaPosDer': ch.value[1][1] if ch.value[1] else None
            })
        return inferencias, deducciones

    def chainApply(self, deduct, iterRules):
        applied = firstAppliedNotNone(deduct, iterRules)
        if(applied != None):
            for ch in applied:
                arbol = Tree(ch)
                if ch[0].kind != RuleType.AXIOM:
                    list(map(lambda x:arbol.addChild(x),self.chainApply(ch[2], iterRules)))
                yield arbol
            return
        yield Tree(('Unable to prove', None, deduct))

    
    def probar(self):
        ruleList = [
            AXIOM_RULE,
            AND_LEFT_RULE,
            OR_RIGHT_RULE,
            OR_LEFT_RULE,
            AND_RIGHT_RULE,
            EQUIV_IMPLIES_LEFT,
            EQUIV_IMPLIES_RIGHT,
            EQUIV_BICOND_LEFT,
            EQUIV_BICOND_RIGHT,
            NOT_LEFT,
            NOT_RIGHT,
        ]
        yield from self.chainApply(self.afirmacion, ruleList)
        

if __name__ == "__main__":
    print("*** Testing Proofs ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    a = And(p, q)
    na = Not(a)
    b = Or(a, na)
    c = Then(p, b)
    ded = Deduction([a, b, p], [na, c, p])
    print("1) Axiom test", ded)
    list(map(lambda x: print(x),AXIOM_RULE.apply(ded)))
    print("2) AndLeft Test", ded)
    list(map(lambda x: print(x),AND_LEFT_RULE.apply(ded)))
    
    