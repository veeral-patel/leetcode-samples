import re


class Input:
    # Models an input string
    def __init__(self, variable, equation, raw):
        self.variable = variable
        self.equation = equation
        self.raw = raw
    
class Evaluator:
    def __init__(self, inputs):
        self.inputs = inputs
        self.values = {} # variable name => value mapping
        self.dependents = {} # variable names => dependent formulas mapping

    def evaluate_one(self, input, evalDependencies=True):
        # populate Python variables for each variable in values
        for variable, value in self.values.items():
            exec('{}={}'.format(variable, value))
        
        # execute the input's equation
        result = eval(input.equation)

        # and store the value for the variable in our hashmap
        self.values[input.variable] = result

        # re-evaluate dependencies
        if evalDependencies:
            self.evaluate_dependencies(input)

        print(result)
        return result
    
    def evaluate_dependencies(self, input):
        # compute and store the dependencies for this input
        dependencies = get_dependencies(input)
        for dependency in dependencies:
            if dependency in self.dependents:
                self.dependents[dependency].append(input)
            else:
                self.dependents[dependency] = [input]
        
        # if this is a assignment, re-compute the dependents of this variable
        if self.is_assignment(input):
            if input.variable in self.dependents:
                deps = self.dependents[input.variable]
                for dep in deps:
                    self.evaluate_one(dep, evalDependencies=False)
    
    def evaluate_all(self):
        for input in self.inputs:
            result = self.evaluate_one(input)
    
    def is_assignment(self, input):
        # Returns true if input is of this form: a = 100
        pattern = re.compile("\w+ = \d+")
        return bool(pattern.match(input.raw))

def get_dependencies(input):
    pieces = input.equation.split()
    equation_pieces = pieces[2:] # If input is "c = b + a + 3", ignore "c ="
    dependencies = [var for var in equation_pieces if var.isalpha()]
    return list(set(dependencies))

if __name__ == "__main__":
    inputStrings = ["a = 100", "b = 5", "c = a + b", "d = b + b + 1", "b = 25", "d = 51", "c = 70"]

    inputs = []
    for inputString in inputStrings:
        # split each input string into the variable name and equation parts
        pieces = [piece.strip() for piece in inputString.split("=")]
        if len(pieces) == 2:
            inputs.append(Input(pieces[0], pieces[1], inputString))

    ev = Evaluator(inputs)
    ev.evaluate_all()