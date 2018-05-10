# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re
import time

file_object = open('rs_id_list.txt','rU')
file_output = open('rs_id_list_out.txt','w')

try: 
    for line in file_object:
        myurl = "".join(["https://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?searchType=adhoc_search&type=rs&rs=",str(line).strip()])
        response = urllib.request.urlopen(myurl)
        html = response.read()
        soup = BeautifulSoup(html,"lxml")
        if (len(soup.find_all(id='Allele'))):
            info = soup.find_all(id='Allele')[0].get_text()
            result = re.findall(".*Alleles:(.*)Allele\ Origin.*",info)
            file_output.write("".join([str(line).strip(),"\t",str(result[0]).strip(),"\n"]))
        else:
            pass
        time.sleep(1)
finally:
     file_object.close()
     file_output.close()
