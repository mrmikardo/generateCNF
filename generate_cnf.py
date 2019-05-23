#!/usr/bin/env python3

import sys

from random import randrange, choice

num_clauses = 100    # default

def gen_clauses(num_vars, num_clauses=100, file_or_stdout="file"):
    
    # TODO use a generator!!

    variables = [v for v in range(0, int(num_vars))]
    variables += [-v for v in range(0, int(num_vars))]
    print(variables)    # debug

    f = "output.cnf"
    with open(f, 'w') as ofile:
        ofile.write("c output.cnf\n")
        ofile.write("c\n")
        for i in range(0, int(num_clauses)):
            cl = gen_clause(variables)
            ofile.write(str(i) + " ")
            for j in range(0, len(cl)):
                ofile.write(str(cl[j]) + " ")
            ofile.write("\n")
    ofile.close()

def gen_clause(variables):
    '''
    Max length of a clause capped at 5 vars

    TODO: this should be an optional parameter
    TODO: negative as well as positive literals!
    '''
    clause_length = randrange(1, 5+1)
    clause = []
    for i in range(0, clause_length):
        clause.append(choice(variables))
    return clause

def main():
    if len(sys.argv) < 2:
        print("Usage: ./generateCNF <number of variables> <OPTIONAL: number of clauses> <OPTIONAL: out file>")
        sys.exit(1)

    # TODO probably use argparse or similar here

    params = sys.argv[1:]
    if len(params) == 3:
        gen_clauses(params[0], params[1], params[2])
    elif len(params) == 2:
        gen_clauses(params[0], params[1])
    else:
        gen_clauses(params[0])

if __name__ == '__main__': main()
