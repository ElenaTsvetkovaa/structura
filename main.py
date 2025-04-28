import os
from file_importer import PdfFileImporter
from pdf_extraction import PdfExtractor
from template_creation.transactions_template_creator import TransactionsTemplateCreator,TransactionsDataHandler


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfFileImporter, transactions_data_handler, transactions_creator):

        self.extractor = extractor
        self.importer = importer

        # Transactions classes
        self.transactions_data_handler = transactions_data_handler
        self.transactions_creator = transactions_creator

    def run(self):
        try:
            file_path = self.importer.import_files()
            tables = self.extractor.extract_tables_from_pdf(file_path)

            file_name = os.path.basename(file_path)
            file_stem = os.path.splitext(file_name)[0]
            folder_path = os.path.dirname(file_path)

            template_creator = self.transactions_creator(tables, file_name, self.transactions_data_handler)
            df = template_creator.create_template()

            output_file = os.path.join(folder_path, f"{file_stem}_extracted.xlsx")
            df.to_excel(output_file, index=False)

            return output_file

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()
    transactions_data_handler = TransactionsDataHandler()

    app = PdfTableExtractor(extractor, importer, transactions_data_handler, TransactionsTemplateCreator)
    app.run()





