import csv
import os

class Setup:
    def dir_setup(dir_list):
        for directory in dir_list:
            if not os.path.isdir(directory):
                os.mkdir(directory)
                print(f"Created {directory}")
            else:
                print(f"Skipped {directory}. It already exists")
                
class Diag:
    import csv
    import os

    def setup(file_path):
#         logwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         pass
        
        loss_log = file_path
        log_headers = ["Time", "Learning Rate", "Loss"]
        
        if not os.path.exists(loss_log):
            print(f"Creating new log at {loss_log}")
            with open(loss_log, 'w', newline='') as csvfile:
                  logwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        else:
            print(f"Using existing log")
