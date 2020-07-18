import concurrent.futures
import time
from better_profanity import profanity
import csv




path = 'cleanMeChats.txt' # here specify the name of your text file



# Your text file is opened here and read in chunks that you specify below
def get_file(chunksize):
    with open('cleanMeChats.txt', 'r') as f:
        while True:
            read_data = f.read(chunksize)
            if not read_data:
                break  # done
            yield (read_data)


# a timer so you can see how long this takes o:
start = time.perf_counter()


def god_func(chur):
    with open('cleanMeChats3.txt', 'w') as f2:
        for value in get_file(chur):
            censored_text = profanity.censor(value)
            f2.write(censored_text)
            print(censored_text) # if you delete this print things will run faster!


# Specify how many records to take in at a time
with concurrent.futures.ProcessPoolExecutor() as executor:
    chunks = [5480] # <---- (change me depending on your needs)



    results = executor.map(god_func, chunks)



finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s) boi!')







