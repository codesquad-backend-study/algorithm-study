def reorder_log_files(logs):
    letter_logs = []
    digit_logs = []

    for log in logs:
        log_arr = log.split()
        if log_arr[1].isalpha():
            letter_logs.append(log_arr)
        else:
            digit_logs.append(log)
    letter_logs.sort(key=lambda x: (x[1:], x[0]))
    letter_logs = [" ".join(log) for log in letter_logs]

    return letter_logs + digit_logs

reorder_log_files(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])