FILEDEFAULT = 'todos.txt'

# define functions with default argument for file path
def get_todos(file_path=FILEDEFAULT):
    """Imports a list of pre-existing items to do from file.
    Usage: get_todos <filepath=infile_path>"""
    with open(file_path, 'r') as f:
        inlist = f.readlines()
        inlist = [this.title() for this in inlist]
        todo_dict = {}
        for item in inlist:
            todo_dict[item] = 1
        return todo_dict

def write_todos(todos_keys, file_path=FILEDEFAULT):
    """Prints the list of items into a file.
    Usage: write_todos <todoList=list_name> <file_path=outfile_path>"""
    with open(file_path, 'w') as f:
        f.writelines(todos_keys)


# print ("functions.py has been imported")
# the below is only ran when functions itself is ran
#   (not when it is imported)
if __name__ == "__main__":
    print (get_todos())
