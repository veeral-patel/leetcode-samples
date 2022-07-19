# https://algo.monster/problems/newspapers_split

def newspapers_split(newspapers_read_times, num_coworkers):
    # if you have one coworker per newspaper, will take
    # the max read time to complete all newspapers
    low = max(newspapers_read_times)

    # if you have one coworker read all papers, will take
    # the combined read time of all papers
    high = sum(newspapers_read_times)

    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def feasible(newspapers_read_times, num_coworkers, time_given):
    coworkers_needed = 1
    time_left = time_given

    for nr_time in newspapers_read_times:
        if nr_time <= time_left:
            time_left -= nr_time
        else:
            time_left = time_given - nr_time
            coworkers_needed += 1

    return coworkers_needed <= num_coworkers

