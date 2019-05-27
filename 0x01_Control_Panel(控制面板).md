# 0x02_Schematic_Editor(原理图编辑器)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库

所有与 EAGLE 有关的文件都在这里进行管理，并且可以实现一些基本的设定。它与各种应用程序和操作系统中常见的文件管理器相似。每个 EAGLE 文件都以小图标的形式显示在树形浏览框内。

通过鼠标右键单击树形浏览框中的某项会出现一个弹出菜单。根据不同的对象，您可以通过该菜单实现不同的操作（重命名、复制、打印、打开、创建新文件夹等）。

该 Control Panel 支持鼠标拖拽。这一特性可在 EAGLE 下的不同程序之间实现。
例如，您可以复制、移动文件、或者创建链接。将用户语言程序或脚本文件通过鼠标从 Control Panel 中拖拽到某个编辑器窗口中就能够自动运行其中的命令。例如，如果用鼠标将一个电路板设计文件拖拽到 PCB 设计编辑器中，该文件就会自动打开。

树形结构为元件库、设计规则、用户语言程序、脚本文件、CAM 处理程序和项目提供快速浏览功能。特殊元件库、文本、制造和文档文件可以包含在某个项目中以及原理图和 PCB 设计中。

当第一次运行程序时，Control Panel 与下图所示相近。如果在树形浏览框中选择了某个对象，相关详细信息将会显示在窗口的右方。只需要通过单击不同的文件夹和文件就可以体验 Control Panel 中的各个功能。

## Control Panel 树形查看对话框
### Libraries 树形分支
该分支下列出了软件中所有可用的元件库名称以及相关描述(包括树形窗口内的Description描述栏和树形窗口右方的详细描述) 。如果您展开某个元件库，库中的内容将显示出来并且每一个元素都带有简要的描述。
窗口底部显示的地址为当前选中的项目在计算机上保存的位置。
单击任意一个元件库则可以查看该元件库中包含的所有Device(元件，例如4000 )和Package (封装，例如DIL14) 。选中任意一个元件后，右方窗口内会显示该元件的原理图符号和封装图形，并且列出可能的几种不同封装，图中的" 4000D"和"4000N" ，单击相应的封装则图形会随之变化。如果此时已经打开了一个原理图编辑器窗口，则在右方窗口中的元件名称右侧会显示 ADD 选项。单击该选项后，将会自动切换到已打开的原理图编辑器窗口，并且该元件粘附在鼠标光标上，这时您就可以将其放置在该原理图中了。

![Alt text](0x01_Control_Panel(控制面板).assets/.1458530548888.png)


同样在 PCB 编辑器中，通过以上操作可以添加封装。另外可以用鼠标将元件从树形浏览框中拖拽到原理图中。如果该 Device 拥有一个以上的Package，将会自动弹出 ADD 对话框，以便选择所需要的 Package。
注意：右键元件库，选择全部使用，可以激活所有元件库，或者单击某个元件库右边的灰色圆球来单独激活。元件库项目后的绿色标记表示该元件库正在使用。即可能正用于当前项目中。该元件库中的 Device 将通过原理图或 PCB 设计中 ADD 对话框的搜索功能进行查找，以便让项目能够使用它们。如果元件库标记为灰色，则不会在该元件库中进行查找。

如果在不打开任何项目的情况下启动 EAGLE（不读取任何 EAGLE.epf 文件，并且在上次关 闭 EAGLE 前已经关闭 了项目） 并创建 一 个新项目（ 从File/New/Project 创建），则所有的元件库自动进入使用状态。然而，当打
开一个已有的项目时，如果该项目在新项目创建之前仅使用了部分元件库，则只有这一部分元件库会进入使用状态。
如果元件库编辑器（Library Editor）窗口已经打开，则您可以将某个完整的元件组（Device set）或者 Package 从 控制面板（Control Panel）中拖拽到元件库编辑器（Library Editor）中。通过这种方法您就可以在不同的元件库（Library）之间进行复制操作。



### Design Rules 设计规则树形分支
Design Rulcs 树形分支下默认只有一个设计规则文件，用户可以通过PCB 编辑器中的 DRC (设计规则检查) 功能来自定义新规则，并保存在C: \Program Files\EAGLE \dru目录下，以便在相应的设计项目中使用。
在树形窗口中双击default. dru 可以打开该文件对应的设计规则窗口。在该窗口中可以修改各项规则并且单击OK 按钮即可以保存。

