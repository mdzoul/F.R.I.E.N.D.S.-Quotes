"""Random quotes from different characters on F.R.I.E.N.D.S."""
from tkinter import Tk, Canvas, PhotoImage, Button
import requests


def get_quote():
    """Get quotes from F.R.I.E.N.D.S."""
    response = requests.get(url="https://friends-quotes-api.herokuapp.com/quotes/random")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    char = data["character"]
    canvas.itemconfig(quote_text, text=f"{quote}\n\n- {char}")


window = Tk()
window.title("Quotes from F.R.I.E.N.D.S.")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightbackground="white")
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 200,
                                text="Click on me",
                                width=250,
                                font=("Arial", 25, "bold"),
                                fill="black")
canvas.grid(row=0, column=0)

logo_img = PhotoImage(file="logo.png")
logo_btn = Button(image=logo_img,
                  highlightcolor="white",
                  highlightbackground="white",
                  command=get_quote)
logo_btn.grid(row=1, column=0)

window.mainloop()
