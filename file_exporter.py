import os

class ExcelExporter:

    TRANSACTION_TEMPLATE_TYPE = 'transactions'
    LINE_ITEMS_TEMPLATE_TYPE = 'line_items'
    GLOBAL_TEMPLATE_TYPE = 'global'

    def __init__(self, transactions_df, line_items_df, global_df, file_path, file_name):
        self.transactions_df = transactions_df
        self.line_items_df = line_items_df
        self.global_df = global_df

        self.file_path = file_path
        self.file_name = file_name

    def create_local_folder(self):

        original_folder_path = os.path.dirname(self.file_path)
        output_folder = os.path.join(original_folder_path, f"{self.file_name}_templates")
        os.makedirs(output_folder, exist_ok=True)

        return output_folder

    def export_to_excel(self):
        output_folder = self.create_local_folder()

        # Export Transactions
        transactions_output_file = self.__export_file_to_excel(output_folder, self.transactions_df,
                                output_file_name=f'{self.file_name}_{self.TRANSACTION_TEMPLATE_TYPE}')

        line_items_output_file = self.__export_file_to_excel(output_folder, self.line_items_df,
                                 output_file_name=f'{self.file_name}_{self.LINE_ITEMS_TEMPLATE_TYPE}')

        global_output_file = self.__export_file_to_excel(output_folder, self.global_df,
                                 output_file_name=f'{self.file_name}_{self.GLOBAL_TEMPLATE_TYPE}')

        return transactions_output_file, line_items_output_file, global_output_file

    def __export_file_to_excel(self, output_folder, template_df, output_file_name):
        output_file = os.path.join(output_folder, f"{output_file_name}.xlsx")
        return template_df.to_excel(output_file, index=False)
