import pandas as pd
from template_creation.defaults import TemplateLineItemColumns
from template_creation.line_logic.line_items_handler import LineItemsDataHandler


class LineItemsCreator(LineItemsDataHandler, TemplateLineItemColumns):

    def __init__(self, xml_data: pd.DataFrame):
        self.xml_data = xml_data
        self.dataframe: pd.DataFrame = pd.DataFrame()

    def extract_data_for_line_items(self):
        header_mapping = self.header_mapping_dict()

        self.dataframe = self.xml_data[header_mapping.keys()].copy()
        self.dataframe.rename(columns=header_mapping, inplace=True)

        return self.create_dataframe()

    def create_dataframe(self):
        self.dataframe = self.dataframe.reindex(columns=self.get_all_columns())
        self.dataframe = self.check_for_empty_columns(self.dataframe)

        return self.dataframe