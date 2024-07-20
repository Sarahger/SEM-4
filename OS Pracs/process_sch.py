class process:
    def __init__(self,code,arrival,burst, priority):
        self.code = code
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0
    
    def cal_TAT_and_WT(self):
        self.turnaround = self.completion - self.arrival
        self.waiting = self.turnaround - self.burst
               
def print_table(process_queue: list):
    avg_TAT, avg_WT = 0.0, 0.0
    print("PID\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT")
    for process in process_queue:
        print(f'{process.code}\t\t{process.arrival}\t\t{process.burst}\t\t{process.completion}\t\t{process.turnaround}\t\t{process.waiting}')
        avg_TAT += process.turnaround
        avg_WT += process.waiting
    avg_TAT = avg_TAT / len(process_queue)
    avg_WT = avg_WT / len(process_queue)
    print(f'Average TAT:{avg_TAT}\t\tAverage WT:{avg_WT}')
    
def cal_ct(queue: list):
    count = 0
    for i in range(len(queue)):
        if count == 0:
            queue[i].completion = queue[i].arrival + queue[i].burst
            count = 1
        else:
            if queue[i].arrival > queue[i - 1].completion:
                extra = queue[i].arrival - queue[i - 1].completion
                queue[i].completion = queue[i - 1].completion + queue[i].burst + extra
            else:
                queue[i].completion = queue[i - 1].completion + queue[i].burst
            
def swap(prevIndex: int, nextIndex: int, queue: list):
    queue[prevIndex], queue[nextIndex] = queue[nextIndex], queue[prevIndex]

def FCFS(queue: list):
    cal_ct(queue)
    for process in queue:
        process.cal_TAT_and_WT()
    print("First Come First Serve")
    print_table(queue)

def SJF(queue: list):
    for i in range(len(queue)):
        for j in range(len(queue)):
            if queue[i].burst < queue[j].burst:
                swap(i,j,queue)
    cal_ct(queue)
    for process in queue:
        process.cal_TAT_and_WT()
    print("\nShorest Job First")
    print_table(queue)

def priority(queue: list):
    for i in range(len(queue)):
        for j in range(len(queue)):
            if queue[i].priority > queue[j].priority:
                swap(i,j,queue)
    cal_ct(queue)
    for process in queue:
        process.cal_TAT_and_WT()
    print("\nPriority Based")
    print_table(queue)

def round_robin(queue: list, quantum: int):
    time, n = 0, len(queue)
    remaining_burst_time = [process.burst for process in queue]
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    remaining_burst_time[i] = 0
                    queue[i].completion = time
        if done:
            break
    for process in queue:
        process.cal_TAT_and_WT()
    print("\nRound Robin (RR)")
    print_table(queue)

if __name__ == '__main__':
    p1, p2, p3 = process('P1',0,5,2),process('P2',1,3,3),process('P3',1,2,1)
    process_queue = [p1,p2,p3]
    FCFS(process_queue)
    SJF(process_queue.copy())
    priority(process_queue.copy())
    round_robin(process_queue.copy(), 2)
