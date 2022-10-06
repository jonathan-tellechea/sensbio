import argparse
from molecular_functions import *


parser = argparse.ArgumentParser(description='Find similar molecules to the input string. This can be used to find TF that may be triggered by your input molecule.')
parser.add_argument('molecule', type=str,
                    help='Your input molecule in SMILES format. Please paste the SMILES string within quotation marks.')

args = parser.parse_args()

if args.molecule != "" and chem_validator(args.molecule)==True:
    dataframe = tanimoto_ranker(args.molecule)
    print(dataframe)
    dataframe.to_csv('molecule_dataframe.csv')
    print("The **molecule_dataframe.csv** file has been created containing all the output information.")
else:
    raise Exception(f"The string \"{args.molecule}\" is not a valid SMILES. Please enter a valid input molecule.")