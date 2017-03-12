import sys
import csv
import numpy as np

Dlm = '\t'          # Delimiter of CSV file
Prefix = "t_"       # Prefix for output files




def main():
    argv = sys.argv
    argc = len(argv)

    # Usage...
    if (argc != 2):
        print("    Usage: # python csvTranspose.py <original CSV file>")
        print()
        quit()

    #CSVTranspose("z001.txt")        #DEBUG
    CSVTranspose(argv[1])




def CSVTranspose(fnameIn):
    fnameOut = Prefix + fnameIn

    # Read input data
    reader = csv.reader(open(fnameIn, "r"), delimiter=Dlm)
    x = list(reader)

    # Transpose
    xT = np.transpose((x))

    # Write output data
    with open(fnameOut, 'w') as f:
        writer = csv.writer(f, delimiter=Dlm, lineterminator='\n')
        writer.writerows(xT)





if __name__ == "__main__":
    main()
