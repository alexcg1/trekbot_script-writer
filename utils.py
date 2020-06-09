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
                  logwriter.writerow(log_headers)
        else:
            print(f"Using existing log")

    def write_row(data, file_path):
        """
        @param: data: list of data you want written to a row, one datum per column
        @param: file_path: path to the CSV file you want to write to
        """
        if not os.path.exists(file_path):
            raise IOError(f"File {file_path} not found")
        else:
            with open(file_path, 'a', newline='') as csvfile:
                  logwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                  logwriter.writerow(data)
