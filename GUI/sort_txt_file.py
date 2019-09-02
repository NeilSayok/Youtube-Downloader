import operator

def correct_txt(filepath):
    for file in ('done.txt','err.txt'):
        lenth = -1
        file = filepath+file
        fh = open(file,'r')
        x = {}
        for i in fh.readlines():
            if not i.strip() == '' :
                x[int(i[i.find(':')+1:i.find('.')].strip())] = i
                if len(i) > lenth:
                    lenth = len(i)
        sorted_x = sorted(x.items(), key=operator.itemgetter(0))
        lines =[]
        for i in sorted_x:
            lines.append(i[1])
        fh.close()
        fw = open(file,'w')
        
        fw.write("No of lines = " + str(len(lines)) + "\n")

        for i in lines:
            fw.write(i)
        fw.write("="*lenth + "\n")
        fw.close()

    print("Done")

