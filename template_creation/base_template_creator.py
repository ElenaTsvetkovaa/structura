from abc import ABC, abstractmethod
from typing import List
import pandas as pd


class BaseTemplateCreator(ABC):

    def __init__(self, tables_dfs: List[pd.DataFrame],template_columns, template_name: str, template_data_handler):
        self.tables_dfs = tables_dfs
        self.template_columns = template_columns
        self.template_name = template_name
        self.template_data_handler = template_data_handler
        self.skipped_content_df: pd.DataFrame | None = None
        self.dataframe: pd.DataFrame | None = None

    @abstractmethod
    @property
    def template_type(self):
        pass

    def create_template(self):
        content = self.extract_data_from_table()
        if content:
            self.dataframe = pd.concat(content , ignore_index=True)
            self.dataframe = self.dataframe.reindex(columns=self.template_columns.get_all_columns())
        else:
            self.dataframe = pd.DataFrame([{col: pd.NA for col in self.template_columns.get_all_columns()}])

        empty_columns = [c for c in self.dataframe.columns if self.dataframe[c].isna().all()]
        if empty_columns:
            self.template_data_handler.populate_df_with_default_values(empty_columns, self.dataframe, self.skipped_content_df)

        return self.dataframe

    @abstractmethod
    def extract_data_from_table(self):
        ...


class TemplateDataHandler(ABC):

    @abstractmethod
    def default_values_dict(self) -> dict:
        ...

    def populate_df_with_default_values(self, empty_columns,df, skipped_lines_df):

        try:
            dict_defaults = self.default_values_dict()
            for c in empty_columns:
                if c in dict_defaults.keys():
                    df[c] = dict_defaults[c]
        except (KeyError, TypeError) as e:
            print(str(e))








