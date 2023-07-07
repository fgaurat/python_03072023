import sys
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import glob
import re

def main():
    log_files = glob.glob('*.log')
    
    reg_ip=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    reg_ip=r"^(.+?)\s"
    reg_404 = r'HTTP/1.\d"\s(\d{3})'
    
    for log_file in log_files:
        with open(log_file) as f:
            for num_line,line in enumerate(f):
                result = re.findall(reg_404, line.strip())
                if '404' in result:
                    print(log_file,"ligne:",num_line+1)
                    print(result)



def main_download():
    url = r"https://logs.eolem.com/"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # links = []    
    # for l in soup.find_all('a'):
    #     if '.log' in l.get('href'):
    #         links.append(l.get('href'))
    
    all_links = soup.find_all('a')
    links = [url+l.get('href') for l in all_links if '.log' in l.get('href')]
    
    for link in links:
        file_name = link.split('/')[-1]
        response_log = requests.get(link)
        with open(file_name,'w') as log_f:
            log_f.write(response_log.text)
        
if __name__=='__main__':
    main()
