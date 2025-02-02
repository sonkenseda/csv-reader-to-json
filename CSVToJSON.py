# Simple CSV to JSON converter
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os
import json

class CSVReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV File Reader")
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.entry_filename = tk.Entry(self.frame, width=40)
        self.entry_filename.pack(side=tk.LEFT, padx=5)

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_csv_file)
        self.browse_button.pack(side=tk.LEFT, padx=(5, 10))

        self.read_button = tk.Button(self.frame, text="Read CSV", command=self.read_csv)
        self.read_button.pack(side=tk.TOP, padx=(5, 10))

    def browse_csv_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file_path:
            file_name = os.path.basename(self.file_path)
            self.entry_filename.delete(0, tk.END)
            self.entry_filename.insert(0, file_name)

    def read_csv(self):
        
        if self.file_path:
            file_name = os.path.splitext(os.path.basename(self.file_path))[0]
            csv_file_name = f"{file_name}.json"

            # Create output folder
            output_folder = "output"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            json_file_path = os.path.join(output_folder, csv_file_name)
            with open(self.file_path, 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                rows = [row for row in csv_reader]

            with open(json_file_path, mode='w') as jsonfile:
                json.dump(rows, jsonfile, indent=4)

            messagebox.showinfo("Success", f"JSON file has been created: {json_file_path}")
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVReaderApp(root)
    root.mainloop()