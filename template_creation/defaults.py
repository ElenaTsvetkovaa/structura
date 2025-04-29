from typing import List

class ColumnsGetter:

    @classmethod
    def get_all_columns(cls) -> List[str]:
        return [
            value for key, value in cls.__dict__.items()
            if not key.startswith("__") and isinstance(value, str)
        ]

class TemplateGlobalInformationColumns(ColumnsGetter):
    RECIPIENT = "Recipient"
    RECIPIENT_PARENT = "Recipient Parent"
    INVOICE_NUMBER = "Invoice Number"
    INVOICE_TYPE = "Invoice Type"
    PRICING_TYPE = "Pricing Type"
    RVG_DISPUTE_VALUE = "RVG - Dispute Value"
    RVG_FEE_RATE = "RVG - Fee Rate"
    CURRENCY = "Currency"
    TOTAL_VAT_EXCLUDED = "Total VAT Excluded"
    TOTAL_VAT_INCLUDED = "Total VAT Included"
    INVOICE_DATE = "Invoice Date"
    DUE_DATE = "Due Date"
    PERIOD_START = "Period Start"
    PERIOD_END = "Period End"
    RECIPIENT_DISPLAY_NAME = "Recipient Display Name"
    RECIPIENT_FIRST_NAME = "Recipient First Name"
    RECIPIENT_LAST_NAME = "Recipient Last Name"
    ISSUER_DISPLAY_NAME = "Issuer Display Name"
    ISSUER_FIRST_NAME = "Issuer First Name"
    ISSUER_LAST_NAME = "Issuer Last Name"
    REFERENCE_PO_NUMBER = "Reference / PO Number"
    IS_DRAFT = "Is Draft"
    DEBIT_INVOICE_NUMBER = "Debit Invoice Number"


class TemplateLineItemColumns(ColumnsGetter):
    DATE_START = "Date Start"
    DATE_END = "Date End"
    IS_HOURS = "Is Hours"
    CODE = "Code"
    DESCRIPTION = "Description"
    QUANTITY = "Quantity"
    UNIT_PRICE = "Unit Price"
    LINE_PRICE = "Line Price"
    VAT_RATE = "VAT Rate"
    COST_TYPE = "Cost Type"
    COST_CENTRE = "Cost Centre"
    PROJECT_1 = "Project 1"
    PROJECT_2 = "Project 2"
    PROJECT_3 = "Project 3"
    WORKSTREAM_1 = "Workstream 1"
    WORKSTREAM_2 = "Workstream 2"
    WORKSTREAM_3 = "Workstream 3"


class TransactionTemplateColumns(ColumnsGetter):

    PROJECT: str = "Project"
    WORKSTREAM: str = "Workstream"
    ORGANISATIONAL_UNIT: str = "Organisational Unit"
    COST_TYPE: str = "Cost Type"
    EXTERNAL_ID: str = "External ID"
    DATE: str = "Date"
    DISPLAY_NAME: str = "Display Name"
    FIRST_NAME: str = "First Name"
    LAST_NAME: str = "Last Name"
    SENIORITY: str = "Seniority"
    DESCRIPTION: str = "Description"
    VOLUME: str = "Volume"
    HOURLY_RATE: str = "Hourly Rate"
    QUANTITY: str = "Quantity"
    IS_HOURS: str = "Is Hours"
    EXPENSE_TOTAL_COST: str = "Expense Total Cost"
    CURRENCY: str = "Currency"


class DefaultValues:

    @property
    def default_cost_type(self):
        return 'Fees'

    @property
    def default_is_hours(self):
        return 'True'

    @property
    def default_currency(self):
        return 'EUR'

    @property
    def default_line_description(self):
        return 'Honorar - '

    @property
    def default_pricing_type(self):
        return 'Time and Material'

    @property
    def default_invoice_type(self):
        return 'Debit'

    @property
    def default_vat_rate(self):
        return 19
