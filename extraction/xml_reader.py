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


    def parse_xml_to_dicts(self, root):
        results = []

        for child in root:
            entry = {}
            child_tag = self.cleaned_tag(child.tag)
            for subchild in child:
                if list(subchild):
                    nested = {}
                    for item in subchild:
                        item_tag = self.cleaned_tag(item.tag)
                        key = f"{child_tag}/{item_tag}"
                        value = (item.text or '').strip()
                        nested[key] = value
                    results.append(nested)
                else:
                    subchild_tag = self.cleaned_tag(subchild.tag)
                    key = f"{child_tag}/{subchild_tag}"
                    value = (subchild.text or '').strip()
                    entry[key] = value
            if entry:
                results.append(entry)

        return results
    #
    # def recurse(self, element, data={}):
    #
    #     # Traverse each child element
    #     for child in element:
    #         if len(child):  # If the child has nested elements
    #             values_dict = self.recurse(child, data)
    #
    #             # Flatten and merge the nested data into the parent dictionary
    #             for key, value in values_dict.items():
    #                 # If the key already exists, append to a list of values
    #                 data[key] = value
    #         else:
    #             tag = self.cleaned_tag(child.tag)
    #             text = (child.text or '').strip()
    #             if text:
    #                 # Add the text under the tag name, ensure lists for multiple values
    #                 if tag in data:
    #                     if isinstance(data[tag], list):
    #                         data[tag].append(text)
    #                     else:
    #                         data[tag] = [data[tag], text]
    #                 else:
    #                     data[tag] = text
    #
    #     return data

    def cleaned_tag(self, tag):
        return tag.split('}')[-1]