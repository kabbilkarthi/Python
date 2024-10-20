#!/depot/Python/Python-3.11.2/bin/python
import main

''' 
AUTHOR: KABBIL GI
DATE: 20-10-2024

Pre-requisites: 
1. Always execute from ecsadmin/Jump-server which requires root/sudo privileges.
2. User environment needs to be aliased with saihost. 
   output: alias saihost='/depot/ems/saidb/bin/getInfo -a Search -e -m'
3. Made for Almalinux 8.4 only
'''

main.extract_datas()
