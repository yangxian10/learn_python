from datetime import *

def parse_date(raw_date): #change 6yue4ri---->2014 6 4
    entry_date = raw_date.decode("gbk")
    month = int(entry_date[0])
    if len(entry_date) == 6:
        day = 10 * int(entry_date[2]) + int(entry_date[3])
    else:
        day = int(entry_date[2])
    return 2014, month, day

#raw_file split to tarin and validation
def split_file(raw_file, seperate_day, begin_date):
    train = open("data/train.csv", "w")
    validation = open("data/validation.csv", "w")
    raw_file.readline()
    for line in raw_file.readlines():
        entry = line.split(",")
        entry_date = date(*parse_date(entry[3]))
        date_delta = (entry_date - begin_date).days
        if date_delta < seperate_day:
            train.write(",".join(entry[:3]) + "," + str(date_delta) + "\n")
        elif int(entry[2]) == 1:
            validation.write(",".join(entry[:2]) + "\n")
            print ",".join(entry[:2])
    train.close()
    validation.close()

#validation save to result.txt
def generate_result(validation):
    entrys = validation.readlines()
    entrys.sort(key=lambda x: x.split(",")[0])
    result = open("data/result.txt", "w")
    for index, entry in enumerate(entrys):
        uid, tid = entry.strip().split(",")
        if index == 0:
            cur_id = uid
            cur_result = [tid]
        elif uid == cur_id:
            cur_result.append(tid)
        else:
            result.write(cur_id + "\t" + ",".join(set(cur_result)) + "\n")
            cur_id = uid
            cur_result = [tid]
    result.close()

###################main
SEPERATEDAY = date(2014, 7, 15)
BEGINDAY = date(2014, 4, 15) #4.15~7.15 train 7.15~8.15 test
raw_file = open("data/t_alibaba_data.csv")
split_file(raw_file, (SEPERATEDAY - BEGINDAY).days, BEGINDAY)
raw_file.close()
validation = open("data/validation.csv")
generate_result(validation)
