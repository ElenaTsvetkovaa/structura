import camelot
import pandas as pd
from typing import List


class PDFReader:

    @staticmethod
    def extract_tables_from_pdf(pdf_path: str) -> List[pd.DataFrame]:
        try:
            tables = camelot.read_pdf(
                pdf_path,
                pages='all',
                flavor='lattice',
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

class PdfExtractor:

    @staticmethod
    def save_tables_to_excel(tables: List[pd.DataFrame], output_path: str, in_single_sheet=True) -> None:

        if in_single_sheet and len(tables) > 1:
            combined = pd.concat(tables)
            combined.to_excel(output_path, index=False)
        else:
            with pd.ExcelWriter(output_path) as writer:
                for i, table in enumerate(tables):
                    table.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)
















