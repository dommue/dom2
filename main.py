# -*- coding: cp949 -*-

import class_clawer as cc
import sys
import re

class lyrc(cc.Craw):
    
    dily={}
    
    def get_lyrc(self):
        ly=self.soup.find(id="lyrics").get_text()
        paly=re.sub('[-=.,#/?:$()}]','', ly)
        return paly
    
    def count_word(self):
        
        paly=self.get_lyrc()
        for i in paly.split():
            if i in self.dily:
                self.dily[i]+=1
            else:
                self.dily[i]=1
    
    def count_h(self):
        for i in self.dily.keys():
            print i+":",
            for j in range(self.dily[i]):
                print "*",
            print "\n"
            
    def best_word(self):
        sdily=sorted(self.dily, key=lambda k:self.dily[k],reverse=True) 
        j=0
        for i in sdily:
            print i
            j+=1
            if j==5:
                break

if __name__=="__main__":
    try: 
        option = sys.argv[1]
        url = sys.argv[2]
        
        l = lyrc(url)
        l.count_word()

        with open("attachments\\sample.txt",'w') as f:
            f.write(l.soup.find(id="lyrics").get_text())
            
        if option == "-c":
            print l.dily
        elif option == '-h':
            l.count_h()
        elif option == '-t':
            l.best_word()
        else:
            print "unknown option"
    except IndexError:
        print "usage:python[파일이름]{옵션1|옵션2|옵션3}[파일대상]"
