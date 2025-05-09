from extraction.pdf_reader import PdfReader
from template_creation.base_template_creator import BaseTemplateCreator


class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_data_extractor = PdfReader()

        self.template_creator = BaseTemplateCreator()


    def create_import_data(self):


        templates = self.create_templates()




    def create_templates(self):
        transactions_template = self.template_creator.__create_transactions_template()
        line_items_template = self.__create_line_items_template()
        global_template = self.__create_global_template()

        return transactions_template, line_items_template, global_template


    def __create_transactions_template(self):
        ...

    def __create_line_items_template(self):
        ...

    def __create_global_template(self):
        ...
