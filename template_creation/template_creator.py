

class TemplateCreator:

    def __init__(self, pdf_data, xml_data):
        self.pdf_data = pdf_data
        self.xml_data = xml_data

        self.skipped_content_df = None


    def create_templates(self):
        transactions_template = self.__create_transactions_template()
        line_items_template = self.__create_line_items_template()
        global_template = self.__create_global_template()

        return transactions_template, line_items_template, global_template


    def __create_transactions_template(self):
        ...

    def __create_line_items_template(self):
        ...

    def __create_global_template(self):
        ...






