from src.record_collection import RecordCollection


def test_add_record():
    collection = RecordCollection()
    title = "Hear Nothing See Nothing Say Nothing"
    artist = "Discharge"
    collection.add_record(title, artist)
    assert collection.records == [
        {
            "title": "Hear Nothing See Nothing Say Nothing",
            "artist": "Discharge",
        }
    ]
