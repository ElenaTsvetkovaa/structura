from abc import ABC

class TemplateDataHandler(ABC):

    def header_mapping_dict(self):
        return {}

    def default_values_dict(self) -> dict:
        ...

    def check_for_empty_columns(self, dataframe):
        empty_columns = [c for c in dataframe.columns if dataframe[c].isna().all()]
        if empty_columns:
            self.populate_df_with_default_values(empty_columns, dataframe)

        return dataframe

    def populate_df_with_default_values(self, empty_columns, df):

        try:
            dict_defaults = self.default_values_dict()
            for c in empty_columns:
                if c in dict_defaults.keys():
                    df[c] = dict_defaults[c]
        except (KeyError, TypeError) as e:
            print(str(e))








