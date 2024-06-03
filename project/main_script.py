import os
import pandas as pd
import random

# Load the datasets
cs_courses_data = pd.read_csv('cs_courses_data.csv')
cs_rooms = pd.read_csv('cs_rooms.csv')
cs_doctors_courses = pd.read_csv('cs_doctors_courses.csv')

time_slots = ['08:30', '10:00', '11:30', '13:00', '14:30', '16:00']
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
used_slots = {}

def initialize_used_slots():
    for day in days:
        used_slots[day] = set()

def is_time_slot_available(day, time):
    return time not in used_slots[day]

def turn_csv_into_df(file):
    return pd.read_csv(file)

def student_signup(student_id, student_name):
    initialize_used_slots()
    filename = f"{student_id}.csv"
    student = {'student_id': student_id, 'student_name': student_name}
    if os.path.exists(filename):
        schedule_df = turn_csv_into_df(filename)
        print(f"Existing schedule loaded for student {student_id}")
        return schedule_df, student
    else:
        print(f"No existing schedule for student {student_id}. Registering new student.")
        return None, student

def choose_courses(titles):
    chosen_courses = []
    for course_title in titles:
        if course_title.lower() == 'done':
            break
        if course_title in cs_courses_data['Course Title'].values:
            if cs_courses_data.loc[cs_courses_data['Course Title'] == course_title, 'Capacity'].iloc[0] > 0:
                chosen_courses.append((course_title, 'Lecture'))
                chosen_courses.append((course_title, 'Section'))
                cs_courses_data.loc[cs_courses_data['Course Title'] == course_title, 'Capacity'] -= 1
    print(f"Chosen courses: {chosen_courses}")
    return chosen_courses

def generate_schedule_for_student(chosen_courses, student):
    initialize_used_slots()
    assignment = csp_backtracking({}, chosen_courses)
    if assignment is not None:
        schedule = []
        for (course, course_type), (day, time) in assignment.items():
            professor_row = cs_doctors_courses[cs_doctors_courses['Course'] == course]
            professor_name = professor_row['Name'].iloc[0] if not professor_row.empty else 'Unknown'
            room_number = random.choice(cs_rooms['Room Number'].tolist())
            schedule.append({
                'Course': course,
                'Type': course_type,
                'Professor': professor_name,
                'Room': room_number,
                'Day': day,
                'Time': time
            })
        schedule_df = pd.DataFrame(schedule)
        print(f"Generated schedule:\n{schedule_df}")
        save_schedule_to_csv(schedule_df, student)
        return schedule_df
    else:
        print("No valid schedule found.")
        return None

def csp_backtracking(assignment, courses):
    if len(assignment) == len(courses):
        return assignment

    course = select_unassigned_course(courses, assignment)
    random.shuffle(days)  # Shuffle days to add randomness
    random.shuffle(time_slots)  # Shuffle time slots to add randomness
    for day in days:
        for time in time_slots:
            if is_assignment_valid(course, day, time, assignment):
                assignment[course] = (day, time)
                used_slots[day].add(time)
                result = csp_backtracking(assignment, courses)
                if result is not None:
                    return result
                del assignment[course]
                used_slots[day].remove(time)
    return None

def select_unassigned_course(courses, assignment):
    for course in courses:
        if course not in assignment:
            return course
    return None

def is_assignment_valid(course, day, time, assignment):
    if time in used_slots[day]:
        return False
    daily_counts = {day: 0 for day in days}
    for assigned_course, (assigned_day, assigned_time) in assignment.items():
        if assigned_day == day:
            daily_counts[day] += 1
        if assigned_day == day and assigned_time == time:
            return False
        if daily_counts[day] >= 3:
            return False
    return True

def format_schedule(schedule):
    pivot_schedule = schedule.pivot_table(
        index='Time', columns='Day', values=['Course', 'Room', 'Professor'],
        aggfunc=lambda x: ' / '.join(x) if not all(val == 'Free Slot' for val in x) else 'Free Slot', fill_value='Free Slot'
    )

    for time in time_slots:
        if time not in pivot_schedule.index:
            for col in pivot_schedule.columns.levels[0]:
                pivot_schedule.loc[time, col] = 'Free Slot'

    pivot_schedule = pivot_schedule.reindex(index=time_slots,
                                            columns=pd.MultiIndex.from_product([['Course', 'Room', 'Professor'], days]),
                                            fill_value='Free Slot')

    combined_schedule = pivot_schedule.apply(
        lambda row: [
            f"{row['Course', day]} \n {row['Room', day]} \n {row['Professor', day]}" if row['Course', day] != 'Free Slot' else 'Free Slot'
            for day in days
        ], axis=1)

    formatted_schedule_df = pd.DataFrame(combined_schedule.tolist(), index=time_slots, columns=days)

    formatted_schedule_df = formatted_schedule_df.fillna('Free Slot')

    print(f"Formatted schedule:\n{formatted_schedule_df}")
    return formatted_schedule_df

def sort_schedule(schedule, column_name='Time', ascending=True):
    return schedule.sort_index(axis=1 if column_name in schedule.columns else 0, ascending=ascending)

def save_schedule_to_csv(schedule, student):
    filename = f"{student['student_id']}.csv"
    print(f"Saving schedule to {filename}")
    schedule.to_csv(filename, index=False)
    print(f"Schedule saved to {filename}")

def check_existing_schedule(student):
    filename = f"{student['student_id']}.csv"
    if os.path.exists(filename):
        schedule = pd.read_csv(filename)
        print("CSV content:\n", schedule)
        schedule['Time'] = pd.Categorical(schedule['Time'], categories=time_slots, ordered=True)
        schedule = schedule.sort_values('Time')
        formatted_schedule = schedule.pivot(index='Time', columns='Day', values='Course').fillna('Free Slot')
        print("Formatted schedule:\n", formatted_schedule)
        return formatted_schedule
    return pd.DataFrame(index=time_slots, columns=days).fillna('Free Slot')

def save_schedule_to_txt(schedule, student):
    filename = f"{student['student_id']}.txt"
    print(f"Saving schedule to {filename}")
    with open(filename, 'w') as file:
        file.write(f"Schedule for {student['student_name']} (ID: {student['student_id']})\n\n")
        file.write(schedule.to_string(header=True, index=True))
    print(f"Schedule saved to {filename}")
