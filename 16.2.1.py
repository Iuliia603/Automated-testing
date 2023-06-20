#with keyword arguments
def show_employee(name, salary="5000"):
    print(name, salary)
show_employee(name="Iulia", salary="6000")


#with 2 positional arguments (means only with values for arguments)
show_employee("Kate", "7000")


#with 1 positional argument (for salary it should use default value)
show_employee("Polina")