from template_creation.base_template_creator import BaseTemplateCreator, TemplateDataHandler
from template_creation.defaults import TemplateLineItemColumns, DefaultValues


class LineItemsTemplateCreator(BaseTemplateCreator):
    pass


class LineItemsDataHandler(TemplateDataHandler, TemplateLineItemColumns, DefaultValues):

    def default_values_dict(self):
        return {
            self.COST_TYPE: self.default_cost_type,
            self.IS_HOURS: self.default_is_hours,
            self.DESCRIPTION: self.default_line_description,
            self.VAT_RATE: self.default_vat_rate
        }



