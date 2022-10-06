from sequence_functions import *
import argparse

database = pd.read_csv('./TF_DB_clean_pathway.csv')

parser = argparse.ArgumentParser(description='BLAST align input protein sequence to find similar TF in the database.')
parser.add_argument('sequence', type=str,
                    help='Your input protein sequence. Please paste the protein string within quotation marks.')

args = parser.parse_args()

output = db_blast(args.sequence, database)
print(output)

output.to_csv('sequence_dataframe.csv')
print("The **sequence_dataframe.csv** file has been created containing all the output information.")