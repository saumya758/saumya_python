def add_record():
    with open("vaccine.txt", "a") as f:
        name = input("Name: ")
        age = input("Age: ")
        dose = input("Dose Number: ")
        f.write(f"{name:15} {age:5} {dose:5}\n")

def show_records():
    print("\n--- All Records ---")
    with open("vaccine.txt", "r") as f:
        print(f.read())

add_record()
show_records()
