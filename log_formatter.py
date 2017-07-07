import sys
import json

args = sys.argv
if len(args) != 2:
    print('usage: {} <log file name>'.format(args[0]))
    exit()

print args[1]
f = open(args[1], 'r')
data = json.load(f)

print('"epoch"\t"main/loss"\t"main/accuracy"\t"validation/loss"\t"validation/accuracy"\t"elapsed_time"')
for d in data:
    print('{}\t{}\t{}\t{}\t{}\t{}'.format(d['epoch'], d['main/loss'], d['main/accuracy'],
                                      d['validation/main/loss'], d['validation/main/accuracy'],
                                      d['elapsed_time']))

f.close()
