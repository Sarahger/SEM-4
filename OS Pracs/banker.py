allocated = [[0, 1, 0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_required = [[7, 5, 3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
available = [ 3, 3, 2]
no_of_resources, no_of_process = 3, 5

def cal_need():
    need = [[ 0 for i in range(no_of_resources)]for i in range(no_of_process)]
    for i in range(no_of_process):
        for j in range(no_of_resources):
            need[i][j] = max_required[i][j] - allocated[i][j]
    return need

def bankers_algo():
    queue = []
    finish = [False] * no_of_process
    global available
    resorce_needed = cal_need()
    for i in range(no_of_process):
        for j in range(no_of_process):
            if not finish[j] and all(resorce_needed[j][k] <= available[k] for k in range(no_of_resources)):
                queue.append(j)
                available = [available[k] + allocated[j][k] for k in range(no_of_resources)]
                finish[j] = True
    return queue

if __name__ == '__main__':
    queue = bankers_algo()
    print(queue)
