import collections
def func(k,messages,timestamps):
    record = {}
    deliverd = []
    for i,msg in enumerate(messages):
        if msg in record:
            last = record[msg]
            if timestamps[i] > last+k:
                deliverd.append('true')
            else:
                record[msg] = timestamps[i]
                deliverd.append('false')
        else:
            deliverd.append('true')
        record[msg] = timestamps[i] 
        
    return deliverd

if __name__=='__main__':
    messages = ['hello','hello','bye','hello']
    timestamp = [1,1,1,11]
    print(func(5,messages,timestamp))