from extraction.pdf_reader import PdfReader
from template_creation.template_creator import TemplateCreator


class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_data = None
        self.xml_data = None

        self.template_creator = TemplateCreator(self.pdf_data, self.xml_data)

    def create_import_data(self):
        self.pdf_data = PdfReader().extract_tables_from_pdf(self.file_path)
        self.xml_data = ...

        templates = self.template_creator.create_templates()

        return templates



