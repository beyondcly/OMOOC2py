<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Py Tkinter-GUI 日记本](#py-tkinter-gui-%E6%97%A5%E8%AE%B0%E6%9C%AC)
  - [V1.0 基本功能实现](#v10-%E5%9F%BA%E6%9C%AC%E5%8A%9F%E8%83%BD%E5%AE%9E%E7%8E%B0)
  - [V1.0 BUG](#v10-bug)
  - [V1.1 更新](#v11-%E6%9B%B4%E6%96%B0)
    - [代码](#%E4%BB%A3%E7%A0%81)
  - [![](http://i11.tietuku.com/451ba10adb620be6.jpg)](#httpi11tietukucom451ba10adb620be6jpg)
  - [V1.1BUG](#v11bug)
- [感想](#%E6%84%9F%E6%83%B3)
- [参考资料](#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Py Tkinter-GUI 日记本

## V1.0 基本功能实现
+ 打开文件
+ 保存文件
+ 关闭窗口
+ 关于（messagebox实现）

 代码是参考一个小例子修改过来的，它是用menu执行，我修改为按钮的方式，
参考案例Menu方式实现效果

 ![](http://i11.tietuku.com/107950c226186fed.jpg)

 
 我修改后的实现效果，界面粗暴，权当学习。

 ![](http://i11.tietuku.com/fc474516d6ac8840.jpg)

附V1.0 我的源代码


    
    # -*- coding: utf-8 -*-

    # 导入Tk GUI模块
    from Tkinter import *
    from ScrolledText import *
    import tkMessageBox
    from tkFileDialog import *
    import fileinput
    import time

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    t1 = []
    root=None

    # Add your code here
    # Delete the description when you start coding.


                  
      
    class diary(Frame):

     def __init__(self,rt):
     
        if rt == None:
          self.t=Tk()    #创建顶层窗口t（master）
        else:
          self.t=Toplevel(rt) #使用toplevel窗口模式
        self.t.title("窗口- %d"%len(t1))
        Frame.__init__(self,rt)
        self.pack(fill=BOTH, expand=1)

        '''定义按钮'''
        '''Possible values are specified as compass directions:
        "n" (north, or top edge), "ne", (north-east, or top right corner), 
        "e", "se", "s", "sw", "w", "nw" or "center".
        Layout布局
        pack side :It can be top, bottom, left and right. The default is top
        color: color names (e.g. "red") or hex RGB codes (e.g. "#ff340a").
        anchor :Pack widget will be anchored to specific side if the width is less than space is assigned. The valid edges are n,e,w,s(东西南北)
        '''

        self.open = Button(self)
        self.open["text"] = "打开文件"
        self.open["fg"] = "Blue"
        self.open["command"] = self.diary_open_txt
        self.open.pack({"side":"left"})
        self.open.pack({"anchor":"n"})
       
        self.save = Button(self)
        self.save["text"] = "保存"
        self.save["fg"] = "#0fff0a" 
        self.save["command"] = self.savefile
        self.save.pack({"side":"left"})
        self.save.pack({"anchor":"n"})
        
        self.quit = Button(self)
        self.quit["text"] = "关闭"
        self.quit["fg"] = "red"
        self.quit["command"] = self.close
        self.quit.pack({"side":"left"})
        self.quit.pack({"anchor":"n"})

        self.guan_yu = Button(self)
        self.guan_yu["text"] = "关于"
        self.guan_yu["fg"] = "red"
        self.guan_yu["command"] = self.about1
        self.guan_yu.pack({"side":"left"})
        self.guan_yu.pack({"anchor":"s"})
        
        
        
        self.f=Frame(self,width=512)
        self.f.pack(expand=1,fill=BOTH)
       
        self.st=ScrolledText(self.f,background="white")
        self.st.pack(side=LEFT,fill=BOTH,expand=1)

    #定义打开文件函数    
     def diary_open_txt(self):
        p1=END
        oname=askopenfilename(filetypes=[("文本文件","*.txt*")])
        if oname:
            for line in fileinput.input(oname):
             self.st.insert(p1,line)

        self.t.title(oname)
     
     def savefile(self):
      sname=asksaveasfilename()
      if sname:
       ofp=open(sname,"w")
       ofp.write(self.st.get(1.0,END))
       ofp.flush()  #刷新
       ofp.close()
       self.t.title(sname + u"已保存")
      
     def close(self):
      self.t.destroy() #注意此处销毁当前窗口
      print "close"

     def about1(self):
      tkMessageBox.showinfo("小小记事本","V1.0\n"
      "创建于2015年10月26日\n"
      "作者：robo_one")
      print u"关于"

      
      
    def neweditor():
     global root
     t1.append(diary(root))
      
    if __name__=="__main__":
     root=None
     t1.append(diary(root))
     root=t1[0].t
    root.mainloop()

    
## V1.0 BUG
+ 新窗口中输入中文字符→保存为新文件.txt→再次打开该文件，正常
+ 直接打开其他中文字符的文件，输出乱码。
 - 参考[Python字符编码详解](http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html)
 - [官方资料Standard Encodings](https://docs.python.org/2/library/codecs.html#standard-encodings)


## V1.1 更新

###代码
+  修改各组件的执行代码顺序
+  熟悉anchor参数， n, ne, e, se, s, sw, w, nw, or center
+  写文件增加时间戳
+  关于按钮尝试增加lambda表达式
+  增加新建（有Bug） 
+  更正GB2312编码文本的输出问题

![](http://i11.tietuku.com/451ba10adb620be6.jpg)
----------


    self.f=Frame(self,width=512)
    self.f.pack(expand=1,fill=BOTH)
   
    self.st=ScrolledText(self.f,background="gray")
    self.st.pack(side=LEFT,fill=BOTH,expand=1)
    
    self.open = Button(self)
    self.open["text"] = "打开文件"
    self.open["fg"] = "Blue"
    self.open["command"] = self.diary_open_txt
    self.open.pack({"side":"left"})
    self.open.pack({"anchor":"nw"})
    
    self.newfile = Button(self)
    self.newfile["text"] = "新建"
    self.newfile["fg"] = "black"
    self.newfile["command"] = neweditor
    self.newfile.pack({"side":"left"})
    self.newfile.pack({"anchor":"nw"})
   
    self.save = Button(self)
    self.save["text"] = "保存"
    self.save["fg"] = "black" 
    self.save["command"] = self.savefile
    self.save.pack({"side":"left"})
    self.save.pack({"anchor":"n"})
    
    self.quit = Button(self)
    self.quit["text"] = "关闭"
    self.quit["fg"] = "red"
    self.quit["command"] = self.close
    self.quit.pack({"side":"left"})
    self.quit.pack({"anchor":"center"})

    self.guan_yu = Button(self)
    self.guan_yu["text"] = "关于"
    self.guan_yu["fg"] = "red"
    self.guan_yu["command"] = lambda:self.about1()
    '''lambda后面跟的是表达式,注意调用函数需要增加()
    可以多试试它，挺不错的'''
    self.guan_yu.pack({"side":"right"})
    self.guan_yu.pack({"anchor":"center"})
        
## V1.1BUG
+ 新建窗口无法打开新的窗口，而是在原窗口下方新建
![](http://i11.tietuku.com/6167a9c30d714899.jpg)



# 感想
+ Python思想：不论函数命名、类、变量的定义力求简单明了
+ Tk.pack布局太坑了~反人类的设计，我想要的是所见即所得的GUI，目前了解的有
 + [PyQT](https://wiki.python.org/moin/PyQt)
 + [Kivy](http://kivy.org/)
   -  [github_kivy](https://github.com/kivy/kivy)
 + [Wxpython](http://wiki.wxpython.org/Getting%20Started)
+  
+ 未完待续

# 参考资料

> [Tkinter什么鬼](https://docs.python.org/2.7/library/tkinter.html?highlight=tkinter)

> [《Practical Programming in Tcl and Tk》](http://www.beedub.com/book/ "Practical Programming in Tcl and Tk")
> [关于Tk中pack的理解](http://my.oschina.net/annieduoduo/blog/71400) 
> 
> + 其实就是一个自适应的窗口容器
> + [TkDocs-最全资料](http://www.tkdocs.com/tutorial/index.html "TkDocs")
>
> [Tkinter pack_layout布局案例](http://my.oschina.net/ScottYang/blog/57192 "Tkinter pack_layout")
> 
> [Python Tkinter Frame](http://www.tutorialspoint.com/python/tk_frame.htm "Python Tkinter Frame")
> 
> [Layout management in Tkinter](http://zetcode.com/gui/tkinter/layout/ "Layout management in Tkinter")
> 
> [An Introduction to Tkinter (Work in Progress)](http://effbot.org/tkinterbook/)
> 
> [The Tkinter Scrollbar Widget](http://effbot.org/tkinterbook/scrollbar.htm )
	 
> + **get()** Gets the current slider position.Offset 0.0 means that the slider is in its topmost (or leftmost) position, and offset 1.0 means that it is in its bottommost (or rightmost) position.
> + [关于 class中的 _ _init_ _](https://docs.python.org/2.7/reference/datamodel.html#object.__init__)

> [Python类的函数为什么要有self参数？](http://www.cnblogs.com/wangkangluo1/archive/2011/09/23/2186479.html) **显胜于隐的哲学思想~~**
> 
> + [What-is-the-purpose-of-self-in-python](http://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self-in-python)
>  - [Thomas-wouters的最佳回答](http://stackoverflow.com/users/17624/thomas-wouters):Python's all for making things explicit, making it obvious what's what, and although it doesn't do it entirely everywhere, it does do it for instance attributes. That's why assigning to an instance attribute needs to know what instance to assign to, and that's why it needs self..
 
> + self在Python里不是关键字。self代表当前对象的地址。self能避免非限定调用造成的全局变量。


> [Python自然语言编码转换](http://blog.csdn.net/zhaoweikid/article/details/1642015)

