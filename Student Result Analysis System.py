import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Ravi", "Sita", "Arun", "Priya", "Kiran"],
    "Python": [85, 72, 45, 92, 35],
    "DBMS": [78, 65, 55, 88, 40],
    "Statistics": [90, 80, 50, 95, 38]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["DBMS"] + df["Statistics"]
df["Percentage"] = df["Total"] / 3

def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)

df["Result"] = df.apply(
    lambda row: "Pass" if row["Python"] >= 40 and row["DBMS"] >= 40 and row["Statistics"] >= 40 else "Fail",
    axis=1
)

print("Student Result Analysis")
print(df)

topper = df.loc[df["Total"].idxmax()]
print("\nTopper:", topper["Name"])
print("Total Marks:", topper["Total"])

print("\nSubject-wise Average:")
print(df[["Python", "DBMS", "Statistics"]].mean())

plt.bar(df["Name"], df["Total"])
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Student Total Marks")
plt.show()
