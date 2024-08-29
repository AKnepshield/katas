Desired functionality

- Welcome screen to tell us what app does
- Menu that allows the user to choose: add new owner or view list of current owner's
- View list of current owner's
- List owner names only. One per line.
- TBD

- Enter owner's name
- Enter artist
- Enter album
- Prints owner's current collection
- Asks for artist again
- Enter artist
- Enter album
- Prints owner's current collection
- Ends

Define how to get data we need from user
-Get user input for what they want to do
-Used input function to store choice
-Put it in "choice" variable

Determine branching logic and stub out (add placeholder logic) functionality
-Created if/else for possible choices
-Put in placeholder print() until we got logic to fulfill requirement

Put in logic for if choice == "2"

Determine if we have data we need to do job
-Do we have data we need?
-Yes, because andy and bjorn were in in_mem_collection

Determine how to get specific with data we need from larger collection
-Looked at how in_mem_collection was stored
-Looked at andy and bjorn
-Saw that they were keys
-Googled how to get keys from dictionary python
-Added for loop for key in in_mem_collection
