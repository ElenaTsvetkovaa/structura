from extraction.pdf_reader import PdfReader
from extraction.xml_reader import XMLReader
from template_creation.template_creator import TemplateCreator


class FileManager:

    def __init__(self, pdf_path, xml_path):
        self.pdf_path = pdf_path
        self.xml_path = xml_path
        self.pdf_data = None
        self.xml_data = None

        self.template_creator = TemplateCreator(self.pdf_data, self.xml_data)

    def create_import_data(self):
        if self.pdf_path is not None:
            self.pdf_data = PdfReader(self.pdf_path).extract_tables_from_pdf()

        if self.xml_path is not None:
            self.xml_data = XMLReader(self.xml_path).extract_xml_data()

        templates = self.template_creator.create_templates()

        return templates



