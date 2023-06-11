from multiprocessing import Process
from threading import Thread
from time import sleep, time

from generate_csv import process_to_csv




def run_all_within_dir(dir):
    methods =('bernsen','contrast','mean','median','midgrey','niblack','otsu','phansalkar','sauvola')
    # methods =('otsu','contrast')
    processes = []
    for name in methods:
        process = Process(target=process_to_csv, args=(name,dir,True))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    start = time()
    run_all_within_dir('result/result_with_sda')
    run_all_within_dir('result/result_without_sda')

    end = time() - start

    print(f'Finished {end/60} min')
    # while(True):
    #     sleep(1)