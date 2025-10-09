def print_workers(worker_names, index=0):
    if index < len(worker_names):
        print(worker_names[index])

        print_workers(worker_names, index + 1)


