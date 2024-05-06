import requests
import pdfkit

path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
companies = {
    "Apple": "0000320193",
    "Meta": "0001326801",
    "Alphabet": "0001652044",
    "Amazon": "0001018724",
    "Netflix": "0001065280",
    "Goldman Sachs": "0000886982"
}

def fetch_data(api_url):
    try:
        headers = {
            "User-Agent": "Sample Company Name AdminContact@<sample company domain>.com"
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Ensures we raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

def get_latest_10k_report(data):
    forms = data['filings']['recent']['form']
    for index, form in enumerate(forms):
        if form == '10-K':
            return {
                'accessionNumber': data['filings']['recent']['accessionNumber'][index],
                'filingDate': data['filings']['recent']['filingDate'][index],
                'primaryDocument': data['filings']['recent']['primaryDocument'][index]
                }
    return None

def download_report(doc_url, filename, config):
    try:
        headers = {"User-Agent": "Sample Company Name AdminContact@<sample company domain>.com"}
        response = requests.get(doc_url, headers=headers)
        response.raise_for_status()  # Ensures we raise an exception for HTTP errors

        # Convert HTML directly to PDF without saving the HTML to a file
        pdf_path = f"{filename}.pdf"
        options = {
            'no-images': '',  # Optional: Disables loading of images
        }
        pdfkit.from_string(response.text, pdf_path, configuration=config, options=options)
        print(f"Converted PDF saved as: {pdf_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download report: {e}")
    except Exception as e:
        print(f"Error converting to PDF: {e}")

def main():
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    for company_name, cik in companies.items():
        print(f"Fetching 10-K for {company_name}")
        api_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        data = fetch_data(api_url)
        if data:
            latest_10k = get_latest_10k_report(data)
            if latest_10k:
                print(f"Latest 10-K Report for {company_name}:")
                doc_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{latest_10k['accessionNumber'].replace('-', '')}/{latest_10k['primaryDocument']}"
                file_path = f"{company_name}_10K_{latest_10k['filingDate']}"
                download_report(doc_url, file_path, config)
            else:
                print(f"No 10-K reports found for {company_name}.")
        else:
            print(f"Failed to fetch data for {company_name}.")

if __name__ == "__main__":
    main()