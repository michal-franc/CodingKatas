class HitCounter:
    def __init__(self) -> None:
        self.queue = {}

    # register hit at timestamp
    def hit(self, timestamp):
        if(timestamp not in self.queue):
            self.queue[timestamp] = 0

        self.queue[timestamp] += 1

    # return last 300s - this is important 300s last
    def getHits(self, timestamp):
        count = 0
        newDict = {}
        timeWindow = timestamp - 300
        for k in self.queue.keys():
            if k > timeWindow:
                count += self.queue[k]
                newDict[k] = self.queue[k]

        self.queue = newDict

        return count
