print("==Welcome to my Score Tracker==")

student_scores={}
while True:
    student_name=input("Enter student name(if not then stop): ")
    if student_name == "stop":
        break
    student_score=int(input("Enter Score: "))
    student_scores.update({student_name:student_score})
print("=====================")
print("Student Score Tracker")
for student_name,student_score in student_scores.items():
    print(f"{student_name}:{student_score}")

print("==Thank You==")