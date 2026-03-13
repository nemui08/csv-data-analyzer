import pandas as pd

df = pd.read_csv("students.csv")
df["average"] = (df["math"] + df["english"] + df["science"]) / 3

while True:

    print("\n=== CSV Data Analyzer ===")
    print("1: Show Data")
    print("2: Top Student")
    print("3: Subject Statistics")
    print("4: Filter Student")
    print("5: Exit")

    choice = input("Choose(1-5): ")

    if choice == "1":
        print(df)
    
    elif choice == "2":
        top = df.sort_values("average", ascending=False).head(1)
        print(top)
    
    elif choice == "3":
        stats = df[["math", "english", "science"]].mean()
        print("Average Score by Subject:")
        print(stats)

    elif choice == "4":

        try:
            score = int(input("Minimum math score: "))
            filtered = df[df["math"] >= score]
            print(filtered)
            
        except ValueError:
            print("Please enter a number")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")