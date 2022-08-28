from os import system
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-o', '--operation', choices=['increase', 'decrease'], required=True)
parser.add_argument('-a', '--amount', required=True)

args = parser.parse_args()

operatorAmount = 0

try:
    operatorAmount = float(args.amount)
except ValueError:
    print("-a takes an Integer or Float")

logOutput = []
latestLog = ""

newSpeed = 1.0
oldSpeed = 1.0

with open('/tmp/speedhack_log') as fifo:
    while True:
        line = fifo.readline()
        if line != "":
            logOutput.append(line)
        else: break

if logOutput:
    logOutput.reverse()
    latestLog = next(filter(lambda line: line.startswith("LibSpeedhack: new timescale"), logOutput), None).strip()
    
    if latestLog:
        oldSpeed = float(latestLog.split(" ")[-1])

if args.operation == "increase":
    newSpeed = float(oldSpeed + operatorAmount)
else:
    newSpeed = float(oldSpeed - operatorAmount)

notifyCommand = "'{}d game speed' '{} -> {}'".format(args.operation.capitalize(), oldSpeed, newSpeed)

echoCommand = "echo {} > /tmp/speedhack_pipe".format(newSpeed)

system(echoCommand)

system("notify-send " + notifyCommand)