import os

def screen_clear():
    _ = os.system('cls')

def remove_duplicate_lines(lines):
    return list(dict.fromkeys(lines))

def contains_keywords(line, keywords):
    return any(keyword in line for keyword in keywords)

def remove_www_prefix(domain):
    return domain.replace('www.', '', 1)

screen_clear()

print("Exp1o5iveDisorder - Cyb3r Drag0nz Team | Domain Filter\n")

input_filename = input("Enter domain list [TXT] >>>: ")
output_filename = 'Filtered_Domains.txt'
keywords_to_remove = ['autodiscover', 'cpanel', 'webmail', 'cpcalendars', 'static.cloud-ips.com', 'cpcontacts', 'webdisk']

with open(input_filename, 'r') as file:
    lines = file.readlines()

lines = remove_duplicate_lines(lines)

filtered_domains = []

for line in lines:
    domain = line.strip()
    domain = remove_www_prefix(domain)
    if not contains_keywords(domain, keywords_to_remove):
        filtered_domains.append(domain)
        print("\033[92mThis domain is not in the filter:\033[0m", domain)

with open(output_filename, 'w') as file:
    file.writelines("\n".join(filtered_domains))

print("\nFiltered Domain's saved to 'Filtered_Domains.txt'")
