import main_script
import gui1
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def execute_main():
    full_name = entry_1.get()
    user_id = entry_2.get()
    existing_schedule, student = main_script.student_signup(user_id, full_name)
    return existing_schedule, student

def on_next_button_click():
    existing_schedule, student = execute_main()
    if isinstance(existing_schedule, pd.DataFrame):
        window.destroy()  # Close the current window
        formatted_schedule = main_script.format_schedule(existing_schedule)
        gui1.display_schedule(formatted_schedule)
    else:
        window.destroy()  # Close the current window
        gui1.run_gui1_script(student)  # Pass student data

window = Tk()
window.geometry("1500x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=800, width=1500, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(1102.5745849609375, 268.9119873046875, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(1108.0003051757812, 98.0, image=image_image_2)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(1109.0, 437.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=897.0, y=413.0, width=424.0, height=46.0)

canvas.create_text(889.0, 382.0, anchor="nw", text="Your Full Name", fill="#A5A0A0", font=("Lato Regular", 16 * -1))

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(1109.0, 517.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=897.0, y=493.0, width=424.0, height=46.0)

canvas.create_text(889.0, 465.0, anchor="nw", text="Your ID", fill="#A5A0A0", font=("Lato Regular", 16 * -1))

button_next = Button(window, text="Log In", borderwidth=0, highlightthickness=0, relief="flat", command=on_next_button_click, bg="#009DDC", fg="white")
button_next.place(x=889.0, y=565.0, width=440.0, height=52.0)

canvas.create_text(1089.5, 579.0, anchor="nw", text="Log In", fill="#FFFFFF", font=("Lato Medium", 16 * -1))

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(353.0, 491.0, image=image_image_3)

window.resizable(False, False)
window.mainloop()
