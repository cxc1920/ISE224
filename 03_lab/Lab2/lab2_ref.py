print('==========Q1==========')

print('Apple')
print('MacOS')

print('==========Q2==========')

brand = input("What is your laptop brand: ")
system = input("What is your operation system: ")

print(brand)
print(system)


print('==========Q3==========')

brand = input("What is your laptop brand: ")
system = input("What is your operation system: ")

print('My laptop brand is '+brand+', and its system is '+system+'.')

print('==========Q4==========')

WorkingHour = float(input('What is your working hour: '))
PayRate = float(input('What is your pay rate: '))

total = WorkingHour*PayRate

print('The total salary is '+str(total))

print('==========Q5==========')
NumFemale = int(input('How many females: '))
NumMale = int(input('How many males: '))

PropFemale = NumFemale/(NumFemale+NumMale)
PropMale = 1-PropFemale

print('The percentage of female is '+str(PropFemale)+', and the percentage of male is '+str(PropMale)+'.')
