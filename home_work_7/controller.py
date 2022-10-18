import input
import write_reader

def click_input():
    person = input.get_info()
    write_reader.write_data(person)

def click_output():
    write_reader.read_data('z.csv')