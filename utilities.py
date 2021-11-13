import os
import json
from bs4 import BeautifulSoup
import re

def generate_personnel_page():
  with open('res/data/personnel.json') as personnel_file:
    for index, person in enumerate(json.load(personnel_file)):
      with open('pages/personnels/template.html') as template_file:
        modified = template_file.read()
        print(person['name'])
        modified = modified.replace('{{name}}', person['name'])

        skill_list_html = ''
        for skill in person['spacializations']:
          skill_list_html += '<div class="col-12 col-md-4"><span class="d-block fs-5 border p-2">' + skill + '</span></div>'

        modified = modified.replace('moistnugget', skill_list_html)
        modified = modified.replace('omegalul', person['image'])
        modified = modified.replace('kaorukomoeta', person['contact']['email'])
        try:
          modified = modified.replace('koronesuki', person['contact']['phone'])
        except:
          pass
        
        try:
          modified = modified.replace('towatowa', person['links']['portofolio'])
        except:
          pass
        try:
          modified = modified.replace('watamewatame', person['links']['github'])
        except:
          pass
        try:
          cert_row1 = person['certificates'][:len(person['certificates'])//2]
          cert_row2 = person['certificates'][len(person['certificates'])//2:]
          cert_row1_html = ''
          cert_row2_html = ''
          switch = False
          for cert in person['certificates']:
            if switch:
              cert_row1_html += '<img class="img-fluid my-1" src="' + cert + '" alt="">'
            else:
              cert_row2_html += '<img class="img-fluid my-1" src="' + cert + '" alt="">'
            switch = not switch
          
          modified = modified.replace('southamerica', cert_row1_html)
          modified = modified.replace('bendover', cert_row2_html)
        except Exception as e:
          print(e)
          pass

        with open('pages/personnels/' + str(index) + '.html', 'w') as modified_file:
          modified_file.write(modified)

def main():
  generate_personnel_page()
  return

if __name__ == '__main__':
  main()