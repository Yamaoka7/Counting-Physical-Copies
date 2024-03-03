def count_physical_books(library_locations):
    total_books = 0
    for location in library_locations:
        total_books += location.get_total_books()
    return total_books

# Example usage:
library_locations = [LibraryLocation('New York'), LibraryLocation('London'), LibraryLocation('Tokyo')]
total_books = count_physical_books(library_locations)
print("Total physical books:", total_books)
