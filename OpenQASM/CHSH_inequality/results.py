
'''
    this is file that takes the results of the CHSH inequality test and makes a conclusion about the universe

    it requires that all {basis_combination}.qasm files are run and their results stored in data/

    the data was collected by running the .qasm scripts on quantum computers via IBM quantum platform

    simulation.ipynb is better because the code is written in quisket and all the results are contained within a notebook
'''


# remove all instances of token from str
def filter(str, token):
    new_str = ""
    for c in str:
        if c != token:
            new_str += c
    return new_str

# read contents from the result csv file
def readFile(filename):
    path = f"data/{filename}.csv"
    with open(path, "r") as f:
        lines = f.readlines()
    rows = []

    # parse lines, skip header
    for line in lines[1:]: 
        # split line by commas and remove special characters
        row = [val.rstrip() for val in line.split(",")]

        # remove " char from the strings
        row = [filter(val, "\"") for val in row]
        
        # convert the frequency row[1] into ints
        frequency = int(row[1])
        row[1] = frequency
        rows.append(row)
    return rows


if __name__ == '__main__':
    basis_states = ["AB", "AB'", "A'B", "A'B'"]

    results = []
    for basis in basis_states:
        result = readFile(basis)
        results.append(result)

    # convert this frequency table into a probability table
    probs = []
    for row in results:
        # item[1] is the frequency associated with the final state (00,01,10,11)
        total = sum([item[1] for item in row])
        row = [[item[0], item[1]/total] for item in row]
        probs.append(row)


    # calculate the expectation values (or expected values since we're physicists ;D ) 
    '''
        for our values associated with each probability:
            if we measure |0>, we multiply by +1 
            if we measure |1>, we multiply by -1
        so 
            |00> -> 1 * 1 = 1
            |01> -> 1 * -1 = -1
            |10> -> -1 * 1 = -1
            |11> -> -1 * -1 = 1
        then 
            E(A,B) = (1)*P_00 + (-1)*P_01 + (-1)*P_10 + (1)*P_11
    '''

    # we will create a dictionary to hold results
    exp_vals = {}

    for index, basis_state in enumerate(basis_states):
        # get index of basis state -> corresponds to row in probs to take results from
        data = probs[index]

        exp_val = data[0][1] - data[1][1] - data[2][1] + data[3][1]
        exp_vals[basis_state] = exp_val

        print(f"E({basis_state}) = {exp_val}")

    # find the quantum correlation value
    S = exp_vals["AB"] + exp_vals["AB'"] + exp_vals["A'B"] - exp_vals["A'B'"]
    print(f"\nS = {S}")

    if S > 2:
        print("\nS > 2")
        print("we disproved Einstein!")
        print("nature is not described by a local hidden variable theory")
        print("quantum mechanics is right")
    else:
        print("\nEinstein war richtig...")



