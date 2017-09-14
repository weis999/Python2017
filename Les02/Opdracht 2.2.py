icor = input (  'Mijn cijfer voor ICOR:' )
prog = input ( 'Mijn cijfer voor PROG:' )
cns = input (  'Mijn cijfer voor CSN:' )
gemiddelde = ( str (float (icor) + (float (prog) + (float (cns) // 3) ) ) )
print( gemiddelde)
print ( 'Mijn cijfers voor icor, prog en cns gemiddeld:', gemiddelde, 'de beloning dan wordt: €' + (str ( float (gemiddelde) * 30) ))

#Hier heb ik voornamelijk de class input, str, float.