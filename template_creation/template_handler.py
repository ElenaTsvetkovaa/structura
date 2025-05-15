from abc import ABC, abstractmethod

class TemplateDataHandler(ABC):

    def header_mapping_dict(self):
        ...

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








