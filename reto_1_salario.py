'''
PROGRAMA: CÁLCULO DE SALARIO

Un empleado de una compañía tiene dudas sobre si los pagos que le realiza la empresa de manera mensual son correctos. Con el propósito de aclarar sus inquietudes y verificar si los descuentos realizados son acordes a lo exigido por la ley, decide construir un programa en Python que le permita verificar el valor que debería ser pagado. Después de consultar sobre la normatividad colombiana y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:

* El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 192. Este valor corresponde
  a la jornada laboral establecida en el contrato (48 horas a la semana y 4 semanas al mes).

* Las horas extras se liquidan con un recargo del 25% sobre el valor de una hora normal.

* Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones del 5% del salario base.

* El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras,
  más las bonificaciones (si las hay).

* Se descontará 3.5% del salario total antes de descuentos para el plan obligatorio de salud.

* Se descontará 4% del salario total antes de descuentos para el aporte a pensión.

* Se descontará 1% del salario total antes de descuentos para caja de compensación.


ENTRADA:

El programa recibirá 3 parámetros:

* El salario base del empleado
* La cantidad de horas extras se representa a través de un número entero positivo. En caso de no de realizar horas
  extras durante el mes, se ingresará el valor 0.
* Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0

SALIDA:

El programa debe imprimir el valor a pagar al empleado luego de realizar los descuentos de ley. El resultado debe imprimirse con un número decimal


'''

salarioBase, cantidadHorasExtras, bonificaciones = input().split() # Ingreso de datos

# Conversión de 'str' a datos numericos
salarioBase = float(salarioBase)
cantidadHorasExtras = int(cantidadHorasExtras)
bonificaciones = int(bonificaciones)

# Calculos
valorHoraNormal = salarioBase / 192
valorHoraExtra = valorHoraNormal * 1.25
valorBonificacion = salarioBase * 0.05
valorHorasExtras = valorHoraExtra * cantidadHorasExtras
salarioAntesDescuentos = salarioBase + valorHorasExtras

# Con bonificación
if(bonificaciones == 1):
   salarioAntesDescuentos = salarioAntesDescuentos + valorBonificacion

# Descuentos
descuentoSalud = salarioAntesDescuentos * 0.035
descuentoPension = salarioAntesDescuentos * 0.04
descuentoCajaCompensacion = salarioAntesDescuentos * 0.01

# Salario a pagar
salarioTotal = salarioAntesDescuentos - descuentoSalud - descuentoPension - descuentoCajaCompensacion

print(round(salarioTotal, 1))