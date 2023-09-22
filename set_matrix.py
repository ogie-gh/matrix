import json
import os


def set_output(value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'matrix={value}', file=fh)

# Create a list of dictionaries representing the jobs
jobs = [
    {
        "prefix": "ABC",
        "summary": "This is my ABC Summary",
        "description": "This is my ABC description"
    },
    {
        "prefix": "TST",
        "summary": "This is my TST Summary",
        "description": "This is my TST description"
    }
]

# Convert the list of dictionaries to a JSON string
json_str = json.dumps(jobs, separators=(',', ':'))

# Print the JSON string
print(json_str)
set_output(json_str)
