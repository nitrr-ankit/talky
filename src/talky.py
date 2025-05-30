from ml import inference
import tkinter as tk

# Create and configure root window 
root = tk.Tk()
root.title("Talky- Your Personal Assistant")
root.minsize(200,400)
root.maxsize(500,800)
root.geometry("400x500+900+100")

# Functionalities
# Button for submititng text
def on_message():
    user_entry = text1.get("1.0", tk.END)
    reply = inference.process_query(user_query=user_entry)
    response_label.configure(text = reply)
    text1.delete("1.0", tk.END)
    text1.mark_set(tk.INSERT, "1.0")

# When enter key is pressed 
def handle_entry(event):
    on_message()

# Add info and image to the window
tk.Label(root, text = "Hi!! I am so happy to have you with me, let's talk").pack()
image = tk.PhotoImage(file = "./resources/test.gif")
tk.Label(root, image = image).pack()

# Add input text box for user msg
text1 = tk.Text(root, width=40, height=2)
text1.bind('<Return>', handle_entry)
text1.pack(pady=10)

tk.Button(root, text="Send", command = on_message).pack()

# Display new number in label
response_label = tk.Label(root, wraplength=300, justify=tk.LEFT)
response_label.pack()
         

# Render the window
root.mainloop()