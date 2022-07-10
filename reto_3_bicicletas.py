N = int(input())     # Data input

database = []        # Declaration of variables
cumplen = []
parametros = [240, 300, 160, 180, 240, 275, 50]    # Comparison parameters

database = [N]       # Data asignment to list, First place for number of iterations

for i in range(N) :
   ejePedalier, bielas, sillin, manilar, precio = input().split()    # Data input

   ejePedalier = int(ejePedalier)      # Datatype convertion
   bielas = int(bielas)
   sillin = int(sillin)
   manilar = int(manilar)
   precio = int(precio)

   database.append((ejePedalier, bielas, sillin, manilar, precio))   # Data asignment to list

for i in range(database[0]) :
   if (database[i+1][0] >= parametros[0] and database[i+1][0] <= parametros[1]) and \
      (database[i+1][1] >= parametros[2] and database[i+1][1] <= parametros[3]) and \
      (database[i+1][2] >= parametros[4] and database[i+1][2] <= parametros[5]) and \
      (database[i+1][3] <= parametros[6]) :
      cumplen.append(database[i+1][4])

if not cumplen :
   print('NO DISPONIBLE')
else :
   for i in cumplen :
      print(i, end=' ')