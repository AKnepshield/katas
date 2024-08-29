from src.record_collection import RecordCollection
from src.json_file_manager import JsonFileManager


def view_or_create_owners_menu(in_mem_collection, json_manager):
    owner_input_choice = view_or_create_owner_input()

    if owner_input_choice == "1":
        create_new_owner(in_mem_collection, json_manager)

    if owner_input_choice == "2":
        view_current_owners(in_mem_collection)


def run(in_mem_collection, json_manager):
    view_or_create_owners_menu(in_mem_collection, json_manager)

    # count = 0

    # while count < 2:
    #     artist = input("Enter an artist: ")
    #     album = input("Enter an album: ")
    #     collection = andys_collection.add_record(artist, album)
    #     retrieved_collection = andys_collection.get_record_collection()
    #     print(retrieved_collection)
    #     in_mem_collection[owner] = andys_collection.get_record_collection()
    #     json_manager.write_data(in_mem_collection)
    #     count += 1


def create_new_owner(in_mem_collection, json_manager):
    new_owner = input("Add new owner's name: ")
    in_mem_collection[new_owner] = []
    json_manager.write_data(in_mem_collection)


def view_current_owners(in_mem_collection):
    for key in in_mem_collection.keys():
        print(key)


# Step 2


def view_or_create_owner_input():
    owner_input_choice = input(
        "Would you like to: 1) add a new owner or 2) view current owners? "
    )
    return owner_input_choice
