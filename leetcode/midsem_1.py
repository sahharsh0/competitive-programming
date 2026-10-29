'''
case study telemetry error code segeration
a mircocontroller maiantains an operational status register bufer logs[0....n-1]
where value of 0 indicates normal perfromance and any positive value represents an anomalous incident code
to optimize subsequent analytaical operations without allocating additional memeory buffers,
formulate an in place 2 pointer partioning algorithm that gathers all non zero incident codes at the front
while compacting all zero codes to the end of the array preserving the initial order of active codes
input:
logs =[ 0,503,0,404,200,0,500],n=7
output:
compact telemetry logs = [503,404,200,500,0,0,0]
'''
def compactTelemetry(logs):
    write = 0
    for read in range(len(logs)):
        if logs[read] != 0:
            logs[write] = logs[read]
            write += 1
    for i in range(write, len(logs)):
        logs[i] = 0
    return logs
logs = [0, 503, 0, 404, 200, 0, 500]
print("Compact telemetry logs =", compactTelemetry(logs))
