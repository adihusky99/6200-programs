"""

File   :  protocol.py
History:  7-Sep-2019, 7-Feb-2021 (updated to use f-strings)

Instruct user how to prepare a 3 ml solution of
10 mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.
"""


def main():
    """Business logic"""

    final_vol = input("Please enter the final volume of the solution (ml): ")

    # allows the user to input the final volume of the solution
    # uses ml volumes throughout the program

    final_vol = float(final_vol)

    # converts to a float number
    # NacL

    nacl_stock = input("Please enter the NaCl stock (mM): ")

    # allows the user to input the NaCL stock
    # use mM concentrations throughout the program

    nacl_stock = float(nacl_stock)

    # converts to a float number
    # use mM concentrations throughout the program

    nacl_final = input("Please enter the NaCl final (mM): ")

    # allows the user to input the final volume of NaCl
    # use mM concentrations throughout the program

    nacl_final = float(nacl_final)

    # converts to a float number
    # concatenation, notice how we are calculating something here!

    step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n"

    # Math operation to determine the amount of NaCl required

    # MgCl2

    mg_stock = input("Please enter the MgCl stock (mM): ")

    # Allows the user to input the MgCl stock
    # use mM concentrations throughout the program

    mg_stock = float(mg_stock)

    # converts to a float number
    # use mM concentrations throughout the program

    mg_final = input("Please enter the MgCl final (mM): ")

    # Allows the user to input the final volume of MgCl
    # use mM concentrations throughout the program

    mg_final = float(mg_final)

    # converts to a float number
    # concatenation, notice how we are calculating something here!

    step2 = f"Add {float(final_vol * (mg_final / mg_stock))} ml MgCl2\n"

    # Math operation to determine the amount of MgCl required

    # Water

    step3 = f"Add water to a final volume of {float(final_vol)} ml and mix"

    # print statement asking user to add water to the final volume
    # Protocol, we can then just print things out b/c they have been formatted earlier`

    print(step1 + step2 + step3)

    # prints out step 1, 2 and 3

if __name__ == '__main__':
    main()

