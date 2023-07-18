import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    text = text_entry.get("1.0", tk.END).strip()
    dest_lang = dest_lang_combobox.get()

    translator = Translator(service_urls=['translate.google.com'])
    translated = translator.translate(text, dest=dest_lang)
    translated_text.delete("1.0", tk.END)
    translated_text.insert(tk.END, translated.text)

    # Detect and display the detected source language
    detected_lang = translator.detect(text).lang
    detected_lang_name = LANGUAGES.get(detected_lang).capitalize()
    detected_label.config(text=f"Detected Source Language: {detected_lang_name}")

def clear_text():
    text_entry.delete("1.0", tk.END)
    translated_text.delete("1.0", tk.END)
    detected_label.config(text="Detected Source Language:")

# Create the main window
window = tk.Tk()
window.title("Language Translator")
window.configure(background="#f0f0f0")

# Set colors
bg_color = "#f0f0f0"
btn_color = "#4c84ff"
btn_hover_color = "#255edb"
text_color = "#000000"
label_color = "#333333"

# Create a frame for the input section
input_frame = tk.Frame(window, padx=10, pady=10, bg=bg_color)
input_frame.pack()

# Create the input text box
text_label = tk.Label(input_frame, text="Enter Text:", bg=bg_color, fg=label_color)
text_label.pack()
text_entry = tk.Text(input_frame, height=8)  # Increased height to 8
text_entry.pack()

# Create the destination language dropdown menu
dest_lang_label = tk.Label(input_frame, text="Destination Language:", bg=bg_color, fg=label_color)
dest_lang_label.pack()
dest_lang_combobox = ttk.Combobox(input_frame, state="readonly")
dest_lang_combobox['values'] = list(LANGUAGES.values())
dest_lang_combobox.pack()

# Create a frame for the translation section
translation_frame = tk.Frame(window, padx=10, pady=10, bg=bg_color)
translation_frame.pack()

# Create the translate button
translate_button = tk.Button(translation_frame, text="Translate", command=translate_text, bg=btn_color,
                             activebackground=btn_hover_color, fg=text_color, activeforeground=text_color,
                             relief=tk.RAISED, bd=0)
translate_button.pack(side=tk.LEFT)

# Create a separator
separator = tk.Frame(translation_frame, height=20, bg=bg_color)
separator.pack(side=tk.LEFT, padx=5)

# Create the clear button
clear_button = tk.Button(translation_frame, text="Clear", command=clear_text,
                         bg=btn_color, activebackground=btn_hover_color, fg=text_color,
                         activeforeground=text_color, relief=tk.RAISED, bd=0)
clear_button.pack(side=tk.LEFT)

# Create a frame for the output section
output_frame = tk.Frame(window, padx=10, pady=10, bg=bg_color)
output_frame.pack()

# Create the detected source language display
detected_label = tk.Label(output_frame, text="Detected Source Language:", bg=bg_color, fg=label_color)
detected_label.pack()

# Create the translated text display
translated_label = tk.Label(output_frame, text="Translated Text:", bg=bg_color, fg=label_color)
translated_label.pack()
translated_text = tk.Text(output_frame, height=8)  # Increased height to 8
translated_text.pack()

# Start the main loop
window.mainloop()
