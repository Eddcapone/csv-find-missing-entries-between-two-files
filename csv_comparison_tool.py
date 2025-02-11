import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def get_first_column_rows(filepath):
    """
    Reads a CSV file (handling quotes correctly) and returns a list of rows.
    Each 'row' is itself a list of columns from that line.
    """
    rows = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for row in reader:
                # Skip empty lines if any
                if row:
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
        # Read all rows from both files
        rows1 = get_first_column_rows(file1)
        rows2 = get_first_column_rows(file2)

        # Build a set of all first-column values in file2 for quick lookup
        first_col_file2 = {row[0] for row in rows2}

        # Find rows in file1 whose first column is NOT in file2
        missing_rows = [row for row in rows1 if row[0] not in first_col_file2]

        # Write the missing rows to a new CSV file
        with open("missing_entries.csv", mode="w", encoding="utf-8", newline="") as out:
            writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
            for row in missing_rows:
                writer.writerow(row)

        messagebox.showinfo("Results", 
            f"Comparison complete.\n\n"
            f"File1 rows: {len(rows1)}\n"
            f"File2 rows: {len(rows2)}\n"
            f"Missing rows saved: {len(missing_rows)}\n\n"
            f"Saved to 'missing_entries.csv'."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_file():
    """
    Opens a file dialog and returns the chosen CSV path.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    return file_path

# ------------------ Build the Tkinter GUI ------------------ #

root = tk.Tk()
root.title("CSV First-Column Comparison Tool")
root.geometry("450x200")

file1_path = tk.StringVar()
file2_path = tk.StringVar()

# File 1 controls
label1 = tk.Label(root, text="Select CSV File 1:")
label1.pack(pady=(10, 0))
entry1 = tk.Entry(root, textvariable=file1_path, width=50)
entry1.pack()
btn1 = tk.Button(root, text="Browse...", 
                 command=lambda: file1_path.set(load_file()))
btn1.pack(pady=(0, 5))

# File 2 controls
label2 = tk.Label(root, text="Select CSV File 2:")
label2.pack()
entry2 = tk.Entry(root, textvariable=file2_path, width=50)
entry2.pack()
btn2 = tk.Button(root, text="Browse...", 
                 command=lambda: file2_path.set(load_file()))
btn2.pack(pady=(0, 10))

# Compare button
compare_btn = tk.Button(root, text="Compare CSVs", command=compare_files)
compare_btn.pack()

root.mainloop()
