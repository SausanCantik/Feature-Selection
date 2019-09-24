'''
A function to treat missing genotype
design by.https://github.com/SausanCantik
'''

def missing_treatment(genotype_dataframe) :
    
    #defining the genotype
    base = ['N']
    
    #listing all features
    features = list(genotype_dataframe)
    
    #missing treatment looping process
    for feature in features :
        
        #identify missing genotype
        genotype = genotype_dataframe[feature].unique()
        
        if base in genotype :
            #calculating missing genotype in a feature
            N_value = genotype_dataframe[feature].value_counts(normalize=True).get('N')
    
            #define the major genotype of each feature
            stats = genotype_dataframe['SNP 1'].describe()
            mode = stats['top']
        
            #setting threshold
            threshold = 0.2
    
            #missing genotype treatment
            if N_value > threshold :
                genotype_dataframe.drop(columns=feature, inplace=True)
        
            else :
                genotype_dataframe[feature].replace('N', mode, inplace=True)
                
        else :
            print('No missing genotype in {}' .format(feature))
                    
    return genotype_dataframe  
