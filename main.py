from src.run_record_collection import run
from src.json_file_manager import JsonFileManager


def import_record_collections_from_file(json_manager):
    in_mem_collection = json_manager.fetch_data()
    return in_mem_collection


# 3
def setup():
    # 4
    json_manager = JsonFileManager("collection.json")
    # 5
    in_mem_collection = import_record_collections_from_file(json_manager)
    # 6
    return in_mem_collection, json_manager


# 1
if __name__ == "__main__":
    # 2
    in_mem_collection, json_manager = setup()
    # 6.5 saves return from setup function
    # 7
    run(in_mem_collection, json_manager)
