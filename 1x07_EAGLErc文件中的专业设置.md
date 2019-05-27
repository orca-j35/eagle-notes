# 1x07_EAGLErc文件中的专业设置
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库

Options for Experts in eaglerc

>The user­specific file eaglerc.usr for Windows and .eaglerc for Linux and Mac stores various settings defined during the work with EAGLE. 
>Among them you find some expert settings that can be adjusted in this file directly. 
>The most important of them are listed here.
>Since version 5.2 it is possible to change these parameters with the help of the SET command in the command line. 
>Please see the help function about the SET command for details.

Windows 系统下的 EAGLErc.usr 以及 Linux 和 Mac 系统下的 .EAGLErc 用户自定义文件保存了使用 EAGLE 时所定义的各种不同设置。
其中您可以看到一些能在该文件中直接修改的专业设置。
在此列出了大部分重要的设置。
从 5.2 版开始通过在命令框中输入 SET 命令就可以修改这些参数了。
请参看 SET 命令的帮助页面以获取更多信息

## 1. CAM Processor – Suppress Drills/Holes Warning

>If you want to suppress the warning that you should activate the Drills and the Holes layer for generating Drill data, write the following line in the eaglerc file 
>Warning.Cam.DrillsAndHolesConcurrent = "0"

假如你想要禁止警告，你应该激活 Drills 和 Holes 层以产生钻孔数据，写入下列文件在 eaglerc 文件中
Warning.Cam.DrillsAndHolesConcurrent = "0"

## 2. Change Component Value Warning
修改元件警告信息
>Some users don't want the warning message about a part not having a user definable value, so this warning can be disabled by appending the line 
>Warning.PartHasNoUserDefinableValue = "0"
>to the file.

某些用户不希望看到关于某元件不具备用户可定义值的警告信息，则该警告信息可以通过在该文件中加入以下命令行来禁用。
Warning.PartHasNoUserDefinableValue = "0"

## 3. Consistency Check
一致性检查
>In order to handle Board/Schematic pairs that have only minor inconsistencies, the user can enable a dialog that allows him to force the editor to perform Forward&Back Annotation, even if the ERC detects that the files are inconsistent. 
>This can be done by appending the line:
>Erc.AllowUserOverrideConsistencyCheck = "1"

为了对仅有很小差别的 PCB 设计和原理图进行一致性处理，即便是 ERC 检测到文件不一致的情况下，用户也可以启用一个对话框来强制编辑器执行正反向标注。
通过在该文件中加入以下命令行可以实现该操作：
Erc.AllowUserOverrideConsistencyCheck = "1"

>PLEASE NOTE THAT YOU ARE DOING THIS AT YOUR OWN RISK!!!
>If the files get corrupted in the process, there may be nothing anybody can do to recover them. 
>After all, the ERC did state that the files were inconsistent!
>请注意执行该操作的风险自负！！！
>如果在该过程中文件受到损坏，没有任何方法能够恢复文件。
>毕竟 ERC已经提示文件存在不一致的情况！

## 4. Delete Wire Joints
删除线路连接点
>If you absolutely insist on having the DELETE command delete wire joints without pressing the Ctrl key, you can append the line 
>Cmd.Delete.WireJointsWithoutCtrl = "1"
>to the file.

如果您一定要在不按下 Ctrl 键的情况下用 DELETE 命令来删除线路接点，您可以在该文件中加入以下命令行。
Cmd.Delete.WireJointsWithoutCtrl = "1"

## 5. Device Name as Value for all Components
将元件的名称作为所有元件的值
>Some users always want to use the device name as part value, even if the part needs a user supplied value. 
>Those who want this can append the line
>Sch.Cmd.Add.AlwaysUseDeviceNameAsValue = "1"
>to the file.

即使某元件需要一个用户提供的值的情况下，某些用户仍然希望能够总是用元件名称来作为该元件的值。
这时可以在该文件中加入以下命令行。
Sch.Cmd.Add.AlwaysUseDeviceNameAsValue = "1"

## 6. Disable Ctrl for Radius Mode
禁止使用 ctrl半径模式
>If you don't like the special mode in wire drawing commands that allows for the definition of an arc radius by pressing the Ctrl key when placing the wire, you can add the line
>Cmd.Wire.IgnoreCtrlForRadiusMode = "1"
>to the file. This will turn this feature off for all commands that draw wires.

如果您不愿意采用在绘制线路时通过按下 Ctrl 键来绘制圆弧的这种线路绘制命令的特殊模式，您可以在该文件中加入以下命令。
Cmd.Wire.IgnoreCtrlForRadiusMode = "1"
这样将在所有线路绘制命令中关闭该功能。

## 7. Group Selection
对象组选择
>Since the context menu function on the right mouse button interferes with the selection of groups, a group is now selected with Ctrl plus right mouse button. 
>If you want to have the old method of selecting groups back, you can add the line 
>Option.ToggleCtrlForGroupSelectionAndContextMenu = "1"
>to the file. 
>This will allow selecting groups with the right mouse button only and require Ctrl plus right mouse button for context menus.

