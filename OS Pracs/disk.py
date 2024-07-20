MAX_REQUESTS = 100
def FCFS(head, requests):
    total_seek_time = 0
    for req in requests:
        total_seek_time += abs(head - req)
        head = req
    return total_seek_time

def SSTF(head, requests):
    visited = [False] * MAX_REQUESTS
    total_seek_time = 0
    for _ in range(len(requests)):
        min_dist = float('inf')
        min_index = -1
        for j in range(len(requests)):
            if not visited[j]:
                dist = abs(head - requests[j])
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
        visited[min_index] = True
        total_seek_time += min_dist
        head = requests[min_index]
    return total_seek_time

def SCAN(head, requests, direction):
    total_seek_time = 0
    requests.sort()
    curr_index = 0
    for i in range(len(requests)):
        if head < requests[i]:
            curr_index = i
            break
    if direction:
        for i in range(curr_index, len(requests)):
            total_seek_time += abs(head - requests[i])
            head = requests[i]
        total_seek_time += abs(head - 199)
        head = 199
        for i in range(curr_index - 1, -1, -1):
            total_seek_time += abs(head - requests[i])
            head = requests[i]
    else:
        for i in range(curr_index - 1, -1, -1):
            total_seek_time += abs(head - requests[i])
            head = requests[i]
        total_seek_time += abs(head - 0)
        head = 0
        for i in range(curr_index, len(requests)):
            total_seek_time += abs(head - requests[i])
            head = requests[i]
    return total_seek_time

if __name__ == "__main__":
    requests = []
    print("Enter the number of requests: ")
    n = int(input())
    print("Enter the request queue:")
    for i in range(n):
        requests.append(int(input()))
    head = int(input("Enter the initial position of the head: "))
    total_seek_time_FCFS = FCFS(head, requests)
    print(f"Total Seek Time for FCFS: {total_seek_time_FCFS}")
    total_seek_time_SSTF = SSTF(head, requests)
    print(f"Total Seek Time for SSTF: {total_seek_time_SSTF}")
    direction = bool(input("Enter the direction for SCAN (0 for left, 1 for right): "))
    total_seek_time_SCAN = SCAN(head, requests, direction)
    print(f"Total Seek Time for SCAN: {total_seek_time_SCAN}")
