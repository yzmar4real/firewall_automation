import json
import pandas as pd
import requests
from pan_fnc import get_api_key,get_object_only,get_sec_rules,get_firewall_info,compare_lists,get_object_details

# Get user input for firewall information
fw_ip, fw_user, fw_pass = get_firewall_info()

api_key = get_api_key(fw_ip, fw_user, fw_pass)

### Pull existing objects from the firewall #####

objects_existing = get_object_only(api_key, fw_ip)

rules_objects = get_sec_rules(fw_ip,api_key)

objects_existing_details = get_object_details(api_key,fw_ip)

# #### comparing both lists to identify what's used vs what's not used ###########
objects_in_rules = []
objects_not_in_rules = []
final_match = []
final_notmatch = []

# Compare existing objects to used objects in security rules
objects_in_rules, objects_not_in_rules = compare_lists(objects_existing, rules_objects)

### Create a new list for item representation 
for item in objects_in_rules:
    for match in objects_existing_details:

        match_name = match['Name']
        match_netmask = match['Details']
        if item == match_name:
            final_match.append({'Name': match_name, 'Details': match_netmask})
        else:
            final_notmatch.append({'Name': match_name, 'Details': match_netmask})

# Print the matching and non-matching objects
# print("Matching objects:", final_match)
# print("Non-matching objects:", final_notmatch)

with open('final_match.json', 'w') as f:
    json.dump(final_match, f)

with open('final_notmatch.json', 'w') as f:
    json.dump(final_notmatch, f)

final_match_df = pd.DataFrame(final_match)
final_notmatch_df = pd.DataFrame(final_notmatch)

with pd.ExcelWriter('output.xlsx') as writer:
    final_match_df.to_excel(writer, sheet_name='final_match')
    final_notmatch_df.to_excel(writer, sheet_name='final_notmatch')
