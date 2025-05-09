import os

from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import filedialog


class PdfWindowImporter:

    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("PDF Importer")
        self.root.geometry("500x300")

        self.file_path = None
        self._create_widgets()
        self._configure_drag_and_drop()

    def _create_widgets(self):
        self._create_drop_area()
        self._create_file_list()
        self._create_buttons()

    def _create_drop_area(self):
        self.drop_label = tk.Label(
            self.root,
            text="Drag & Drop PDF files here\nor click 'Browse'",
            bg="lightgray",
            relief=tk.RIDGE,
            height=5
        )
        self.drop_label.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

    def _configure_drag_and_drop(self):
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind("<<Drop>>", self._handle_drop)

    def _create_file_list(self):
        self.file_list = tk.Listbox(self.root, height=5)
        self.file_list.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=True)

    def _create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        browse_btn = tk.Button(button_frame, text="Browse", command=self._handle_browse)
        browse_btn.pack(side=tk.LEFT, padx=5)

        import_btn = tk.Button(button_frame, text="Import", command=self._handle_import)
        import_btn.pack(side=tk.LEFT, padx=5)

    def _handle_drop(self, event):
        # The event data returns a value like this -> {'C:\FILE_PATH'}
        # so I need to extract only the clean path
        raw_path = self.root.tk.splitlist(event.data)[0]
        clean_path = raw_path.strip("{}'\"")

        if self.__is_valid_pdf(clean_path):
            self.file_path = clean_path
            self._update_listbox()
        else:
            print(f"Invalid PDF file: {clean_path}")

    def _handle_browse(self):
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.__is_valid_pdf(path):
            self.file_path = path
            self._update_listbox()

    def _handle_import(self):
        if self.file_path is not None:
            self.root.destroy()  # If the import is confirmed, the window closes

    @staticmethod
    def __is_valid_pdf(path):
        return path.lower().endswith(".pdf") and os.path.exists(path)

    def _update_listbox(self):
        """ Updates the Listbox to display the selected file. """
        self.file_list.delete(0, tk.END)
        self.file_list.insert(tk.END, self.file_path)

    def import_file(self):
        self.root.mainloop()
        return self.file_path

    @property
    def file_name(self):
        return os.path.basename(self.file_path)