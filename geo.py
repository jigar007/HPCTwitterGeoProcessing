import json
from mpi4py import MPI
import datetime
from collections import Counter
import time

start_time = time.time()

comm = MPI.COMM_WORLD

count_tweet = {}
geoloc_box = {}

size = comm.Get_size()
rank = comm.Get_rank()
name = comm.Get_name()

with open('melbGrid.json') as f:
    data = json.load(f)

for feature in data['features']:
    count_tweet[feature['properties']['id']] = 0

    geoloc_box[feature['properties']['id']] = [feature['properties']['xmin'],
                                               feature['properties']['xmax'],
                                               feature['properties']['ymin'],
                                               feature['properties']['ymax']]

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

if rank == 0:
    prepro_start_time = time.time()
    print ("Job started on ", name, size, datetime.datetime.now())
    mylist = []
    with open('smallTwitter.json') as fp:
        for each in fp:
            each = each.rstrip("]" + "[" + "," + "\n")
            if len(each) > 3:
                j = json.loads(each)
                mylist.append(j['json']['coordinates']['coordinates'])

    fp.close()

    prepro_stop_time = time.time()

    if size > 1:
        mylist = chunkIt(mylist, size)
        for i in range(1, size):
            comm.send(mylist[i], dest=i)
        mylist = mylist[0]
else:
    mylist = comm.recv(source=0)

for each in mylist:
    x = each[0]
    y = each[1]

    for key, value in geoloc_box.iteritems():
        xmin = value[0]
        xmax = value[1]
        ymin = value[2]
        ymax = value[3]

        if xmin <= x <= xmax and ymin <= y <= ymax:
            count_tweet[key] += 1

print ("Search ended on " , name, rank, datetime.datetime.now())

#Blocks untill all processes finish search.
comm.barrier()
gather_data = comm.gather(count_tweet, root=0)

#Flattening my lists
if rank == 0:

    count_tweet_gather = Counter()
    for dictionary in gather_data:
        count_tweet_gather.update(dictionary)

    ###############################################
    print "Ordered (rank) grid boxes based on total number of tweets made in each box:"

    # Sorted makes dictionary sorting in asending order where [::-1] makes it in descending order
    descending_dictionary = sorted(count_tweet_gather, key=count_tweet_gather.get)[::-1]

    for item in descending_dictionary:
        print item + ": " + str(count_tweet_gather[item])

    ###############################################
    print "Ordered (rank) the rows based on the total number of tweets in each row:"

    tuple_list = [(key[0] + "-Row", int(value)) for (key, value) in count_tweet_gather.iteritems()]
    defalut_dict = {}
    for (key, val) in tuple_list:
        defalut_dict.setdefault(key, []).append(int(val))
    total = {k: sum(v) for k, v in defalut_dict.iteritems()}

    for item in sorted(total, key=total.get)[::-1]:
        print item + ": " + str(total[item])

    #################################################
    print "Order (rank) the columns based on the total number of tweets in each column:"

    tuple_list = [("Column" + key[1], int(value)) for (key, value) in count_tweet_gather.iteritems()]
    defalut_dict = {}
    for (key, val) in tuple_list:
        defalut_dict.setdefault(key, []).append(int(val))
    total = {k: sum(v) for k, v in defalut_dict.iteritems()}

    for item in sorted(total, key=total.get)[::-1]:
        print item + ": " + str(total[item])

    prepro_time = prepro_stop_time - prepro_start_time
    total_time = time.time() - start_time
    print "Total preprocessing time: " + str(prepro_time) + " Seconds"
    print "Total time: " + str(total_time) + " Seconds"
    print "T0tal time for actual processting: " + str(total_time-prepro_time) + " Seconds"