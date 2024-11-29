import customtkinter
from gemini_file import summarize_image

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="summarize", command=summarize_image)
button.pack(padx=20, pady=20)

app.mainloop()