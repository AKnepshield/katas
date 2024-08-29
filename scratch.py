def setup():
    json_manager = JsonFileManager("collection.json")
    in_mem_collection = json_manager.fetch_data()
    choice = input("Would you like to: 1) add a new owner or 2) view current owners? ")

    # Print choices for user with print statement
    # Capture user choice input with input statement
    # Temporarily store the choice with choice variable

    # If loop for choice as new owner
    if choice == "1":
        # Ask user for new owner name
        # Input statement for new owner
        # Store new owner as new_owner
        new_owner = input("Add new owner's name: ")
        # Use new_owner to create new owner dict
        in_mem_collection[new_owner] = []
        # in_mem is dictionary that holds a key, value pair
        # assign empty list to new_owner as key
        # update collection to json file

    # Tell setup what owner looks like with key value pair
    # Create key value pair with key as owner and value as empty list
    # Store new owner as new_owner variable
    # Add new_owner to in_mem_collection (it is just a variable that holds a dict)
    # Use jsonFileManager to save in_mem_collection
    json_manager.write_data(in_mem_collection)
    # If successful new_owner will be in json file
    # End goal - new owner in json with key("owner") & empty list([])
    # "Tamara": []

    # Ask user for owner name with input statement
    # Use choice variable to create a new owner
    #
    # Create new key:value dictionary in database
    # Print list of owners with new owner
    # Tell user new owner created
    # Show choices to add record to collection
    # Show new owner in list of owners
