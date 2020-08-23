import xmltodict
from dicttoxml import dicttoxml

with open('Exchange/DirectoryExport/TargetDictionary.xml') as fd:
    doc = xmltodict.parse(fd.read())

for bm in doc['TargetsDictionary']['Targets']['Target']:
    print(bm['@Name'], '|', bm['@Mnemonics'], bm['@Code'])


