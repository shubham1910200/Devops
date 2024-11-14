import json
import yaml

# Create a dictionary wit some cloud services information.
services_dict = {
    "aws": "ec2",
    "azure": "VM",
    "gcp": "compute engine"
}

# Writing a dictonary to a JSON file
with open('services.json', 'w') as json_file:  # This is open a file called `services.json` in writing mode. which means it will create a file it does't exist, or overwrite the existing file it does exist.
    json.dump(services_dict, json_file, indent=4) # This converts the dictionary (service_dict) into json format and writes it to the file(services.json). the indent = 4 means argument makes output nicely formatted with indentation of 4 spaces.

print("Dictionary successfully written to services.json")

# Reads the json file to load the data
with open('services.json', 'r') as json_file: # open the file in read mode, meaning your are going to read from it.
    services_data = json.load(json_file) # This loads the contents of json file into a python dictionary (called servies_data), so you can work with in python.

# print the data to console
for provider, service in services_data.items(): # print the dictionary service_data (which was read from json file)
    print(f"{provider} : {service}") # provder will representkey and service value

# Attempts to read from yaml file 
with open('services.yaml', 'r') as yaml_file: # this open the service.yaml file in read mode 
    yaml_data = yaml.safe_load(yaml_file) # this read the content of yaml file and converted it into python object. the safe_load() methood is used to load the yaml file in safe way, avoiding some potential security issues risk.

# Converts the yaml data to json format
json_data = json.dumps(yaml_data, indent=4)

print("Converted YAML to JSON:")
print(json_data)
