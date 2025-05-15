import pandas as pd
from template_creation.defaults import TransactionTemplateColumns
from template_creation.transactions_logic.transactions_handler import TransactionsDataHandler


class TransactionsExtractor(TransactionsDataHandler, TransactionTemplateColumns):

    def __init__(self,pdf_data, template_name: str):
        self.pdf_data = pdf_data
        self.template_name = template_name

        self.skipped_content_df: pd.DataFrame | None = None
        self.dataframe: pd.DataFrame | None = None

    def extract_data_for_transactions(self):
        """
        Iterate through the extracted tables dataframes and if the table has the same
        columns names as those we have in the mapping dict,
        we found the correct table for this template and we extract the data
        """
        res = []
        header_map = self.header_mapping_dict()
        skipped_map = self.skipped_content_dict()
        header_keys = set(header_map.keys())

        for table in self.pdf_data:
            for idx, row in enumerate(table.itertuples(index=False, name=None)):
                if header_keys.issubset(set(row)):
                    table.columns = row
                    table = table.iloc[idx + 1:]

                    table.rename(columns=header_map, inplace=True)
                    table.reset_index(drop=True, inplace=True)
                    res.append(table)
                    break
            else:
                self.skipped_content_df = table.rename(columns=skipped_map)

        return self.dataframe, self.skipped_content_df


    def __create_template(self, content):
        if content:
            self.dataframe = pd.concat(content , ignore_index=True)
            self.dataframe = self.dataframe.loc[:, ~self.dataframe.columns.duplicated()]
            self.dataframe = self.dataframe.reindex(columns=self.template_columns.get_all_columns())
        else:
            self.dataframe = pd.DataFrame([{col: pd.NA for col in self.template_columns.get_all_columns()}])

        empty_columns = [c for c in self.dataframe.columns if self.dataframe[c].isna().all()]
        if empty_columns:
            self.template_data_handler.populate_df_with_default_values(empty_columns, self.dataframe, self.skipped_content_df)

        return self.dataframe




