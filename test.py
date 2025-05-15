import xml.etree.ElementTree as ET
import pandas as pd


class XMLReader:

    def __init__(self, xml_path):
        self.xml_path = xml_path

        self.tree = ET.parse(self.xml_path)
        self.root = self.tree.getroot()
        self.ns = {}

        self.xml_data = self.extract_xml_data()

    def extract_xml_data(self):
        return self.parse_xml_to_dicts(self.root)


    def recurse(self, element):
        base_data = {}
        rows = []

        for child in element:
            tag = child.tag
            if len(child):
                nested = self.recurse(child)
                if isinstance(nested, list):
                    for entry in nested:
                        combined = base_data.copy()
                        combined.update(entry)
                        rows.append(combined)
                else:
                    base_data.update(nested)
            else:
                text = (child.text or '').strip()
                if text:
                    base_data[tag] = text

        if rows:
            # Merge base_data into each row if not already present
            final_rows = []
            for row in rows:
                merged = base_data.copy()
                merged.update(row)
                final_rows.append(merged)
            return final_rows
        else:
            return [base_data]

    def parse_xml_to_dicts(self, root):
        results = []

        for child in root:
            entry = {}
            for subchild in child:
                if list(subchild):
                    nested = {}
                    for item in subchild:
                        key = f"{child.tag}/{item.tag}"
                        value = item.text.strip()
                        nested[key] = value
                    results.append(nested)

                else:
                    # директен елемент без поддеца (напр. <Title>)
                    key = f"{child.tag}/{subchild.tag}"
                    value = subchild.text.strip()
                    entry[key] = value
            if entry:
                results.append(entry)

        return results


reader = XMLReader('C:\\Users\oWorkers\PycharmProjects\PdfAutomation\\xml.xml')

print(reader.extract_xml_data())
a=1






