'''
from files to tree display
https://www.youtube.com/watch?v=eD3a2tFLBVA
In this video, I'm reacting to this mock interview:  https://www.youtube.com/watch?v=MRy7M3E0La8&t=0s  
Python interview with a Google engineer: Print folder structure  
Save when you book a mock interview: https://www.byte-by-byte.com/intervie...
RESOURCES & LINKS MENTIONED IN THIS VIDEO:
[Free Training] Minimum Viable Interview Prep: https://www.byte-by-byte.com/training 
Coding Interview Questions and Answers Playlist: https://www.youtube.com/watch?v=c0OMP...
'''
files=[
    "/webapp/assets/html/a.html",
    "/webapp/assets/html/b.html",
    "/webapp/assets/js/c.js",
    "/webapp/index.html"
]
folders={}
for fi in sorted(files):
    parts=fi.split('/')
    #print(parts)
    file_name=parts[len(parts)-1]
    file_sep = "/"
    dir=file_sep.join(parts[0:len(parts)-1])
    #print(dir,file_name)
    if dir in folders:
        folders[dir].append(file_name)
    else:
        folders[dir]=[file_name]
prev_dir="" 
for d in folders.keys():
    #print(d,folders[d])
    if d!=prev_dir:
        prev_parts=prev_dir.split('/')
        this_parts=d.split('/') 
        indent=0   
        prev_dir=d    
        for i in range(len(this_parts)):
            if i>=len(prev_parts) or (prev_parts[i] != this_parts[i]):
                break
            indent += 1
        for i in range(indent,len(this_parts)):
            print((indent-1)*'  ','--'+this_parts[i])
            indent += 1
    for file_name in folders[d]:
        print((indent-1)*'  ',"-"+file_name)
