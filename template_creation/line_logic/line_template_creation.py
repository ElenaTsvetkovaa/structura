from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TemplateLineItemColumns, DefaultValues


class LineItemsTemplateCreator(BaseTemplateCreator, TemplateLineItemColumns):

    def header_mapping_dict(self):
        return {
            'Dauer': self.QUANTITY,
            'Stundensatz': self.UNIT_PRICE,
            'Summe': self.LINE_PRICE,
            'Anwalt': 'Honorar - ' + self.DESCRIPTION,
        }

    def extract_data_from_table(self):

        table = self.tables_dfs.copy()

        table.columns = table.iloc[0]
        table = table.drop(table.index[0])
        table = table[table['Anwalt'] != 'Gesamtsumme']

        table.rename(columns=self.header_mapping_dict(), inplace=True)
        # table.drop(columns=list(self.skipped_content_dict().keys()), inplace=True, errors='ignore')

        table.reset_index(drop=True, inplace=True)
        self.skipped_content_df = table

        return [table]


class LineItemsDataHandler(TemplateDataHandler, TemplateLineItemColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
        }



