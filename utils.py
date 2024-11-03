import json

file_path = 'data.json'

# file reading function 
def read_file():
    with open(file_path, "r") as f:
        return json.load(f)
    

# write into file function
def write_file(new_data):
        # opening to write
    with open(file_path, 'w') as file_write:
        
        # dump back the data with the new dictionary
        json.dump(new_data, file_write, indent=4)

def add_expense():
     # input from user
    description = input("\nYour task: ")
    amount = input("\nStatus: ")
    date = input("\nDate: ")

    # save as a dictionary
    new_data = {
            "description": description,
            "amount" : amount,
            "date" : date
    }

        # opening the file for read
    try:
        data = read_file()

    except (json.JSONDecodeError, FileNotFoundError):
        # if something went wrong creating an empty array
        data = []        

    # adding the new data into the loaded json data
    data.append(new_data)

    # write it into the jsone file
    write_file(data)

