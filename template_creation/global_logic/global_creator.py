
from template_creation.defaults import TemplateGlobalInformationColumns
from template_creation.global_logic.global_handler import GlobalDataHandler
from template_creation.xml_df_creator import XmlDataframeCreator


class GlobalTemplateCreator(XmlDataframeCreator, GlobalDataHandler, TemplateGlobalInformationColumns):

    def __init__(self, xml_data):
        super().__init__(xml_data, self.get_all_columns())










