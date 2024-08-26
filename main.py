from src.record_collection import RecordCollection
from src.json_file_manager import JsonFileManager


def run(andys_collection, in_mem_collection, json_manager):
    count = 0

    while count < 2:
        artist = input("Enter an artist: ")
        album = input("Enter an album: ")
        collection = andys_collection.add_record(artist, album)
        retrieved_collection = andys_collection.get_record_collection()
        print(retrieved_collection)
        in_mem_collection["andy"] = andys_collection.get_record_collection()
        json_manager.write_data(in_mem_collection)
        count += 1


def setup():
    json_manager = JsonFileManager("collection.json")
    in_mem_collection = json_manager.fetch_data()
    if not in_mem_collection:
        in_mem_collection = {"andy": []}
        json_manager.write_data(in_mem_collection)
    andys_collection = RecordCollection()
    andys_collection.record_collection = in_mem_collection["andy"]
    return in_mem_collection, andys_collection, json_manager


if __name__ == "__main__":
    in_mem_collection, andys_collection, json_manager = setup()
    run(andys_collection, in_mem_collection, json_manager)


# Example usage
# json_manager = JsonFileManager('data.json')
#
# # Fetch data from the JSON file
# data = json_manager.fetch_data()
# print(data)
#
# # Write new data to the JSON file
# new_data = {"name": "John", "age": 30}
# json_manager.get_data(new_data)
#
# # Update specific data in the JSON file
# json_manager.update_data("age", 31)
