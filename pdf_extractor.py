# pdf_extractor.py
# extracts all pdf files which are downloadable from a website

import requests, os, bs4

os.chdir('/Users/michele/Desktop/Documents-Local/WebScraping/EpistomologyTheo')
url = input('Enter url: ')
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

pdf_links = []
for ele in soup.find_all('a', href=True):
    href = ele['href']
    if href.endswith('.pdf'):
        pdf_links.append(href)

cwd = str(os.getcwd())
for count, ele in enumerate(pdf_links):
    save_path = os.path.join(cwd + f'/file{count}' + '.pdf')
    res = requests.get(ele)
    res.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(res.content)