![Alt text](0x01_Control_Panel(控制面板).assets/.1458530573676.png)

在 EAGLE 中可以配置特殊的 Design Rules 来规范电路板设计。这些规则可以通过数据组（data sets）的形式保存在特殊的文件里（.dru）。用于当前项目的参数组可以在树形浏览框中的设计规则（Design Rules）项中进行配置。如果没有为设计规则（DRC 命令）提供配置数据，那么 EAGLE 将自动配置参数。文件右方的标记为当前项目指定了默认参数设置。PCB 设计将根据这些标准来进行设计规则检查（DRC）。关于设计规则检查（DRC）和设计规则（Design Rules）的更多信息请参考用户手册第 121 页。

### User Language Programs 用户语言程序树形分支
该分支下列出了EAGLE 自带的所有ULP 程序，这些程序都保存在安装目录的ULP 文件夹中。
EAGLE 集成了一种类C 语言解释器，能够让用户以文本的方式编写类C 语言程序并保存为ULP 文件，通过这种程序设计人员可以访问EAGLE 的内部数据以及来自其他位置(比如网站和远程计算机等)的外部数据。
例如，熟悉C 语言的用户可以自行编写一个文件转换器，将EAGLE 的数据导出或者将外部数据导人EAGLE ，或者编写一个工具程序来实现特定的功能。EAGLE 的官方网站上提供了大量ULP 程序下载，这些程序大部分由EAGLE
爱好者自行编写，涵盖了多种岁样的功能。
http : // www. cadsoftusa . com/ downlo-ad .htm

### Scripts 脚本树形分支
脚本文件是由一系列EAGLE 命令组成的文本文件，用于实现一连串简单操作，避免逐条输入命令和参数。
![Alt text](0x01_Control_Panel(控制面板).assets/.1458530643082.png)
然后保存为DeleteAllSingnal.scr，这样就可以在需要时直接运行该脚本来快捷的删除PCB设计中所有的信号线。

### CAM Jobs CAM作业树形分支
CAM 处理程序可以产生用于制造电路板的文件，以便让PCB生产商按照设计者的要求来制作电路板，
CAM jobs 树形分支下是EAGLE 自带的几个CA M 程序实例，单击选中任意实例后，可以在右边窗口查看该实
例的描述。双击任意实例可以打开相应的配置窗口，设计人员可以在其中对输出数据进行配置。

User Language Programs 用户语言程序、Scripts 脚本、CAM 处理程序文件（CAM Jobs）
这些选项显示了各个目录下的用户语言程序文件（ *.ulp ）、脚本文件.scr和 CAM 处理程序文件.cam。它们是 CAM 处理程序输出数据时需要使用的文件。如果在控制面板（Control Panel）中选中某个文件，则会显
示该文件的详细描述。通过选项/目录设置菜单可以对路径进行设置。
### Projects 工程树形分支
Projects 树形分支下列出了EAGLE 软件保存的所有设计项目实例。单击项目右方的灰色圆球形标记，或者双击项目文件夹下的文件，就可以在相应的编辑器中打开文件，这时灰色图球变成较大的绿色圆球，再次单击绿色圆球或单击另外一个灰色标记时，则会关闭该项目下的文件。打开或关闭项目的另一个方法是在树形浏览框中双击该项目内的文件或者选中该项目内的文件后按下空格键（Space）或回车键（Enter）。
这些文件夹都位于选项/目录设置/项目菜单中所设定的路径下。在该菜单中可以设定一条以上的路径。
Projects 树形分支下的eagle 文件夹路径为`$ HOME\eagle` ， 其中`$ HOME` 为Windows系统变量。而examples 文件夹路径为`$ EAGLEDIR\projects\examples` ， 其中`$ EAGLEDIR`代表EAGLE 的安装目录。根据`$ HOME` 和`$ EAGLEDIR` 指向的路径就可以在硬盘中找到项目保存的实际位置。
![Alt text](0x01_Control_Panel(控制面板).assets/.1458530702970.png)
![Alt text](0x01_Control_Panel(控制面板).assets/.1458530708984.png)
一个项目通常包含一个名称为该项目名的文件夹和该项目的配置文件EAGLE.epf。该文件夹通常包含了您的项目的所有文件，例如原理图和PCB设计文件、特殊库文件、脚本文件等。当关闭项目时，如果已经选中了选项/备份设置菜单中的自动保存项目文件选项，则当前打开的编辑器窗口的设置将会保存在相应的项目文件 EAGLE.epf 中。如果项目文件是由另一个 EAGLE 版本生成，而不是当前版本，则会询问您是否同意覆盖该文件。

