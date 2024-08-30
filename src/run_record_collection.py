from src.owners_menu import view_or_create_owners_menu


def run(in_mem_collection, json_manager):

    while True:
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
