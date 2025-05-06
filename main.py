import os
from enum import global_str

from file_exporter import ExcelExporter
from file_importer import PdfWindowImporter
from pdf_extraction import PdfExtractor
from template_creation.defaults import TemplateLineItemColumns, TransactionTemplateColumns, \
    TemplateGlobalInformationColumns
from template_creation.global_ltemplate_creation import GlobalDataHandler, GlobalTemplateCreator
from template_creation.line_logic.line_template_creation import LineItemsDataHandler, LineItemsTemplateCreator
from template_creation.transactions_logic.transactions_template_creator import TransactionsDataHandler, \
    TransactionsTemplateCreator


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, importer: PdfWindowImporter, excel_exporter, transactions_data_handler,
                 transactions_creator, line_items_data_handler, line_items_creator, global_data_handler, global_creator):

        self.extractor = extractor
        self.importer = importer
        self.excel_exporter = excel_exporter

        # Transactions classes
        self.transactions_data_handler = transactions_data_handler
        self.transactions_creator = transactions_creator

        # Line Item classes
        self.line_items_data_handler = line_items_data_handler
        self.line_items_creator = line_items_creator

        # Global
        self.global_data_handler = global_data_handler
        self.global_creator = global_creator

    def run(self):
        try:
            file_path = self.importer.import_files()
            tables = self.extractor.extract_tables_from_pdf(file_path)
            file_name = os.path.basename(file_path)

            # Transactions
            trans_creator = self.transactions_creator(tables, TransactionTemplateColumns, file_name, self.transactions_data_handler)
            transactions_df = trans_creator.create_template()

            # Line Items
            line_creator = self.line_items_creator(trans_creator.skipped_content_df, TemplateLineItemColumns, file_name, self.line_items_data_handler)
            line_df = line_creator.create_template()

            # Global
            global_creator = self.global_creator(tables, TemplateGlobalInformationColumns, file_name, self.global_data_handler)
            global_df = global_creator.create_template()

            exporter = self.excel_exporter(file_path, file_name, transactions_df, line_df, global_df, )
            exporter.export_to_excel()

        except Exception as e:
            raise e


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfWindowImporter()
    transactions_data_handler = TransactionsDataHandler()
    line_items_data_handler = LineItemsDataHandler()
    global_data_handler = GlobalDataHandler()

    app = PdfTableExtractor(extractor, importer, ExcelExporter, transactions_data_handler, TransactionsTemplateCreator,
                            line_items_data_handler, LineItemsTemplateCreator, global_data_handler, GlobalTemplateCreator)
    app.run()





