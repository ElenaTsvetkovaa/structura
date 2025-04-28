import os
from file_importer import PdfFileImporter
from pdf_extraction import PdfExtractor
from template_creation.line_template_creation import LineItemsDataHandler, LineItemsTemplateCreator
from template_creation.transactions_template_creator import TransactionsTemplateCreator,TransactionsDataHandler

from template_creation.defaults import TemplateLineItemColumns, TransactionTemplateColumns


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfFileImporter, transactions_data_handler, transactions_creator,
                 line_items_data_handler, line_items_creator):

        self.extractor = extractor
        self.importer = importer

        # Transactions classes
        self.transactions_data_handler = transactions_data_handler
        self.transactions_creator = transactions_creator

        # Line Item classes
        self.line_items_data_handler = line_items_data_handler
        self.line_items_creator = line_items_creator

    def run(self):
        try:
            file_path = self.importer.import_files()
            tables = self.extractor.extract_tables_from_pdf(file_path)

            file_name = os.path.basename(file_path)
            file_stem = os.path.splitext(file_name)[0]
            original_folder_path = os.path.dirname(file_path)
            output_folder = os.path.join(original_folder_path, "output_files")
            os.makedirs(output_folder, exist_ok=True)

            # Transactions
            transactions_creator = self.transactions_creator(tables, TransactionTemplateColumns, file_name, self.transactions_data_handler)

            output_file = os.path.join(output_folder, f"{file_stem}_transactions.xlsx")
            trans_df.to_excel(output_file, index=False)

            # Line Items
            line_creator = self.line_items_creator(tables, TemplateLineItemColumns, file_name, self.line_items_data_handler)

            output_file = os.path.join(output_folder, f"{file_stem}_line_items.xlsx")
            line_df.to_excel(output_file, index=False)


            return output_file

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()
    transactions_data_handler = TransactionsDataHandler()
    line_items_data_handler = LineItemsDataHandler()

    app = PdfTableExtractor(extractor, importer, transactions_data_handler, TransactionsTemplateCreator,
                            line_items_data_handler, LineItemsTemplateCreator)
    app.run()





