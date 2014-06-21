# Extensions for [PopClip](http://pilotmoon.com/popclip/)

##插件列表
1. 下载豆瓣日志信息

##如何创建自己的插件
参考
 
1. [Create Your Own Custom Extension for PopClip](http://computers.tutsplus.com/tutorials/create-your-own-custom-extension-for-popclip--mac-50637)
2. [gitRepo for popclipext](https://github.com/hzlzh/PopClip-Extensions)


注意事项

There are five main kinds of actions supported by PopClip extensions.

| Action Type | Description | Example |
|------|-------------|---------|
|Service|Invoke a Mac OS X Service, passing the selected text.| [MakeSticky](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/MakeSticky)| 
|AppleScript|Run an AppleScript, with the selected text embedded.|[Evernote](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Evernote)|
|Shell Script|Run a shell script, with the selected text passed as an environment variable.| [Uppercase](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Uppercase)
|URL|Open an HTTP URL, with the selected text URL-encoded and inserted.|[GoogleTranslate](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/GoogleTranslate)|
|Keypress|Press a key combination.| [Delete](https://github.com/pilotmoon/PopClip-Extensions/tree/master/source/Delete)|




##如何发布自己的插件
1. 修改插件源码文件后缀 plugin -> plugin.popclipext
2. 压缩plugin.popclipext 并命名为plugin.popclipextz