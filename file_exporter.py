import os

class ExcelExporter:

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
        transactions_output_file = os.path.join(output_folder, f"{self.file_name}_transactions.xlsx")
        self.transactions_df.to_excel(transactions_output_file, index=False)

        # Export Line Items
        line_items_output_file = os.path.join(output_folder, f"{self.file_name}_line_items.xlsx")
        self.line_items_df.to_excel(line_items_output_file, index=False)

        global_output_file = os.path.join(output_folder, f'{self.file_name}_global.xlsx')
        self.global_df.to_excel(global_output_file, index=False)

        return transactions_output_file, line_items_output_file, global_output_file

