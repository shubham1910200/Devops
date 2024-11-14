import json
import yaml

aws_services = {
    "ec2": "server",
    "s3" : "storage",
    "lambda" : "serverless",
    "iam": " Restricted the perimission",
    "vpc": "virtual private cloud"
}

with open('aws_services.json','w') as json_files:
    json.dump(aws_services, json_files, indent=4)

print("Dictionary successfully written to aws_services.json")

with open('aws_services.json','r') as json_file:
    aws_services_data = json.load(json_file)

for service, description in aws_services_data.items():
    print(f"{service} : {description}")

with open('services.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

print('Converted YAML to JSON')
 
json_data = json.dumps(yaml_data, indent=4)
print(json_data)