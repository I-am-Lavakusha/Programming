def daily_temperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []  # indices

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)

    return res

# Example
temps = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temps))  # [1,1,4,2,1,1,0,0]
