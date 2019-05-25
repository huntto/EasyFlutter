#!/usr/bin/python
import json
import xml.sax
import sys
import os
import getopt

data = {}
class XmlToJsonHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.value = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "string":
            self.name = attributes["name"]

    def endElement(self, tag):
        if tag == "string":
            data[self.name] = self.value.strip('"')

    def characters(self, content):
        if self.CurrentData == "string":
            self.value = content

def usage():
    print(
"Usage:", sys.argv[0],
""" [option]
-i or --input：input strings.xml
-o or --output：output strings.json or strings.arb
-h or --help: print this message
"""
    )

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help","input=","output="])
except getopt.GetoptError:
    print("argv error,please input")

output_file = "strings.json"
input_file = "strings.xml"
for cmd, arg in opts:
    if cmd in ("-h", "--help"):
        usage()
        sys.exit()
    elif cmd in ("-o", "--output"):
        output_file = arg
    elif cmd in ("-i", "--input"):
        input_file = arg
    
if not os.path.exists(input_file) :
    usage()
    sys.exit()

if ( __name__ == "__main__"):
    print("converting...")
    
    parser = xml.sax.make_parser()

    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = XmlToJsonHandler()
    parser.setContentHandler(handler)
    parser.parse(input_file)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    print("done. output file:", output_file)
