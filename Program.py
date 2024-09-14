import Person
# from Calculation import bmiCalculator
import Calculation
class Program:

    # BMI calcation for p1
    bmi1 = Calculation.bmiCalculator(Person.p1.weight, Person.p1.length)
    print("Calculating Bmi for " + Person.p1.name + " her/his bmi is ") 
    print(bmi1)
