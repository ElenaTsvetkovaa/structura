
from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TransactionTemplateColumns, DefaultValues


class TransactionsTemplateCreator(BaseTemplateCreator, TransactionTemplateColumns):

    def header_mapping_dict(self):
            return {
                'Datum': self.DATE,
                'RA': self.DISPLAY_NAME,
                'Beschreibung': self.DESCRIPTION,
                'Std.': self.QUANTITY,
                'Std. Satz': self.HOURLY_RATE,
                'Betrag': self.VOLUME,
            }

    def skipped_content_dict(self):
        return {
        }

    def extract_data_from_table(self):
        """
        Iterate through the extracted tables dataframes and if the table has the same
        columns names as those we have in the mapping dict,
        we found the correct table for this template and we extract the data
        """
        res= []
        header_found = False
        header_map = self.header_mapping_dict()
        header_keys = set(header_map.keys())

        for table in self.tables_dfs:
            for idx, row in table.iterrows():
                row_values = set(row.values)
                if header_keys.issubset(row_values):
                    table.columns = row
                    table = table.iloc[idx+1:]
                    header_found = True
                    break

            if header_found:
                table.rename(columns=self.header_mapping_dict(), inplace=True)
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



