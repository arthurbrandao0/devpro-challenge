import datetime


def log_message(file_name, message, log_level):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} [{log_level}] {message}\n"

    with open(file_name, 'a') as log_file:
        log_file.write(log_entry)

    # Show in console the same content that was written in log file
    print(log_entry)


# Examples
log_message("application.log", "User logged in", "INFO")
log_message("application.log", "Failed login attempt", "WARNING")
log_message("application.log", "User logged out", "INFO")
