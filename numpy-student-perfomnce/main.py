import numpy as np


# ==========================================
# 1. CREATE STUDENT DATASET
# ==========================================

np.random.seed(42)

marks = np.random.randint(0, 101, size=(100, 5))

roll_no = np.arange(1, 101)

subjects = ["Python", "Math", "Statistics", "Database", "AI"]


# ==========================================
# 2. CREATE MISSING VALUES
# ==========================================

marks = marks.astype(float)

missing_rows = np.random.randint(0, 100, 10)
missing_cols = np.random.randint(0, 5, 10)

marks[missing_rows, missing_cols] = np.nan

print("Missing values before cleaning:",
      np.isnan(marks).sum())


# ==========================================
# 3. HANDLE MISSING VALUES
# ==========================================

for i in range(5):

    mean = np.nanmean(marks[:, i])

    marks[np.isnan(marks[:, i]), i] = mean

print("Missing values after cleaning:",
      np.isnan(marks).sum())


# ==========================================
# 4. DISPLAY STUDENT MARKS
# ==========================================

print("\n" + "=" * 70)
print("                    STUDENT MARKS")
print("=" * 70)

print(
    "Roll No | Python | Math | Statistics | Database | AI"
)

print("-" * 70)

for i in range(10):

    print(
        roll_no[i], "|",
        round(marks[i, 0], 2), "|",
        round(marks[i, 1], 2), "|",
        round(marks[i, 2], 2), "|",
        round(marks[i, 3], 2), "|",
        round(marks[i, 4], 2)
    )

print("... Showing first 10 students")


# ==========================================
# 5. TOTAL MARKS & PERCENTAGE
# ==========================================

total = np.sum(marks, axis=1)

percentage = (total / 500) * 100


# ==========================================
# 6. SUBJECT-WISE AVERAGE
# ==========================================

subject_avg = np.mean(marks, axis=0)

print("\nSubject Average:")

for i in range(5):

    print(
        subjects[i],
        ":",
        round(subject_avg[i], 2)
    )


# ==========================================
# 7. STRONGEST & WEAKEST SUBJECT
# ==========================================

highest_index = np.argmax(subject_avg)

lowest_index = np.argmin(subject_avg)

print("\nStrongest Subject:",
      subjects[highest_index])

print("Weakest Subject:",
      subjects[lowest_index])


# ==========================================
# 8. TOP 10 STUDENTS
# ==========================================

ranking = np.argsort(percentage)[::-1]

top_10 = ranking[:10]

print("\n" + "=" * 55)
print("                    TOP 10 STUDENTS")
print("=" * 55)

for rank, i in enumerate(top_10, start=1):

    print(
        rank,
        "→ Roll No:", roll_no[i],
        "| Percentage:", round(percentage[i], 2)
    )


# ==========================================
# 9. PASS / FAIL SYSTEM
# ==========================================

pass_marks = 33

passed = np.all(marks >= pass_marks, axis=1)

print("\nPass Students:", np.sum(passed))

print("Fail Students:", np.sum(~passed))


# ==========================================
# 10. GRADE SYSTEM
# ==========================================

grades = np.empty(100, dtype="<U2")

grades[percentage >= 90] = "A+"

grades[
    (percentage >= 80) &
    (percentage < 90)
] = "A"

grades[
    (percentage >= 70) &
    (percentage < 80)
] = "B"

grades[
    (percentage >= 60) &
    (percentage < 70)
] = "C"

grades[
    (percentage >= 50) &
    (percentage < 60)
] = "D"

grades[percentage < 50] = "F"


# ==========================================
# 11. CLASS STATISTICS
# ==========================================

class_average = np.mean(percentage)

highest_percentage = np.max(percentage)

lowest_percentage = np.min(percentage)

print("\n" + "=" * 50)
print("                CLASS STATISTICS")
print("=" * 50)

print(
    "Class Average:",
    round(class_average, 2),
    "%"
)

print(
    "Highest Percentage:",
    round(highest_percentage, 2),
    "%"
)

print(
    "Lowest Percentage:",
    round(lowest_percentage, 2),
    "%"
)


# ==========================================
# 12. SUBJECT-WISE HIGHEST & LOWEST
# ==========================================

highest_marks = np.max(marks, axis=0)

lowest_marks = np.min(marks, axis=0)

print("\nSubject-wise Highest & Lowest Marks:")

for i in range(5):

    print(
        subjects[i],
        "→ Highest:",
        round(highest_marks[i], 2),
        "| Lowest:",
        round(lowest_marks[i], 2)
    )


# ==========================================
# 13. SUBJECT-WISE PASS PERCENTAGE
# ==========================================

subject_pass_percentage = (
    np.mean(marks >= 33, axis=0) * 100
)

print("\nSubject Pass Percentage:")

for i in range(5):

    print(
        subjects[i],
        ":",
        round(subject_pass_percentage[i], 2),
        "%"
    )


# ==========================================
# 14. STUDENT SEARCH SYSTEM
# ==========================================

search_roll = 25

index = search_roll - 1

print("\n" + "=" * 45)
print("              STUDENT REPORT")
print("=" * 45)

print("Roll No:", roll_no[index])

for i in range(5):

    print(
        subjects[i],
        ":",
        round(marks[index, i], 2)
    )

print(
    "Total:",
    round(total[index], 2)
)

print(
    "Percentage:",
    round(percentage[index], 2),
    "%"
)

print(
    "Grade:",
    grades[index]
)

print(
    "Result:",
    "PASS" if passed[index] else "FAIL"
)

print("=" * 45)


# ==========================================
# 15. TOP 5 DETAILED REPORT
# ==========================================

print("\n" + "=" * 60)
print("                 TOP 5 STUDENTS")
print("=" * 60)

for rank, i in enumerate(top_10[:5], start=1):

    print(
        rank,
        "→ Roll No:",
        roll_no[i],
        "| Total:",
        round(total[i], 2),
        "| Percentage:",
        round(percentage[i], 2),
        "%",
        "| Grade:",
        grades[i]
    )


# ==========================================
# 16. FINAL DASHBOARD
# ==========================================

print("\n" + "=" * 60)
print("          STUDENT PERFORMANCE ANALYTICS")
print("=" * 60)

print("Total Students     :", len(roll_no))

print("Total Subjects     :", len(subjects))

print(
    "Class Average      :",
    round(class_average, 2),
    "%"
)

print(
    "Highest Percentage :",
    round(highest_percentage, 2),
    "%"
)

print(
    "Lowest Percentage  :",
    round(lowest_percentage, 2),
    "%"
)

print(
    "Pass Students      :",
    np.sum(passed)
)

print(
    "Fail Students      :",
    np.sum(~passed)
)

print(
    "Strongest Subject  :",
    subjects[highest_index]
)

print(
    "Weakest Subject    :",
    subjects[lowest_index]
)

print("=" * 60)


# ==========================================
# 17. SAVE CLEAN DATASET
# ==========================================

np.save("student_marks.npy", marks)

print("\nClean dataset saved successfully.")
