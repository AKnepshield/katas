def view_or_create_owners_menu(in_mem_collection, json_manager):
    # 10
    owner_input_choice = view_or_create_owner_input()
    # 13
    # owner_input_choice is saved as "3"

    if owner_input_choice == "1":
        create_new_owner(in_mem_collection, json_manager)
        return True

    if owner_input_choice == "2":
        view_current_owners(in_mem_collection)
        return True

    # 14
    if owner_input_choice == "3":
        # 15
        return False
    # TBD

    return True


def create_new_owner(in_mem_collection, json_manager):
    new_owner = input("Add new owner's name: ")
    in_mem_collection[new_owner] = []
    json_manager.write_data(in_mem_collection)


def view_current_owners(in_mem_collection):
    for key in in_mem_collection.keys():
        print(key)


# TODO: Step 2 - Create exit function in menu file

# Step 2


def view_or_create_owner_input():
    # 11
    owner_input_choice = input(
        "Would you like to: 1) add a new owner or 2) view current owners? 3) Exit "
    )
    # 12
    return owner_input_choice


# TODO: Step 1 - Add exit option to input DONE
