from Bio.Blast.Applications import NcbiblastpCommandline
import pandas as pd

def db_blast(query, db):
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

        dataframe = db.merge(blast_df).sort_values(by=['bit_score'], ascending=False).reset_index(drop=True)
        return dataframe
    else:
        print("Please, paste your target protein sequence")

