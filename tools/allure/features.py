from enum import Enum



class AllureFeature(str, Enum):

    USERS = "Users"
    AUTHENTICATION = "Authentication"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"