# 🔗 URL Extractor Pro

A powerful Python tool for extracting URLs from web pages with beautiful console output and dual export capabilities. Developed by **xlrsec**.

![Demo](https://img.shields.io/badge/Demo-Coming_Soon-blue) 
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- Dual output formats (categorized & combined)
- Automatic URL normalization
- Colorful console interface 🎨
- Progress tracking with estimates ⏳
- Smart error handling
- Cross-platform compatibility
- HTTP/HTTPS support
- User-agent spoofing

## 📥 Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
Download tool:
<pre>git clone https://github.com/pankajkryadav/urexcli.git
cd url-extractor-pro</pre>

🚀 **Basic Usage**

<pre>`python urexcli.py -i input.txt -o categorized.txt -c combined.txt`</pre>
**🛠️ Full Options**

<pre>$ python urexcli.py --help</pre>

<pre>Usage: urexcli.py [-h] -i INPUT [-o OUTPUT] [-c COMBINED]</pre>

**CLI URL Extractor Tool**

<pre>Options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input text file containing URLs (required)
  -o OUTPUT, --output OUTPUT
                        Categorized output file (default: output.txt)
  -c COMBINED, --combined COMBINED
                        Combined output file (all URLs in one list)</pre>
**📂 Arguments Details**
`<Flag	Description	Example`
<pre>-i	Input file with URLs (required)	-i urls.txt
-o	Categorized output (groups by source domain)	-o domain_sorted.txt
-c	Combined output (all URLs in single file)	-c all_urls.txt</pre>
🎨 Sample Output

<pre>Processing URLs: 100%|██████████| 10/10 [00:15<00:00,  1.55s/url]
  ✔ Success: 8 URLs processed
  ✖ Errors: 2 URLs failed`

`Processing complete!`
- Categorized results: categorized.txt
- Combined results: combined.txt
Colors will automatically work in most terminals (Windows users: run python -m pip install colorama first)</pre>

**📝 Notes**
<pre>Input file should contain one URL per line

Handles both formatted (https://) and unformatted (example.com) URLs

Timeout set to 10 seconds per request

Results include both internal and external links

Duplicate URLs in combined output are automatically removed</pre>


**Input URLs are publicly accessible**

**Websites don't block scrapers**

**No JavaScript rendering required**

**Results may vary based on website structure**

**Developed with ❤️ by xlrsec**



