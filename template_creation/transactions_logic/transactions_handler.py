from template_creation.base_template_creator import TemplateDataHandler
from template_creation.defaults import TransactionTemplateColumns, DefaultValues


class TransactionsDataHandler(TemplateDataHandler, TransactionTemplateColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.CURRENCY: self.default_currency
        }

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
