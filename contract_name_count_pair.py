import os
import re

# Path to the directory containing the .sol files
directory = "./Smart_Contracts"

# Dictionary to store contract reference counts
contract_counts = {}

# Iterate over each .sol file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".sol"):
        # Read the contents of the file
        with open(os.path.join(directory, filename), "r") as file:
            contents = file.read()
        # Find all contract names in the file
        contracts = re.findall("contract\s+(\w+)\s*\{", contents)
        # Count references to each contract in the file
        for contract in contracts:
            count = contents.count(contract)
            if contract in contract_counts:
                contract_counts[contract] += count
            else:
                contract_counts[contract] = count

# Sort contracts by reference count in descending order
sorted_contracts = sorted(contract_counts.items(), key=lambda x: x[1], reverse=True)

# Write the list of contracts and their reference counts to a file
with open("contract_counts2.txt", "w") as file:
    for contract, count in sorted_contracts:
        file.write(f"{contract}: {count}\n")

with open("contract_counts2.csv", "w") as file:
    for contract, count in sorted_contracts:
        file.write(f"{count}\n")
