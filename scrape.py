import json
import requests
from scipy.stats import norm
import pickle
import course

#Creating dictionary to store filter IDs
filters = {
    'Fall 2018': 22598,
    'Spring 2018': 22597,
    'Fall 2017': 22596,
    'Spring 2017': 22595,
    'Fall 2016': 22594,
    'Spring 2016': 22593,
    'Fall 2015': 22592,
    'Spring 2015': 22591,
    'Fall 2014': 22590,
    'Spring 2014': 22589,
    'Fall 2013': 22588,
    'Spring 2013': 22587
}


#parses JSON objects into a useful Course object 
def parse_class(json_class):
    return Course(
        json_class['title'],
        json_class['abbreviation'] + ' ' + json_class['course_number'],
        json_class['id'])


#Gets all the course information for each semester 
def get_courses_per_filter(filter_num):
    url = "https://www.berkeleytime.com/catalog/filter/?filters=" + str(filter_num)
    js = json.loads(requests.get(url).text)
    return set([parse_class(cls) for cls in js])
	

#Creating a set of all courses
all_courses = set()
for f in filters:
    print("Collecting " + f + "...")
    f = filters[f]
    all_courses = all_courses.union(get_courses_per_filter(f))


#Saving the course information locally
with open('courses', 'wb') as f:
    pickle.dump(all_courses, f)


#Loading the course information locally
# with open('courses', 'rb') as f:
#     all_courses = pickle.load(f)


#Fetches the standard deviation information for a course 
def get_std(course):
    response = requests.get("https://www.berkeleytime.com/grades/course_grades/" + str(course.id))
    response = json.loads(response.text)
    ids = [str(grade['grade_id']) for grade in response]

    response = requests.get("https://www.berkeleytime.com/grades/sections/" + '&'.join(ids))
    dist = json.loads(response.text)
    grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-"] 
    for grade in grades:
        low_percentile = dist[grade]['percentile_low']
        high_percentile = dist[grade]['percentile_high']

        low_SD = norm.ppf(low_percentile)
        high_SD = norm.ppf(high_percentile)

        print(f"To get a grade of {grade}, you must be between {low_SD} and {high_SD} SD.")

#Gets the
def get_grade_dist():
    course_abbrev = input("Enter Course Abbreviation (e.g. COMPSCI 70):")
    for course in all_courses:
        if course.abbrev == course_abbrev:
            get_std(course)
            return

get_grade_dist()
