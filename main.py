from file_manager import FileManager
from input.file_importer import FileImporter
from output.file_exporter import ExcelExporter


class InvoiceDataCreator:

    @staticmethod
    def run():
        file_importer = FileImporter()
        file_name = file_importer.file_name
        pdf_path, xml_path = file_importer.import_file()

        file_manager = FileManager(pdf_path, xml_path)
        templates = file_manager.create_import_data()

        exporter = ExcelExporter(pdf_path, file_name, *templates)
        exporter.export_to_excel()

if __name__ == "__main__":
    InvoiceDataCreator().run()






