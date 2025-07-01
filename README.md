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



