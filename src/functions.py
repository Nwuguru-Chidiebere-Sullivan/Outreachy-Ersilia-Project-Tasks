import numpy as np
from rdkit import Chem
from standardiser import standardise
from rdkit.Chem import inchi, DataStructs, AllChem



def standardise_smiles(smiles):
    mols = []
    for smi in smiles:
        try:
            mol = Chem.MolFromSmiles(smi)
        except:
            mol=np.nan
        mols += [mol]
    st_mols = []
    for mol in mols:
        if mol is not None:
            try:
                st_mol = standardise.run(mol)
            except:
                st_mol = np.nan
        else:
            st_mol = np.nan
        st_mols += [st_mol]
    st_smiles = []
    for st_mol in st_mols:
        if st_mol is not None:
            try:
                st_smi = Chem.MolToSmiles(st_mol)
            except:
                st_smi=np.nan
        else:
            st_smi = np.nan
        st_smiles += [st_smi]
    return st_smiles


def generate_inchi_key(smiles):
    if isinstance(smiles, str):  
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            inchi_key = inchi.MolToInchiKey(mol)
            return inchi_key
    return None

def standardise_inchikey(inchikeys):
    st_inchikeys = []
    for inchikey in inchikeys:
        if inchikey:
            st_inchikey = inchikey.strip().upper()
        else: 
            st_inchikey = np.nan
        st_inchikeys.append(st_inchikey)
    return st_inchikeys


def calc_stats(pred_array, true_array, insol_thresh=-6, sol_thresh=-4):
        '''
        This function will calculate the following on the predicted array:
           Hit% = #correct(lower_sol_thresh,upper_sol_thresh) / #(lower_sol_thresh,upper_sol_thresh)
           Fail% = #true(insol_thresh)pred(lower_sol_thresh,upper_sol_thresh) / #pred(lower_sol_thresh,upper_sol_thresh)
    
        Assumptions: pred_array,true_array are paired numpy arrays.
        '''
    
        #first we need to access the examples which have true in (lower_sol_thresh, upper_sol_thresh)
        true_mask=(true_array > sol_thresh)
    
        #calculating the Hit%
        num_true=len(true_array[true_mask])
        poss_hits=pred_array[true_mask]
        num_hits=np.sum((poss_hits>sol_thresh))
        hit=num_hits/float(num_true)
    
        #calculating the Fail%
        pred_mask=(pred_array > sol_thresh)
        insol_mask=true_array <= insol_thresh
        fail=np.sum(insol_mask & pred_mask) / float(np.sum(pred_mask))
    
    return hit,fail,np.sum(true_mask),np.sum(pred_mask)
