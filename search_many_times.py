from datetime import datetime

t = datetime.now()

with open('ranges.txt') as f:
        for line in f:
                b = line[:13]
                d_before = int(b[:4])
                h_before = int(b[5:7])
                m_before = int(b[8:10])
                s_before = int(b[11:13])
                a = line[15:27]
                d_after = int(a[:4])
                h_after = int(a[5:7])
                m_after = int(a[8:10])
                s_after = int(a[11:13])
                # 
                with open('times.txt') as g:
                        for line in g:
                                input_time = int(line[:-1])
                                execfile("search_time.py")

print("Time elapsed: "+str(datetime.now() - t)+" (hh:mm:ss.ms)")
