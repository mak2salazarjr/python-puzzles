# Let's examine one example -- '00:00:00', '00:00:30', '+2 seconds at 6 seconds'.
# 0th step: The real and fake time is "00:00:00".
# When the real time is "00:00:06", the fake time is "00:00:08".
# At real "00:00:18", fake is "00:00:24".
# At real "00:00:21", fake is "00:00:28".
# At real "00:00:22", fake is "00:00:29.333...".
# At real "00:00:22.5", fake is "00:00:30".
# So answer is "00:00:22.5" after rounding down "00:00:22"
# Input: Three arguments: Correct starting time, current wrong time and broken clock descriptions
#  as strings.
# Output: The real time as a string.
# Precondition:
# "wrong_time" is later than "starting_time".


time_multiplier = {'seconds': 1, 'second': 1,
                   'minutes': 60, 'minute': 60,
                   'hours': 3600, 'hour': 3600}


def broken_clock(starting_time, wrong_time, error_description):
    start_hours, start_minutes, start_seconds = starting_time.split(':')
    start_time = int(start_hours) * 3600 + int(start_minutes) * 60 + int(start_seconds)
    wrong_hours, wrong_minutes, wrong_seconds = wrong_time.split(':')
    wrong_elapsed_time = int(wrong_hours) * 3600 + int(wrong_minutes) * 60 + int(wrong_seconds)
    error = error_description.split(' ')
    error_time = int(error[0]) * time_multiplier[error[1]]
    elapsed_time = int(error[3]) * time_multiplier[error[4]]
    correct_time = start_time + int((wrong_elapsed_time - start_time) * elapsed_time /
                                          (error_time + elapsed_time))
    correct_hours = correct_time // 3600
    correct_time -= correct_hours * 3600
    correct_minutes = correct_time // 60
    correct_seconds = correct_time - correct_minutes * 60
    time_str = '{:02d}:{:02d}:{:02d}'.format(correct_hours, correct_minutes, correct_seconds)
    return time_str

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
    assert broken_clock('03:14:10', "10:20:30", "+4 minutes at 2 hours") == "10:06:44", 'Six'