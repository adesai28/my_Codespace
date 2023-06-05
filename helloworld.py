print ("Hello World!") # normal string
print (1+2)  # basic calculation add 2 in 1
print (9-5)  # basic calculation subsract 5 from 9
# Below is the rule for performing complex calculation PEMDAS
'''
 P Parentheses first  
 E Exponents (ie Powers and Square Roots, etc.)
 M D Multiplication and Division (left-to-right)
 AS Addition and Subtraction (left-to-right)

 Addition	+	1 + 2 = 3
 Subtraction	-	5 - 4 = 1
 Multiplication	*	2 * 4 = 8
 Division	/	6 / 3 = 2
 Exponent	**	3 ** 2 = 9
 '''

print( ( (1 + 3) * (9 - 2) / 2 ) ** 2)  # => ((28/2)**2) => 14**2 => 14*14 =>> 196

test_var = 4 + 5  # variable assignment
''' They can't have spaces (e.g., test var is not allowed)
        They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
        They have to start with a letter or underscore (e.g., 1_var is not allowed) '''

print ("test_var") # prints the string as is
print (test_var)  # now prints the value in the variable which is of type int!
print (type(test_var))
my_var=test_var+28
print(my_var)

#Seconds calculation
num_years=1
days_per_year=365
hours_per_day=24
mins_per_hour=60
secs_per_min=60
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
print(type(total_secs))
days_per_year=365.25
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print("In leap year total seconds would be:",total_secs)
print(type(total_secs))