# 欢迎使用manim lecture!

这是一个用于演示如何使用manim的项目。其中分为两大类：python部分以及manim部分。

# 本项目在网上的传播，使用均需得到现任PHormation社长的授权与同意
## 环境安装与配置

**禁止使用python3.13或往上！！！！！！！！！**

### 零基础中文教程：先装 Python 与编辑器（PyCharm/VS Code）

本小节面向从未接触过 Python 的同学：先把 Python 与编辑器装好、确认版本无误，再继续下面的 mac/windows Manim 安装流程。

建议你优先选择一种使用方式，避免新手把环境装成“两套”导致混乱：

- 如果你主要在 **PyCharm** 里运行本项目：以 PyCharm 里选定的 Python 解释器与安装的软件包为准
- 如果你主要在 **系统终端** 里运行 `manim` 命令：以终端里 `python/python3` 对应的环境为准

#### 1) Python（必须先装）

**重要：禁止使用 Python 3.13 或更高版本。**

推荐版本：

- Windows：Python 3.10.x（项目 Release 已提供对应安装文件说明）
- macOS：Python 3.10.x 或 3.11.x（建议 3.11.x；如果遇到依赖问题再降到 3.10.x）

Windows 安装（推荐走本项目 Release 的版本）：

- 去本项目 `ManiumLecture` 的 Release 页面下载 `python-3.10.11-amd64.exe`
- **把安装包放在桌面**并双击安装
- **在安装第一页务必勾选 "Add python.exe to PATH"（添加到环境变量/Path）**
- 安装后按 `Win + R` 输入 `cmd` 回车，运行：

```bash
python --version
```

macOS 安装：

- 方式 A（官网下载）：https://www.python.org/downloads/macos/ 下载 `Python 3.11.x`（不要 3.13+）
- 安装后在「终端」验证：

```bash
python3 --version
```

#### 2) 编辑器/IDE（二选一或都装）

本项目现有步骤里大量使用了 PyCharm 的描述；如果你是完全新手，建议先用 PyCharm。

PyCharm：

- 下载：https://www.jetbrains.com/pycharm/download/
- 推荐：`Community`（免费版）

VS Code：

- 下载：https://code.visualstudio.com/
- 建议安装扩展：`Python`（Microsoft）

#### 3) 关于 Manim 的安装方式（避免重复安装导致混乱）

下面 `### mac 安装` 里有两种思路：

- `brew install manim`：偏“系统级”，终端里通常能直接用 `manim`
- PyCharm 解释器里安装 `manim` 包：偏“项目级”，适合在 PyCharm 里直接运行项目代码

对新手来说：**任选一种能成功运行即可**，不需要两种都做。

Windows 部分使用 `uv` 创建/管理环境：建议你在一个固定目录执行（例如桌面或你自己新建的文件夹），避免后面 `cd manimations` 找不到目录。

### mac 安装

#### 1. 安装 homebrew

在pycharm(下简称pc)终端输入
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

如果显示安装时间过长，请使用镜像源
```bash
/bin/bash -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

#### 2. 使用 brew 下载 manim

在pc终端中输入
```bash
brew install manim 
```
#### 3. 在 PyCharm 中安装

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
