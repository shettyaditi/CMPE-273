import psutil
from operator import itemgetter, attrgetter
from collections import namedtuple
from collections import OrderedDict
from itertools import groupby

n = psutil.net_connections(kind="tcp")

SocketConn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr', 'status', 'pid'])
output = []
final = {}
for i in n:
    x = SocketConn(*i)
    if x.laddr and x.raddr:
        output.append((str(x.pid), "\"" + str(x.pid) + "\",\"" + str(x.laddr[0]) + "@" + str(x.laddr[1]) + "\",\"" + str(x.raddr[0]) + "@" + str(x.raddr[1]) + "\",\"" + x.status + "\""))

for key, group in groupby(sorted(output), lambda x: x[0]):
    for i in group:
        if key in final:
            final[key].append(i[1])
        else:
            final[key] = [i[1]]

finalDict = OrderedDict(sorted(final.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))

print "\"pid\",\"laddr\",\"raddr\",\"status\""

for key, value in finalDict.items():
    for process in value:
        print (process)
