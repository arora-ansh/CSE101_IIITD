import math
import os
import random
import re
import sys

class strr_pal():
    def _init_(self,s_org,l,s_new=-1):
        self.s_org=s_org
        self.l=l
        self.s_new=s_new
    def construct_pal(self):
        string=self.s_org
        l=self.l
        pal=self.s_new
        rev=string[::-1]
        rev=list(rev)
        for i in range(l):
            if (rev[i]!='?') and (string[i]!='?') and (string[i]!=rev[i]):
                return pal
            if (rev[i]=='?') and (string[i]!='?'):
                rev[i]=string[i]
            elif (rev[i]=='?') and (string[i]=='?'):
                rev[i]='a'
        pal=''.join(rev)
        return pal

if _name_ == '_main_':
    # you have to create the class as described,take the input and print the output, create the class above and take input, create object,invoke method and print output here in this main section.
    string=input()
    l=len(string)
    o=strr_pal(string,l)
    print(o.construct_pal())