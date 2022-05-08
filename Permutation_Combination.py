
# Importing a function from another pyhton file/module/program
# import Factorial

from Factorial import fact

# Syntax
# import <file_name>
# or from <file_name> import <function>

n = int(input("Enter n : "))
r = int(input("Enter r : "))

#permutation = Factorial.fact(n) / Factorial.fact(n - r)

permutation = fact(n) / fact(n - r)
combination = fact(n) / (fact(n - r) * fact(r))

print("Permutation :" , permutation)
print("Combination :" , combination)
