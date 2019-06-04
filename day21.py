#!/usr/bin/env python3
"""Problem - Day 21
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
def roomsNeeded(times):
    if not times:
        return 0
    rooms_needed = 1
    times.sort()
    booked = [times[0]]
    passed_times = []
    for time in times[1:]:
        if time[0] >= booked[-1][1]:
            booked.append(time)
        else:
            passed_times.append(time)
    if passed_times:
        rooms_needed += roomsNeeded(passed_times)
    return rooms_needed


def main():
    times1 = [(30, 75), (0, 50), (60, 150)]
    print(roomsNeeded(times1))

    times2 = [(110, 150), (50, 80), (0, 10), (140, 150), (100, 140),
              (40, 80), (80, 100), (70, 100), (130, 140), (90, 110)]
    print(roomsNeeded(times2))


if __name__ == '__main__':
    main()

