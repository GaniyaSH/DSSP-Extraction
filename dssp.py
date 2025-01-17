# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 04:49:32 2023

@author: Ganu
"""
import pandas as pd
import os
import shutil
import Bio
import os
import sys
import Bio.PDB
import Bio.SeqRecord

def dssp(pdb_file, location):
  from Bio.PDB import PDBParser
  from Bio.PDB.DSSP import DSSP
  import pandas as pd
  p=PDBParser()
  structure=p.get_structure('{}'.format(pdb_file),'{}'.format(location))
  model=structure[0]

  dssp=DSSP(model,'{}'.format(location),dssp='mkdssp')


  ppb=Bio.PDB.PPBuilder()
  global seq
  chains=list(model.get_chains())
  pps=ppb.build_peptides(chains[0])
  seq=pps[0].get_sequence()


  df=pd.DataFrame(dssp)

  df=df.transpose()
  df= df.iloc[[1,2],range(0,len(seq),1)]
  df.iloc[0]=df.iloc[0].str.lower()
  return df

location='C:/Users/Ganu/.spyder-py3/1dc9.pdb'
dssp('1dc9.pdb',location)
