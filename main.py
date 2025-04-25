from file_importer import PdfFileImporter
from pdf_extraction import PdfExtractor
from template_manipulation.template_creator import TransactionsTemplateCreator


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfFileImporter):

        self.extractor = extractor
        self.importer = importer


    def run(self):
        try:

            # file_path = r"C:\Users\oWorkers\Downloads\300247 11.10.2024.pdf"
            file_path = self.importer.import_files()

            tables = self.extractor.extract_tables_from_pdf(file_path)

            template_creator = TransactionsTemplateCreator(file_path.split('\\')[-1], tables)
            output_path = "output.xlsx"
            template_creator.extract_data_from_table()

            return output_path

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()

    app = PdfTableExtractor(extractor, importer)
    app.run()





