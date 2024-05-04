# SEC 10-K Report Fetcher and PDF Converter

This project fetches the latest 10-K reports for a set list of companies from the SEC's EDGAR database and converts them into PDF format using `pdfkit` and `wkhtmltopdf`.

## Requirements

- Python 3.x
- pip
- wkhtmltopdf

## Setup

### Install Python Dependencies

First, install the required Python libraries with pip:
```
pip install -r requirements.txt
```

### Install wkhtmltopdf
wkhtmltopdf needs to be installed separately as it is used by pdfkit to render PDFs. Please download it from wkhtmltopdf downloads and install it according to your operating system.
```
https://wkhtmltopdf.org/downloads.html
```

### Configuration
Ensure wkhtmltopdf is installed in the default path or update the path in the script:
```
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

### Usage
Run the script from the command line:
```
python main.py
```
The script will fetch the latest 10-K reports for predefined companies and convert each to a PDF file saved in the current directory.
