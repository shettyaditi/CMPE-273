
import psutil
import heapq
import csv
from operator import itemgetter, attrgetter
from collections import namedtuple
from collections import Counter

class pid_sorted :
    def __init__(self, x, ):
        self.user_id = y

    def __repr__(self):
       return str(self.pid)

n = psutil.net_connections()

SocketConn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr', 'status', 'pid'])
output = []
for i in n:
    x = SocketConn(*i)
    output.append(x.pid)

print("PID and its frequency")
counter = Counter(output)
top_hundred = counter.most_common(100)
for i in top_hundred:
    print(i)
