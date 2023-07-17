#!/usr/bin/env python3
"""
101-main.py
"""
'''
{
    _id: ObjectId("64b580819d6462aed1c07ee9"),
    name: 'Amy',
    topics: [
      { title: 'Algo', score: 9.1 },
      { title: 'C', score: 14.2 },
      { title: 'Python', score: 4.8 }
    ]
  }
'''
def top_students(mongo_collection):
    """
    Returns all the students sorted by averge score.
    """
    students = {}
    list_students = mongo_collection.find()
    for student in list_students:
        student["averageScore"] = 0
        for index, topic in enumerate(student["topics"]):
            students["count"] = index + 1
            if student["name"] in students:
                students[student["name"]] += topic["score"]
            else:
                students[student["name"]] = topic["score"]
                

    new = {student: score / students["count"] for student, score in students.items()}
    print(list(list_students))
    return new
