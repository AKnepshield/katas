def view_or_create_owners_menu(in_mem_collection, json_manager):
    owner_input_choice = view_or_create_owner_input()

    if owner_input_choice == "1":
        create_new_owner(in_mem_collection, json_manager)

    if owner_input_choice == "2":
        view_current_owners(in_mem_collection)


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
