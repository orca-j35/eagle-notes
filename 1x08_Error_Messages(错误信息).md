# 1x08_Error_Messages(错误信息)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库



## 1. When Loading a File
当载入文件时

### 1.1 Restring smaller than in older version
铜箔的圆环尺寸小于旧的版本中的尺寸
![Alt text](1x08_Error_Messages(错误信息).assets/.1465287262282.png)
➢ Pad diameter changed

>In EAGLE version prior 4.0 the pad diameter has been fixed in the Package definition. 
>Due to the given values in the Design Rules the pad diameters have changed.
>Please check and, if required, change the Restring settings. 
>Run the Design Rule Check in any rate to recognize possible clearance errors.

在 EAGLE 4.0 之前的版本中焊盘直径在 Package 定义中就已经确定了。
之后的版本由于设计规则中已经规定了数值，因此焊盘直径会被修改。
请在必要时检查并修改 Restring 设置，并随时运行设计规则检查来识别可能的间距错误。

### 1.2 Library objects with the same names
名称相同的元件库对象
![Alt text](1x08_Error_Messages(错误信息).assets/.1465287374630.png)
➢ Update report: Objects with the same name
更新报告：名称相同的对象

>The Text Editor shows this message if you attempt to load an older file (BRD or SCH) that contains different versions of a library element. 
>In this case it added @1, @2, @3... to the names of the Devices so that they can be identified.
>This message can also appear if you use COPY and PASTE commands.

如果您试图载入一个旧版本文件（比如 BRD 或 SCH 文件）并且该文件包含了某个库文件的不同版本，则文本编辑器将会显示该信息。
这时会在元件名称中加入@1，@2，@3 等字符以便区分。
在您使用 COPY 和 PASTE 命令时也会显示该信息。


### 1.3 Pad, Via Replaced with a Hole
用安装孔替换焊盘和过孔
>In older versions of EAGLE it was possible to define pads in which the hole diameter was larger than the pad diameter.
>This is no longer permitted.
>If you attempt to load a library file that was created with an earlier version and that contains such a pad, the following message appears:

在旧版 EAGLE 中可以定义焊盘的安装孔直径大于焊盘直径。现在的版本中已经取消了该功能。
如果您试图载入由较早版本的软件创建的库文件并且该库文件包含了以上提到的焊盘，则会出现以下信息：

![Alt text](1x08_Error_Messages(错误信息).assets/.1465287691054.png)
➢ 更新信息：用安装孔替换过孔

>The pad or via is automatically converted into a hole, provided it is not connected by CONNECT to a pin in one of the library's Devices.
>If there is pad that has a connection to a pin (it is defined in the library), the following message appears:
>In that case the Library file must be manually edited in order to correct the pad. 
>Then you can update the board file with the new library definition.

如果该焊盘或过孔不会通过 CONNECT 命令连接到任何一个库文件元件中的任何一个引脚，则它们会自动替换为安装孔。
如果焊盘连接到某个引脚（在元件库中定义），则会显示以下信息：
![Alt text](1x08_Error_Messages(错误信息).assets/.1465287883786.png)
➢ 更新报告：用安装孔替换焊盘
这时库文件必须手动修改以便连接焊盘。
然后您就可以用新定义的元件库来更新电路板文件了。

### 1.4 Skipped unsuitable objects
>If this message is shown, while you are loading a file or copying objects with COPY and PASTE from one file into another, the data structure contains objects that do not belong to the current file type and can't be displayed. 
>For example, a text or rectangle that has a non­orthogonal angle and is placed in a user­defined layer (above 100) in the Layout editor which should be pasted into a schematic. 
>The Schematic editor doesn't allow non­orthognal angles and therefore can't display such an object.
>This message could be prompted as well, if the file's origin is one of the first EAGLE versions. 
>The file can be used without problems nevertheless. 
>The data structure is cleaned up automatically while loading it.

忽略不适合的对象 Skipped unsuitable objects
当您载入文件时或者用 COPY 和 PASTE 命令将对象从一个文件复制到另一个文件中时，如果出现该信息，则说明该数据中包含了不属于当前文件类型的对象并且不能显示。
例如，将一个 PCB 编辑器内用户自定义层中（第 100 层以上）带有非直角的文本或多边形放置到原理图编辑器中时，由于原理图编辑器不允许非直角存在，因此无法显示这样的对象。
如果该文件是由第一版 EAGLE 创建的，则也会弹出该信息。但是该文件仍然可以正常使用。
在载入时其数据结构会被自动清除。

