from src.run_record_collection import run
from src.json_file_manager import JsonFileManager


def import_record_collections_from_file(json_manager):
    in_mem_collection = json_manager.fetch_data()
    return in_mem_collection


def setup():
    # Step 1
    json_manager = JsonFileManager("collection.json")
    in_mem_collection = import_record_collections_from_file(json_manager)
    return in_mem_collection, json_manager


if __name__ == "__main__":
    in_mem_collection, json_manager = setup()
    run(in_mem_collection, json_manager)
