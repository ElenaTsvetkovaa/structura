from template_creation.defaults import TemplateLineItemColumns
from template_creation.line_logic.line_items_handler import LineItemsDataHandler
from template_creation.xml_df_creator import XmlDataframeCreator


class LineItemsCreator(XmlDataframeCreator, LineItemsDataHandler, TemplateLineItemColumns):

    def __init__(self, xml_data):
        super().__init__(xml_data, self.get_all_columns())