由于鼠标右键的弹出菜单与对象组的选择之间存在干扰，因此现在可以通过 Ctrl 加上鼠标右键来选择对象组。
如果您想要使用以前的方式来选择对象组，您可以在该文件中加入以下命令行。
Option.ToggleCtrlForGroupSelectionAndContextMenu = "1"
该命令允许仅使用鼠标右键选择对象组并且需要在按下 Ctrl 键时通过鼠标右键来使用弹出菜单。

## 8. Load Matching File Automatically
自动载入相关文件
>If you have a board and schematic editor window open and load another board (or schematic) in one of these windows, and if that other drawing has a matching schematic (or board), EAGLE asks whether that other drawing shall also be loaded. By setting Option.
>AutoLoadMatchingDrawingFile = "1"
>this query will be suppressed.

如果您同时打开 PCB 和原理图编辑器窗口并且载入另一个电路板文件（或者原理图），当被载入这个绘图文件有相关联的原理图（或电路板文件）存在时 ，EAGLE 会询问是否同时载入相关联的文件。
通过以下设置：
Option.AutoLoadMatchingDrawingFile = "1"
可以关闭询问机制。

## 9. Name of Net, Busses, Signals and Polygons
网络、总线、信号和多边形的名称
>If a net consists of more than one segment, the NAME command by default acts only upon the selected segment. In order to rename the entire net set
>Cmd.Name.RenameEntireNetByDefault = "1"
>This parameter also applies to busses.
>If a signal contains a polygon, and the NAME command is applied to that polygon, by default only the polygon gets renamed. Setting
>Cmd.Name.RenameEntireSignalByDefault = "1"
>makes the NAME command act upon the entire signal by default.

如果一个网络包含了多个线段，则默认情况下 NAME 命令仅作用于选中的线段。
要对整个网络进行重命名，请使用如下设置：
Cmd.Name.RenameEntireNetByDefault = "1"
该参数同样对总线有效。
如果一个信号包含了多边形，并且对多边形执行了 NAME 命令，则默认情况下只有该多边形被重新命名。
通过以下设置：
Cmd.Name.RenameEntireSignalByDefault = "1"
可以实现默认情况下 NAME 命令对整个信号有效。

## 10. Open Project
打开项目
>The automatic opening of the project folder at program start (or when activating a project by clicking onto its gray button) can be disabled by appending the line
>ControlPanel.View.AutoOpenProjectFolder = "0"
>to the file.

在程序启动时（或者当通过单击项目的灰色圆点来激活项目时）自动打开项目文件夹的功能可以通过在该文件中加入以下命令行来禁用
ControlPanel.View.AutoOpenProjectFolder = "0"


## 11. Panning Drawing Window
平移绘图窗口
>Panning can be done with the Ctrl button (as in previous versions) by writing
>Interface.UseCtrlForPanning = "1"
>into the file. Note, though, that the Ctrl key is now used for special functions in some commands, so when using these special functions (like selecting an object at its origin in MOVE) with this parameter enabled you may inadvertently pan your drawing window.


通过在该文件中写入以下命令行则能够用 Ctrl 键实现绘图窗口平移功能（与之前版本中的用法相同）
Interface.UseCtrlForPanning = "1"
但是请注意，这时 Ctrl 键用于某些命令的特殊功能，因此在启用该参数的情况下使用这些特殊功能时（比如在 MOVE 命令下选中对象的原点），您可能会不经意的平移您的绘图窗口。

## 12. Polygon Edges as Continuous Lines
用连续直线显示多边形边缘
>If you don't like the way unprocessed polygons display their edges (as dotted lines), you can add the line
>Option.DrawUnprocessedPolygonEdgesContinuous = "1"
>The edges of polygons will be displayed as continuous lines then.

如果您不喜欢多边形各个边的显示方式（点状线），您可以在该文件中加入以下命令
Option.DrawUnprocessedPolygonEdgesContinuous = "1"
多边形的边将显示为连续直线。

## 13. Reposition of the Mouse Cursor
>Normally EAGLE does not automatically position the mouse cursor. 
>However, if you prefer the cursor to be repositioned to the point where it has been before a context menu in the drawing editor was opened, add the line:
>Option.RepositionMouseCursorAfterContextMenu = "1"

鼠标重新定位一般来说 EAGLE 不会自动定位鼠标的位置。
但是如果您希望将鼠标重新定位到在绘图编辑器中打开弹出菜单之前的位置，请在该文件中加入以下命令行：
Option.RepositionMouseCursorAfterContextMenu = "1


## 14. Units in Dialogs
对话框中的单位
>The automatic unit determination in dialog input fields can be controlled by appending the line
>Interface.PreferredUnit = "x"
>to the file, where "x" can be
>"0" for automatic unit determination (default)
>"1" for imperial units
>"2" for metric units.

对话框中文本输入框内的单位自动确定功能可以通过在该文件中加入以下命令行来实现
Interface.PreferredUnit = "x"
这里“x”可以是：
"0" 代表开启单位自动确定（默认）
"1" 代表英制单位
"2" 代表公制单位