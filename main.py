"""Kanye West will tell you what he thinks"""
import json
import random
from tkinter import Tk, Canvas, PhotoImage, Button
import requests


def get_quote():
    """Get quotes from Kanye West"""
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    quote = data["quote"]

    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
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

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img,
                      highlightcolor="white",
                      highlightbackground="white",
                      command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