注意：项目文件夹右方的圆球形标记表示该项目文件夹下包含了项目配置文件.epf(项目配置文件)，这时该文件夹图标带省略号，未带有圆球形标记的文件夹则不包含项目配置文件，并且显示为普通的文件夹。单击灰色圆球会变成较大的绿色圆球，这不仅可以打开该项目下的原理图和PCB设计，而且表示该项目已经激活，之后针对该项目的所有设置和操作都会在退出软件时自动保存到.epf文件夹中，下次启动时 EAGLE会自动读取该配置文件所保存的信息，并恢复到最后一次退出时的状态。

## File Menu 文件
![Alt text](0x01_Control_Panel(控制面板).assets/.1458530927789.png)

该菜单项用于对Project（项目)、Schematic（原理图)、Board（PCB设计- ) 等文件的新建和打开操作，并且可以通过Save all 选项一次性保存原理图编辑器、PCB编辑器、元件库编辑器中的文件以及在软件中所做的任何修改。选择Exit 命令或者按Alt +X 组合键即可以退出软件。
- 新建：
创建一个新的 PCB 设计（电路板）、原理图、库文件、CAM 文件、用户语言程序（ULP）、脚本或文本文件。选择项目（Project）选项可以创建一个目录，与该项目有关的文件将保存在这个目录内。这些项目文件通常包括原理图 、PCB 设计、特殊的元件库、脚本文件、用户语言程序、存档文件、以及用于保存项目设置的 EAGLE.epf 文件。各种文件的默认保存目录可在选项/目录设置菜单中进行设定。CAM 处理程序文件是为 CAM 处理程序输出数据提供输出条件设定。脚本和用户语言程序（ULP）文件是包含了 EAGLE 命令语言或 EAGLE 用户语言中的命令序列的一种文本文件。它们可以通过 EAGLE 文本编辑器或者某个第三方文本编辑器来创建或编辑。

### Open 打开
打开一个上述类型的文件。
### Open recent projects 打开最近的项目
列出最近访问过的项目。
Open recent projects 打开最近的项目
列出最近访问过的项目。
- Save all 保存所有
保存所有修改过的文件。即使没有选中选项/备份设置...菜单中的自动保存项目文件（Automatically save project file）选项，该项目的当前设置仍然会保存在文件EAGLE.epf 中 。 用户设置则保存在文件EAGLErc.usr （Windows 系统下）或者 EAGLErc 中（Linux/Mac 系统下）。
### 关闭工程 Close project
项目设置将保存在当前项目目录下的 EAGLE.epf 文件中。当您覆盖保存了老版本（6.0 以下）的项目文件时，尺寸数值将会以另一种格式存档。如果您再次用老版本的 EAGLE 载入该文件，所有的菜单项（例如线宽或钻孔直径）都会恢复到默认值。
### Exit 退出
关闭程序。当再次启动 EAGLE 时，将恢复上一次程序退出时的状态，即程序窗口以及其他工作环境参数保持不变。如果上一次关闭前没有载入任何项目，则再次启动软件时只会打开控制面板（Control Panel）。当您在任何 EAGLE 程序模块打开的情况下通过 Alt-X 热键退出 EAGLE 时，当前状态也会得到保存。
如 果 您 通 过 选 项 / 用 户 界 面 菜 单 禁 用 了 编 辑 器 窗 口 （ Editor windows）的下拉菜单（Pull-down menu），则 Alt+X 热键失效。这时请使用 QUIT 命令。您也可以通过 ASSIGN 命令来将 QUIT 命令关联到热键 Alt+X。

