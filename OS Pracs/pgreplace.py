from queue import Queue
frame = set()

def LRU(pages, no_of_pages, capacity):
    indexes = {}
    page_faults = 0
    for i in range(no_of_pages):
        if len(frame) < capacity:
            if pages[i] not in frame:
                frame.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
        else:
            if pages[i] not in frame:
                lru = float('inf')
                for page in frame:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page
                frame.remove(val)
                frame.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
    return page_faults

def FIFO(pages, no_of_pages, frame_size):
    indexes = Queue()
    page_faults = 0
    for i in range(no_of_pages):
        if (len(frame) < frame_size):
            if (pages[i] not in frame):
                frame.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
        else:
            if (pages[i] not in frame):
                    val = indexes.queue[0]
                    indexes.get()
                    frame.remove(val)
                    frame.add(pages[i])
                    indexes.put(pages[i])
                    page_faults += 1
        # print(indexes.queue)
        # print(frame)
    return page_faults

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    no_of_pages = len(pages)
    frame_size = 4
    page_fault = FIFO(pages,no_of_pages,frame_size)
    hits = no_of_pages - page_fault
    print(f"FIFO:\nPage-faults:{page_fault}\tHits:{hits}")
    frame.clear()
    page_fault = LRU(pages,no_of_pages,frame_size)
    hits = no_of_pages - page_fault
    print(f"LRU:\nPage-faults:{page_fault}\tHits:{hits}")
