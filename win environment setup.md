首先按win+R启动“运行”。在打开栏输入`cmd`然后点击确定

然后在`cmd`窗口中依次输入这些指令

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
uv python install
```

**禁止使用python3.14！！！！！！！！！**

``` bash
uv init --python 3.13 manimations
```

``` bash
cd manimations
```

``` bash
uv add manim
```

去`ManiumLecture`项目的release里面下载`miktexsetup_standalone.exe`文件然后**放在桌面**

安装它（**不要更改安装路径**）

首先按win+R启动“运行”。在打开栏输入`sysdm.cpl`然后点击确定

点`高级`

点`环境变量`

点下面的那一个`新建`

变量名填`MiKTeX`，变量值填`C:\Users\10288\AppData\Local\Programs\MiKTeX\miktex\bin\x64`

连续确定

按win+R启动“运行”。在打开栏输入`cmd`然后点击确定

以管理员身份运行，依次运行下面两行

``` bash
cd manimations
```

``` bash
uv run manim checkhealth
```