## View Menu 查看
![Alt text](0x01_Control_Panel(控制面板).assets/.1458530978544.png)
- Extended mode 扩展模式
The Documentation and the Project branch分支 of the tree view show all files bydefault. 
文件和项目分支的树状视图默认显示所有文件。
Image and other binary files can be opened directly with the appropriate相应 default application. 
图片和其它二进制文件可以在相应的默认应用中被打开。
If this mode is switched off, only EAGLE related files will be shown.
假如该模式是关闭的，仅仅显示EAGLE相关文件。
- Refresh 刷新
刷新树形浏览框中的内容。
- Sort 排序
树形浏览框中的内容将以名称（name）或类型（type）排序。
## Options Menu
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531016812.png)
### 目录设置：设置文件存放的路径
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531035688.png)
	`$EAGLEDIR` : 表示EAGLE 的安装目录，如果EAGLE 安装在D: \EAGLE 目录下，则`$  EAGLEDIR\lbr `表示元件库的路径为D : \EAG CE\lbr 。
`$HOME`: 如果在操作系统的环境变量中设置了HOME 变量，则该参数指向HOME变量所定义的路径。如果没有在操作系统的环境变量中设叠HOM'E 变量，则该参数指向的路径由操作系统注册表中的字符串决定，字符串位置如下: HKEY_ CURRENT_ USER\Software \Microsoft\ Windows\ Current Version \Explorer\Shell Folders \Personal，字符串Personal 的值即为`$HOME` 变量代表的路径，在Windows 系统中一般情况下指向我的文档文件夹。
### Backup/Locking...：备份/锁定...
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531065167.png)
- Maxim backup level : 
即最大备份级数，表示备份文件的最大保存数量，支持保存0~9个备份文件，默认为9 个。在单击编辑器保存按钮后，系统自动把修改前的文件保存为备份文件，原理图文件名以 s#x 结尾，PCB 设计文件以 b#x 结尾，库文件以 l#x 结尾。x 的值可以从 1 到 9。x = 1 时表示该文件是最新的备份文件。每次单击保存按钮都会增加一个备份文件，它们都保存在相应项目的文件夹中。
- 自动保存间隔时间：
自动备份功能支持定期备份。EAGLE 对修改过的绘图自动保存文件的时间间隔，以防断电等突发情况而丢失数据，可选择off 命令来关闭该功能。时间间隔可以从 1 分钟到 60 分钟（默认为 5 分钟）。备份文件名称分别以b##、s## 和 l##结尾，它们都保存在相应项目的文件夹中。

最大备份等级：此项所保存的内容是修改之前的文件。
自动保存间隔时间：此项所保存的内容是修改之后的文件。
当单击保存按钮时，后者内容被保存在当前文件中.s##或 .b##文件会消失， * . s#1* 或. s#1文件出现(保存修改之前的内容)。所有这些备份文件在更名为常用文件后缀（brd、sch、lbr）后都可以通过EAGLE 程序进行处理。

