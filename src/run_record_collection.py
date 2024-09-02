from src.owners_menu import view_or_create_owners_menu


def run(in_mem_collection, json_manager):

    # 8
    keep_running = True
    # 8.5 - Checks if keep_running is True
    # if keep_running == True
    while keep_running == True:
        # 9
        keep_running = view_or_create_owners_menu(in_mem_collection, json_manager)
        # 16 - saving value to any_name


# TODO: Step 3 - Run function from run_record_collection
# TODO: Step 4 - Change True to variable in while loop
