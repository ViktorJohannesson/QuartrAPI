# SEC 10-K Report Fetcher and PDF Converter

This project fetches the latest 10-K reports for a set list of companies from the SEC's EDGAR database and converts them into PDF format using `pdfkit` and `wkhtmltopdf`.

## Requirements

- Python 3.x
- pip
- wkhtmltopdf

## Setup

### Install Python Dependencies

First, install the required Python libraries with pip:

```bash
pip install -r requirements.txt

Install wkhtmltopdf
wkhtmltopdf needs to be installed separately as it is used by pdfkit to render PDFs. Please download it from wkhtmltopdf downloads and install it according to your operating system.

Configuration
Ensure wkhtmltopdf is installed in the default path or update the path in the script:
python
Copy code
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
Usage
Run the script from the command line:

bash
Copy code
python main.py
The script will fetch the latest 10-K reports for predefined companies and convert each to a PDF file saved in the current directory.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

makefile
Copy code

### `requirements.txt`

```plaintext
requests==2.25.1
pdfkit==0.6.1
Notes
requirements.txt lists the versions of requests and pdfkit that are known to work with your script. You might need to update these versions based on your environment or if there are new releases.
README.md includes basic setup instructions, a brief description of the script, and how to run it. It points out the necessity to install wkhtmltopdf because pdfkit relies on it for PDF conversion.
Adjust the path to wkhtmltopdf in the script if it's installed in a different location on your system or if you deploy this on a different operating system.
This setup should make it straightforward for anyone cloning your repository to get started quickly. If you wish to include more detailed documentation or additional features like error handling and logging, you might want to expand the README.md accordingly.
