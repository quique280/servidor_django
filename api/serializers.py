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
from django.db.utils import IntegrityError

import datetime
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
    deducciones = DeduccionSerializer(many=True, read_only=False)
    inferencias = InferenciaSerializer(many=True, read_only=False)
    class Meta:
        model = Prueba
        fields = ('afirmacion', 'fecha', 'deducciones', 'inferencias')
    
    def to_internal_value(self, data):
        data['inferencias'] = []
        data['deducciones'] = []
        
        return super(PruebaSerializer,self).to_internal_value(data)

    def create(self, validated_data):
        afir = validated_data.pop('afirmacion')
        lexer = WangLexer(InputStream(afir))
        token_stream = CommonTokenStream(lexer)
        parser = WangParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())
        try:
            tree = parser.deduction()
        except SyntaxError as e: #TODO: Manejar mejor la excepcion
            print(e.msg)
            error = {'afirmacion': "Failed to parse"}
            raise serializers.ValidationError(error)
        visitor = WangCreateDeductionVisitor()
        ded = visitor.visit(tree)
        pr = Probador(ded)
        if not 'fecha' in validated_data:
            fec = datetime.datetime.now()
        validated_data['afirmacion'] = str(pr.afirmacion)
        validated_data['fecha'] = fec
        validated_data['inferencias'] = pr.inferencias
        validated_data['deducciones'] = pr.deducciones
        inferencias_data = validated_data.pop('inferencias')
        deducciones_data = validated_data.pop('deducciones')
        try:
            prueba = Prueba.objects.create(**validated_data)
            for ded_data in deducciones_data:
                Deduccion.objects.update_or_create(prueba=prueba, **ded_data)
            for infer_data in inferencias_data:
                deductAnt = Deduccion.objects.get(afirmacion=infer_data.pop('deduccionVieja'), prueba=prueba)
                deductSig = Deduccion.objects.get(afirmacion=infer_data.pop('deduccionNueva'), prueba=prueba)
                Inferencia.objects.update_or_create(prueba=prueba, deduccionVieja=deductAnt, deduccionNueva=deductSig, **infer_data)
            return prueba
        except IntegrityError as ex:
            error = {'afirmacion': "prueba with this afirmacion already exists."}
            raise serializers.ValidationError(error)