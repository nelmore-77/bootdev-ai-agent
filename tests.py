from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

run_cases = [
    ("calculator", "main.py",),
    ("calculator", "pkg/calculator.py",),
    ("calculator", "/bin/cat",),
    ("calculator", "pkg/does_not_exist.py",),
]

def tests(working_directory, file_path):
        print("--------------------------")
        print(f"Input_directory: {working_directory}")
        print(f"target: {file_path}")
        result = get_file_content(working_directory, file_path)
        print("Actual Output:")
        return result

def main_test():
    for run_case in run_cases:
        run_result = tests(run_case[0], run_case[1])
        print(run_result)

main_test()