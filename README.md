# copymanga
拷贝漫画爬虫

最近找到一个漫画网站，还不错，只是他的lazyload机制实在是不舒服

解决方案目前大致有两个
1、爬虫，将希望看的漫画下载到本地看
2、写个chrome插件，将lazyload去掉，改为一次性加载

先尝试用1方案
爬取指定漫画

爬取中遇到问题：漫画目录是js动态生成的，并且获取目录好像还是加密的，虽然解密过程应该是可以找到代码的，懒得找了，直接用selenium吧；
好久不用了，selenium更新了好几百个版本，更费内存了，只能放到服务器上去跑了。

爬取内容的时候也是遇到了新情况，这些盗版平台居然在防爬虫能做出各种花里胡哨，厉害了。文件名是动态生成的，同目录算法。但是居然需要往下滚动窗口才能触发展示所有图片链接，没有破解他的算法的情况下，还需要模拟滚动屏幕。