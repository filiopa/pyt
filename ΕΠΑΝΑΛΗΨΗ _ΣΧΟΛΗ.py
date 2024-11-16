# Decimals!
yo = str(float(input('give me input number (if decimal, use dot instead of comma): ')))
print(yo + ' is an amazing decimal number indeed.')

# 1st letter 'UPPERCASE', rest 'lowercase'
kati = input('Write something: ')
kati = kati[0].upper() + kati[1:].lower()
print(kati)


# ΕΠΑΝΑΛΗΨΗ PYTHON ΑΠΟ ΣΧΟΛΗ!

# display the data type of x:
x = str("Hello World")
print(x)
print(type(x))

# Τελεστές
x = int(input('Διάλεξε τιμή για x: '))
y = int(input('Διάλεξε τιμή για y: '))
print('x=' + str(x) + ', y=' + str(y))
# output x+y = 
print("x+y=", x+y) 
# output x-y = 
print("x-y=", x-y)
# output x*y = 
print("x*y=", x*y)
# output x/y = 
print("x/y=", x/y)
# output x//y = 
print("x//y=", x//y) # αυτό είναι η ακέραια διαίρεση x δια y (χωρίς υπόλοιπο)
# output x//y = 
print("x**y=", x**y) # x εις την y
# output x%y = 
print("x%y=", x%y) # αυτό είναι το υπόλοιπο της διαίρεσης x δια y

# Booleans
print(10<9)
print(10>9)
print(10==9)

# Compare values!
x = int(input("x = "))
while x < 0:
    print(f"{x} is not an accepted value! Insert a positive number: ")
    x = int(input("x = "))
if x<10:
     print(f"{x} is below 10 :(")
if x>10:
  print(f"{x} is above 10")
if x>20:
    print(f"{x} is also above 20!")
elif 10<x<20:
  print(f"but {x} is not above 20!")

# Εκπτώσεις!!!
Αγορά = int(input("Ποσό αγοράς (σε €) = "))
if Αγορά < 100:
  έκπτωση = Αγορά * 0.05
  print(f"Έκπτωση 5 %, άρα {έκπτωση:.2f} € λιγότερα!")
elif Αγορά < 500:
  έκπτωση = Αγορά * 0.10
  print(f"Έκπτωση {έκπτωση:.2f} €")
else:
  έκπτωση = Αγορά * 0.15
  print(f"Έκπτωση 15 %, άρα {έκπτωση:.2f} € λιγότερα!")
print("Τελικό ποσό = ", Αγορά - έκπτωση)