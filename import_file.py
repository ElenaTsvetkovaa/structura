import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import camelot
import pandas as pd

class PDFImportWindow:

    def __init__(self, root):
        self.root = root
        self.root.title('PDF Import Window')
        self.root.geometry('500x300')
        self.set_up_ui()
        self.drop_area = None

    def set_up_ui(self):

        # Main window look
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Drag and drop area
        self.drop_area = tk.Label(
            main_frame,
            text="Drag and Drop PDF File Here\nor\nClick to Browse",
            relief=tk.RIDGE,
            width=50,
            height=10,
            bg="#f0f0f0"
        )
        self.drop_area.pack(pady=20, fill=tk.BOTH, expand=True)

        self.drop_area.bind("<Button-1>", self.browse_file)
        self.drop_area.bind("<DragEnter>", self.on_drag_enter)
        self.drop_area.bind("<DragLeave>", self.on_drag_leave)
        self.drop_area.bind("<Drop>", self.on_drop)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")]
        )
        if file_path:
            self.process_pdf(file_path)

    def on_drag_enter(self, event):
        self.drop_area.config(bg="#e0e0ff")

    def on_drag_leave(self, event):
        self.drop_area.config(bg="#f0f0f0")

    def on_drop(self, event):
        self.drop_area.config(bg="#f0f0f0")
        file_path = event.data.strip()
        if file_path.endswith('.pdf'):
            self.process_pdf(file_path)
        else:
            messagebox.showerror("Error", "Please drop a PDF file")

    def process_pdf(self, file_path):
        try:
            self.status.config('Processing', fg='blue')
            self.root.update()
            #TODO



if __name__ == "__main__":
    root = tk.Tk()
    # app = PDFTableExtractor(root)
    root.mainloop()
