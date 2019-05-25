[TOC]

# 让开发Flutter更简单
在开发Flutter应用的过程中，遇到了一些重复性的工作，这里做一个简单的总结。

## 生成assets目录树
### 描述
在Flutter中使用资源文件需要在`pubspec.yaml`文件中指定资源的路径，如：
```
flutter:
  assets:
    - assets/my_icon.png
    - assets/background.png
```
每次添加资源文件时，我都得手动输入，如果成百上千个资源文件要添加，那我的敲到什么时候。为了节省时间，是时候编写一个[脚本](https://github.com/huntto/EasyFlutter/blob/master/traverse.sh)来自动完成这部分工作。

### 方法
1. 下载[traverse.sh](https://github.com/huntto/EasyFlutter/blob/master/traverse.sh)到你的计算机当中。
2. 环境配置（可选）：
    * 把[traverse.sh](https://github.com/huntto/EasyFlutter/blob/master/traverse.sh)拷贝到`/usr/local/bin`目录下；
    * 使用命令`chmod +x /usr/local/bin/traverse.sh`确保[traverse.sh](https://github.com/huntto/EasyFlutter/blob/master/traverse.sh)可执行；
    * 然后执行命令`ln /usr/local/bin/traverse.sh /usr/local/bin/traverse`生成软连接。
3. 使用`traverse`命令。进入`assets`目录，如：
    ```
    ➜  assets ls
    images
    ```
    然后使用命令：
    ```
    traverse -p "- assets/" images
    ```
    即可得到如下输出：
    ```
    - assets/images/home/btn_about_normal.png
    - assets/images/home/btn_about_pressed.png
    - assets/images/home/btn_arrow_up_normal.png
    - assets/images/home/btn_arrow_up_pressed.png
    - assets/images/home/btn_help_normal.png
    - assets/images/home/btn_help_pressed.png
    - assets/images/home/btn_scan_normal.png
    - assets/images/home/btn_scan_pressed.png
    - assets/images/home/btn_scan_small_normal.png
    - assets/images/home/btn_scan_small_pressed.png
    - assets/images/home/guide_first_one.png
    - assets/images/home/guide_first_two.png
    - assets/images/home/guide_second_one.png
    - assets/images/home/guide_second_two.png
    - assets/images/home/icon_device_indicator.png
    - assets/images/home/icon_select_off.png
    - assets/images/home/icon_select_on.png
    - assets/images/home/icon_wifi_indicator.png
    - assets/images/home/maxhub_logo.png
    - assets/images/menu/Icon_control.png
    - assets/images/menu/Icon_mirror.png
    - assets/images/menu/icon_audio.png
    - assets/images/menu/icon_connected.png
    - assets/images/menu/icon_document.png
    - assets/images/menu/icon_help_normal.png
    - assets/images/menu/icon_help_pressed.png
    - assets/images/menu/icon_picture.png
    - assets/images/menu/icon_video.png
    - assets/images/widget/icon_black_back.png
    - assets/images/widget/icon_white_back.png
    ```
    然后你就可以把这些输出拷贝到你的`pubsepc.yaml`文件中了。
    
## strings.xml文件转strings.arb文件
### 描述
如果你有一个Android项目，想要把这个项目使用Flutter来实现，这时候你可能会遇到一个问题：国际化（多语言支持）。如果你和我一样使用的是Flutter i18n这个Android Studio插件。
> Flutter i18n会根据`/res/values/string_*.arb`文件自动生成`i18n.dart`文件，使用`i18n.dart`可以很方便的实现多语言支持。

这时候你需要把`strings.xml`文件中的每一个字符串以json的格式添加到`strings_*.arb`文件中，如果还支持不同国家的语音，那这工作用手工来完成得多无聊啊。

### 方法
同样这次也采用脚本来实现`strings.xml`转`strings_*.arb`文件，不过这次使用的是python3，所以要确保你的计算机上装有Python3。

1. 下载[axs2fjs.py](https://github.com/huntto/EasyFlutter/blob/master/axs2fjs.py)脚本。
2. 使用如下命令进行转换：
    ```
    python3 axs2fjs.py -i your_path/string.xml -o your_path/strings_en.arb
    ```
3. 将生成的`strings_*.arb`文件拷贝到Flutter i18n插件指定的目录中。

... 持续更新中 ...

## 参考文档
[1] [在Flutter中添加资源和图片](https://flutterchina.club/assets-and-images/)
[2] [Python3 JSON 数据解析](https://www.runoob.com/python3/python3-json.html)
[3] [Python3 XML 解析](https://www.runoob.com/python3/python3-xml-processing.html)
[4] [Python模块之命令行参数解析](https://www.cnblogs.com/madsnotes/articles/5687079.html)
[5] [国际化Flutter App](https://flutterchina.club/tutorials/internationalization/)