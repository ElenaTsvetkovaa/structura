from typing import List
import pandas as pd
from template_manipulation.columns import TemplateColumns



class TransactionsTemplateCreator(TemplateColumns):

    def __init__(self, template_name: str, tables_dfs: List[pd.DataFrame]):
        self.template_name = template_name
        self.tables_dfs = tables_dfs
        self.template_content = []
        self.dataframe: pd.DataFrame | None = None

    def create_template(self):
        self.dataframe = pd.concat(self.template_content, ignore_index=True)
        self.dataframe = self.dataframe.reindex(columns=TemplateColumns.get_all_columns())
        return self.dataframe


    def header_mapping_dict(self):
        return {
            'Datum': self.DATE,
            'Bearbeiter': self.DISPLAY_NAME,
            'Tätigkeitsbeschreibung': self.DESCRIPTION,
            'Dauer': self.QUANTITY,
            'Stunden-Satz': self.HOURLY_RATE,
            'Summe': self.VOLUME,
        }


    def extract_data_from_table(self):

        for table in self.tables_dfs:

            if all(header in table.iloc[0].values for header in self.header_mapping_dict().keys()):
                table.columns = table.iloc[0]
                table = table.drop(0)

                table.rename(columns=self.header_mapping_dict(), inplace=True)

                table = table[table[self.DATE] != 'Gesamt']

                table.reset_index(drop=True, inplace=True)

                self.template_content.append(table)

        if self.template_content:
            self.create_template()












