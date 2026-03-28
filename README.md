
# Course Schedule Maker (Beta Version) 📅

**Authors:** Reem Hussin Mostafa Ibrahim, Mohanned Mahmoud, Mahmoud Essa.

## 📖 Project Overview
The project aims to develop an automated course scheduling system for students. This system allows students to sign up for courses, choose from available course titles, and generate a personalized, conflict-free schedule. 

By employing a **Constraint Satisfaction Problem (CSP)** backtracking algorithm, the system guarantees an efficient assignment of courses to available time slots while adhering to all defined constraints such as course capacities and avoiding overlapping time slots.

---

## ✨ Features & User Flow

1. **User Authentication (Input Page):** Students enter their Full Name and ID to log in. If a student ID already exists, the system loads their previously saved schedule. Otherwise, it registers them as a new student.
2. **Interactive Course Selection:** Users can choose up to a maximum of 5 courses from a GUI grid. The system verifies that the selected courses have available capacity before adding them.
3. **Automated Schedule Generation:** Once courses are selected (or the "Done" button is clicked), the system plots every course twice (once for the Lecture, once for the Section). It automatically assigns professors and randomly selects available rooms.
4. **Visual Schedule Output:** The final schedule is displayed in a formatted Tkinter grid showing the days (Sunday to Thursday) and time slots (08:30 to 17:30).
5. **Data Persistence:** Schedules are formatted and saved automatically to both `.csv` and `.txt` files named after the student's ID.

---

## 🧠 Theoretical Background: CSP & Backtracking
An essential subject in operations research and artificial intelligence is constraint satisfaction problems (CSPs). In CSPs, a problem is described by a set of variables, domains, and constraints that limit the values variables may have simultaneously.

This project utilizes a **Backtracking Algorithm**. This method involves assigning values to variables sequentially and backtracking whenever a constraint is violated. To ensure valid schedules, the algorithm enforces strict constraints:
* **No Overlaps:** A time slot cannot be used twice on the same day.
* **Daily Limits:** A student cannot be assigned more than 3 classes in a single day.

*(For further reading on CSP enhancements like Constraint Propagation and Minimum Remaining Values (MRV) heuristics, see the project's literature review references.)*

---

## 💻 System Architecture & Code Explanation

The codebase comprises several functions that work together in a modular structure:

### 1. `main.py` (Frontend Login)
* Sets up the main GUI window using Tkinter.
* Captures user input (Name and ID) and triggers the backend logic to either load an existing schedule or proceed to course selection.

### 2. `gui1.py` (Course Selection & Output Interface)
* **`run_gui1_script(student)`:** Renders the course selection interface with buttons for each available course.
* **`select_courses(title, student)`:** Manages selections, ensuring unique entries and enforcing the 5-course maximum.
* **`display_schedule(schedule)`:** Uses a Tkinter Canvas and Scrollbar to build a visual grid displaying the final schedule.

### 3. `main_script.py` (Backend Engine / `test.py` logic)
* **Data Loading:** Loads `cs_courses_data.csv`, `cs_rooms.csv`, and `cs_doctors_courses.csv` using Pandas DataFrames.
* **`csp_backtracking(assignment, courses)`:** The core algorithm that shuffles days and time slots to find a valid assignment of courses.
* **`is_assignment_valid(...)`:** Validates proposed assignments against constraints (overlapping times, max courses per day).
* **`format_schedule(schedule)`:** Uses Pandas `pivot_table` to format the raw generated schedule into a readable table with grouped Course, Room, and Professor data.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed along with the following required libraries:
```sh
pip install tk pandas random2 pathlib
```

### Running the Application
Ensure all asset folders (`/assets/frame0`, `/assets/frame1`) and CSV data files are in the correct directories.
Run the entry point file:
```sh
python main.py
```

---

## 📚 References
1. *An Improved Algorithm of CSP*
2. *ScienceDirect: Constraint Satisfaction Problem methodologies*
3. *Applications of CSPs (University of Southampton)*
