import requests
from xhtml2pdf import pisa

companies = {
    "Apple": "0000320193",
    "Meta": "0001326801",  # Previously known as Facebook
    "Alphabet": "0001652044",  # Google's parent company
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
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

def get_latest_10k_report(data):
    if 'filings' in data and 'recent' in data['filings']:
        forms = data['filings']['recent'].get('form', [])
        for index, form in enumerate(forms):
            if form == '10-K':
                return {
                    'accessionNumber': data['filings']['recent'].get('accessionNumber', [])[index],
                    'filingDate': data['filings']['recent'].get('filingDate', [])[index],
                    'primaryDocument': data['filings']['recent'].get('primaryDocument', [])[index]
                }
    return None

def preprocess_html(html_content):
    # Example: Simplifying table structures (basic example)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            if len(row.find_all('td', recursive=False)) != len(table.find_all('col')):  # Checking column consistency
                row.decompose()  # This removes the row; consider other adjustments as needed
    return str(soup)

def download_report(doc_url, filename):
    headers = {"User-Agent": "Sample Company Name AdminContact@<sample company domain>.com"}
    try:
        response = requests.get(doc_url, headers=headers)
        response.raise_for_status()
        html_content = response.text

        # Preprocess HTML to simplify tables
        processed_html = preprocess_html(html_content)

        with open(f"{filename}_not_as_good.pdf", "wb") as pdf_file:
            pdf = pisa.CreatePDF(processed_html, pdf_file)
            if pdf.err:
                raise Exception(f"PDF creation error: {pdf.err}")
        print(f"PDF successfully saved as: {filename}_not_as_good.pdf")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download HTML: {e}")
    except Exception as e:
        print(f"Error during PDF creation: {e}")

def main():
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
                download_report(doc_url, file_path)
            else:
                print(f"No 10-K reports found for {company_name}.")
        else:
            print(f"Failed to fetch data for {company_name}.")

if __name__ == "__main__":
    main()
