
from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TransactionTemplateColumns, DefaultValues


class TransactionsTemplateCreator(BaseTemplateCreator, TransactionTemplateColumns):

    def header_mapping_dict(self):
            return {
                'Datum': self.DATE,
                'Bearbeiter': self.DISPLAY_NAME,
                'Tätigkeitsbeschreibung': self.DESCRIPTION,
                'Dauer': self.QUANTITY,
                'Stunden-Satz': self.HOURLY_RATE,
                'Summe': self.VOLUME,
            }

    def skipped_content_dict(self):
        return {
            'Anwalt': self.DISPLAY_NAME,
            'Position': self.SENIORITY
        }

    def extract_data_from_table(self):
        res= []
        for table in self.tables_dfs:

            if all(header in table.iloc[0].values for header in self.header_mapping_dict().keys()):
                table.columns = table.iloc[0]
                table = table.drop(0)

                table.rename(columns=self.header_mapping_dict(), inplace=True)

                table = table[~table[self.DATE].isin(['Total', 'Gesamtsumme', 'Gesamt'])]

                table.reset_index(drop=True, inplace=True)

                res.append(table)
            else:
                self.skipped_content_df = table.rename(columns=self.skipped_content_dict())

        return res


class TransactionsDataHandler(TemplateDataHandler, TransactionTemplateColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.CURRENCY: self.default_currency
        }



