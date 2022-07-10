
# --------------- Función agregar --------------

def agregar(codi, nombr, prec, inve):   
   for key, value in dicTienda.items():            # Recorrer el diccionario con los productos
      if codi == key:                                 # Encuentra el producto en la lista
         return True            
   
   if not existeProducto:                          # El producto que intenta agregar no existe en la tienda, puede agregarlo (Lo niega porque 'existeProducto' tiene por defecto el valor False)
      dicTienda.update({codi:[nombr, prec, inve]})




# --------------- Función actualizar --------------

def actualizar(codi, nombr, prec, inve):
   existeProducto = False                          # Reinicia la bandera, como si no existiera el producto en la tienda
   for key, value in dicTienda.items():            # Recorrer el diccionario con los productos
      if codi == key:                                 # Si existe el producto que intenta actualizar, actualiza, sale del cilco, no busca más
         dicTienda.update({codi:[nombr, prec, inve]})
         return True
      
   if not existeProducto:                              # Si no encuentro el producto a actualizar
      return False

   



# --------------- Función borrar --------------

def borrar(codi, nombr, prec, inve):
   existeProducto = False                       # Reinicia la bandera, como si no existiera el producto
   for key, value in dicTienda.items():
      if codi == key and value[0] == nombr and value[1] == prec and value[2] == inve:     # Todos los valores deben coincidir
         dicTienda.pop(codi)
         return True                            # Debe retornar 'True' para que pueda imprimir la lista con los resultados

   if not existeProducto:
      return False



# ============== Inicio de ejecución ==============

# ----- Definición de variables -----

inventarioTotal = 0                               # Variable que guardara el inventario total
nombreMayor = ''                             # Variable que guardará el nombre del producto con mayor precio
nombreMenor = ''                             # Variable que guardará el nombre del producto con menor precio
acumuladoPrecios = 0                         # Variable que guardará la suma los precios de todos los productos
existeProducto = False                       # Bandera para saber si un producto existe en la tienda

lisResultado = []                            # Lista para guardar los datos que serán impresos al final

dicNombrePrecio = {}                         # Diccionario que guardará los nombres y precios
dicTienda = {                                # Diccionario con los productos iniciales
   1 : ['Manzanas', 5000.0, 25],
   2 : ['Limones', 2300.0, 15],
   3 : ['Peras', 2700.0, 33],
   4 : ['Arandanos', 9300.0, 5],
   5 : ['Tomates', 2100.0, 42],
   6 : ['Fresas', 4100.0, 3],
   7 : ['Helado', 4500.0, 41],
   8 : ['Galletas', 500.0, 8],
   9 : ['Chocolates', 3500.0, 80],
  10 : ['Jamon', 15000.0, 10]
}


# ----- Ingreso de datos -----

operacion = input()                                                     # Ingresa operación a realizar
operacion = operacion.upper()                                           # Operación a realizar se pasa a mayusculas

codigo, nombre, precio, inventario = input().split()                    # Ingresa producto sobre el cual se operará

codigo = int(codigo)                                                    # Conversión de tipos
precio = float(precio)
inventario = float(inventario)



# ----- Llamado a las funciones segun operacion ingresada -----

if operacion == 'ACTUALIZAR':
   existeProducto = actualizar(codigo, nombre, precio, inventario)      # Si el producto no existe, retorna 'False'
elif operacion == 'BORRAR':
   existeProducto = borrar(codigo, nombre, precio, inventario)
elif operacion == 'AGREGAR':
   existeProducto = agregar(codigo, nombre, precio, inventario)         # Si el producto existe en la tienda, retorna 'True'


# ----- Procesos -----

for llave, valor in dicTienda.items():                     # Recorrer el diccionario inicial
   dicNombrePrecio[valor[0]] = valor[1]                     # Crear un diccionario con solo nombres y precios
   inventarioTotal += valor[1] * valor[2]                        # Genera el valor del inventario
   # print(f'{llave} : {valor}')

# print('\n')
# for a in dicNombrePrecio:                                # Recorrer el nuevo diccionario de nombres y precios
#    print(a, dicNombrePrecio[a])  

precioMayor = max(dicNombrePrecio.values())                 # Sacamos el precio mayor usando el nuevo diccionario de nombre y precios
precioMenor = min(dicNombrePrecio.values())                 # Sacamos el precio menor usando el mismo diccionario

encontroMayor = False
encontroMenor = False

for key, value in dicNombrePrecio.items():               # Recorrer el nuevo diccionario de nombres y precios
   acumuladoPrecios += value                                # Genera el acumulado de precios de todos los productos
   if value == precioMayor and not encontroMayor:                                 # Encuentra el precio mayor para guardar el nombre
      nombreMayor = key
      encontroMayor = True                                  # Guarda el primer numero si existe mas de uno que sean los mayores
   elif value == precioMenor and not encontroMenor:                               # Encuentra el precio menor para guardar el nombre
      nombreMenor = key
      encontroMenor = True                                  # Guarda el primer numero si existe mas de uno que sean los menores

promedioPrecios = acumuladoPrecios / len(dicNombrePrecio)

# print(f'\nProducto precio mayor: {nombreMayor}')
# print(f'Producto precio menor: {nombreMenor}')
# print(f'Promedio de precios: {promedioPrecios}')
# print(f'Valor del inventario: {inventario}')

lisResultado.append(nombreMayor)
lisResultado.append(nombreMenor)
lisResultado.append(round(promedioPrecios, 1))              # Redondear a un decimal
lisResultado.append(round(inventarioTotal, 1))

if (existeProducto and operacion == 'AGREGAR') or (not existeProducto and (operacion == 'ACTUALIZAR' or operacion == 'BORRAR')):      # Intentó ingresar un producto ya existente ó intento borar o actualizar un producto que no existe en la tienda (Se niega 'existeProducto' porque las funciones 'ACTUALIZAR y BORRAR' retornan 'False' y un 'if' solo pasa si al final la condición es 'True')
   print('ERROR')
else:                                                       # La operación se realizó con exito, entonces imprime los resultados
   # print('Nuevo inventario\n')
   # for key, value in dicTienda.items():
   #    print(f'{key}:{value}')
   for k in lisResultado:
      print(k, end=' ')