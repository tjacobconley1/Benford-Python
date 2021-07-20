
#=========================================================Benford's Law
#Benford's law, also called the Newcomb–Benford law,
#the law of anomalous numbers, or the first-digit law,
#is an observation about the frequency distribution of
#leading digits in many real-life sets of numerical data.
#=========================================================Formula
#Scientifically, Benford's Law is based on base-10 logarithms
#that show the probability that the leading digit of a number
#will be n can be calculated as:
#                                        log10(1+1/n)
#import numpy n such
import numpy as np
#Variables to hold vector dimension sizes 
#(side thought: 'Angstroms are a measure of size)
Vs = 100
Vs2 = 100
#create a big ass RANDOM array
bigAssArray = np.random.rand(Vs, Vs)
#print that shiz
print("bigAssArray")
print(bigAssArray)
#Perform Benford's law
#variables for loop iterations
i = 0
j = 0
#variables to hold frequency of each possible digit
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
err = 0
for i in range(Vs):
    for j in range(Vs2):
        if 1 > bigAssArray[i][j] >= 0.9: nine = nine + 1
        elif 0.9 > bigAssArray[i][j] >= 0.8: eight = eight + 1
        elif 0.8 > bigAssArray[i][j] >= 0.7: seven = seven + 1
        elif 0.7 > bigAssArray[i][j] >= 0.6: six = six + 1
        elif 0.6 > bigAssArray[i][j] >= 0.5: five = five + 1
        elif 0.5 > bigAssArray[i][j] >= 0.4: four = four + 1
        elif 0.4 > bigAssArray[i][j] >= 0.3: three = three + 1
        elif 0.3 > bigAssArray[i][j] >= 0.2: two = two + 1
        elif 0.2 > bigAssArray[i][j] > 0: one = one + 1
err = (Vs*Vs2) - (one + two + three + four + five + six + seven + eight + nine)
print("1's: " + str(one))
print("2's: " + str(two))
print("3's: " + str(three))
print("4's: " + str(four))
print("5's: " + str(five))
print("6's: " + str(six))
print("7's: " + str(seven))
print("8's: " + str(eight))
print("9's: " + str(nine))
print(str(err))
