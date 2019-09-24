'''
A function to identify the accession code of sample from genotype data
design by.https://github.com/SausanCantik
'''

def sample_in_genotpe (genotype_dataframe) :
    sample_genotype = []
    for sample in genotype_dataframe['Samples']:
        name_split = sample.split('-', 5)
        sample_accession = name_split [5]
        sample_genotype.append(sample_accession)
        
    sample_genotype.sort()
    return sample_genotype
