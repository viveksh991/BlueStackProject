import re
from pathlib import Path


def scrape_logs_from_log_file(assignment_folder, file_path, first_pattern, second_pattern):
    """
    Parse log file
    :param assignment_folder: log file folder location
    :param file_path: path of first log file
    :param first_pattern:
    :param second_pattern:
    :return:
    """
    with open(assignment_folder + file_path, "r", encoding="utf8") as fl:
        file_content = fl.read()  # Read whole file as pattern can be searched
        l1 = re.search(first_pattern, file_content)
        if l1:
            second_pattern_result = re.search(f"({second_pattern})", file_content[l1.span()[1]:])
            if second_pattern_result:
                second_pattern_result_str = second_pattern_result.groups()[0]

                # search for 2nd pattern in Logs
                new_file_path = f"{assignment_folder}Assignment2/Logs/{second_pattern_result_str}"
                if second_pattern_result_str and Path(new_file_path):
                    with open(new_file_path, "r", encoding="utf8") as fl2:
                        for line in fl2:
                            if "assignment_completed" in line:
                                print(next(fl2, '').strip())
                                break
            else:
                print(f"{second_pattern} not found after {first_pattern} in {file_path}")
        else:
            print(f"{first_pattern} not found in {file_path}")


if __name__ == '__main__':
        scrape_logs_from_log_file(assignment_folder="D:/Driver/",
                              file_path="Assignment2/start_assignment.log",
                              first_pattern="beginning of assignment",
                              second_pattern="required_pattern_.*")
