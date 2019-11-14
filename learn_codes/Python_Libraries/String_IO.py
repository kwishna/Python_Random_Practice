from io import StringIO

s = StringIO('My Name Is Anthony Gonsalves. I Am Alone In This World.')  # Creates A Kind Of File
print('Reading The S :: ',s.read())

s.write(" Hmmmmmmmmmm")

s.seek(0)

print('Reading After Adding Hmmmmmmmm ::', s.read())

##################################################
print('30**30 % 11 :: ', pow(30, 30, 11))
print('Round Up To 3 Decimal Positions :: ', round(3.95793487592375, 3))

##################################################
