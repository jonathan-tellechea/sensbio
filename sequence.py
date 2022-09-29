from Bio.Blast.Applications import NcbiblastpCommandline
import pandas as pd
import argparse
    
def db_blast(query):
    validate = False
    if query:
        try:
            blastp_cline = NcbiblastpCommandline(db="BLASTdb", outfmt="6 sseqid pident evalue bitscore")
            out, err = blastp_cline(stdin=query)
            validate = True
        except:
            print("Wrong sequence format!", query)
            validate = False

    if query and validate:
        results = [i.split('\t') for i in out.splitlines()]
        for i in results:
            if '|' in i[0]:
                i[0] = i[0].split('|')[1]

        blast_df = pd.DataFrame(data=results, columns=['NCBI_Accession', 'id_pc','e_value','bit_score'])

        blast_df['bit_score'] = pd.to_numeric(blast_df['bit_score'])

        dataframe = database.merge(blast_df).sort_values(by=['bit_score'], ascending=False).reset_index(drop=True)
        return dataframe
    else:
        print("Please, paste your target protein sequence")

database = pd.read_csv('./TF_DB_clean_pathway.csv')

parser = argparse.ArgumentParser(description='BLAST align input protein sequence to find similar TF in the database.')
parser.add_argument('sequence', type=str,
                    help='Your input protein sequence. Please paste the protein string within quotation marks.')

args = parser.parse_args()

output = db_blast(args.sequence)
print(output)

output.to_csv('sequence_dataframe.csv')
print("The **sequence_dataframe.csv** file has been created containing all the output information.")