- 自动保存工程文件 Automatically save project file：
如果启用了自动保存项目配置文件选项，则在您关闭当前项目或关闭程序时会自动保存项目配置文件，该文件名称为. epf ，位于相应项目的文件夹中。启用该选项后，软件会在项目关闭时自动保存项目的设定，比如通过编辑器中的CHANGE 命令修改的设置以及该项目所激活的文件库等设置。在不启用该选项时关闭项目，则软件不会保存对该项目设定的修改。
注意：如果要让EAGLE 每次启动时默认关闭  Automatically save project file 项，则不仅需要在取消选中状态，还需执行file>save all 命令，这样在下次启动EAGLE时自动保存项目文件会默认处于禁用状态，但再次选中该功能后，不需要save all 即可默认开启。尽管该功能可以自动保存某些设置，但在关闭编辑器或退出EAGLE时，如果看到提示保存的窗口，也应该选择保存，以保证所有修改生效。
- Enable file locking
EAGLE supports a simple file locking mechanism. 
EAGLE 支持一个简单的文件锁定机制。
All files loaded in an EAGLE drawing editor or the text editor are locked for writing by default. 
加载到 EAGLE 绘图编辑器或文本编辑器中的所有文件，默认情况下写入被锁定。
The lock is released as soon as the editor is closed or another file is loaded. 
一旦编辑器被关闭或是另一个文件被加载，锁定被释放。
The locking mechanism uses a lock file named .file.lck where file is the name of the file to be locked. 
锁定机制使用一个名为 .file.lck 的锁定文件，该文件的文件名称被锁定。
If an already locked file should be loaded, EAGLE offers提供 several choices how to proceed, like save the file with a different name, retry to load, delete or ignore the lock. 
假如已经被锁定的文件再次被加载，EAGLE 提供几种选择如何继续的选择，像是用不同的名字保存文件，重新加载，删除或忽略锁定。
Retry can be used after the lock owner has closed the file. 
在锁的拥有者关闭文件后，可以被重新使用。
Deleting the lock may fail depending on the file access rights you have for the lock file. 
删除锁可能会失败，取决于你对锁定文件拥有的访问权限。
It's advisable明智 to inform通知 the lock owner in case以防 you deleted his lock. 
它是最好告知锁的所有者，以防你删除他的锁。
The delete option is also useful, if the lock file remained保留, for example after an unintended power failure. 
删除选项也是有用的，如果锁定文件仍然存在，例如意外的断电故障后的。
If you decide to ignore the lock, you can edit the file, but you have to save it with a different name. 
如果您决定忽略锁，您可以编辑该文件，但你必须用一个不同的名称保存它。
This option is convenient, if you do not intend to change the file but just want to try or check something. 
此选项很方便，如果你做不打算更改文件，但只是想要尝试或检查的东西。
Locking is not applicable for the CAM processor and for read-only files loaded. 
锁定不是适用于CAM处理器和只读文件加载的。
Locking can be switched off in the Control Panel menu Options / 'Backup / Locking' or with the SET command. 
可以在控制面板菜单选项关闭锁定 / '备份 / 锁定' 或使用 SET 命令。
If the locking is switched off, EAGLE respects locks from other users with locking enabled (and reports this if necessary). 
如果锁关掉，EAGLE关联锁从其他用户锁定启用 （和报告这，如有必要）。
It just doesn't create own locks. 
它只是不能创造自己的锁。
The setting is stored in the eaglerc user file. 
设置存储在 eagle.rc 用户文件。
### User Interface 用户界面
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531136414.png)
#### - 控制
可以指定在编辑器窗口中显示的内容。如果您禁用控制（Controls）区域中的所有选项，则在编辑器窗口中只会显示命令行输入框。这样能够让绘图区域的可用面积达到最大化。
#### - Layout 布局: 
这一部分用于配置PCB 编辑器的Background (背景颜色)和Cursor( 鼠标光标)大小， Background 项包含了Black (黑色) 、White (白色)和Colored (彩色) 三种选择， Cursor 项下可以选择Small( 小鼠标指针)和Large ( 大鼠标指针) ，小鼠标指针在编辑器内显示为小十字形状，大鼠标指针则显示为贯穿整个绘图区域的大十字坐标轴的形状。


#### - 原理图 : 
这一部分的配置项与Layout 部分类似，区别在于该部分是针对原理图编辑器的设置，而不是PCB 编辑器。

