import json
import os


def set_output(value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'matrix={value}', file=fh)

# Create a list of dictionaries representing the jobs
jobs = [
    {
        "job_name": "Run ubuntu-latest jobs",
        "command": "ubuntu-latest command",
        "os": "ubuntu-latest"
    },
    {
        "job_name": "Run windows-latest jobs",
        "command": "windows-latest command",
        "os": "windows-latest"
    }
]

# Convert the list of dictionaries to a JSON string
json_str = json.dumps(jobs, indent=2)

# Print the JSON string
print(json_str)
set_output(json_str)
