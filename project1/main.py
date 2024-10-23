#!/depot/Python/Python-3.11.2/bin/python
import subprocess
import re


''' 
AUTHOR: KABBIL GI
DATE: 20-10-2024
Pre-requisites: 
1. Always execute from ecsadmin/Jump-server which requires root/sudo privileges.
2. User environment needs to be aliased with saihost. 
   output: alias saihost='/depot/ems/saidb/bin/getInfo -a Search -e -m'
3. Made for Almalinux only
'''

def extract_datas():
    # Open 'hosts' file and process each line
    output = ""
    with open('hosts', 'r') as hosts:
        for h in hosts:
            host = h.strip()
            try:
                # Execute the command and capture inventory output
                host_out = subprocess.check_output(['/bin/bash', '-i', '-c', f'saihost {host} | jq | grep -Ei "hostname|pri_owner|nic_mac|ls_location"'])
                decoded_output = host_out.decode()
                
                # Execute the command and capture the netmask output
                out = subprocess.check_output(['/bin/bash', '-i', '-c', f'ssh 2> /dev/null {host} ifconfig | head -n 2 | grep -i mask'])
                decoded = out.decode()

                # Extract netmask value using regex
                netmask_match = re.search(r"netmask (\d+\.\d+\.\d+\.\d+)", decoded)  # OS >= 7
                mask_match = re.search(r"Mask:(\d+\.\d+\.\d+\.\d+)", decoded)  # OS < 7
                if netmask_match:
                    netmask = netmask_match.group(1)
                elif mask_match:
                    netmask = mask_match.group(1)
                else:
                    netmask = "Not found"

                # Extract information using regex
                hostname_match = re.search('"hostname": "(.*?)"', decoded_output)
                hostnames = hostname_match.group(1)

                owner_match = re.search('"pri_owner": "(.*?)"', decoded_output)
                owner = owner_match.group(1)

                location_match = re.search('"ls_location": "(.*?)"', decoded_output)
                location = location_match.group(1).replace(' ', '-')

                nic_match = re.search('"nic_mac": "(.*?)"', decoded_output)
                nic = nic_match.group(1)

                # Collect the formatted output
                collected_output = f'/remote/kickstart/bin/ks_ansible --- MYQSC=QSC-W MYOS=AlmaLinux8.4_amd64 MYHOST={hostnames} MYNETMASK={netmask} MYOWNER={owner} MYLOCATE={location} MYSNPSLEVEL=prod MYMAC={nic} MYPATCHLEVEL=22P2\n'
                output += collected_output + "\n"

            except subprocess.CalledProcessError as e:
                output += f"Command failed for {host}: {e}\n\n"
            except AttributeError as e:
                output += f"Regex matching failed for {host}: {e}\n"
            except Exception as e:
                output += f"Unexpected error for {host}: {e}\n"

    return output
if __name__ == "__main__":
    result = extract_datas()
    print(result)