# This program explores lambda functions in the context of a Constraint-Satisfaction problem
from constraint import *

problem = Problem()

variables = [1, 2, 3, 4]
domains = ['Monday', 'Tuesday', 'Wednesday']
temp = 16

problem.addVariables(variables, domains)

problem.addConstraint(lambda x: x != domains[2], [variables[0]])

print(problem.getSolution())


