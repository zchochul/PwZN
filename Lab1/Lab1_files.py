with open('Lab1_tqdm.py', 'r') as f: #do odczytu otwieramy
    for line in f:
        print(line.strip().split(' ')) #strip oczyszcza ze znaków końca linii i tabów, a split dzieli stringi