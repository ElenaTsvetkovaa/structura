from typing import List


class TemplateColumns:

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

    @classmethod
    def get_all_columns(cls) -> List[str]:
        return [
            value for key, value in cls.__dict__.items()
            if not key.startswith("__") and isinstance(value, str)
        ]


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


