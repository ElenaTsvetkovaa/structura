from abc import ABC, abstractmethod
from typing import List
import pandas as pd
from template_creation.defaults import TransactionTemplateColumns, ColumnsGetter


class BaseTemplateCreator(ABC):

    def __init__(self, tables_dfs: List[pd.DataFrame],template_columns, template_name: str, template_data_handler):
        self.tables_dfs = tables_dfs
        self.template_columns = template_columns
        self.template_name = template_name
        self.template_data_handler = template_data_handler
        self.template_content = []
        self.skipped_content_df: pd.DataFrame | None = None
        self.dataframe: pd.DataFrame | None = None

    def create_template(self):
        self.dataframe = pd.concat(self.template_content , ignore_index=True)
        self.dataframe = self.dataframe.reindex(columns=self.get_all_columns())

        empty_columns = [c for c in self.dataframe.columns if self.dataframe[c].isna().all()]
        if empty_columns:
            self.template_data_handler.populate_df_with_default_values(empty_columns, self.dataframe)

        return self.dataframe

    @abstractmethod
    def extract_data_from_table(self):
        ...


class TemplateDataHandler(ABC):

    @abstractmethod
    def populate_df_with_default_values(self, empty_columns,df, skipped_lines_df):
        ...








