def calculate_salary(worker_info):
    for worker, details in worker_info.items():
        monthly_salary =  (details['Зарплата']/30)*details['Дні']
        print(f"{worker} отримає за місяць : {monthly_salary:.2f} грн")

