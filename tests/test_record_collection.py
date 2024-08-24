from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()

    record = collection.add_record("Peace & Security", "Death Threat")

    expected_record = {"title": "Peace & Security", "artist": "Death Threat"}

    assert expected_record == record


def test_get_record_by_title():
    collection = RecordCollection()
    record = collection.add_record("Peace & Security", "Death Threat")
    returned_record = collection.get_record_by_title("Peace & Security")
    expected_record = {"title": "Peace & Security", "artist": "Death Threat"}
    assert expected_record == returned_record


def test_get_record_collection():
    collection = RecordCollection()
    collection.add_record("Peace & Security", "Death Threat")
    collection.add_record("Big Kiss Goodnight", "Trapped Under Ice")

    returned_collection = collection.get_record_collection()

    expected_returned_collection = [
        {"title": "Peace & Security", "artist": "Death Threat"},
        {"title": "Big Kiss Goodnight", "artist": "Trapped Under Ice"},
    ]

    assert returned_collection == expected_returned_collection


def test_remove_record_by_title():
    collection = RecordCollection()
    collection.add_record("Peace & Security", "Death Threat")
    collection.add_record("Big Kiss Goodnight", "Trapped Under Ice")
    collection.add_record("Heatwave", "Trapped Under Ice")
    collection.add_record("World Be Free", "World Be Free")

    removed_record = collection.remove_record_by_title("Peace & Security")
    current_collection = collection.get_record_collection()

    expected_removed_record = {"title": "Peace & Security", "artist": "Death Threat"}

    expected_collection_without_removed_record = [
        {"title": "Big Kiss Goodnight", "artist": "Trapped Under Ice"},
        {"title": "Heatwave", "artist": "Trapped Under Ice"},
        {"title": "World Be Free", "artist": "World Be Free"},
    ]

    assert removed_record == expected_removed_record
    assert expected_collection_without_removed_record == current_collection
