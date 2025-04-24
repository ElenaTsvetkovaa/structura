import os

from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import filedialog


class PdfFileImporter:

    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("PDF Importer")
        self.root.geometry("500x300")
        self.file_path = None
        self._setup_ui()

    def _setup_ui(self):
        # Drop area
        self.drop_label = tk.Label(
            self.root,
            text="Drag & Drop PDF files here\nor click 'Browse'",
            bg="lightgray",
            relief=tk.RIDGE,
            height=5
        )
        self.drop_label.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind("<<Drop>>", self._on_drop)

        # File list
        self.file_list = tk.Listbox(self.root, height=5)
        self.file_list.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=True)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        browse_btn = tk.Button(button_frame, text="Browse", command=self._browse_files)
        browse_btn.pack(side=tk.LEFT, padx=5)

        import_btn = tk.Button(button_frame, text="Import", command=self._confirm_import)
        import_btn.pack(side=tk.LEFT, padx=5)

    def _on_drop(self, event):
        # The event data returns a value like this -> {'C:\FILE_PATH'}
        # so I need to extract only the clean path
        path = self.root.tk.splitlist(event.data)[0].strip("{}").strip("'").strip('"')

        if path.lower().endswith(".pdf") and os.path.exists(path):
            self.file_path = path
            self._update_listbox()
        else:
            print(f"Invalid PDF file: {path}")

    def _browse_files(self):
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path and path.lower().endswith(".pdf"):
            self.file_path = path
            self._update_listbox()

    def _update_listbox(self):
        self.file_list.delete(0, tk.END)
        self.file_list.insert(tk.END, self.file_path)

    def _confirm_import(self):
        if self.file_path is not None:
            self.root.destroy()  # Close the window

    def import_files(self):
        self.root.mainloop()
        return self.file_path

