# [“a = 100”, “b = 5”, “c = a + b”, “d = b + b + 1”, “b = 25”, “d = 51”, “c = 70”]

def evaluator(inputs):
    dependencies = {}
    formulas = {}

    for input in inputs:
        deps = get_dependencies(input)
        variable_name = get_variable_name(input)
        if variable_name in dependencies:
            dependencies[variable_name].extend(deps)
        else:
            dependencies[variable_name] = deps
    
    print(dependencies)

def get_dependencies(input):
    pieces = input.split()
    equation_pieces = pieces[2:]
    dependencies = [var for var in equation_pieces if var.isalpha()]
    return list(set(dependencies))

def get_variable_name(input):
    pieces = input.split()
    return pieces[0]