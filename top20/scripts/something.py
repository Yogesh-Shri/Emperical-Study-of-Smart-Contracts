import slither

# Load the Solidity file
contract = slither.Contract("path/to/contract.sol")

# Get the maximum cyclomatic complexity
max_complexity = max([function.cfg_complexity() for function in contract.functions])

# Get the sum of cyclomatic complexity
sum_complexity = sum([function.cfg_complexity() for function in contract.functions])

print(f"Maximum cyclomatic complexity: {max_complexity}")
print(f"Sum of cyclomatic complexity: {sum_complexity}")
