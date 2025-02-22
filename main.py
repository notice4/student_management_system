import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit,
    QTableWidget, QWidget, QStatusBar, QTableWidgetItem, QComboBox
)
from PyQt5.QtGui import QFont
from datetime import datetime
import sqlite3
from data_models import Student, Group, session, Subject, StudentSubject


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Management System")
        self.setGeometry(100, 100, 954, 723)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Labels
        self.title_label = QLabel("Student Management System", self)
        self.title_label.setFont(QFont("Arial", 30, QFont.Black))
        self.title_label.setGeometry(260, 10, 600, 42)

        self.student_id_label = QLabel("Student ID:", self)
        self.student_id_label.setGeometry(20, 120, 71, 16)

        self.first_name_label = QLabel("First Name:", self)
        self.first_name_label.setGeometry(20, 150, 71, 16)

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_label.setGeometry(20, 180, 71, 16)

        self.age_label = QLabel("Age:", self)
        self.age_label.setGeometry(40, 210, 31, 16)

        self.enrollment_date_label = QLabel("Enrollment Date:", self)
        self.enrollment_date_label.setGeometry(10, 240, 101, 16)

        self.group_id_label = QLabel("Group ID:", self)
        self.group_id_label.setGeometry(30, 290, 61, 16)

        self.select_subject_id_label = QLabel("Subject ID:", self)
        self.select_subject_id_label.setGeometry(30, 320, 65, 16)

        self.group_name_label = QLabel("Group Name:", self)
        self.group_name_label.setGeometry(20, 320, 81, 16)
        self.group_name_label.hide()

        self.group_description_label = QLabel("Group Description:", self)
        self.group_description_label.setGeometry(10, 350, 112, 16)
        self.group_description_label.hide()

        self.subject_id_label = QLabel("Subject ID:", self)
        self.subject_id_label.setGeometry(520, 120, 71, 16)
        self.subject_id_label.hide()

        self.subject_name_label = QLabel("Subject Name:", self)
        self.subject_name_label.setGeometry(510, 150, 91, 16)
        self.subject_name_label.hide()

        self.credit_number_label = QLabel("Credit Number:", self)
        self.credit_number_label.setGeometry(510, 180, 101, 16)
        self.credit_number_label.hide()

        self.subject_description_label = QLabel("Subject Description:", self)
        self.subject_description_label.setGeometry(490, 210, 131, 16)
        self.subject_description_label.hide()

        # Input Fields
        self.student_id_input = QLineEdit(self)
        self.student_id_input.setGeometry(130, 120, 351, 21)

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setGeometry(130, 150, 351, 21)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setGeometry(130, 180, 351, 21)

        self.age_input = QLineEdit(self)
        self.age_input.setGeometry(130, 210, 351, 21)

        self.enrollment_date_input = QLineEdit(self)
        self.enrollment_date_input.setGeometry(130, 240, 351, 21)

        self.group_id_input = QLineEdit(self)
        self.group_id_input.setGeometry(130, 290, 351, 21)

        self.select_subject_id_input = QLineEdit(self)
        self.select_subject_id_input.setGeometry(130, 319, 351, 21)

        self.group_name_input = QLineEdit(self)
        self.group_name_input.setGeometry(130, 320, 351, 21)
        self.group_name_input.hide()

        self.group_description_input = QLineEdit(self)
        self.group_description_input.setGeometry(130, 350, 351, 21)
        self.group_description_input.hide()

        self.subject_id_input = QLineEdit(self)
        self.subject_id_input.setGeometry(620, 120, 301, 21)
        self.subject_id_input.hide()

        self.subject_name_input = QLineEdit(self)
        self.subject_name_input.setGeometry(620, 150, 301, 21)
        self.subject_name_input.hide()

        self.credit_number_input = QLineEdit(self)
        self.credit_number_input.setGeometry(620, 180, 301, 21)
        self.credit_number_input.hide()

        self.subject_description_input = QLineEdit(self)
        self.subject_description_input.setGeometry(620, 210, 301, 21)
        self.subject_description_input.hide()

        # Buttons
        self.add_button = QPushButton("Add", self)
        self.add_button.setGeometry(540, 300, 101, 41)

        self.add_button.setStyleSheet('''
            background-color: green; 
            color: white; 
            border: 1px solid gray; 
            padding: 5px 10px; 
            border-radius: 5px;
            margin-right: 10px;
        ''')

        self.edit_button = QPushButton("Edit", self)
        self.edit_button.setGeometry(640, 300, 101, 41)

        self.edit_button.setStyleSheet('''
            background-color: yellow; 
            color: black; 
            border: 1px solid gray; 
            padding: 5px 10px; 
            border-radius: 5px;
            margin-right: 10px;
        ''')

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setGeometry(740, 300, 101, 41)

        self.delete_button.setStyleSheet('''
            background-color: red; 
            color: white; 
            border: 1px solid gray; 
            padding: 5px 10px; 
            border-radius: 5px;
            margin-right: 10px;
        ''')

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(840, 300, 101, 41)

        self.clear_button.setStyleSheet('''
            background-color: white; 
            color: black; 
            border: 1px solid gray; 
            padding: 5px 10px; 
            border-radius: 5px;
            margin-right: 10px;
        ''')

        self.show_students_database_button = QPushButton("Show Students Database", self)
        self.show_students_database_button.setGeometry(30, 60, 201, 41)

        self.show_groups_database_button = QPushButton("Show Groups Database", self)
        self.show_groups_database_button.setGeometry(250, 60, 201, 41)

        self.show_subjects_database_button = QPushButton("Show Subjects Database", self)
        self.show_subjects_database_button.setGeometry(470, 60, 201, 41)

        self.show_student_subjects_database_button = QPushButton("Show Student_Subjects Database", self)
        self.show_student_subjects_database_button.setGeometry(690, 60, 231, 41)

        # Table
        self.database_tables = QTableWidget(self)
        self.database_tables.setGeometry(10, 420, 931, 261)

        # Notifications
        self.notifications_label = QLabel("Notifications:", self)
        self.notifications_label.setGeometry(20, 386, 81, 16)

        self.show_notifications_label = QLabel("", self)
        self.show_notifications_label.setGeometry(110, 380, 811, 30)

        # Status Bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        # Dropdown for selecting entity
        self.object_type_combo = QComboBox(self)
        self.object_type_combo.setGeometry(20, 10, 150, 30)
        self.object_type_combo.addItem("Student")
        self.object_type_combo.addItem("Group")
        self.object_type_combo.addItem("Subject")
        self.object_type_combo.currentTextChanged.connect(self.update_ui_for_selected_object)

        # Connect signals
        self.add_button.clicked.connect(self.handle_button_click)
        self.edit_button.clicked.connect(self.handle_button_click)
        self.delete_button.clicked.connect(self.handle_button_click)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.show_students_database_button.clicked.connect(self.show_students_database)
        self.show_groups_database_button.clicked.connect(self.show_groups_database)
        self.show_subjects_database_button.clicked.connect(self.show_subjects_database)
        self.show_student_subjects_database_button.clicked.connect(self.show_student_subjects_database)

        # Database connection
        self.conn = sqlite3.connect("student_management_system.db")
        self.cursor = self.conn.cursor()

    def update_ui_for_selected_object(self, selected_object):
        # Update UI and show fields based on the selected type

        self.clear_inputs()

        if selected_object == "Student":
            self.show_student_fields()
        elif selected_object == "Group":
            self.show_group_fields()
        elif selected_object == "Subject":
            self.show_subject_fields()

    def show_student_fields(self):
        # Show only student related fields

        self.student_id_label.show()
        self.student_id_input.show()
        self.first_name_label.show()
        self.first_name_input.show()
        self.last_name_label.show()
        self.last_name_input.show()
        self.age_label.show()
        self.age_input.show()
        self.enrollment_date_label.show()
        self.enrollment_date_input.show()
        self.group_id_label.show()
        self.group_id_input.show()
        self.select_subject_id_label.show()
        self.select_subject_id_input.show()

        self.group_name_label.hide()
        self.group_name_input.hide()
        self.group_description_label.hide()
        self.group_description_input.hide()
        self.subject_id_label.hide()
        self.subject_id_input.hide()
        self.subject_name_label.hide()
        self.subject_name_input.hide()
        self.credit_number_label.hide()
        self.credit_number_input.hide()
        self.subject_description_label.hide()
        self.subject_description_input.hide()

    def show_group_fields(self):
        # Show only group related fields

        self.group_id_label.show()
        self.group_id_input.show()
        self.group_name_label.show()
        self.group_name_input.show()
        self.group_description_label.show()
        self.group_description_input.show()

        self.student_id_label.hide()
        self.student_id_input.hide()
        self.first_name_label.hide()
        self.first_name_input.hide()
        self.last_name_label.hide()
        self.last_name_input.hide()
        self.age_label.hide()
        self.age_input.hide()
        self.enrollment_date_label.hide()
        self.enrollment_date_input.hide()
        self.subject_id_label.hide()
        self.subject_id_input.hide()
        self.subject_name_label.hide()
        self.subject_name_input.hide()
        self.credit_number_label.hide()
        self.credit_number_input.hide()
        self.subject_description_label.hide()
        self.subject_description_input.hide()
        self.select_subject_id_label.hide()
        self.select_subject_id_input.hide()

    def show_subject_fields(self):
        # Show only subject related fields

        self.subject_id_label.show()
        self.subject_id_input.show()
        self.subject_name_label.show()
        self.subject_name_input.show()
        self.credit_number_label.show()
        self.credit_number_input.show()
        self.subject_description_label.show()
        self.subject_description_input.show()

        self.student_id_label.hide()
        self.student_id_input.hide()
        self.first_name_label.hide()
        self.first_name_input.hide()
        self.last_name_label.hide()
        self.last_name_input.hide()
        self.age_label.hide()
        self.age_input.hide()
        self.enrollment_date_label.hide()
        self.enrollment_date_input.hide()
        self.group_id_label.hide()
        self.group_id_input.hide()
        self.group_name_label.hide()
        self.group_name_input.hide()
        self.group_description_label.hide()
        self.group_description_input.hide()
        self.select_subject_id_label.hide()
        self.select_subject_id_input.hide()

    def handle_button_click(self):
        # Handle the add/edit/delete operation based on the selected object type
        selected_object = self.object_type_combo.currentText()
        sender_button = self.sender()  # Get the button that was clicked

        if sender_button == self.add_button:
            if selected_object == "Student":
                self.add_student()
            elif selected_object == "Group":
                self.add_group()
            elif selected_object == "Subject":
                self.add_subject()
        elif sender_button == self.edit_button:
            if selected_object == "Student":
                self.edit_student()
            elif selected_object == "Group":
                self.edit_group()
            elif selected_object == "Subject":
                self.edit_subject()
        elif sender_button == self.delete_button:
            if selected_object == "Student":
                self.delete_student()
            elif selected_object == "Group":
                self.delete_group()
            elif selected_object == "Subject":
                self.delete_subject()

    def add_student(self):
        # Add a student

        first_name = self.first_name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        age = self.age_input.text().strip()
        enrollment_date = self.enrollment_date_input.text().strip()
        group_id = self.group_id_input.text().strip()
        subject_id = self.select_subject_id_input.text().strip()

        if not first_name or not last_name or not age or not enrollment_date or not group_id or not subject_id:
            self.show_message("All fields must be filled!")
            return

        try:
            age = int(age)
            enrollment_date = datetime.strptime(enrollment_date, "%Y-%m-%d").date()
            group = session.query(Group).filter_by(id=group_id).first()
            subject = session.query(Subject).filter_by(id=subject_id).first()

            if not group:
                self.show_message("Invalid Group ID!")
                return
            if not subject:
                self.show_message("Invalid Subject ID!")
                return

            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                age=age,
                enrollment_date=enrollment_date,
                group_id=group_id,
                subject_id=subject_id
            )

            session.add(new_student)
            session.commit()

            self.show_message("Student added successfully!")
            self.auto_fill_student_subject_database()
            self.refresh_student_table()
            self.clear_inputs()

        except ValueError:
            self.show_message("Invalid age or date format!")
        except Exception as e:
            self.show_message(f"Error: {e}")

    def edit_student(self):
        # Edit a student

        student_id = self.student_id_input.text().strip()

        if not student_id:
            self.show_message("Please enter a Student ID to edit.")
            return

        student = session.query(Student).filter_by(id=student_id).first()

        if not student:
            self.show_message("Student not found!")
            return

        # Update student fields
        student.first_name = self.first_name_input.text().strip()
        student.last_name = self.last_name_input.text().strip()
        student.age = int(self.age_input.text().strip()) if self.age_input.text().strip().isdigit() else student.age
        try:
            student.enrollment_date = datetime.strptime(self.enrollment_date_input.text().strip(), "%Y-%m-%d").date()
        except ValueError:
            self.show_message("Invalid date format! Use YYYY-MM-DD.")
            return

        group_id = self.group_id_input.text().strip()
        subject_id = self.subject_id_input.text().strip()
        if group_id:
            group = session.query(Group).filter_by(id=group_id).first()
            if not group:
                self.show_message("Invalid Group ID!")
                return
        if subject_id:
            subject = session.query(Subject).filter_by(id=subject_id).first()
            if not subject:
                self.show_message("Invalid Subject ID!")
                return

            student.group_id = group_id
            student.subject_id = subject_id

        try:
            session.commit()
            self.show_message("Student details updated successfully!")
            self.refresh_student_table()
            self.clear_inputs()
        except Exception as e:
            self.show_message(f"Error updating student: {e}")

    def delete_student(self):
        # Delete a student

        student_id = self.student_id_input.text().strip()

        if not student_id:
            self.show_message("Please enter a Student ID to delete.")
            return

        student = session.query(Student).filter_by(id=student_id).first()

        if not student:
            self.show_message("Student not found!")
            return

        try:
            session.delete(student)
            session.commit()
            self.show_message("Student deleted successfully!")
            self.refresh_student_table()
            self.clear_inputs()
        except Exception as e:
            self.show_message(f"Error deleting student: {e}")

    def add_group(self):
        # Add a group

        name = self.group_name_input.text().strip()
        description = self.group_description_input.text().strip()

        if not name:
            self.show_message("Group name is required!")
            return

        new_group = Group(name=name, description=description)
        session.add(new_group)
        try:
            session.commit()
            self.show_message("Group added successfully!")
            self.refresh_groups_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error adding group: {e}")

    def edit_group(self):
        # Edit a group

        group_id = self.group_id_input.text().strip()
        if not group_id:
            self.show_message("Please enter a Group ID to edit.")
            return

        group = session.query(Group).filter_by(id=group_id).first()
        if not group:
            self.show_message("Group not found!")
            return

        group.name = self.group_name_input.text().strip() or group.name
        group.description = self.group_description_input.text().strip() or group.description

        try:
            session.commit()
            self.show_message("Group details updated successfully!")
            self.refresh_groups_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error updating group: {e}")

    def delete_group(self):
        # Delete a group

        group_id = self.group_id_input.text().strip()
        if not group_id:
            self.show_message("Please enter a Group ID to delete.")
            return

        group = session.query(Group).filter_by(id=group_id).first()
        if not group:
            self.show_message("Group not found!")
            return

        try:
            session.delete(group)
            session.commit()
            self.show_message("Group deleted successfully!")
            self.refresh_groups_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error deleting group: {e}")

    def add_subject(self):
        # Add a subject

        name = self.subject_name_input.text().strip()
        credits = self.credit_number_input.text().strip()
        description = self.subject_description_input.text().strip()

        if not name or not credits.isdigit():
            self.show_message("Subject name and valid credit number are required!")
            return

        new_subject = Subject(name=name, credits=int(credits), description=description)
        session.add(new_subject)
        try:
            session.commit()
            self.show_message("Subject added successfully!")
            self.refresh_subjects_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error adding subject: {e}")

    def edit_subject(self):
        # Edit a subject

        subject_id = self.subject_id_input.text().strip()
        if not subject_id:
            self.show_message("Please enter a Subject ID to edit.")
            return

        subject = session.query(Subject).filter_by(id=subject_id).first()
        if not subject:
            self.show_message("Subject not found!")
            return

        subject.name = self.subject_name_input.text().strip() or subject.name
        if self.credit_number_input.text().strip().isdigit():
            subject.credits = int(self.credit_number_input.text().strip())
        subject.description = self.subject_description_input.text().strip() or subject.description

        try:
            session.commit()
            self.show_message("Subject details updated successfully!")
            self.refresh_subjects_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error updating subject: {e}")

    def delete_subject(self):
        # Delete a subject

        subject_id = self.subject_id_input.text().strip()
        if not subject_id:
            self.show_message("Please enter a Subject ID to delete.")
            return

        subject = session.query(Subject).filter_by(id=subject_id).first()
        if not subject:
            self.show_message("Subject not found!")
            return

        try:
            session.delete(subject)
            session.commit()
            self.show_message("Subject deleted successfully!")
            self.refresh_subjects_table()
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            self.show_message(f"Error deleting subject: {e}")

    def auto_fill_student_subject_database(self):
        try:
            # Get the last student ID
            last_student = session.query(Student).order_by(Student.id.desc()).first()
            if last_student is None:
                self.show_message("No students found in the database.")
                return  # Exit if no students exist

            student_id = last_student.id

            # Get the subject ID from the input field
            subject_id_str = self.select_subject_id_input.text().strip()
            if not subject_id_str:
                self.show_message("No Subject id provided.")
                return

            try:
                subject_id = int(subject_id_str)
            except ValueError:
                self.show_message("Invalid Subject ID format.")
                return

            subject = session.query(Subject).filter_by(id=subject_id).first()

            if not subject:
                self.show_message("Invalid Subject ID.")
                return

            # Check if the association already exists (important!)
            existing_association = session.query(StudentSubject).filter_by(
                student_id=student_id, subject_id=subject_id
            ).first()
            if existing_association:
                self.show_message("This student is already assigned to this subject.")
                return

            auto_fill = StudentSubject(student_id=student_id, subject_id=subject_id)

            session.add(auto_fill)
            session.commit()
            self.show_message("Student assigned to subject successfully!")
            self.refresh_student_subjects_database()

        except Exception as e:
            session.rollback()  # Rollback on error
            self.show_message(f"Error: {e}")

    def clear_inputs(self):
        # Clear all input values

        self.student_id_input.clear()
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.age_input.clear()
        self.enrollment_date_input.clear()
        self.group_id_input.clear()
        self.group_name_input.clear()
        self.group_description_input.clear()
        self.subject_id_input.clear()
        self.subject_name_input.clear()
        self.credit_number_input.clear()
        self.subject_description_input.clear()
        self.select_subject_id_input.clear()

    def show_message(self, message):
        # Display a message to the user
        self.show_notifications_label.setText(message)

    def refresh_student_table(self):
        # Display the list of students

        students = session.query(Student).all()
        self.database_tables.setRowCount(len(students))
        self.database_tables.setColumnCount(7)
        self.database_tables.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Age", "Enrollment Date", "Group ID", "Subject ID"])

        for row, student in enumerate(students):
            self.database_tables.setItem(row, 0, QTableWidgetItem(str(student.id)))
            self.database_tables.setItem(row, 1, QTableWidgetItem(student.first_name))
            self.database_tables.setItem(row, 2, QTableWidgetItem(student.last_name))
            self.database_tables.setItem(row, 3, QTableWidgetItem(str(student.age)))
            self.database_tables.setItem(row, 4, QTableWidgetItem(student.enrollment_date.strftime("%Y-%m-%d")))
            self.database_tables.setItem(row, 5, QTableWidgetItem(str(student.group_id) if student.group_id else "None"))
            self.database_tables.setItem(row, 6, QTableWidgetItem(str(student.subject_id) if student.subject_id else "None"))

    def refresh_groups_table(self):
        # Display the list of groups

        groups = session.query(Group).all()
        self.database_tables.setRowCount((len(groups)))
        self.database_tables.setColumnCount(3)
        self.database_tables.setHorizontalHeaderLabels(["ID", "Name", "Description"])

        for row, group in enumerate(groups):
            self.database_tables.setItem(row, 0, QTableWidgetItem(str(group.id)))
            self.database_tables.setItem(row, 1, QTableWidgetItem(group.name))
            self.database_tables.setItem(row, 2, QTableWidgetItem(group.description))

    def refresh_subjects_table(self):
        # Display the list of subjects

        subjects = session.query(Subject).all()
        self.database_tables.setRowCount((len(subjects)))
        self.database_tables.setColumnCount(4)
        self.database_tables.setHorizontalHeaderLabels(["ID", "Name", "Credits", "Description"])

        for row, subject in enumerate(subjects):
            self.database_tables.setItem(row, 0, QTableWidgetItem(str(subject.id)))
            self.database_tables.setItem(row, 1, QTableWidgetItem(subject.name))
            self.database_tables.setItem(row, 2, QTableWidgetItem(str(subject.credits)))
            self.database_tables.setItem(row, 3, QTableWidgetItem(subject.description))

    def refresh_student_subjects_database(self):
        # Display the list of students and the subjects they are enrolled in

        # Get student-subject relations
        student_subjects = session.query(Student, Subject).join(StudentSubject, Student.id == StudentSubject.student_id).join(Subject, Subject.id == StudentSubject.subject_id).all()

        # Update the table to show student-subject data
        self.database_tables.setRowCount(len(student_subjects))
        self.database_tables.setColumnCount(4)  # 4 Columns
        self.database_tables.setHorizontalHeaderLabels(["Student ID", "Subject ID", "Student Name", "Subject Name"])

        for row, (student, subject) in enumerate(student_subjects):
            self.database_tables.setItem(row, 0, QTableWidgetItem(str(student.id)))
            self.database_tables.setItem(row, 1, QTableWidgetItem(str(subject.id)))
            self.database_tables.setItem(row, 2, QTableWidgetItem(f"{student.first_name} {student.last_name}"))
            self.database_tables.setItem(row, 3, QTableWidgetItem(subject.name))

    def show_students_database(self):
        self.refresh_student_table()

    def show_groups_database(self):
        self.refresh_groups_table()

    def show_subjects_database(self):
        self.refresh_subjects_table()

    def show_student_subjects_database(self):
        self.refresh_student_subjects_database()


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
