from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    record = collection.add_record("Misfits", "Hybrid Moments")
    expected_record = {"artist": "Misfits", "title": "Hybrid Moments"}
    assert expected_record == record


def test_get_record():
    collection = RecordCollection()
    record = collection.add_record("Misfits", "Hybrid Moments")
    collection.get_record_by_title("Hybrid Moments")
    expected_record = {"artist": "Misfits", "title": "Hybrid Moments"}
    assert expected_record == record


def test_get_whole_collection():
    collection = RecordCollection()
    collection.add_record("Misfits", "Hybrid Moments")
    collection.add_record("Misfits", "Earth AD")
    collection.add_record("Danzig", "Danzig I")
    collection.add_record("Samhain", "Initium")

    current_collection = collection.get_record_collection()

    expected_collection = [
        {"artist": "Misfits", "title": "Hybrid Moments"},
        {"artist": "Misfits", "title": "Earth AD"},
        {"artist": "Danzig", "title": "Danzig I"},
        {"artist": "Samhain", "title": "Initium"},
    ]

    assert expected_collection == current_collection


def test_remove_record_by_title():
    collection = RecordCollection()
    collection.add_record("Misfits", "Hybrid Moments")
    collection.add_record("Misfits", "Earth AD")
    collection.add_record("Danzig", "Danzig I")
    collection.add_record("Samhain", "Initium")

    current_collection = [
        {"artist": "Misfits", "title": "Hybrid Moments"},
        {"artist": "Misfits", "title": "Earth AD"},
        {"artist": "Danzig", "title": "Danzig I"},
        {"artist": "Samhain", "title": "Initium"},
    ]
    removed_record = collection.remove_record_by_title("Earth AD")
    collection_without_removed_record = collection.get_record_collection()
    expected_removed_record = {"artist": "Misfits", "title": "Earth AD"}

    expected_collection = [
        {"artist": "Misfits", "title": "Hybrid Moments"},
        {"artist": "Danzig", "title": "Danzig I"},
        {"artist": "Samhain", "title": "Initium"},
    ]

    assert expected_collection == collection_without_removed_record


def test_count_records():
    collection = RecordCollection()
    collection.add_record("Misfits", "Hybrid Moments")
    collection.add_record("Misfits", "Earth AD")
    collection.add_record("Danzig", "Danzig I")
    collection.add_record("Samhain", "Initium")

    counted_records = collection.count_records()

    expected_count = 4

    assert counted_records == expected_count


def test_list_unique_artists():
    collection = RecordCollection()
    collection.add_record("Misfits", "Hybrid Moments")
    collection.add_record("Misfits", "Earth AD")
    collection.add_record("Danzig", "Danzig I")
    collection.add_record("Samhain", "Initium")

    unique_artists = collection.list_unique_artists()

    expected_artists = ["Misfits", "Danzig", "Samhain"]

    assert sorted(expected_artists) == sorted(unique_artists)
