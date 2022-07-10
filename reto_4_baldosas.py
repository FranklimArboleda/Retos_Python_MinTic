
'''
En una fabrica de baldosas de cerámica se producen por día una gran cantidad de este producto.
Es importante hacer control de calidad sobre el producto. Este control consiste en revisar si en un
lote de N baldosas hay baldosas defectuosas (puede variar la textura o el color). La solicitud del
gerente de la planta es que se construya un programa en Python que pueda detectar la cantidad
de baldosas defectuosas en una de las líneas de producción de la fabrica.

Para detectar si una baldosa es diferente a otra, un sensor escanea las baldosas y si hay alguna
diferencia, guarda un registro en la memoria. La memoria del sensor esta limitada por la cantidad
de baldosas que se producen en un intervalo de tiempo determinado

ENTRADA:
   La entrada estará formada por dos líneas:
      -> La primera línea aparecerá dos números N y K que indican el número de baldosas a revisar
         y el número de baldosas que el sensor es capaz de guardar (1≤ N ≤ 1000, 1 ≤ K ≤ 1000)
      -> La segunda línea contiene M números (entre 1 y 100) separados por espacios que
         representan las baldosas revisadas por el sensor
      -> Las baldosas se consideran defectuosas si están representados por el mismo número

SALIDA:
   El programa imprimirá tres números separados por un espacio.
      -> El primero representará el número total de fallas detectadas
      -> El segundo representará la cantidad de fallas detectadas por el sensor considerando
         que al revisar una baldosa solo es capaz de guardar las 𝐾 baldosas anteriores
      -> El tercero representa la cantidad de baldosas revisadas por el sensor
'''

# ----- Función leerDatosPrimeraLinea() -----

def leerDatosPrimeraLinea() :
   n, k = input().split()           # Entrada de datos primer línea
   
   # Conversión de tipos
   n = int(n)                       # Número de baldosas a revisar
   k = int(k)                       # Número de baldosas que guarda el sensor

   return n, k                      # Valores que retorna


# ----- Función leerDatosSegundaLinea() -----

def leerDatosSegundaLinea() :
   listaEnteros = []
   listaCaracteres = list(input().split(' '))      # Ingreso de las n baldosas
   for i in listaCaracteres :
      listaEnteros.append(int(i))                  # Llenar la lista con enteros
   return listaEnteros



# ----- Función leerDatosSegundaLinea() -----

def detectarFallas(baldosas, k):
   fallasTotales = 0
   fallasSensor = 0
   diccionario = {}

   for i in baldosas :
      diccionario.update({i:baldosas.count(i)})    # Llenar el diccionario con los números y repeticiones

   for clave, valor in diccionario.items() :       # Recorrer el diccionario para contar las fallas totales
      if valor > 1 :                               # Se repite como mínimo una vez
         fallasTotales += valor - 1                # Se resta '1',  no debe tener en cuenta el que usa para comparar
   
   for a in range(len(baldosas)) :
      if a == 0 :                                  # No compara el primer valor, no tiene con quien
         continue

      existe = False                               # Bandera, se reinicia a 'False' en cada cambio de busqueda

      for b in range(len(baldosas)) :              # Recorrer doblemente la lista de baldosas
         if baldosas[a] == baldosas[b] and b < a and a - b <= k :    # (b < a) compara hasta antes del mismo elemento y (a - b <= k) representa máximo 'k' elementos previos para comparar
            existe = True                          
         
      if existe :
         fallasSensor += 1                         # Solo suma al salir del ciclo anidado porque cuando se ingresa el mismo número varias veces, dentro del ciclo sumaria muchas repeticiones
   
   return fallasTotales, fallasSensor



# ---------- Inicio del programa ----------

n, k = leerDatosPrimeraLinea()      # Llamado a la función que leerá los datos de la primera línea

baldosas = leerDatosSegundaLinea()  # Llamado a la función que leerá los datos de la segunda línea

fallasTotales, fallasSensor = detectarFallas(baldosas, k)

print(fallasTotales, fallasSensor, n)