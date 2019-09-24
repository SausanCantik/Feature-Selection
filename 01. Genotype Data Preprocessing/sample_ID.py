'''
A function to list sample from genotype data given the accession code
design by.https://github.com/SausanCantik
'''

def sample_ID(genotype_dataframe) :
    to_remove = []
    ID = split_combine(genotype_dataframe)
    sample_to_remove = 'Ca09-6', 'Ca27-7', 'Ca32-6', 'Ca35-6', 'Ca36-6', 'Ca39-1', 'Ca45-7', 'Ca55-7', 'Ca58-7'
    for sample in sample_to_remove :
        hapus = ID[sample] + '-' + sample
        to_remove.append(hapus)
        
    return to_remove
