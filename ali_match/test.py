from collections import defaultdict

predict_num = 0
hit_num = 0
brand = 0
result = defaultdict(set)
f = open("data/result.txt")
for line in f.readlines():
    line = line.strip()
    uid, bid = line.split("\t")
    result[uid] = bid.split(",")
    brand += len(result[uid])
f.close()


f = open("data/predict.txt")
for line in f.readlines():
    line = line.strip()
    uid, bid = line.split("\t")
    bid = bid.split(",")
    predict_num += len(bid)
    if uid not in result:
        continue
    else:
        for i in bid:
            if i in result[uid]:
                hit_num += 1

print "predict num is ", predict_num
print "hit num is ", hit_num
print "total brand is ", brand

precision = float(hit_num)/predict_num
callrate = float(hit_num)/brand
print "precision is ", precision
print "call rate is ", callrate

print "F1 is ", 2*precision*callrate/(precision+callrate)
