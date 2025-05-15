from template_creation.defaults import TemplateGlobalInformationColumns, DefaultValues
from template_creation.template_handler import TemplateDataHandler


class GlobalDataHandler(TemplateDataHandler, TemplateGlobalInformationColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.PRICING_TYPE: self.default_pricing_type,
            self.INVOICE_TYPE: self.default_invoice_type,
            self.CURRENCY: self.default_currency,
        }

    def header_mapping_dict(self):
        return {}
