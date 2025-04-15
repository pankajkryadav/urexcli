import argparse
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import colorama
from collections import defaultdict

colorama.init()

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def normalize_url(url):
    """Ensure URL has http/https prefix"""
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        return f'http://{url}'
    return url

def extract_urls_from_page(url):
    urls = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                if is_valid_url(absolute_url):
                    urls.append(absolute_url)
    except Exception as e:
        pass
    return urls

def process_input_file(input_file, output_file, combined_file):
    try:
        with open(input_file, 'r') as f:
            raw_urls = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"{colorama.Fore.RED}Error: Input file '{input_file}' not found.{colorama.Style.RESET_ALL}")
        sys.exit(1)

    results = defaultdict(list)
    all_urls = []
    
    with tqdm(raw_urls, desc=f"{colorama.Fore.YELLOW}Processing URLs{colorama.Style.RESET_ALL}") as pbar:
        for raw_url in pbar:
            url = normalize_url(raw_url)
            pbar.set_postfix_str(f"{colorama.Fore.WHITE}Processing: {raw_url[:20]}...{colorama.Style.RESET_ALL}")
            
            if not is_valid_url(url):
                results[raw_url] = {
                    'status': f"{colorama.Fore.RED}Invalid URL{colorama.Style.RESET_ALL}",
                    'urls': []
                }
                continue
                
            try:
                extracted_urls = extract_urls_from_page(url)
                results[raw_url] = {
                    'status': f"{colorama.Fore.GREEN}Success ({len(extracted_urls)} URLs found){colorama.Style.RESET_ALL}",
                    'urls': extracted_urls
                }
                all_urls.extend(extracted_urls)
                pbar.set_postfix_str(f"{colorama.Fore.GREEN}Found {len(extracted_urls)} URLs{colorama.Style.RESET_ALL}")
            except Exception as e:
                results[raw_url] = {
                    'status': f"{colorama.Fore.RED}Error: {str(e)[:30]}{colorama.Style.RESET_ALL}",
                    'urls': []
                }

    with open(output_file, 'w') as f:
        for base_url, data in results.items():
            f.write(f"Base URL: {base_url}\n")
            f.write(f"Status: {data['status']}\n")
            f.write("Extracted URLs:\n")
            for url in data['urls']:
                f.write(f"  {url}\n")
            f.write("\n" + "="*80 + "\n\n")

    if combined_file:
        with open(combined_file, 'w') as f:
            f.write("\n".join(all_urls))

    print(f"\n{colorama.Fore.GREEN}Processing complete!{colorama.Style.RESET_ALL}")
    print(f"- Categorized results saved to {colorama.Fore.CYAN}{output_file}{colorama.Style.RESET_ALL}")
    if combined_file:
        print(f"- Combined results saved to {colorama.Fore.CYAN}{combined_file}{colorama.Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description='Advanced URL Extractor Tool', 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=True, help='Input text file containing URLs')
    parser.add_argument('-o', '--output', default='output.txt', 
                        help='Categorized output file (groups URLs by source)')
    parser.add_argument('-c', '--combined', help='Combined output file (all URLs in one list)')
    args = parser.parse_args()

    process_input_file(args.input, args.output, args.combined)

if __name__ == "__main__":
    main()
