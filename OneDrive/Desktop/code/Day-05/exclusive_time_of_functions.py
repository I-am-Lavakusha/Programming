"""
LeetCode 636: Exclusive Time of Functions
Program to calculate exclusive execution time of functions from logs.
"""

def exclusive_time(n, logs):
    res = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        fid, typ, time = log.split(":")
        fid, time = int(fid), int(time)

        if typ == "start":
            if stack:
                res[stack[-1]] += time - prev_time
            stack.append(fid)
            prev_time = time
        else:  # "end"
            res[stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return res

# Example
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(exclusive_time(n, logs))  # [3, 4]

