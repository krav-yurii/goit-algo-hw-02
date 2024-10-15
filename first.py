import queue
import random
import time

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)  
    request_queue.put(f"Заявка #{request_id}")
    print(f"Згенеровано нову заявку: Заявка #{request_id}")

def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Обробляється {current_request}")
        request_queue.task_done()
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    try:
        while True:
            user_input = input("Натисніть Enter для генерації та обробки заявки або 'q' для виходу: ")
            if user_input.lower() == 'q':
                print("Завершення програми.")
                break
            generate_request()
            time.sleep(1)
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма завершена.")

if __name__ == "__main__":
    main()