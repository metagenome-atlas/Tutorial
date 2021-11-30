#!/usr/bin/env python

import os
import atlas
from glob import glob

atlas_dir= os.path.dirname(atlas.__file__)

rules_folder= os.path.join(atlas_dir,"workflow","rules")


for file_to_modify in glob(rules_folder+"/*.smk"):

    with open(file_to_modify) as f:
        filecontent= f.read()

    filecontent.replace("checkm lineage_wf","checkm lineage_wf --reduced")


    with open(file_to_modify,"w") as f:
        f.write(filecontent)


# comment out annotations in template config
# only let "genes"

file_to_modify= os.path.join(atlas_dir,"template_config.yaml")
with open(file_to_modify) as f:
    filecontent= f.read()
for annotation in ["gtdb_tree", "gtdb_taxonomy","kegg_modules","dram"]:

    listitem = '  - '+annotation
    filecontent.replace(listitem, '# '+listitem)

with open(file_to_modify,"w") as f:
    f.write(filecontent)
