"""
Assignment 1, program calculates the
estimated molecular weight of the protein
by hardcoding the protein
"""

def calc_daltons():
    """code calculates the
estimated molecular weight of the protein
by hardcoding the protein """
    length = "MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC" \
             "CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH" \
             "KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ" \
             "KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ" \
             "EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK" \
             "GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM" \
             "EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE" \
             "NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY" \
             "PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF" \
             "DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV"

    # the length of the protein is defined with the above command

    length = length.replace('\r', '').replace('\n', '')

    # provides the length of the protein

    lop = len(length)

    # assigns a variable to the protein length

    print("The lenght of 'Protein kinase C beta type' is: ", lop)

    # prints out the protein length

    average_mw = 110

    # assigns the average molecular weight per amino acid to a variable

    total_mw = lop * average_mw

    # math operation used to calculate the
    # total average weight of the protein seqeunce.

    total_mw_kd = total_mw / 1000

    # converts from dalton to kilo dalton

    print("The average weight of this protein sequence in kilodaltons is:", total_mw_kd)

    # prints out the average weight of the protein sequence

calc_daltons()
