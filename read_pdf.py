import camelot
import pandas as pd
from typing import List, Optional


class PDFReader:

    @staticmethod
    def extract_tables_from_pdf(pdf_path: str) -> List[pd.DataFrame]:
        try:
            tables = camelot.read_pdf(pdf_path, pages='all')
            return [table.df for table in tables]
        except Exception as e:
            raise Exception(f"Failed to process PDF: {str(e)}")

    @staticmethod
    def save_tables_to_excel(tables: List[pd.DataFrame], output_path: str) -> None:
        with pd.ExcelWriter(output_path) as writer:
            for i, table in enumerate(tables):
                table.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)
















