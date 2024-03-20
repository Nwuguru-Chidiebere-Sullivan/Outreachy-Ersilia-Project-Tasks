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



