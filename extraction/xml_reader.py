import xml.etree.ElementTree as ET
import pandas as pd

class XMLReader:

    def __init__(self, xml_path):
        self.xml_path = xml_path

        self.tree = ET.parse(self.xml_path)
        self.root = self.tree.getroot()

        self.xml_data = self.extract_xml_data()

    def extract_xml_data(self):
        rows = self.parse_xml_to_dicts(self.root)

        return pd.DataFrame(rows)

    def parse_xml_to_dicts(self, root):
        results = []

        for child in root:
            entry = {}
            for subchild in child:
                if list(subchild):
                    nested = {}
                    for item in subchild:
                        key, value = self.__build_entry(subchild, item)
                        nested[key] = value
                    results.append(nested)
                else:
                    key, value = self.__build_entry(child, subchild)
                    entry[key] = value
            if entry:
                results.append(entry)

        return results

    def __clean_tag(self, raw_tag):
        return raw_tag.split('}')[-1]

    def __build_entry(self, parent_tag, element):
        parent_tag = self.__clean_tag(parent_tag)
        tag = self.__clean_tag(element.tag)
        key = f"{parent_tag}/{tag}"
        value = (element.text or '').strip()
        return key, value