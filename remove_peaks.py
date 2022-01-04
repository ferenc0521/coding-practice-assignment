#remove_peaks.py
def detect_peaks(a):
    peaks=[]
    if len(a)==0:
        return []
    if len(a)==1:
        return [0]
    for i in range(len(a)):
        if (i==0 and a[i]>a[i+1]) or (i==len(a)-1 and a[i]>a[i-1]) or (a[i]>a[i-1] and a[i]>a[i+1]) :
            peaks.append(i)
    return peaks
def remove_peak(a,i):
    if i==0:
        return (a[i+1:len(a)])
    else:
        if i == len(a)-1 :
            return (a[0:len(a)-1])
        else:
            return a[0:i] + a[i+1:len(a)]
#def select_peak(a,p):

def reduce_peaks(a):
    print("\nreducing")
    chunk=a
    removed=[]
    while len(chunk)>0 :
        peaks=detect_peaks(chunk)
        maxpeak = -1
        maxpeaki = -1
        for i in range(len(peaks)):
            if chunk[peaks[i]]>maxpeak:
                maxpeaki=peaks[i]
                maxpeak=chunk[maxpeaki]
        removed.append(chunk[maxpeaki])
        print (chunk,peaks,removed,maxpeaki,maxpeak)
        chunk=remove_peak(chunk,maxpeaki)
    return removed
print([7,1,2,3,11,6,5,4,8],reduce_peaks([7,1,2,3,11,6,5,4,8]))
#print([7,1,2,3,11,6,5,4,8],remove_peak([7,1,2,3,11,6,5,4,8],4))
#print([7,1,2,3,11,6,5,4,8],remove_peak([7,1,2,3,11,6,5,4,8],0))
#print([7,1,2,3,11,6,5,4,8],remove_peak([7,1,2,3,11,6,5,4,8],8))