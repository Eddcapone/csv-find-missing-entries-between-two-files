import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class ToolTip(object):
    """
    Create a tooltip for a given widget as the mouse goes on it.
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milliseconds, time to wait before showing the tooltip
        self.wraplength = 250   # pixels, max width of the tooltip text
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show(self):
        x, y, cx, cy = self.widget.bbox("insert")  # get the bounding box of the widget
        x += self.widget.winfo_rootx() + 20        # calculate to display tooltip 
        y += self.widget.winfo_rooty() + 20        # right below the widget
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hide(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

def get_first_column_rows(filepath):
    rows = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for row in reader:
                if row:  # Skip empty lines
                    rows.append(row)
    except Exception as e:
        raise e
    return rows

def compare_files():
    file1 = file1_path.get()
    file2 = file2_path.get()

    if not file1 or not file2:
        messagebox.showwarning("Warning", "Please select both CSV files.")
        return

    try:
        rows1 = get_first_column_rows(file1)
        rows2 = get_first_column_rows(file2)
        first_col_file2 = {row[0] for row in rows2}
        missing_rows = [row for row in rows1 if row[0] not in first_col_file2]

        with open("missing_entries.csv", mode="w", encoding="utf-8", newline="") as out:
            writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
            for row in missing_rows:
                writer.writerow(row)

        messagebox.showinfo("Results", 
            f"Comparison complete.\n\nFile1 rows: {len(rows1)}\nFile2 rows: {len(rows2)}\nMissing rows saved: {len(missing_rows)}\n\nSaved to 'missing_entries.csv'."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    return file_path

root = tk.Tk()
root.title("CSV First-Column Comparison Tool")
root.geometry("500x250")
root.grid_columnconfigure(1, weight=1)

file1_path = tk.StringVar()
label1 = tk.Label(root, text="Select Reference File (File 1):")
label1.grid(row=0, column=0, sticky='e', padx=(10, 2), pady=(20, 5))
info1 = tk.Label(root, text="?", font=("Arial", 12, "bold"), fg="blue", cursor="hand2")
info1.grid(row=0, column=1, sticky='w', padx=(0, 10))
ToolTip(info1, "Select the Reference File. This file contains the baseline data to compare against.")
entry1 = tk.Entry(root, textvariable=file1_path, width=40)
entry1.grid(row=1, column=0, columnspan=2, sticky='ew', padx=10)
btn1 = tk.Button(root, text="Browse...", command=lambda: file1_path.set(load_file()))
btn1.grid(row=1, column=2, padx=10)

file2_path = tk.StringVar()
label2 = tk.Label(root, text="Select Target File (File 2):")
label2.grid(row=2, column=0, sticky='e', padx=(10, 2), pady=(10, 5))
info2 = tk.Label(root, text="?", font=("Arial", 12, "bold"), fg="blue", cursor="hand2")
info2.grid(row=2, column=1, sticky='w', padx=(0, 10))
ToolTip(info2, "Select the Target File. This file will be checked for missing entries based on the Reference File.")
entry2 = tk.Entry(root, textvariable=file2_path, width=40)
entry2.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
btn2 = tk.Button(root, text="Browse...", command=lambda: file2_path.set(load_file()))
btn2.grid(row=3, column=2, padx=10)

compare_btn = tk.Button(root, text="Compare CSVs", command=compare_files)
compare_btn.grid(row=4, column=0, columnspan=3, pady=20, padx=10)

root.mainloop()
