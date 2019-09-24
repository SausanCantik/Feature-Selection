'''
A function to remove sample. This function is to make sure the samples in both genotype and phenotype data are the same.
design by.https://github.com/SausanCantik
'''
def remove_samples(sample_to_remove) :
    length = len(sample_to_remove)
    for i in range(length) :
        sample = sample_to_remove[i]
        if sample in sample_genotype :
            #confirming the sample is in the list
            print('Before : is {} in the list ?    ' .format(sample), sample in sample_genotype) #shoud be true
        
            #removing the sample
            sample_genotype.remove(sample)
        
            #confirming the sample is removed
            print('After : is {} in the list ?    ' .format(sample), sample in sample_genotype, '\n') #should be false
        else :
            print('{} is no longer in the list' .format(sample))
        
    #confirming the Samples are now equal
    df = pd.DataFrame()
    df['Genotype'] = sample_genotype
    df['Phenotype'] = sample_phenotype
    print('Any NaN value anymore? ', df.isnull().any().any())
    
    return df
