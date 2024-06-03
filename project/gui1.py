import main_script as test
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Scrollbar, Label
from pathlib import Path
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")
courses = []

def select_courses(title, student):
    if title not in courses:
        if title == 'done' or len(courses) >= 5:
            chosen_courses = test.choose_courses(courses)
            schedule = test.generate_schedule_for_student(chosen_courses, student)

            if schedule is not None:
                formatted_schedule = test.format_schedule(schedule)
                windoww.destroy()
                display_schedule(formatted_schedule)
            else:
                print("No valid schedule found.")
        else:
            if len(courses) < 5:
                courses.append(title)
                print("Courses selected so far:", courses)
    else:
        print(f"Course {title} already selected. Please choose a different course.")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_schedule(schedule):
    schedule_window = Tk()
    schedule_window.title("Generated Schedule")
    schedule_window.geometry("1200x1000")
    schedule_window.configure(bg='#FFFFFF')
    title_label = Label(schedule_window, text="Schedule Maker", font=("Helvetica", 48, "bold"), bg='#FFFFFF')
    title_label.pack(pady=10)

    frame = Frame(schedule_window, bg='#FFFFFF')
    frame.pack(pady=10)

    container = Frame(schedule_window)
    canvas = Canvas(container, bg='#FFFFFF')
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg='#FFFFFF')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    time_slots = ["08:30", "10:00", "11:30", "13:00", "14:30", "16:00"]
    display_time_slots = ["8:30 \nto\n 10:00", "10:00 \nto\n 11:30", "11:30 \nto\n 13:00", "13:00 \nto\n 14:30", "14:30 \nto\n 16:00", "16:00 \nto\n 17:30"]

    for i, day in enumerate([""] + days):
        day_label = Label(frame, text=day, font=("Helvetica", 24, "bold"), bg='#ADD8E6', width=15, height=2)
        day_label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

    for i, display_time_slot in enumerate(display_time_slots):
        time_label = Label(frame, text=display_time_slot, font=("Helvetica", 16, "bold"), bg='#d0e8f2', width=15, height=2)
        time_label.grid(row=i + 1, column=0, padx=5, pady=5, sticky='nsew')

        for j, day in enumerate(days):
            try:
                cell_text = schedule.loc[time_slots[i], day]
            except KeyError:
                cell_text = "Free Slot"
            cell_label = Label(frame, text=cell_text, font=("Helvetica", 18), bg='#ADD8E6', width=15, height=4, relief='ridge', anchor='center')
            cell_label.grid(row=i + 1, column=j + 1, padx=5, pady=5, sticky='nsew')

    for i in range(6):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(6):
        frame.grid_columnconfigure(i, weight=1)

    schedule_window.mainloop()

def run_gui1_script(student):
    global windoww
    windoww = Tk()
    windoww.geometry("1500x800")
    windoww.configure(bg="#FFFFFF")
    windoww.title("Course Selection")




    canvas = Canvas(windoww, bg="#FFFFFF", height=800, width=1500, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(751.0, 401.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    CSCI102 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI102", student), relief="flat")
    CSCI102.place(x=207.0, y=458.0, width=239.0, height=84.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    CSCI207 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI207", student), relief="flat")
    CSCI207.place(x=207.0, y=600.0, width=239.0, height=83.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    CSCI208 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI208", student), relief="flat")
    CSCI208.place(x=490.0, y=458.0, width=240.0, height=84.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_8.png"))
    CSCI112 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI112", student), relief="flat")
    CSCI112.place(x=490.0, y=600.0, width=240.0, height=83.0)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    CSCI322 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI322", student), relief="flat")
    CSCI322.place(x=774.0, y=458.0, width=239.0, height=84.0)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    CSCI205 = Button(image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI205", student), relief="flat")
    CSCI205.place(x=774.0, y=600.0, width=239.0, height=83.0)

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    CSCI217 = Button(image=button_image_7, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI217", student), relief="flat")
    CSCI217.place(x=207.0, y=316.0, width=239.0, height=84.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_4.png"))
    done_button = Button(image=button_image_8, borderwidth=0, highlightthickness=0, command=lambda: select_courses("done", student), relief="flat")
    done_button.place(x=691.0, y=720.0, width=117.0, height=42.0)

    button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
    MATH301i = Button(image=button_image_9, borderwidth=0, highlightthickness=0, command=lambda: select_courses("MATH301i", student), relief="flat")
    MATH301i.place(x=490.0, y=316.0, width=240.0, height=84.0)

    button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
    AIS201 = Button(image=button_image_10, borderwidth=0, highlightthickness=0, command=lambda: select_courses("AIS201", student), relief="flat")
    AIS201.place(x=774.0, y=316.0, width=239.0, height=84.0)

    button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
    AIS351 = Button(image=button_image_11, borderwidth=0, highlightthickness=0, command=lambda: select_courses("AIS351", student), relief="flat")
    AIS351.place(x=1051.0, y=458.0, width=239.0, height=84.0)

    button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
    MATH211 = Button(image=button_image_12, borderwidth=0, highlightthickness=0, command=lambda: select_courses("MATH211", student), relief="flat")
    MATH211.place(x=1051.0, y=600.0, width=239.0, height=83.0)

    button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
    CSCI311 = Button(image=button_image_13, borderwidth=0, highlightthickness=0, command=lambda: select_courses("CSCI311", student), relief="flat")
    CSCI311.place(x=1051.0, y=318.0, width=239.0, height=84.0)

    image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(749.0, 549.0, image=image_image_15)

    image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
    image_16 = canvas.create_image(749.2200927734375, 33.0, image=image_image_16)

    image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))
    image_17 = canvas.create_image(749.0, 186.7969970703125, image=image_image_17)

    windoww.resizable(False, False)
    windoww.mainloop()

if __name__ == "__main__":
    student = {student}
    run_gui1_script(student)
