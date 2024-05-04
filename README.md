# SEC 10-K Report Fetcher and PDF Converter

This project fetches the latest 10-K reports for a set list of companies from the SEC's EDGAR database and converts them into PDF format using `pdfkit` and `wkhtmltopdf`.

## Requirements

- Python 3.x
- pip
- wkhtmltopdf

## Setup

### Install wkhtmltopdf (to run the GoodVersion)
wkhtmltopdf needs to be installed separately as it is used by pdfkit to render PDFs. Please download it from wkhtmltopdf downloads and install it according to your operating system.
```
https://wkhtmltopdf.org/downloads.html
```

### Configuration
Ensure wkhtmltopdf is installed in the default path or update the path in the script:
```
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

### Install Python Dependencies
To run the code using a virtual machine, run the following commands;
```
python -m venv venv
```
For Windows:
```
.\venv\Scripts\activate
```
For macOS/Linux:
```
source venv/bin/activate
```
Install the required Python libraries with pip:
```
pip install -r requirements.txt
```

### Usage

Run the script from the command line:
```
python .\GoodVersion.py
```
or
```
python .\WorseVersion.py
```
The scripts will fetch the latest 10-K reports for predefined companies and convert each to a PDF file saved in the current directory.

The difference is that GoodVersion need wkhtmltopdf to work, while WorseVersion does not. However, WorseVersion uses a local library that does not need external libraries but that is worse at interpret the content of a HTML document. So if you run that version it will fail at interpret, for example, the Table of Contents. 
