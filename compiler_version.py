import os
import json

search_strings = ['"CompilerVersion": "v0.4.0+','"CompilerVersion": "v0.4.1+','"CompilerVersion": "v0.4.2+','"CompilerVersion": "v0.4.3+','"CompilerVersion": "v0.4.4+',
    '"CompilerVersion": "v0.4.5+','"CompilerVersion": "v0.4.6+','"CompilerVersion": "v0.4.7+','"CompilerVersion": "v0.4.8+','"CompilerVersion": "v0.4.9+','"CompilerVersion": "v0.4.10+',
    '"CompilerVersion": "v0.4.11+', '"CompilerVersion": "v0.4.12+', '"CompilerVersion": "v0.4.13+', '"CompilerVersion": "v0.4.14+', '"CompilerVersion": "v0.4.15+', '"CompilerVersion": "v0.4.16+','"CompilerVersion": "v0.4.17+', '"CompilerVersion": "v0.4.18+', '"CompilerVersion": "v0.4.19+','"CompilerVersion": "v0.4.20+', '"CompilerVersion": "v0.4.21+', '"CompilerVersion": "v0.4.22+','"CompilerVersion": "v0.4.23+', '"CompilerVersion": "v0.4.24+', '"CompilerVersion": "v0.4.25+',
    '"CompilerVersion": "v0.4.26+',
    '"CompilerVersion": "v0.5.0+', '"CompilerVersion": "v0.5.1+','"CompilerVersion": "v0.5.2+','"CompilerVersion": "v0.5.3+', '"CompilerVersion": "v0.5.4+','"CompilerVersion": "v0.5.5+','"CompilerVersion": "v0.5.6+', '"CompilerVersion": "v0.5.7+','"CompilerVersion": "v0.5.8+','"CompilerVersion": "v0.5.9+', '"CompilerVersion": "v0.5.10+','"CompilerVersion": "v0.5.11+','"CompilerVersion": "v0.5.12+', '"CompilerVersion": "v0.5.13+','"CompilerVersion": "v0.5.14+','"CompilerVersion": "v0.5.15+', '"CompilerVersion": "v0.5.16+','"CompilerVersion": "v0.5.17+'] 
directory = "./contracts"  # the directory containing the JSON files
counts = {string: 0 for string in search_strings}  # initialize the counts to zero for each string

# loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)
        with open(file_path) as f:
            # load the JSON file
            data = json.load(f)
            # count the occurrences of each string in the JSON data
            for string in search_strings:
                counts[string] += json.dumps(data).count(string)

# print the counts for each string
for string, count in counts.items():
    print(f"{string} found {count} times in {directory}")

print(counts)
