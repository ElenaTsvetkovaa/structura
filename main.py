import os

from file_importer import PdfFileImporter
from pdf_extraction import PdfExtractor
from template_manipulation.template_creator import TransactionsTemplateCreator


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfFileImporter, template_creator_cls):

        self.extractor = extractor
        self.importer = importer
        self.template_creator_cls = template_creator_cls

    def run(self):
        try:
            file_path = self.importer.import_files()
            tables = self.extractor.extract_tables_from_pdf(file_path)

            file_name = os.path.basename(file_path)
            file_stem = os.path.splitext(file_name)[0]
            folder_path = os.path.dirname(file_path)

            template_creator = self.template_creator_cls(file_name, tables)
            template_creator.extract_data_from_table()
            df = template_creator.create_template()

            output_file = os.path.join(folder_path, f"{file_stem}_extracted.xlsx")
            df.to_excel(output_file, index=False)

            return output_file

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()

    app = PdfTableExtractor(extractor, importer, TransactionsTemplateCreator)
    app.run()





