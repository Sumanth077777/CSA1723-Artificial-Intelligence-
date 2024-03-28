class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for constraint in self.constraints.get(variable, []):
            if constraint[0] in assignment and not constraint[1](value, assignment[constraint[0]]):
                return False
        return True

    def backtrack_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        var = next(v for v in self.variables if v not in assignment)
        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack_search(assignment)
                if result is not None:
                    return result
                assignment.pop(var)
        return None

def not_equal(value1, value2):
    return value1 != value2

def main():
    # Input variables and domains
    variables = input("Enter variables (separated by spaces): ").split()
    domains = {}
    for var in variables:
        domain = input(f"Enter domain for {var} (separated by spaces): ").split()
        domains[var] = domain

    # Input constraints
    constraints = {}
    print("Enter constraints (variable1, variable2, constraint_type):")
    print("Constraint types: '!=', '==', '>', '<'")
    print("Enter 'done' when finished.")
    while True:
        constraint_input = input("Enter constraint: ")
        if constraint_input.lower() == 'done':
            break
        var1, var2, constraint_type = constraint_input.split()
        if var1 not in constraints:
            constraints[var1] = []
        constraints[var1].append((var2, eval(constraint_type)))

    # Create CSP instance
    map_coloring_csp = MapColoringCSP(variables, domains, constraints)

    # Solve CSP
    solution = map_coloring_csp.backtrack_search()

    if solution is not None:
        print("Solution found:")
        for var, value in solution.items():
            print(f"{var}: {value}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
