def read_file(f_name):
    try:
        with open(f_name,'r') as file:
            for i in file:
                print(i.strip())
    except FileNotFoundError:
        print(f"Error : {f_name} dosen't exists")

read_file('sample.txt')
