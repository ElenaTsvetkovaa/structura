import os

from file_exporter import ExcelExporter
from file_importer import PdfFileImporter
from pdf_extraction import PdfExtractor
from template_creation.line_template_creation import LineItemsDataHandler, LineItemsTemplateCreator
from template_creation.transactions_template_creator import TransactionsTemplateCreator,TransactionsDataHandler

from template_creation.defaults import TemplateLineItemColumns, TransactionTemplateColumns


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfFileImporter, excel_exporter, transactions_data_handler,
                 transactions_creator, line_items_data_handler, line_items_creator):

        self.extractor = extractor
        self.importer = importer
        self.excel_exporter = excel_exporter

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

            # Transactions
            transactions_df = self.transactions_creator(tables, TransactionTemplateColumns, file_name, self.transactions_data_handler)

            # Line Items
            line_df = self.line_items_creator(tables, TemplateLineItemColumns, file_name, self.line_items_data_handler)

            self.excel_exporter.export_to_excel(transactions_df, line_df, file_path, file_name)

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()
    transactions_data_handler = TransactionsDataHandler()
    line_items_data_handler = LineItemsDataHandler()

    app = PdfTableExtractor(extractor, importer, ExcelExporter, transactions_data_handler, TransactionsTemplateCreator,
                            line_items_data_handler, LineItemsTemplateCreator)
    app.run()





