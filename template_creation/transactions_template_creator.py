from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TemplateColumns, DefaultValues


class TransactionsTemplateCreator(BaseTemplateCreator, TemplateColumns):

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

        return self.template_content


class TransactionsDataHandler(TemplateDataHandler, TemplateColumns, DefaultValues):

    def populate_df_with_default_values(self, empty_columns, df):
        mapper = {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.CURRENCY: self.default_currency
        }

        try:
            for c in empty_columns:
                if c in mapper.keys():
                    df[c] = mapper[c]
        except (KeyError, TypeError) as e:
            print(str(e))