### 1.5 Can't Update File
>If this message appears when loading an EAGLE file that was made with a version earlier than 2.60 it is necessary first to convert the file.
>The program update26.exe, which is located in the eagle/bin directory, is used for this purpose.
>Copy the file that is to be converted into the directory containing both update26.exe and the file layers.new. 
>Then open a DOS window under Windows, and change into this directory. Type the command:
>update26 dateiname.ext
>The file is converted, after which it can be read by the new version of EAGLE.
>If the conversion is successful, the message in the DOS box is: ok...
>If the message Please define replacement for layer xxx in layers.new should appear, it means that you have defined your own layers in layout/schematic/library.
>Because of the new layer structure used since version 2.6, a new layer number (greater than 100) must be assigned.
>This requires you to edit the file layers.new using a simple text editor, adding, for example, a new layer number as the last line of the file. 
>If, for instance, you have used layer 55, and want to give it number 105, enter:
>55 105
>![Alt text](1x08_Error_Messages(错误信息).assets/.1465288269148.png)
>更新报告：文件版本低于 2.6 版

无法更新文件
如果在载入低于 2.60 版本的 EAGLE 所创建的文件时出现该信息，则需要首先转换该文件。
位于 EAGLE/bin 目录下的 update26.exe 程序即用于该转换功能。
将需要转换的文件复制到包含了 update26.exe 和 layers.new 文件的目录下。
然后打开 Windows 中的 DOS 窗口并进入该目录。
输入命令：
update26 dateiname.ext
该文件转换后即可用于新版 EAGLE。
如果转换成功，则会在 DOS 窗口中显示：
ok...
如果出现“Please define replacement for layer xxx in layers.new”的信息，则表示您已经在 layout/schematic/library 中定义了自定义层。
由于从 2.6 版开始使用了新的层架构，所以应该使用新的层编号（大于100）。
这需要您用某个普通的文本编辑器来编辑 layers.new 文件，在该文件的最后一行加入信息，比如新的层编号。
例如，如果您使用了第 55 层，并且想要将其定义为 105 层，请输入：
55 105


## 2. In a Library
### 2.1 Package/Symbol is in use
>If a Package or Symbol is already used in a Device, no pads or pins which are already referenced to a pin or pad with the help of the CONNECT comand, may be deleted . 
>In such a case EAGLE shows the following messages:
>But it is allowed to CHANGE or NAME such pins or pads. It's also possible to add further pins/pads with the PIN or PAD/SMD command and you are allowed to DELETE pins/pads which are not referenced via the CONNECT command.
>This message also appears, if you try to remove the whole Package/Symbol from the library with the REMOVE command.
>You have to delete the whole Device or the Package variant or symbol in the Device before.

![Alt text](1x08_Error_Messages(错误信息).assets/.1465288485048.png)
编辑 Package 或 Symbol 时的错误信息

Package/Symbol 正在使用
如果 Package 或者 Symbol 已经用于某个元件，则通过CONNECT 命令与某个引脚或焊盘关联的焊盘或引脚无法被选中。
这时 EAGLE 会显示以上信息：

但是可以对这些引脚或焊盘使用 CHANGE 或 NAME 命令。
也可以用 PIN 或者PAD/SMD 命令来添加更多的引脚/焊盘，并且您还可以用 DELETE 命令来删除没有通过 CONNECT 命令进行关联的引脚/焊盘。

## 3. In the CAM Processor
在 CAM 处理程序中
### 3.1 Polygon may cause extremely large plot data
多边形敷铜区可能造成过于庞大的绘图数据
![Alt text](1x08_Error_Messages(错误信息).assets/.1465288819430.png)
多边形的线宽为 0

>This message appears, if you selected a layer in the CAM Processor which contains a signal polygon in the layout whose line thickness is less than the resolution of the selected output driver (Device).
>In order to avoid unnecessary large plot files you should assign a higher value to the polygon's line width (CHANGE width).

如果您在 CAM 处理程序中选择了一个层，并且该层的 PCB 设计中包含的多边形敷铜区的线宽小于选定输出驱动的分辨率所能输出的线宽，则会显示该信息。
为了避免不必要的过大绘图文件，您需要为多边形敷铜区线宽分配一个较大的值（命令 CHANGE width）。

## 4. In the Light, Free Trial or Standard Edition
在简化版、免费试用版和标准版中
### 4.1 Can't perform the requested action
无法执行所请求的操作
![Alt text](1x08_Error_Messages(错误信息).assets/.1465288949285.png)
>This message is shown if the limits of the Light, Free Trial or Standard Edition are exceeded. 
>This can be the case, for example, if you want to place a part outside the Layout size limits, if you want to start the Autorouter, or set parameters for the Follow­me router, although there are parts outside the Layout limits, or you want to define a not allowed inner layer.

如果超出简化版、免费试用版或者标准版软件的限制，则会显示该信息。
超出限制的情况可能是您要放置一个超出 PCB 设计的尺寸限制的元件，或者您想要启动 Autorouter（自动布线器），或者为 Follow-me router（跟随布线器）设置参数，又或者有超出 PCB 设计限制的元件存在，以及定义不被允许的内部层。