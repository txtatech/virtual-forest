The directory_structure.json is required only because the virtual-forest AI engine is part of the DNA encoding scripts used here.

Preperation is optional. The scripts are already setup to work without these steps:

Optional Step 1:

python3 simpy_basher.py

It reads the sim.py file (you could use any readable file), finds words occuring more than four times and maps them to DNA variations.

The script then outputs the following file:

combo.txt

Optional Step 2:

bash simpy_basher-sort.sh

This sorts the combo.txt file and produces the following file:

sorted_combo.txt

Optional Step 3:

Use the new mappings to update the main scripts. 

# USAGE #

Step 1:

python3 playsim_more.py

launches a game instance and produces the following files:

dna_rna_structure.json

sim_dna_rna.py

Step 2:

Exit the playsim_more.py script

python3 djinnfluxer2.py

launches the DNA encoder and produces the following file:

encoded_dna.json
 
