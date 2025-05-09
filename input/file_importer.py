import os

from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import filedialog, Label


class FileImporter:

    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("File Importer")
        self.root.geometry("500x300")

        self.pdf_path = None
        self.xml_path = None

        self._create_widgets()
        self._configure_drag_and_drop()

    def _create_widgets(self):
        self._create_drop_areas()
        self._create_buttons()

    def _create_drop_areas(self):
        self.pdf_drop_label = self.__initialize_drop_label('PDF')
        self.xml_drop_label = self.__initialize_drop_label('XML')

    def __initialize_drop_label(self, type):
        label = tk.Label(
            self.root,
            text=f"Drag & Drop {type} files\nor click 'Browse'",
            bg="lightgray",
            relief=tk.RIDGE,
            height=6
        )
        label.pack(fill=tk.X, padx=10, pady=10)
        return label

    def _configure_drag_and_drop(self):

        for lbl, extension, file_type in (
                (self.pdf_drop_label, '.pdf', 'pdf'),
                (self.xml_drop_label, '.xml', 'xml')
        ):
            lbl.drop_target_register(DND_FILES)
            lbl.dnd_bind("<<Drop>>", lambda e, x=extension, t=file_type: self.assign_file(self._extract_path(e), x, t))

    def _create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        buttons = {'Browse PDF': lambda: self._handle_browse("pdf", ".pdf", ("PDF files", "*.pdf")),
                    'Browse XML': lambda: self._handle_browse("xml", ".xml", ("XML files", "*.xml")),
                    'Import': self._handle_import}

        for btn_type, command in buttons.items():
            tk.Button(button_frame, text=btn_type, command=command).pack(side=tk.LEFT, padx=5)

    def _handle_drop(self, event, extension, file_type):
        path = self._extract_path(event)
        self.assign_file(path, extension, file_type)

    def _handle_browse(self, file_type, extension, allowed_files):
        path = filedialog.askopenfilename(filetypes=[allowed_files])
        self.assign_file(path, extension, file_type)

    def _handle_import(self):
        if self.xml_path and self.pdf_path:
            self.root.destroy()  # If the import is confirmed, the window closes

    def assign_file(self, path, extension, file_type):

        if self.__is_valid_file(path, extension):
            name = os.path.basename(path)
            if file_type == "pdf":
                self.pdf_path = path
                self.pdf_drop_label.config(text=name)
            elif file_type == "xml":
                self.xml_path = path
                self.xml_drop_label.config(text=name)

    @staticmethod
    def __is_valid_file(path, extension):
        return path.lower().endswith(extension) and os.path.exists(path)

    def _extract_path(self, event):
        raw_path = self.root.tk.splitlist(event.data)[0]
        return raw_path.strip("{}'\"")

    # def _update_listbox(self):
    #     """ Updates the Listbox to display the selected file. """
    #     self.file_list.delete(0, tk.END)
    #     if self.pdf_path:
    #         self.file_list.insert(tk.END, f"PDF: {self.pdf_path}")
    #     if self.xml_path:
    #         self.file_list.insert(tk.END, f"XML: {self.xml_path}")

    def import_file(self):
        self.root.mainloop()
        return {"pdf": self.pdf_path, "xml": self.xml_path}

    @property
    def file_name(self):
        return os.path.basename(self.pdf_path)