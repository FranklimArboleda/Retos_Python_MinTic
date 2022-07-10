''' PROGRAMA SOBRE MULTAS '''

distanciaMetros, velocidadPermitidaKm, tiempoTardaConductorSeg = input().split()

distanciaMetros = float(distanciaMetros)
velocidadPermitidaKm = float(velocidadPermitidaKm)
tiempoTardaConductorSeg = int(tiempoTardaConductorSeg)

tiempoEnHoras = tiempoTardaConductorSeg / 3600
velocidadRealConductor = (distanciaMetros / 1000) / tiempoEnHoras

if (distanciaMetros < 0 or velocidadPermitidaKm < 0 or tiempoTardaConductorSeg < 0) :
   print('ERROR')
else :
   if velocidadRealConductor <= velocidadPermitidaKm :
      print('OK')
   else :
      if(velocidadRealConductor > velocidadPermitidaKm and velocidadRealConductor < velocidadPermitidaKm * 1.2) :
         print('MULTA')
      elif velocidadRealConductor >= velocidadPermitidaKm * 1.2 :
         print('CURSO SENSIBILIZACION')