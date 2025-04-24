from file_importer import PdfFileImporter
from pdf_extraction import PDFReader, PdfExtractor


class PdfTableExtractor:

    def __init__(self, extractor: PdfExtractor, pdf_reader: PDFReader, importer: PdfFileImporter, progress_reporter):

        self.extractor = extractor
        self.pdf_reader = pdf_reader
        self.importer = importer
        self.progress_reporter = progress_reporter

    def _update_progress(self, value: int, message: str):
        if self.progress_reporter:
            self.progress_reporter.update_progress(value, message)

    def run(self):
        try:

            # file_path = r"C:\Users\oWorkers\Downloads\300247 11.10.2024.pdf"
            file_path = self.importer.import_files()

            tables = self.pdf_reader.extract_tables_from_pdf(file_path)
            self._update_progress(60, f"Extracted {len(tables)} tables")

            # Export tables
            output_path = "output.xlsx"  # Would come from user in actual impl
            self.extractor.save_tables_to_excel(tables, output_path)
            self._update_progress(100, "Export complete")

            return output_path

        except Exception as e:
            self._update_progress(0, f"Error: {str(e)}")
            raise


if __name__ == "__main__":
    extractor = PdfExtractor()
    importer = PdfFileImporter()
    progress_reporter = None
    reader = PDFReader()

    app = PdfTableExtractor(extractor, reader, importer, progress_reporter)
    app.run()





