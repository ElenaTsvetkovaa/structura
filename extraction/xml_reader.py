import xml.etree.ElementTree as ET
import pandas as pd

class XMLReader:

    def __init__(self, xml_path):
        self.xml_path = xml_path

        self.tree = ET.parse(self.xml_path)
        self.root = self.tree.getroot()
        self.ns = {}

        self.xml_data = self.extract_xml_data()


    def __extract_namespaces(self):
        for event, element in self.root.iterparse(events=['start-ns']):
            prefix, uri = element
            self.ns[prefix] = uri

    def _tag_name(self, tag):
        if ':' in tag:
            prefix, local_el = tag.split(':')
            uri = self.ns[prefix]
            return f"{{{uri}}}{local_el}"
        else:
            return tag

    def extract_xml_data(self):
        rows = []

        for child in self.root:
            row_data = self.recurse(child)
            if isinstance(row_data, list):
                for rd in row_data:
                    rows.append(rd)
            else:
                rows.append(row_data)

        return pd.DataFrame(rows)

    def recurse(self, element):
        data = {}
        nested_data = []

        for child in element:
            if len(child):
                values_dict = self.recurse(child)
                if isinstance(values_dict, list):
                    nested_data.extend(values_dict)  # flatten if already a list
                else:
                    nested_data.append(values_dict)
            else:
                tag = self.cleaned_tag(child.tag)
                text = (child.text or '').strip()
                if text:
                    data[tag] = text

        if nested_data:
            return nested_data

        return data

    def cleaned_tag(self, tag):
        return tag.split('}')[-1]