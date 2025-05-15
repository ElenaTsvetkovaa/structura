import pandas as pd
from template_creation.defaults import TransactionTemplateColumns
from template_creation.transactions_logic.transactions_handler import TransactionsDataHandler


class TransactionsCreator(TransactionsDataHandler, TransactionTemplateColumns):

    def __init__(self, pdf_data):
        self.pdf_data = pdf_data

        self.skipped_content_df: pd.DataFrame | None = None
        self.dataframe: pd.DataFrame = pd.DataFrame()
        self.skipped_map = self.skipped_content_dict()

    def extract_data_for_transactions(self):
        """
        Iterate through the extracted tables dataframes and if the table has the same
        columns names as those we have in the mapping dict,
        we found the correct table for this template and we extract the data
        """
        extracted_tables = []
        header_map = self.header_mapping_dict()
        header_keys = set(header_map.keys())

        for table in self.pdf_data:
            for idx, row in enumerate(table.itertuples(index=False, name=None)):
                if header_keys.issubset(set(row)):
                    table.columns = row
                    table = table.iloc[idx + 1:]

                    table.rename(columns=header_map, inplace=True)
                    table.reset_index(drop=True, inplace=True)
                    extracted_tables.append(table)
                    break
            else:
                self.skipped_content_df = table.rename(columns=self.skipped_map)

        return self.create_dataframe(extracted_tables)


    def create_dataframe(self, extracted_tables):
        if extracted_tables:
            self.dataframe = pd.concat(extracted_tables, ignore_index=True)

        if self.skipped_content_df is not None:
            self.merge_skipped_lines()

        self.check_for_empty_columns(self.dataframe)
        return self.dataframe

    def merge_skipped_lines(self):
        for old_col, new_col in self.skipped_map.items():
            if old_col in self.skipped_content_df.columns and new_col not in self.dataframe.columns:
                self.dataframe[new_col] = self.skipped_content_df[old_col]