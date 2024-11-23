# Host Data Extraction Script

## Author
**KABBIL GI**

## Date
20-10-2024

## Description
This script extracts host data, including `hostname`, `pri_owner`, `nic_mac`, and `ls_location` from a `hosts` file. It executes commands via a jump server with root/sudo privileges, processes the outputs, and formats the data. Additionally, it extracts the netmask value from the remote hosts.

### Pre-requisites
1. Execute from `Jump-server` which requires root/sudo privileges.
2. Ensure the user environment is aliased with `saihost`.
   - Example: `alias saihost='/depot/ems/saidb/bin/getInfo -a Search -e -m'`
3. The script is made for Almalinux only.

### Installation
1. **Python Version**: Ensure you have Python 3.11.2 installed.
2. **Install Required Packages**:
    ```bash
    subprocess, smtplib, re