#### - 杂项：
**Always vcctor font 始终使用矢量字体** 矢量字体能够在绘图缩放时保证字体清晰，不会变形。选项采用内嵌的矢量字体来显示和打印文本，而不使用源文件中采用的字体。使用矢量字体（Vectorfont）能够确保打印机或 CAM 处理程序的输出效果与编辑器窗口中显示的效果完全相同。除了矢量字体以外的其他字体根据系统设置而定，而不是由 EAGLE进行控制。非矢量字体的输出效果可能会与编辑器中的效果有差别。从任意一个编辑器窗口（比如 PCB 设计编辑器）中打开用户界面（ User Interface）对话框时，“总是采用矢量字体”（Always vector font）选项下还提供了一 个额外的选项名为 “ 在本会图中一直使用 ”（ **Persistent in this drawing** ） 。选中该选项能够让EAGLE 将 Always vector font 设置保存在当前绘图文件中。因而您就可以确保在另一台计算机上显示该 PCB 设计时也是采用矢量字体（例如在电路设计工作室的任一台计算机上显示）。
**Limit zoom fator 极限缩放因子**  对编辑器窗口中的最大缩放因数进行限制。绘图宽度的最小缩放等级为大约 1 毫米（约 40 mil）。关闭该选项后可见栅格的缩放宽度等级可以达到 0.003125 微米。
**Mouse wheel zoom鼠标滚轮缩放** 表示鼠标滚轮滚动一格时绘图缩放的倍数，有效值为- 10~ + 10 ，负值表示反转滚轮滚动时的缩放效果。数值为 0 时该功能关闭，这时滚轮仅用于滚动窗口。EAGLE 也支持在触摸板上使用两根手指来进行移动和缩放。
**External text editor 外部文字编辑器** 文本框用于指定外部文本编辑器，指定后在Control Panel 的树形窗口中双击ULP 或SCR 文件时，将会用该文本编辑器来打开文件，而不是EAGLE 自带的文本编辑器。若输入 “C:\Program Files\Notepad++/notepad++.exe” -n%L-c%C%F(包括引号和空格)，则指定使用 Notepad++ 作为默认文本编辑器，%F表示打开被双击的文件，如果不输入该参数，则双击时会打开一个新建的空白记事本。-n和-c为Notepad++的行参数和列参数，%L和%D为行和列的数值，比如输入-n3和-c3，则打开文件后鼠标指针自动停留在文本的第3行第3列的位置，其它编辑器可能参数有所不同，因此输入时需要不同的参数。
**Bubble help 帮助气泡**: 启用该选项后. 将鼠标指针放在Schematic 或其他编辑器巾的任意一个按钮上，将会在鼠标指针旁边显示该按钮的名称。
**User guidance 用户指导**: 启用该选项后，如果在任意一个编辑器对话框中激活了某个命令，比如"MOVEC 移动)"命令，则在编辑器对话框底部会显示关于下一步操作的提示信息，比如"Left - click to select object to movc (左键选择需要移动的对象)" 。诸如网络或信号名称、网络分类、或者元件名称和值（在使用 NET，MOVE，ROUTE，SHOW 等命令时）、以及可能的鼠标操作指示等等鼠标所选对象的相关信息将显示在编辑器窗口的状态栏中。
####  - Vertical text 竖排文字 
定义绘图中竖排文字的阅读方向，包括向上和向下阅读两种。



### Window Positions 窗口位置
 ![Alt text](0x01_Control_Panel(控制面板).assets/.1458531194745.png)
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531202553.png)
**Store Positions of the currently open windows** : 该选项并单击OK 按钮，软件会保存此时处于打开状态的每个对话框在桌面上的位置和大小， 下次打开相同的对话框时会自动恢复到前一次关闭时的状态。
**Delete all stored window positions** : 该选项并单击OK 按钮，即可以删除软件所保存的对话框位置信息。下次启动时软件将按照默认的位置和大小来显示窗口。
**注意**：通过单击Control Panel 的树形查看对话框中的工程分支下项目文件夹右方的圆球，来关闭原理图和PCB编辑器窗口时，软件会自动保存对话框位置信息，但无法通过以上选项删除，此时对话框位置信息不受以上两个选项影响。当直接通过双击项目分支下工程分支下项目文件夹内的文件来打开，或者通过 文件>打开 菜单选择除工程选项外的任意项来打开文件时，则需要关闭窗口前通过图中的第一个选项来手动保存窗口位置信息，关闭后可以通过第二个选项来手动删除窗口位置信息。


## Windows Menu
Window 菜单列出了当前所有处于打开状态的对话框名称，如图所示，表示当前
EAGLE 打开的3 个对话框，可通过该菜单来切换到需要的对话框。
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531232959.png)

## Help Menu
![Alt text](0x01_Control_Panel(控制面板).assets/.1458531275793.png)
- 常规性帮助 General : 单击该选项即可打开帮助对话框，对话框默认显示General Help 的帮助信息。
- 上下文 Contcxt : 单击该选项即可打开帮助对话框， 此处对话框默认显示Control Panel 的帮助信息。
- Control Panel : 与Context 选项的效果相同。
- EAGLE License : 该选项打开的对话框包含4 个按钮， 分别是Use license fileC 使用许可文件) 、Fr eemium(使用免费试用码) 、Run as freeware C 以免费软件运行)和Cancel (取消)。通过这些按钮可以重新选择EAGLE 的许可授权方式。
- Check for Update : 单击该选项后，软件会自动连接EAGLE 官方网站检查是否存在最
新版本。
- About EAGLE : 通过该选项可以查看EAGLE 的版本和注册信息。