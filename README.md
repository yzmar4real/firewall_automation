# Firewall Automation

Python Code that allows Security Engineers to audit their palo alto firewalls, specifically checking through the rules and policies for objects that are not in use. This is particularly helpful in instances where brownfield environments are onboarded, or cybersecurity audits are carried out to ensure that objects are well-organized and comply with specific standards. 

# Use-Case Description 




# Contacts

Oluyemi Oshunkoya (yemi_o@outlook.com)

# Prerequisites

Before running this tool, you need to have the following:

Python 3.x installed on your system
The requests library installed. You can install it using the following command: pip install requests
Pandas library installed. You can install it using the following command: pip install pandas
Access to a Palo Alto firewall with API access enabled

# Setup

1. Clone the repository

git clone https://github.com/yzmar4real/firewall_automation.git

2. CD into the directory 

cd firewall_automation

3. (Optional) Use the directory as a virtual environment for the project

python3 -m venv . 

4. (Optional) Start the virtual environment and install the requirements for the project

source bin/activate

# Usage
1. Run the Main.py file using the command - python Main.py

2. Follow the prompts to enter the firewall IP address, username, and password

3. The tool will retrieve the firewall objects and security rules and policies, compare them, and output the used and non-used objects as json files and a excel sheet. 
