
"""
Assignment 1, program asks the user for a gene name hen asks the user for the number of nucleotides
in its coding sequence. The program then will calculate the number
of amino acids in the resulting protein and
its estimated molecular weight (in kilodaltons)
"""

import sys

# imports system specefic parameters and function

def calc_number_amino_acids():
    """ Section of code where the program will
    calculate the number of amino acids
    and the resulting protein"""
    name = input('Please enter a name for the DNA sequence: ')

    # allows the user to input a name of the sequence

    print ("Your sequence name is:", name)

    # prints out the name of the sequence

    length = input("Please enter the length of the sequence: ")

    # allows the user to put in the length of the sequence

    length = float(length)

    # converts the length to a float value

    if length%3==0:
        # if statement that runs if the length is divisible by 3

        print("The length of the DNA sequence is: ", length)

        # prints the lenght of the DNA sequence if divisible by 3

        length_dc = length / 3

        # divides the length of the sequence by 3 to give the decoded
        # protein

        print("The length of the decoded protein is: ", length_dc)

        # prints the decoded protein

        average_mw = 110

        # assigns the average molecular weight of an amino acid
        # to a variable

        total_mw = length_dc * average_mw

        # math operation used to calculate the
        # total average weight of the protein seqeunce.

        total_mw_kd = total_mw / 1000

        # converts from dalton to kilo dalton

        print("The average weight of the protein sequence is: ", total_mw_kd)

        # prints out the average weight of the protein sequence

    else:
        # if the lenght isnt divisibl by 3, this part of the code executes
        print("\n\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)

        # prints out error statement
        # print to STDERR

        sys.exit(1)

        # give it a non-zero exit value, since zero is considered "successful termination"


calc_number_amino_acids()
