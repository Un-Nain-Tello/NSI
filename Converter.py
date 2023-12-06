import tkinter as tk
import ttkbootstrap as ttk

def m2k():
   mile_input = entry_int.get()
   km_output = mile_input * 1.61
   output_string.set(km_output)



# window
window = ttk.Window(themename = 'journal')
window.title('Converter')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = m2k)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(
   master = window, 
   text = 'Output', 
   font = 'Calibri 24',
   textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()