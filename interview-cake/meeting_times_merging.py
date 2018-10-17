#Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
# Examples

#[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#[(0, 1), (3, 8), (9, 12)]

def merge_time(meetings):

    sorted_meetings = sorted(meetings)

    overlapped_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_meeting_start, last_meeting_end = overlapped_meetings[-1]

        # in example last_meeting -> (0, 1)
        # current -> (3, 5)
        # 1 <= 3 -> doesnt overlap
        if current_meeting_start <= last_meeting_end:
            # max used here to merge meeting that is 'inside' another one
            overlapped_meetings[-1] = (last_meeting_start, max(last_meeting_end, current_meeting_end))
        else:
            overlapped_meetings.append((current_meeting_start, current_meeting_end))

    return overlapped_meetings

test = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

print(merge_time(test))
