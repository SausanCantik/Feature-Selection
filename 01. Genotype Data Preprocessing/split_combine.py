'''
A function to identify the sample plate code from the accession code
design by.https://github.com/SausanCantik
'''

def split_combine (genotype_data) :
    #genotype_data = genotype_data.drop(labels=400, axis=0)
    label_genotype = list(genotype_data)
    sample_id = genotype_data[label_genotype[0]]
    ID = {}
    for sample in sample_id :
        name_split = sample.split('-', 5)
        sample = name_split[0] + '-' + name_split[1] + '-' + name_split[2] + '-' + name_split[3] + '-' + name_split[4]
        ID[name_split[5]] = sample 
        
    return ID
