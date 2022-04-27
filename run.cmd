@echo off

Rem This script runs the three different scripts one after another using temp files to store the output.  
Rem The temp files is then deleted, leaving only the final file

python capitalize_password.py > passord_temp0.txt

python merger3.py > passord_temp1.txt

python symbols.py > passord-final.txt

del passord_temp0.txt

del passord_temp1.txt



