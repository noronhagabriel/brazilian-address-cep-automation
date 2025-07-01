# CEP Auto-Fill Automation from Addresses in Brazil - Python

This project automates the lookup and filling of postal codes (CEPs) for a list of addresses (street, city, and state) using public Brazilian APIs like ViaCEP.

---

## Features

- Reads addresses from a CSV file.
- Queries the postal code (CEP) for each address via public API.
- Updates the CSV file with the found CEPs.
- Implements retry logic and error handling for robustness.
- Includes delay between requests to avoid API rate limits.

---

## Requirements

- Python 3.7 or higher
- `requests` library

---

## Installation

1. Clone this repository:

  
   git clone https://github.com/your-username/your-repo.git
   
   cd your-repo


2. (Optional) Create and activate a virtual environment:


python -m venv .venv

source .venv/bin/activate    # macOS/Linux

.\.venv\Scripts\activate     # Windows


3. Install dependencies:

pip install -r requirements.txt


## CSV Input Format

The script reads a CSV file with the following structure:

| Column | Description                            |
|--------|----------------------------------------|
| rua    | Street name                            |
| cidade | City name (use accents where needed)   |
| estado | Two-letter uppercase state abbreviation (e.g., SP, RJ) |
| cep    | Leave this empty – it will be filled by the script |

## Example Output

### Input CSV (before running the script)

```csv
rua,cidade,estado,cep
Avenida Paulista,São Paulo,SP,
Rua das Flores,Campinas,SP,
Rua do Comércio,Santos,SP,
Rua XV de Novembro,Curitiba,PR,
Rua Boa Vista,Recife,PE,

rua,cidade,estado,cep
Avenida Paulista,São Paulo,SP,01311-921
Rua das Flores,Campinas,SP,13056-084
Rua do Comércio,Santos,SP,11010-140
Rua XV de Novembro,Curitiba,PR,80020-924
Rua Boa Vista,Recife,PE,52191-605
