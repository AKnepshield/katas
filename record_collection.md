RecordCollection Kata  
[python]

Here's a kata centered around creating a `RecordCollection` class that manages a collection of music records. The class will allow you to add records, retrieve information about records, and perform some basic operations on the collection.

### Kata: RecordCollection Class

**Objective:**
Create a Python class called `RecordCollection` that manages a collection of records. Each record will have a title and an artist.

### Requirements:

1. **Instantiation:**

   - The `RecordCollection` class should be instantiated without any parameters, and it should initialize an empty collection.

2. **Add Records:**

   - Implement a method `add_record(title, artist)` to add a record to the collection. Each record should be stored as a dictionary with keys `'title'` and `'artist'`.

3. **Retrieve Records:**

   - Implement a method `get_records()` that returns a list of all records in the collection.
   - Implement a method `get_record(title)` that returns the record with the specified title. If the record is not found, it should return `None`.

4. **Remove Records:**

   - Implement a method `remove_record(title)` that removes the record with the specified title from the collection. If the record is not found, it should do nothing.

5. **Count Records:**

   - Implement a method `count_records()` that returns the total number of records in the collection.

6. **List Artists:**
   - Implement a method `list_artists()` that returns a list of all unique artists in the collection.

### Example Usage:

```python
# Instantiating the class
collection = RecordCollection()

# Adding records
collection.add_record("Hear Nothing See Nothing Say Nothing", "Discharge")
collection.add_record("Ace of Spades", "Motörhead")
collection.add_record("Victims of a Bomb Raid", "Anti-Cimex")

# Retrieving records
print(collection.get_records())
# Output: [{'title': 'Hear Nothing See Nothing Say Nothing', 'artist': 'Discharge'}, {'title': 'Ace of Spades', 'artist': 'Motörhead'}, {'title': 'Victims of a Bomb Raid', 'artist': 'Anti-Cimex'}]

# Getting a specific record
print(collection.get_record("Ace of Spades"))
# Output: {'title': 'Ace of Spades', 'artist': 'Motörhead'}

# Removing a record
collection.remove_record("Ace of Spades")

# Counting records
print(collection.count_records())  # Output: 2

# Listing artists
print(collection.list_artists())  # Output: ['Discharge', 'Anti-Cimex']
```

### Task Steps:

1. Define the `RecordCollection` class.
2. Implement the constructor (`__init__`) to initialize an empty collection.
3. Implement the `add_record(title, artist)` method to add records to the collection.
4. Implement the `get_records()` method to retrieve all records.
5. Implement the `get_record(title)` method to retrieve a specific record by title.
6. Implement the `remove_record(title)` method to remove a record by title.
7. Implement the `count_records()` method to return the total number of records.
8. Implement the `list_artists()` method to return a list of unique artists in the collection.

### Additional Challenge:

Extend the `RecordCollection` class to include:

- A method `find_records_by_artist(artist)` that returns a list of all records by a specified artist.
- A method `clear_collection()` that removes all records from the collection.

This kata will help you practice working with classes, managing collections, and performing operations on data in Python. Enjoy coding!
