#My First Code detection system #FBM#_P1
import threading
import queue

def get_input(q):
    while True:
        user_input = input("Enter something (timeout in 30s): ")
        q.put(user_input)



q = queue.Queue()
thread = threading.Thread(target=get_input, args=(q,), daemon=True)
thread.start()

inputs = []

while True:
    try:
        user_input = q.get(timeout=30)
        inputs.append(user_input)
        partial_dictionary_of_code_words = ['apple', 'orange', 'banana', 'all', 'words', 'etc']
        first_code_detection = ['']
        possible_code_word = ''
        list_of_possible_code_words = []
        for letter in inputs:
            first_code_detection[0] = first_code_detection[0] + letter
            possible_code_word += letter[0]
        if possible_code_word in partial_dictionary_of_code_words:
            sound_alarm = True
            list_of_possible_code_words.append(possible_code_word + ': True')
            print(list_of_possible_code_words)
        else:
            sound_alarm = False
    except queue.Empty:
        print("\nNo input received for 30 seconds. Exiting...")
        break
