def validate_index(index, tasks):
    if 0 <= index < len(tasks):
        return True
    else:
        print("Invalid task index.")
        return False
