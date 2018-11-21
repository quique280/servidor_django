from django.db import models
# Create your models here.

class Prueba(models.Model): #Grafo/Arbol
    afirmacion = models.CharField(primary_key=True, max_length=255)
    fecha = models.DateTimeField('Fecha de la Prueba', blank=True, null=True)
    def __str__(self): return self.afirmacion 

class Deduccion(models.Model): #Nodos
    class Meta:
        unique_together = (('afirmacion', 'prueba'),)
    afirmacion = models.CharField(max_length=255)
    prueba = models.ForeignKey(Prueba,related_name='deducciones',on_delete=models.CASCADE)
    def __str__(self): return self.afirmacion 

class Inferencia(models.Model): #Arcos
    class Meta:
        unique_together = (('prueba', 'deduccionVieja', 'deduccionNueva'))
    prueba = models.ForeignKey(Prueba,related_name='inferencias',on_delete=models.CASCADE,)
    deduccionVieja = models.ForeignKey(Deduccion,related_name='inferencias_posteriores',on_delete=models.CASCADE)
    deduccionNueva = models.ForeignKey(Deduccion,related_name='inferencias_anteriores',on_delete=models.CASCADE)
    regla = models.CharField(max_length=50)
    reglaPosIzq = models.IntegerField('Posicion izquierda de regla aplicada', blank=True, null=True)
    reglaPosDer = models.IntegerField('Posicion derecha de regla aplicada', blank=True, null=True)

    def __str__(self): return f"{self.regla} ({self.reglaPosIzq}, {self.reglaPosDer}), {self.deduccionNueva_id}"

    