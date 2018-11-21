from rest_framework import serializers
from pruebas.models import Prueba
from pruebas.models import Deduccion
from pruebas.models import Inferencia
from rest_framework.serializers import SerializerMethodField


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
    deducciones = DeduccionSerializer(many=True, read_only=True)
    inferencias = InferenciaSerializer(many=True, read_only=True)
    class Meta:
        model = Prueba
        fields = ('afirmacion', 'fecha', 'deducciones', 'inferencias')
    
    def to_internal_value(self, data):
        return super(PruebaSerializer,self).to_internal_value(data)

    def create(self, validated_data):
        inferencias_data = validated_data.pop('inferencias')
        deducciones_data = validated_data.pop('deducciones')
        prueba = Prueba.objects.create(**validated_data)
        for ded_data in deducciones_data:
            Deduccion.objects.update_or_create(prueba=prueba, **ded_data)
        for infer_data in inferencias_data:
            deductAnt = Deduccion.objects.get(afirmacion=infer_data.pop('deduccionVieja'), prueba=prueba)
            deductSig = Deduccion.objects.get(afirmacion=infer_data.pop('deduccionNueva'), prueba=prueba)
            Inferencia.objects.update_or_create(prueba=prueba, deduccionVieja=deductAnt, deduccionNueva=deductSig, **infer_data)
        
        return prueba