# -*- coding:gbk -*-
import os,sys,re
with open("1.html","w") as of:
    of.write("<meta http-equiv=\"content-type\" content=\"text/html; charset=gbk\">\n")
with open(sys.argv[1],"r") as f:
    for t in f.readlines():
        try:
            t=t.replace(' ',"&nbsp;").decode("utf-8").encode("gbk")
        except UnicodeEncodeError as e:
            t=""
        if re.search('@@.*@@',t)<>None:
            t=t.replace(re.search('@@.*@@',t).group(),"")
        if t.startswith("+"):
            t="<p style=\"line-height:50%\"><font color=green>"+t.rstrip()+"</font></p>\n"
        elif t.startswith("-"):
            t = "<p style=\"line-height:50%\"><font color=red><s>" + t.rstrip() + "</s></font></p>\n"
        elif t.startswith("&nbsp;"):
            t = "<p style=\"line-height:50%\">"+t.rstrip()+"</p>\n"
        else:
            t =""
        with open(os.path.splitext(sys.argv[1])[0]+".html","a+") as of:
            of.write(t)