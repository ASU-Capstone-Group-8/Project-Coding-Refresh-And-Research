# Data Structures
# src/basics/data_structures.py

def data_structures_demo():
    # List (similar to Java's ArrayList)
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)

    # Tuple (immutable, similar to Java's List.of)
    my_tuple = (1, 2, 3)

    # Set (no duplicates, similar to Java's HashSet)
    my_set = {1, 2, 3, 4}
    my_set.add(5)

    # Dictionary (similar to Java's HashMap)
    my_dict = {"name": "Alice", "age": 30}
    my_dict["city"] = "Wonderland"

    return my_list, my_tuple, my_set, my_dict

def list_comprehension_demo():
    # Example of list comprehension (concise way to create lists)
    squares = [x * x for x in range(10)]
    return squares

if __name__ == "__main__":
    print(data_structures_demo())
    print(list_comprehension_demo())