# Python
Python is an open-source, high-level programming language that’s renowned for its simplicity and readability. Created by Guido van Rossum, Python has grown into a major player in the programming world.

## Task 1: Getting started
Here's what we're going to do get started with Python:
1. Verify the installation
``` bash
python --version
```
2. Explore Python Data Types: Python has several key data types:

  1. Integers: Whole numbers.

  2. Floats: Numbers with decimals.

 3. Strings: Text enclosed in quotes.

 4. Lists: Ordered collections.

 5. Tuples: Immutable ordered collections.

 6. Dictionaries: Key-value pairs.

 7. Sets: Unordered collections of unique items.

## What are Data types?
Data types classify the kind of data we work with in Python. Since everything in Python is an object, data types are essentially classes, and our variables are instances of these classes. Here’s a quick rundown of Python’s built-in data types:

1. Numeric: Integers (e.g., 42) Floats (e.g., 3.14) Complex Numbers (e.g., 1+2j)

2. Sequential: Strings (e.g., "Hello World") Lists (e.g., [1, 2, 3]) Tuples (e.g., (1, 2, 3))

3. Boolean: True or False

4. Set: Unordered collections of unique items (e.g., {1, 2, 3})

5. Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25})

To check the type of a variable
your_variable = 100 print(type(your_variable))

## Understanding Data Structures
Data structures are ways of organizing and storing data to make it accessible and efficient.

### Python offers several built-in data structures:

1. Lists: Ordered collections of items. Mutable, meaning you can change their content. Example: my_list = [1, 2, 3, 'Python']

2. Tuples: Ordered collections of items, similar to lists. Immutable, meaning once created, they cannot be changed. Example: my_tuple = (1, 2, 3, 'Python')

3. Dictionaries: Unordered collections of key-value pairs. Keys are unique and used to access corresponding values. Example: my_dict = {"name": "Alice", "age": 25}

## Hands-On Tasks
List, Tuple, and Set Comparison

### To understand the differences between lists, tuples, and sets, here’s a brief comparison:

1. Lists: Mutable, ordered, can contain duplicate items. Tuples: Immutable, ordered, can contain duplicate items. Sets: Mutable, unordered, no duplicate items.

Here’s how you might use each:
``` bash
 my_list = [1, 2, 2, 3]
 my_tuple = (1, 2, 2, 3)
 my_set = {1, 2, 3}
```
2. Working with Dictionaries

Create a dictionary of your favorite tools and use dictionary methods to retrieve values:
```bash
 fav_tools = { 
 1: "Linux", 
 2: "Git", 
 3: "Docker", 
 4: "Kubernetes", 
 5: "Terraform", 
 6: "Ansible", 
 7: "Chef" 
 } 
 print(fav_tools[1]) # Output: Linux
```
3. Manipulating Lists

Create and modify a list of cloud service providers: 

```python
 cloud_providers = ["AWS", "GCP", "Azure"] 
 cloud_providers.append("Digital Ocean") 
 cloud_providers.sort() 
 print(cloud_providers) 
 # Output: ['AWS', 'Azure', 'Digital Ocean', 'GCP']
```

# Creating and Writing a Python Dictionary to a JSON File
JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write. It’s also easy for machines to parse and generate. Python’s built-in json library makes it incredibly straightforward to work with JSON data.
Let’s start by creating a Python dictionary and writing it to a JSON file.

```python
import json

# Creating a dictionary 
services_dict = {
    "aws": "ec2",
    "azure": "VM",
    "gcp": "compute engine"
}

# Writing the dictionary to a JSON file 
with open('services.json', 'w') as json_file:
    json.dump(services_dict, json_file, indent=4)

print("Dictionary successfully written to services.json")

```
Here, we created a simple dictionary representing cloud services from AWS, Azure, and GCP. The json.dump() method is used to write the dictionary to a services.json file, with indent=4 to make the JSON output more readable.

## Reading and Parsing a JSON File
Now that we have our services.json file, the next step is to read the file and extract information from it. This is a crucial step when working with JSON configurations or API responses.
```json
with open('services.json', 'r') as json_file:
    services_data = json.load(json_file)

for provider, service in services_data.items():
    print(f"{provider} : {service}")
    print("\n")
```
In this snippet, we used json.load() to read the JSON data into a Python dictionary. We then iterated over the dictionary to print each cloud provider and their corresponding service.

## Reading YAML Files and Converting Them to JSON
YAML (YAML Ain’t Markup Language) is another human-readable data serialization format, often used for configuration files in DevOps tools like Ansible, Kubernetes, and Docker Compose. Python’s pyyaml library allows us to easily parse and convert YAML files.

Let’s see how we can read a YAML file and convert it to JSON.

```python
import yaml 
import json

# Reading from a YAML file 
with open('services.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Converting YAML data to JSON
json_data = json.dumps(yaml_data, indent=4)

print("Converted YAML to JSON:")
print(json_data)
```
In this example, we used yaml.safe_load() to read the YAML file into a Python dictionary. We then converted this dictionary to a JSON string using json.dumps(). The indent=4 parameter ensures the JSON output is well-formatted.

# Sample Code 

```python
import json
import yaml

services_dict = {
    "aws": "ec2",
    "azure": "VM",
    "gcp": "compute engine"
}

with open('services.json', 'w') as json_file:
    json.dump(services_dict, json_file, indent=4)

print("Dictionary successfully written to services.json")

with open('services.json', 'r') as json_file:
    services_data = json.load(json_file)

for provider, service in services_data.items():
    print(f"{provider} : {service}")

with open('services.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

json_data = json.dumps(yaml_data, indent=4)

print("Converted YAML to JSON:")
print(json_data)
```