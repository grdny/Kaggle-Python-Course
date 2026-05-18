

#Loops: Loops are a way to repeatedly execute some code. 


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:  # metin şeklinde gezegenleri yazdırır.
    print(planet, end=' ')  #end='' alt satıa geçme, bir boşluk bırak

print(planets)  #liste şeklinde gezegenleri yazdırır.



multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)




s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''

for char in s:
    if char.isupper():
        print(char, end=' ')




#range(): A function that returns a sequence of numbers.

for i in range(5):
    print("Doing important work. i =",i)



#while:  Which iterates until some condition is met.

i = 0
while i < 10:
    print(i, end=' ')
    i += 1



#List comprehensions

squares = [n**2 for n in range(10)]
print(squares)

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)


short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)


#str.upper()

loud_short_planets = [planet.upper() + '!' for planet in planets if len (planet) < 6]
print(loud_short_planets)

loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]
print(loud_short_planets)



k = [15 for planet in planets]
print(k)


#Verilen listedeki negatif sayıların sayısını veren kod.

x = [5, -1, -2, 0, 3]

def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

print(count_negatives(x))


def count_negatives(nums):
    return len([num for num in nums if num < 0])

print(count_negatives(x))


def count_negatives(nums):
    return sum([num < 0 for num in nums])

print(count_negatives(x))
