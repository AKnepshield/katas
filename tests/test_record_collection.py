from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    record = collection.add_record("The Smiths", "Hatful Of Hollow")
    expected_record = {"artist": "The Smiths", "title": "Hatful Of Hollow"}
    assert expected_record == record


def test_get_record_by_title():
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    retrieved_record = collection.get_record_by_title("Hatful Of Hollow")
    expected_record = {"artist": "The Smiths", "title": "Hatful Of Hollow"}
    assert retrieved_record == expected_record


def test_get_record_collection():
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways")
    retrieved_collection = collection.get_record_collection()
    expected_collection = [
        {"artist": "The Smiths", "title": "Hatful Of Hollow"},
        {"artist": "The Smiths", "title": "The Queen Is Dead"},
        {"artist": "The Smiths", "title": "Strangeways"},
    ]
    assert retrieved_collection == expected_collection


def test_remove_record():
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways")
    removed_record = collection.remove_record("Strangeways")
    current_collection = collection.get_record_collection()
    current_collection_without_record = [
        {"artist": "The Smiths", "title": "Hatful Of Hollow"},
        {"artist": "The Smiths", "title": "The Queen Is Dead"},
    ]
    assert current_collection_without_record == current_collection


def test_count_records():
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways")
    record_count = collection.count_records()
    expected_count = 3
    assert expected_count == record_count


def test_list_unique_artists():
    collection = RecordCollection()
    collection.add_record("The Smiths", "Hatful Of Hollow")
    collection.add_record("The Smiths", "The Queen Is Dead")
    collection.add_record("The Smiths", "Strangeways")
    collection.add_record("Morrissey", "Your Arsenal")
    listed_artists = collection.list_unique_artists()
    expected_listed_artists = ["The Smiths", "Morrissey"]
    assert sorted(expected_listed_artists) == sorted(listed_artists)
