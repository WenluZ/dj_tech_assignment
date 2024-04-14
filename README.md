# About Customer Data Segment

This repository hosts a Python project designed to segment customer data into three categories ('Low', 'Medium', 'High') based on their purchase amounts.

## Input and Output Examples.

- **Input**:
'''
[
  {"customer_id": 1, "name": "John Doe", "email": "john@example.com", "purchase_amount": 120.50, "purchase_date": "2023-01-15"},
  {"customer_id": 2, "name": "Jane Smith", "email": "jane@example.com", "purchase_amount": 75.20, "purchase_date": "2023-02-02"},
  {"customer_id": 3, "name": "Bob Johnson", "email": "bob@example.com", "purchase_amount": 200.00, "purchase_date": "2023-02-20"}
]
'''
- **Output**:
'''
customer_id	name	email	purchase_amount	segment
1	John Doe	john@example.com	120.5	Medium
2	Jane Smith	jane@example.com	75.2	Low
3	Bob Johnson	bob@example.com	    200	    Medium
'''

## What this repo contains

- **main.py**: Core functionality file responsible for data ingestion, processing, and export.
- **data_generator.py**: Python script to generate 5000 records adhering to the structure outlined in CustData_Sample.json.

- **data/**: Directory to store input data. Once 5000 random customer data records are generated, they will be exported here.
- **output/**: Directory to store final segment outputs in CSV format.
- **tests/**: Directory housing pytest files for testing Python project functions.

```text
.
├── LICENSE
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-39.pyc
│   ├── main.cpython-39-pytest-8.1.1.pyc
│   └── main.cpython-39.pyc
├── data
│   └── CustData_Sample.json
├── main.py
├── output
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── data_generator.cpython-39.pyc
│   └── data_generator.py
├── startup.sh
└── tests
    ├── __pycache__
    │   └── test_segment.cpython-39-pytest-8.1.1.pyc
    └── test_segment.py
```

## Prerequisites

- **python3**: [Install Python3](https://www.python.org/downloads/).
- **Windows**: Windows Subsystem for Linux (WSL) to run the bash based command `startup.sh`. Please follow [Windows Subsystem for Linux Installation (WSL)](https://docs.docker.com/docker-for-windows/wsl/) and [Using Docker in WSL 2](https://code.visualstudio.com/blogs/2020/03/02/docker-in-wsl2), to get started.

## Get started

### Step one: Getting Started

##### clone the project:
```bash
git clone https://github.com/WenluZ/dj_tech_assignment
cd dj_tech_assignment
```
##### set up and activate python venv:
```bash
python3 -m venv ./venv  
source venv/bin/activate
```

### Step two: Running the Project

Execute the Python project to install required packages (the process will last around 1 min), generate a customer dataset, process the data, and export it to a final CSV output.

```bash
bash startup.sh start
```

### Step three: Testing the Python Project.

```bash
bash startup.sh test
```


### Further Explanation of Supporting Files.

#### startup.sh

The repository includes a sample shell script named startup.sh at its root. Run the following command to receive detailed explanations of all startup commands:

```bash
bash startup.sh help
```
#### requirements.txt

A list of required Python libraries for this project.

## What's next?

- Learn the requirements, including: load frequency (one-off or incremental), data structure/schema, relationships with other data in the data warehouse, orchestration, and other transformation requirements, etc.  
- Learn any validation required. 
