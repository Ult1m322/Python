from data_input import input_worker
from calculations import *
from general import *
def main():
    worker = input_worker()
    calculate_salary(worker)

    worker_names = list(worker.keys())
    print("Всі співробітники команди:")
    print_workers(worker_names)

if __name__ == "__main__":
    main()
