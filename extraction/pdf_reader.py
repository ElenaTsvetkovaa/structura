import camelot
import pandas as pd
from typing import List


class PdfReader:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_tables_from_pdf(self) -> List[pd.DataFrame]:
        try:
            tables = camelot.read_pdf(
                self.pdf_path,
                pages='all',
                flavor='network',
                strip_text='\n',
                split_text=True
            )
            print(f"Number of tables detected: {len(tables)}")

            # Print information about each table (page, position, etc.)
            for i, table in enumerate(tables):
                print(f"Table {i + 1}:")
                print(table.parsing_report)
            return [table.df for table in tables]
        except Exception as e:
            raise Exception(f"Failed to process PDF: {str(e)}")


