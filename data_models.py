from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///student_management_system.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Group(Base):
    # One-to-Many relationship
    # In one group could be many students (more than 1)

    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    students = relationship("Student", back_populates="group")


class Subject(Base):
    # Many-to-Many relationship
    # Many students could choose many subjects

    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    students = relationship("Student", secondary="student_subjects", back_populates="subjects")


class Student(Base):
    # Many-to-Many relationships
    # Many students could choose many subjects and each subject include many students

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    enrollment_date = Column(Date, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    group = relationship("Group", back_populates="students")
    subjects = relationship("Subject", secondary="student_subjects", back_populates="students")


class StudentSubject(Base):
    __tablename__ = 'student_subjects'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)


Base.metadata.create_all(engine)
