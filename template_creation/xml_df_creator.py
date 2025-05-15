import pandas as pd
from template_creation.template_handler import TemplateDataHandler


class XmlDataframeCreator(TemplateDataHandler):

    def __init__(self, xml_data, generic_columns):
        self.xml_data = xml_data
        self.header_mapping = self.header_mapping_dict()
        self.generic_columns = generic_columns
        self.dataframe = pd.DataFrame()

    def create_dataframe_from_xml(self):
        if self.xml_data is not None:
            self.dataframe = self.xml_data[self.header_mapping.keys()].copy()
            self.dataframe.rename(columns=self.header_mapping, inplace=True)

            return self.create_dataframe()

    def create_dataframe(self):
        self.dataframe = self.dataframe.reindex(columns=self.generic_columns)
        self.dataframe = self.check_for_empty_columns(self.dataframe)

        return self.dataframe
