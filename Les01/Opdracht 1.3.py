a = 6
b = 7
print (a + b)  #Hier worden beide variables met elkaar opgeteld. Boven zijn beide variables aangegeven.
c = ( ( a + b ) / 2)  #Hier geef je aan dat C is als a + b opgeteld worden en gedeeld worden door 2.
print (c)

inventaris = [ 'papier', 'nietjes', 'pennen']  #Hier is de variable inventaris de lijst met enkele strings.
inventaris = tuple (inventaris)  #Hier wordt een lijst een tuple (het wordt geconverteerd, tevens is dit definitief dan)
print(inventaris[2].index('p'))    #Hiermee geef je aan dat de variable inventaris en dan de laatste string op de letter p met geindex worden.
print(inventaris[2])   #Hiermee geef je de laatste string volledig mee weer.

voornaam = 'Weis '
tussenvoegsel = ''
achternaam = 'Mateen '
mijnnaam = (voornaam + tussenvoegsel + achternaam)
print (mijnnaam)   #Met de , wordt de spatie gegeven.