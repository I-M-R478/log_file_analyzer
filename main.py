import re
from collections import Counter

# Function to parse the log file
def parse_log_file(file_path):
    """Define regex pattern to extract log level and message"""
    log_pattern = re.compile(r'\[(INFO|WARN|ERROR)\]\s+(.*)')  # Matches [LEVEL] Message
    logs = {"INFO": [], "WARN": [], "ERROR": []}

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = re.match(log_pattern, line)
                if match:
                    log_level, message = match.groups()
                    logs[log_level].append(message)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return logs

# Function to analyze the parsed logs
def analyze_logs(logs):
    """Find the count occureneces of logs"""
    log_counts = {level: len(messages) for level, messages in logs.items()}
    
    # Find the most common errors
    error_counter = Counter(logs["ERROR"])
    most_common_errors = error_counter.most_common(5)  # Top 5 errors
    
    return log_counts, most_common_errors

# Main function to execute the log analyzer


def main():
    """Now it will analyze log files"""
    file_path = "plain.log"

    # parse the log file
    logs = parse_log_file(file_path)

    # analyze the logs
    log_counts, most_common_errors= analyze_logs(logs)

    # display the results
    print("=== Log Analysis Results ===")
    print("\nLog Level Counts:")
    for level, count in log_counts.items():
        print(f"{level}: {count}")

    print("\nMost Common Errors:")
    if most_common_errors:
        for error, count in most_common_errors:
            print(f"'{error}': {count} occurrence(s)")
    else:
        print("No errors found.")

# entry point of the script
if __name__ == "__main__":
    main()