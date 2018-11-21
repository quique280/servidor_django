from rest_framework import serializers
from pruebas.models import Prueba
from pruebas.models import Deduccion
from pruebas.models import Inferencia
from rest_framework.serializers import SerializerMethodField

from api.parser.grammar.WangLexer import WangLexer
from api.parser.grammar.WangParser import WangParser
from api.src.visitor import WangPrintVisitor, WangCreateDeductionVisitor
from api.src.wang import MyErrorListener
from pruebas.src.proof import Probador

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener

class InferenciaSerializer(serializers.ModelSerializer):
    deduccionVieja = serializers.StringRelatedField()
    deduccionNueva = serializers.StringRelatedField()
    class Meta:
        model = Inferencia
        fields = ('prueba', 'deduccionVieja', 'deduccionNueva', 'regla', 'reglaPosIzq', 'reglaPosDer')
        
class DeduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduccion
        fields = ('prueba', 'afirmacion')

class PruebaSerializer(serializers.ModelSerializer):
    deducciones = DeduccionSerializer(many=True)
    inferencias = InferenciaSerializer(many=True)
    class Meta:
        model = Prueba
        fields = ('afirmacion', 'fecha', 'deducciones', 'inferencias')
    
    def create(self, validated_data):
        print(validated_data)
        lexer = WangLexer(InputStream(validated_data.pop('afirmacion')))
        token_stream = CommonTokenStream(lexer)
        #Setup Parser (and own ErrorListener)
        parser = WangParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())
        try:
            tree = parser.deduction()
        except SyntaxError as e: #TODO: Manejar mejor la excepcion
            print(e.msg)
            sys.exit(-1)
        #Setup the Visitor and visit Parse tree
        visitor = WangPrintVisitor()
        visitor2 = WangCreateDeductionVisitor()
        ded = visitor2.visit(tree)
        print("*** Starts visit of data ***")
        visitor.visit(tree)
        print("***Formula creada***")
        print(ded)
        print(ded.to_formula())
        pr = Probador(ded)
        #print(pr.arbolPrueba)
        pr.arbolPrueba.printear()
        prueba, created = Prueba.objects.update_or_create(afirmacion=str(ded),
            fecha=validated_data.pop('fecha'))
        #return prueba