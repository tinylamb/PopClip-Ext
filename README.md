# Extensions for [PopClip](http://pilotmoon.com/popclip/)

##插件列表
1. 下载豆瓣日志信息 `DoubanDiary`
		
	依赖包: [lxml](http://lxml.de/)
	
	使用  : Popclip 遇到 
	
		http://www.douban.com/people/[anyid]/notes
	
	触发.下载该id的日志信息,保存到$HOME下.
		
2. 下载Github代码片段 `Github Mate`

	依赖包: lxml
	
	用途 : 如果不想git clone 保存全部Repo的话，就用Github Mate保存代码片段.[想法来源](https://ruby-china.org/topics/16269)
	
3. Bing.cn Search `Bing`

       墙的厉害,折衷了.
	

4. Google.mirror Search `Google`

       墙的厉害,靠[镜像](http://www.xiexingwen.com/)了

##如何创建自己的插件
###参考
 
1. [Create Your Own Custom Extension for PopClip](http://computers.tutsplus.com/tutorials/create-your-own-custom-extension-for-popclip--mac-50637)
2. [author's PopClip-Extensions](https://github.com/pilotmoon/PopClip-Extensions)
3. [popclipext branch](https://github.com/hzlzh/PopClip-Extensions)


###插件基本工作原理

There are five main kinds of actions supported by PopClip extensions.

| Action Type | Description | Example |
|------|-------------|---------|
|Service|Invoke a Mac OS X Service, passing the selected text.| [MakeSticky](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/MakeSticky)| 
|AppleScript|Run an AppleScript, with the selected text embedded.|[Evernote](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Evernote)|
|Shell Script|Run a shell script, with the selected text passed as an environment variable.| [Uppercase](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Uppercase)
|URL|Open an HTTP URL, with the selected text URL-encoded and inserted.|[GoogleTranslate](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/GoogleTranslate)|
|Keypress|Press a key combination.| [Delete](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Delete)|

###注意事项

1. Image File背景透明.[用PreView制作背景透明的图片](http://www.macx.cn/thread-2093768-1-1.html)




##如何发布自己的插件
1. 修改插件源码文件后缀 plugin -> plugin.popclipext
2. 压缩plugin.popclipext 并命名为plugin.popclipextz
3. 或 在Source目录下执行 ./ext.sh PlugginName 插件保存到Downloads中
