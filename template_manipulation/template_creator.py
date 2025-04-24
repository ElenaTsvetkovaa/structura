import pandas as pd

from template_manipulation.columns import TemplateColumns


class TemplateCreator(TemplateColumns):

    def __init__(self, template_name: str):
        self.template_name = template_name
        self.template_content = []
        self.dataframe: pd.DataFrame | None = None

    def create_template(self):
        self.dataframe = pd.DataFrame(self.template_content, columns=self.get_all_columns())
        return self.dataframe

    def insert_data_into_template(self, populated_df, empty_df):
        pass






















