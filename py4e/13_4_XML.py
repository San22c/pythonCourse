
import xml.etree.ElementTree as ET

#Triple comma is for big string
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

data2 = ''' <persons><person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
     </person>
     <person>
         <name>Sandra</name>
         <phone type="intl">
             +1 555 55 555
         </phone>
         <email hide="no"/>
          </person></persons>'''

tree = ET.fromstring(data)   #Make a tree xml
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

tree2 = ET.fromstring(data2)   #Make a tree xml
lst = tree2.findall('person')

for person in lst:
    print('Name ls:', person.find('name').text)
    print('Atrr ls:', person.find('email').get('hide'))
