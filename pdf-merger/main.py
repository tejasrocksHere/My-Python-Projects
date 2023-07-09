import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger


def select_files():
    file_paths = filedialog.askopenfilenames(title="Select PDF Files", filetypes=(("PDF Files", "*.pdf"),))
    if len(file_paths) > 0:
        for file_path in file_paths:
            listbox.insert(tk.END, file_path)


def merge_files():
    file_paths = listbox.get(0, tk.END)
    if len(file_paths) == 0:
        print("No files selected. Exiting.")
        return

    merger = PdfMerger()
    for file_path in file_paths:
        merger.append(file_path)

    output_file_path = filedialog.asksaveasfilename(title="Save Merged PDF", defaultextension=".pdf",
                                                    filetypes=(("PDF Files", "*.pdf"),))
    if output_file_path:
        merger.write(output_file_path)
        print("PDF files merged successfully!")
        message_label.config(text="PDF files merged successfully!", fg="green")
    else:
        print("No output file path provided. Exiting.")
        message_label.config(text="No output file path provided. Exiting.", fg="red")

    merger.close()


# Create the main window
root = tk.Tk()
root.title("PDF Merger")

# Create a Listbox to display selected files
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(padx=10, pady=10)

# Create the "Select Files" button
select_button = tk.Button(root, text="Select Files", command=select_files, bg="blue", fg="white")
select_button.pack(padx=10, pady=5)

# Create the "Merge Files" button
merge_button = tk.Button(root, text="Merge Files", command=merge_files, bg="green", fg="white")
merge_button.pack(padx=10, pady=5)

# Create a Label to display messages
message_label = tk.Label(root, text="", fg="black")
message_label.pack(padx=10, pady=5)

# Run the GUI
root.mainloop()
