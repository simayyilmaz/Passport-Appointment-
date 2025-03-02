# Python Selenium Automation Project

## Overview
This project automates a specific web navigation process using the Selenium WebDriver. The script navigates through a series of web pages, performs actions based on the page contents, and sends an email notification with the status of the process.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Dependencies
Install the required Python packages using the following command:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- selenium

### Setup
1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Configuration
Create a `info2.py` file in the project directory with the following content, replacing the placeholders with your actual credentials:
```python
kimlik = "YOUR_ID_NUMBER"
sifre = "YOUR_PASSWORD"
mailUser = "YOUR_EMAIL_ADDRESS"
mailPass = "YOUR_EMAIL_PASSWORD"
```

## Running the Script
Execute the script using the following command:
```bash
python main.py
```

## Note
- The script runs in an infinite loop and can be stopped manually.
- Ensure you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Google Chrome).

## Disclaimer
Use this script responsibly and ensure you have permission to automate interactions with the target website.

## License
[MIT License](LICENSE)

```