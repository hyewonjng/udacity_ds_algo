def smallest_positive(in_list):    
    smallest_pos = None
    
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

    

# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
print(smallest_positive([-6, -9, -7]))
# Correct output: None
print(smallest_positive([]))


# This exercise uses a data structure that stores course information.
# The data structure format is:
#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }
course_per_semeter = {'spring2020':{'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
            'fall2020':{'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
            'spring2044':{'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},}
    }
def when_offered(courses, course):
    # TODO: Fill out the function here.
    # TODO: Return list of semesters here.
    res = []

    for term, cs_classes in courses.items():
        for cs_class in cs_classes:
            if cs_class == course:
                res.append(term)
    
    return res


def when_offered(course_per_semeter, course):
    semesters = []
    for semester in course_per_semeter:
        if course in course_per_semeter[semester]:
            semesters.append(semester)
    return semesters


print(when_offered(course_per_semeter, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']
print(when_offered(course_per_semeter, 'bio893'))
# Correct result: 
# []