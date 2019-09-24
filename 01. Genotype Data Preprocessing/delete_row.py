'''
A function to delete the row of particular sample from the genotype data
design by.https://github.com/SausanCantik
'''

def delete_row(genotype_dataframe) :
    print ('Dimension Before: ', genotype_dataframe.shape )
    
    #gather the list of samples to remove
    to_remove = sample_ID(genotype_data)
    
    for sample in to_remove :
        genotype_dataframe = genotype_dataframe[genotype_dataframe.Samples != sample]
        
    print ('Dimension After: ', genotype_dataframe.shape )
    
    #write output
    file_output = genotype_dataframe.to_excel('genotype_after_treatment.xlsx')
    
    return file_output
