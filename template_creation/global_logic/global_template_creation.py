
from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TemplateGlobalInformationColumns, DefaultValues


class GlobalTemplateCreator(BaseTemplateCreator):

    def extract_data_from_table(self):
        ...


class GlobalDataHandler(TemplateDataHandler, TemplateGlobalInformationColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.PRICING_TYPE: self.default_pricing_type,
            self.INVOICE_TYPE: self.default_invoice_type,
            self.CURRENCY: self.default_currency,
        }







