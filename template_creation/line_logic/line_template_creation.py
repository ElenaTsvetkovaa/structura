from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TemplateLineItemColumns, DefaultValues


class LineItemsTemplateCreator(BaseTemplateCreator, TemplateLineItemColumns):

    def header_mapping_dict(self):
        return {
            'Dauer': self.QUANTITY,
            'Stundensatz': self.UNIT_PRICE,
            'Summe': self.LINE_PRICE,
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
            self.DESCRIPTION: self.default_line_description
        }

    def populate_df_with_default_values(self, empty_columns, df, skipped_lines_df):

        try:
            for c in empty_columns:
                if c == self.DESCRIPTION and skipped_lines_df is not None:
                    if 'Anwalt' in skipped_lines_df.columns:
                        people = skipped_lines_df['Anwalt'].astype(str).reset_index(drop=True)
                        df[c] = self.default_line_description + " - " + people
                    else:
                        df[c] = self.default_line_description
                elif c in mapper.keys():
                    df[c] = mapper[c]
        except (KeyError, TypeError) as e:
            print(str(e))



