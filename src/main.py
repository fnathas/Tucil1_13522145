import read
import result
import time
import save
import acak

print("""
_________        ___.                                     __     _________________________________ 
\_   ___ \___.__.\_ |__   _________________  __ __  ____ |  | __ \_____  \   _  \______  \______  |
/    \  \<   |  | | __ \_/ __ \_  __ \____ \|  |  \/    \|  |/ /  /  ____/  /_\  \  /    /   /    /
\     \___\___  | | \_\ \  ___/|  | \/  |_> >  |  /   |  \    <  /       \  \_/   \/    /   /    / 
 \______  / ____| |___  /\___  >__|  |   __/|____/|___|  /__|_ \ \_______ \_____  /____/   /____/  
        \/\/          \/     \/      |__|              \/     \/         \/     \/     
                   
          """)

print("Welcome to the breach protocol minigame solver!")
print("=== Menu ===")
print("1. input file")
print("2. input terminal")
print("3. exit")

choice = input("Masukkan pilihan anda: ")

if choice == "1":
    file = input("Masukkan nama file: ")
    start_time = time.time()
    buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, rewards = read.read_file(file)
    all_paths = read.generate_strict_combinations(matrix, buffer_size)

    results = read.compare_paths(all_paths, sequences, rewards)
    result.result(results, buffer_size)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(f"{round(execution_time_ms)} ms")
    save.toFile(results, buffer_size)

elif choice == "2":
    print("Masukkan input anda: ")
    sumToken = int(input(""))
    tokens = input("")
    token_list = tokens.split()
    bufferSize = int(input(""))
    rows, cols = map(int, input("").split())
    sumSequence = int(input(""))
    maxSequence = int(input(""))

    start_time = time.time()
    matrix = acak.randMatrix(token_list, rows, cols)
    print("Matrix: ")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    print()

    print("Sequences: ")
    sequences = acak.randSequences(token_list, maxSequence, sumSequence)
    rewards = acak.randRewards(sumSequence)
    for i in range(sumSequence):
        for j in range(len(sequences[i])):
            print(sequences[i][j], end=" ")
        print()
        print(rewards[i], end=" ")
        print()
    
    print()
    all_paths = read.generate_strict_combinations(matrix, bufferSize)
    results = read.compare_paths(all_paths, sequences, rewards)
    result.result(results, bufferSize)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(f"{round(execution_time_ms)} ms")
    save.toFile(results, bufferSize)

else:
    print("Terima kasih telah menggunakan program ini!")
    exit()