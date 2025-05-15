import pandas as pd

from template_creation.global_logic.global_creator import GlobalTemplateCreator
from template_creation.line_logic.line_item_creator import LineItemsCreator
from template_creation.transactions_logic.transactions_creator import TransactionsCreator


class TemplateCreator:

    def __init__(self, pdf_data, xml_data):
        self.pdf_data = pdf_data
        self.xml_data = xml_data

        self.content = []
        self.transactions_creator = TransactionsCreator(self.pdf_data)
        self.line_items_creator = LineItemsCreator(self.xml_data)
        self.global_creator = GlobalTemplateCreator(self.xml_data)

    def create_templates(self):
        transactions_template = self.__compose_transactions_dataframe()
        line_items_template = self.__compose_line_items_template()
        global_template = self.__compose_global_template()

        return transactions_template, line_items_template, global_template

    def __compose_transactions_dataframe(self):
        transactions_dataframe = self.transactions_creator.extract_data_for_transactions()
        return transactions_dataframe

    def __compose_line_items_template(self):
        line_items_dataframe = self.line_items_creator.create_dataframe_from_xml()
        return line_items_dataframe

    def __compose_global_template(self):
        global_dataframe = self.global_creator.create_dataframe_from_xml()
        return global_dataframe


