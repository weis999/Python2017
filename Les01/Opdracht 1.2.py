s = 'Supercalifragilisticexpialidocious'
print (len(s))           #Hierbij wordt len gebruikt om de lengte van variable s te weergeven hoeveel letters deze heeft

print ('ice' in s )
#Hiermee wil je kijken of er ice in de variable s zit. En de operator in gebruik je daarvoor.

a = 'Antidisestablishmentarianism'
b = 'Honorificabilitudinitatibus'
print ('a' > 'b') #Wordt aangegeven of het variable a langer is dan variable b.

print ( min (['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']) )  #Alfabetisch oplopend
print ( max (['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']) ) #Alfabetisch aflopend

eerste = min('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
laatste = max('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
print ( eerste, laatste )  #De variable eerste en laatste woorden weergegeven. Want in beide variable's zijn de max en min al verwerkt.
