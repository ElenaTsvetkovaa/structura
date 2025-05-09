from file_manager import FileManager
from input.file_importer import FileImporter
from output.file_exporter import ExcelExporter


class InvoiceDataCreator:

    @staticmethod
    def run():
        pdf_importer = FileImporter()
        file_path = pdf_importer.import_file()

        file_manager = FileManager(file_path)
        file_manager.create_import_data()

        # exporter = ExcelExporter()
        # exporter.export_to_excel()

if __name__ == "__main__":
    InvoiceDataCreator().run()






