# 欢迎使用manim lecture!
这是一个用于演示如何使用manim的项目。其中分为两大类：python部分以及manim部分。

## 环境安装与配置

**禁止使用python3.13或往上！！！！！！！！！**

### mac 安装

1. 安装 homebrew

在pycharm(下简称pc)终端输入
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. 使用 brew 下载 manim

在pc终端中输入
```bash
brew install manim 
```
3. 在 PyCharm 中安装

```aiignore
settings-> python-> interpreter-> + ->搜索manim->install package->ok->ok
```

### windows 安装

去`ManiumLecture`项目的release里面下载`python-3.10.11-amd64.exe`文件然后**放在桌面**

**在下载页第一页一定要勾选path选项！！！**

按win+R启动“运行”。在打开栏输入`cmd`然后点击确定

运行（打开VPN）：

``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

关掉`cmd`窗口

按win+R启动“运行”。在打开栏输入`cmd`然后点击确定

运行（打开VPN）：

``` bash
uv init --python 3.10 manimations
cd manimations
uv add manim
```

去`ManiumLecture`项目的release里面下载`miktexsetup_standalone.exe`文件然后**放在桌面**

安装它（**不要更改安装路径**）（**在最后一页选择检查更新**）

过一会会自动提示更新，看见了立即更新

按win+R启动“运行”。在打开栏输入`cmd`然后点击确定

运行：

``` bash
cd manimations
uv run manim checkhealth
```

*此时所有都应显示为`PASS`*

重新打开PyCharm

按`Ctrl+Alt+S`进入设置，找到`解释器`

点击`添加解释器`	点击`添加本地解释器`	点击`选择现有`	点击`Python 3.10`（刚刚下载的版本）	点击`确定`	点击左上角的`+`	搜索`manim`	点击`安装软件包`	点击`应用`	点击`确定`

在右下角锁形标志旁选择刚刚配置好的python版本（也有可能自动选择了）

运行代码`lecture1中的manim_structure.py`文件进行测试

提示为以下正常

```txt
C:\Users\10288\AppData\Local\Programs\Python\Python310\lib\site-packages\pydub\utils.py:170: RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
  warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
```

首次运行弹出`宏包安装`窗口，选择安装

接着弹出一个视频则为正常

关掉视频

去`ManiumLecture`项目的release里面下载`ffmpeg-git-essentialse`文件然后**放在桌面**

解压

解压后文件放在C盘根目录（如果你实在是不同意这样做，你可以来找我）

按win+R启动“运行”。在打开栏输入`sysdm.cpl`然后点击确定

点击`高级`	点击`环境变量` 	在`系统变量`中找到`Path`	点它，然后点`编辑` 	点击`新建`	填入`C:\ffmpeg-git-essentials\bin`	连续点击`确定`直到返回桌面

重启`PyCharm`

全部完成，恭喜！！！
