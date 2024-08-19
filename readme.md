# Tanzanian Banks

This project aims to provide information and insights on Tanzanian banks. It includes data on various banks operating in Tanzania, their branches, contacts, addresses, swift-codes and other relevant information.

## Table of Contents
- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Tanzanian Banks is a comprehensive repository that offers insights into the banking sector in Tanzania. It provides a centralized library for accessing information about different banks, their braches,  locations, addresses, contacts and swift codes. Whether you are a developer, researcher, investor, or simply curious about the Tanzanian banking industry, this library is a valuable resource.

## Data Sources
The data used in this project is sourced from reputable financial institutions, regulatory bodies, and publicly available reports. We strive to ensure the accuracy and reliability of the information provided. However, please note that the data may be subject to change and it is always recommended to verify the information from official sources.

## Features
- Banks
- Banks categories
- Banks braches
- Banks contacts and addresses
- Banks locations
- Banks swift codes
- Retrieve specific bank details by bank code
- Retrieve contacts for specific banks
- Retrieve all banks regions
- Retrieve all bank categories
- Filter banks by category (e.g., commercial banks, microfinance banks)
- Retrieve all branches for all banks
- Retrieve branches for a specific bank
- Retrieve branches for all banks in a specific region
- Retrieve branches for a specific bank in a specific region

## Installation
To use this project, follow these steps:

1. Run the command on terminal: `pip install tanzanian-banks`

OR:

1. Clone the repository: `git clone https://github.com/misingo255/tanzanian-banks.git`
2. Open the directory on terminal: `cd tanzanian-banks`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

### 1. Retrieve All Banks

```python
from tanzanian_banks import tanzanian_banks
banks = tanzanian_banks.get_banks()
print(banks)
```

### 2. Retrieve Specific Bank by Code

```python
from tanzanian_banks import tanzanian_banks
bank = tanzanian_banks.get_bank("crdbplc")
print(bank)
```

### 3. Retrieve Contacts for a Specific Bank

```python
from tanzanian_banks import tanzanian_banks
contacts = tanzanian_banks.get_bank_contacts("crdbplc")
print(contacts)
```

### 4. Retrieve All Regions

```python
from tanzanian_banks import tanzanian_banks
regions = tanzanian_banks.get_regions()
print(regions)
```

### 5. Retrieve All Bank Categories

```python
from tanzanian_banks import tanzanian_banks
categories = tanzanian_banks.get_categories()
print(categories)
```

### 6. Filter Banks by Category

#### Retrieve Commercial Banks

```python
from tanzanian_banks import tanzanian_banks
commercial_banks = tanzanian_banks.get_commercial_banks()
print(commercial_banks)
```

#### Retrieve Microfinance Banks

```python
from tanzanian_banks import tanzanian_banks
microfinance_banks = tanzanian_banks.get_microfinance_banks()
print(microfinance_banks)
```

### 7. Retrieve All Branches for All Banks

```python
from tanzanian_banks import tanzanian_banks
branches = tanzanian_banks.get_all_branches_for_all_banks()
print(branches)
```

### 8. Retrieve Branches for a Specific Bank

```python
from tanzanian_banks import tanzanian_banks
branches = tanzanian_banks.get_bank_branches("crdbplc")
print(branches)
```

### 9. Retrieve Branches for All Banks in a Specific Region

```python
from tanzanian_banks import tanzanian_banks
branches = tanzanian_banks.get_all_branches_for_all_banks_by_region("dar")
print(branches)
```

### 10. Retrieve Branches for a Specific Bank in a Specific Region

```python
from tanzanian_banks import tanzanian_banks
branches = tanzanian_banks.get_bank_branches_by_region("crdbplc", "dar")
print(branches)
```


## Contributing
Contributions to this project are welcome. If you have suggestions, bug reports, or would like to contribute new features, please open an issue or submit a pull request. We appreciate your contributions in making this project more comprehensive and accurate.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.
