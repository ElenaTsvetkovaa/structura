from template_creation.template_handler import TemplateDataHandler
from template_creation.defaults import TemplateLineItemColumns, DefaultValues


class LineItemsDataHandler(TemplateDataHandler, TemplateLineItemColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.DESCRIPTION: self.default_line_description,
            self.VAT_RATE: self.default_vat_rate
        }

    def header_mapping_dict(self):
        return {}

