import os

class ExcelExporter:

    def __init__(self, file_path, file_name, transactions_df, line_items_df, global_df,):
        self.file_path = file_path
        self.file_name = file_name

        self.template_dataframes = {
            'transactions': transactions_df,
            'line_items': line_items_df,
            'global': global_df
        }

    def export_to_excel(self):
        output_folder = self._create_local_folder()
        output_files = {}

        for key, df in self.template_dataframes.items():
            file_name = f'{self.file_name}_{key}'
            output_files[file_name] = self.__export_file_to_excel(output_folder, df, file_name)

        return tuple(output_files.values())

    def _create_local_folder(self):

        original_folder_path = os.path.dirname(self.file_path)
        output_folder = os.path.join(original_folder_path, f"{self.file_name}_templates")
        os.makedirs(output_folder, exist_ok=True)

        return output_folder

    @staticmethod
    def __export_file_to_excel(output_folder, template_df, output_file_name):
        output_file = os.path.join(output_folder, f"{output_file_name}.xlsx")
        return template_df.to_excel(output_file, index=False)
