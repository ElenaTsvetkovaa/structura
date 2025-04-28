from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TransactionTemplateColumns, DefaultValues


class LineItemsTemplateCreator(BaseTemplateCreator, TransactionTemplateColumns):

    def header_mapping_dict(self):
        return {
            'Dauer': self.QUANTITY,
            'Stundensatz': self.HOURLY_RATE,
            'Summe': self.VOLUME,
        }

    def skipped_content_dict(self):
        return {
            'Anwalt': self.DISPLAY_NAME,
            'Position': self.SENIORITY
        }


    def extract_data_from_table(self):
        table = self.tables_dfs[0].copy()

        table.columns = table.iloc[0]
        table = table.drop(table.index[0])
        table = table[table['Anwalt'] != 'Gesamtsumme']

        self.skipped_content_df = table[list(self.skipped_content_dict().keys())]
        table.rename(columns=self.header_mapping_dict(), inplace=True)
        table.drop(columns=list(self.skipped_content_dict().keys()), inplace=True, errors='ignore')


        table.reset_index(drop=True, inplace=True)

        self.template_content.append(table)

        return self.template_content


class LineItemsDataHandler(TemplateDataHandler, TransactionTemplateColumns, DefaultValues):

    def populate_df_with_default_values(self, empty_columns, df, skipped_lines_df):
        mapper = {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.DESCRIPTION: self.default_line_description
        }

        try:
            for c in empty_columns:
                if c == self.DESCRIPTION and not skipped_lines_df.empty:
                    if 'Anwalt' in self.skipped_lines_df.columns:
                        people = skipped_lines_df['Anwalt'].astype(str).reset_index(drop=True)
                        df[c] = self.default_line_description + " - " + people
                    else:
                        df[c] = self.default_line_description
                elif c in mapper.keys():
                    df[c] = mapper[c]
        except (KeyError, TypeError) as e:
            print(str(e))



