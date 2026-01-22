#act1
test_row = {
    0: "a",
    1: "b",
    2: "c"
}

def create_row(names):
    # seats = ["Terry", "Rayan", "Cosmin"]
    length = len(names)
    result_row = {}
    for i in range(length):
        result_row[i] = names[i]
    return result_row

print(f"BEFORE: {test_row}")
test_row = create_row(["Terry", "Cosmin", "Rayyan"])
print(f"AFTER: {test_row}")


def get_student_at(seats, index):
    if index in seats:
        return seats[index]
    return None

def swap_seats(seats, index1, index2):
    index1, index2 = input("what seats should switch: ")
    index1 = seats.append(index2)
    index2 = seats.append(index1)

# def remove_student(seats, name):

#act2
