import json


class JsonFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def fetch_data(self):
        """
        Reads and returns data from the JSON file.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"The file {self.file_path} does not exist.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {self.file_path}.")
            return None

    def write_data(self, data):
        """
        Writes data to the JSON file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def update_data(self, key, value):
        """
        Updates a specific key in the JSON file with a new value.
        """
        data = self.fetch_data()
        if data is not None:
            data[key] = value
            self.get_data(data)
            print(f"Updated {key} with value {value}.")
        else:
            print("Unable to update data; no data fetched.")


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
