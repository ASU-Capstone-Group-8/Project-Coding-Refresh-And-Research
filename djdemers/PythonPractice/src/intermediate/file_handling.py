# src/intermediate/file_handling.py

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def append_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)

if __name__ == "__main__":
    write_file("file_handling.txt", "This is a test content.")
    append_to_file("file_handling.txt", " Appending more content.\n")
    print(read_file("file_handling.txt"))
