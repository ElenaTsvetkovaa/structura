

class TemplateColumns:

    PROJECT = 'Project'
    WORKSTREAM = 'Workstream'
    ORGANISATIONAL_UNIT = "Organisational Unit"
    COST_TYPE = "Cost Type"
    EXTERNAL_ID = "External ID"
    DATE = "Date"
    DISPLAY_NAME = "Display Name"
    FIRST_NAME = "First Name"
    LAST_NAME  = "Last Name"
    SENIORITY = "Seniority"
    DESCRIPTION = "Description"
    VOLUME = "Volume"
    HOURLY_RATE = "Hourly Rate"
    QUANTITY = "Quantity"
    IS_HOURS = "Is Hours"
    EXPENSE_TOTAL_COST = "Expense Total Cost"
    CURRENCY = "Currency"

    @classmethod
    def get_all_columns(cls) -> list:
        return [cls.PROJECT, cls.WORKSTREAM, cls.ORGANISATIONAL_UNIT,
                cls.COST_TYPE, cls.EXTERNAL_ID, cls.DATE,
                cls.DISPLAY_NAME, cls.FIRST_NAME, cls.LAST_NAME,
                cls.SENIORITY, cls.DESCRIPTION, cls.VOLUME,
                cls.HOURLY_RATE, cls.QUANTITY, cls.IS_HOURS,
                cls.EXPENSE_TOTAL_COST, cls.CURRENCY]

















