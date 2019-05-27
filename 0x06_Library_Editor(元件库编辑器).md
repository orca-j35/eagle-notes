# 0x06_Library_Editor(元件库编辑器)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库



Components are defined as Devices. 
元件被定义为devices
In the Device editing mode you do not draw anything, but you define the following:
在Device编辑模式下，你不用绘制任何图形，但是你要定义如下内容：

1. which Package variant is used,
使用了哪些封装变体

2. which Symbol(s) is/are used (called Gate within the Device),
使用了哪个/哪些 Symbol(s) (调用元件内部的Gate)

3. which names are provided for the Gates (e.g. A, B), 
为gate 提供什么名字，例如A,B

4. which technologies are available (e.g. 74L00, 74LS00, 74HCT00),
哪些工艺是可用的，例如74L00, 74LS00, 74HCT00

5.  if the Device should have additional追加 user ­definable attributes,
Device 是否需要追加用户可定义的参数

6.  if there are equivalent等效 Gates which can be interchanged互换 (Swaplevel),
等效的gate是否可以互换，设置互换等级

7. how the Gate behaves when added to a schematic (Addlevel),
当添加gate到原理图时，gate的行为，添加等级。

8. the prefix for the component name, if a prefix is used,
假如要使用前缀，要考虑元件名的前缀。

9. if the value of the component can be changed or if the value should be fixed固定 to the Device name,
元件的值是否能被修改，或元件值是否被固定到设备名。

10. which pins relate关联 to the pads of the Package (CONNECT command)
Symbol 的引脚和 Package 的封装之间的关联（CONNECT 命令）

11. whether a description for this component should be stored in the library.
元件的描述是否需要存储在元件库中。

The following diagram shows the fully完整的 defined 7400 Device with four NAND gates and a supply gate in various多个 Package and technology versions.

If you click onto one of the gates with the right mouse button, the context menu with the executable commands pops up. 
Furthermore此外 you can display the Properties of the gate. 
Click on Edit Symbol to open the Symbol Editor.

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459824546194.png)


EAGLE 的元件库以文件的形式默认保存在安装路径的 LBR 文件夹内，文件格式为 .lbr。
每一个元件库都由3 种元素组成，Symbol(原理图符号)、Package(封装符号)以及Device(元件)。
**Symbol** 用于原理图绘图
**Package** 用于PCB 编辑器的绘图
**Device** 包含了 Symbol 的引脚和 Package 的焊盘之间的对应关系。
因此在建立元件库时需要同时建立这3 种元素，才能完成一个元件库的创建工作。
需要注意的是，在 Control Panel 的 Libraries 树形分支中依次显示元件库名称、Device、Package、 Symbol，相应的 Symbol 也会包含在其所属的 Device 中。

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459326227720.png)
EAGLE 的元件库、Device 和 Package 三者的关系结构如上图。
从图中可以看出，EAGLE 的每一个元件库即为一个扩展名为 .lbr 的文件，其中包含了多个Device 和Package。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459326287775.png)
Device 可以被原理图编辑器调用，以便放置Symbol ，即原理图符号，而Package 则只能由PCB 编辑器调用，以便放置封装。
通过Control Panel 的File→ New→Library 菜单即可以打开EAGLE 的新元件库编辑主界面。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459383160418.png)

The Library Editor window opens when you load a library for creating or editing components 元件.
当您加载一个库文件来创建或者编辑元件时会打开库编辑器

A library normally has three different elements元素: Packages, Symbols and Devices.
一个元件库通常包 含 3 个 元 素 ： 封 装 （ Package ） 、 原 理 图 符 号 （ Symbol ） 和 元 件（Device）。

- A Package is a Device's housing壳体, as will be used in the Layout Editor (on the board).
  **封装（Package）**是元件（Device）的外形构架，在板卡布局编辑器中使用；
- The Symbol contains the way in which the Device will be shown in the schematic.
 **原理图符号（Symbol）**是元件（Device）在原理图编辑器中的一种表现方式；
- The Device represents表示 the link between one (or more) Symbol(s) and a Package. 
**元件（Device）**把一个或者多个原理图符号（Symbol）和一个封装（Package）关联起来，
Here we define the connection between a pin of a Symbol and the referring pad(s) of the Package.
此处的关联是指原理图符号（Symbol）的引脚和封装（Package）的焊盘之间的联系。
We call it a Device set组 if the component exists存在 in more than one Package and/or technology variant变体.
如果一个元件有多个 PCB 封装和/或多种 Technology变体，我们称之为元件组。

Even if you do not have the Schematic Editor, you can still create and edit Symbols and Devices.
即便没有原理图编辑器，您仍然可以创建和编辑 Symbol 和 Device。

A library need not contain only real components. 
元件库不仅仅包含实际的元件。

Ground or supply symbols as well as drawing frames can also be stored as Devices in a library. 
地或者电源符号的外形一样可以在库中创建，并作为一个元件（Device）来保存。

These Symbols do not normally contain any pins.
这些符号实际上并没有任何引脚。

There are also libraries that only contain Packages. 
在库中还可以创建只有封装（Package）的元件。

These libraries can only be used in the Layout Editor.
当然，这样的库只能在 PCB编辑器中使用。

Extensive大量 examples of the definition定义 of library elements are to be found in a section entitled提名为 Component Design Explained through Examples, starting on page 223 in this manual.

关于如何定义元件库元素的实例可以参考本手册第 223 页的章节《 通过实例来讲解如何设计一个元件》。

##Table Of Contents 内容列表
When a library is loaded the following window appears first:
当加载一个库时，首先出现的窗口如下：
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459385236429.png)
Library Editor: Table of Contents with three columns for Devices,Packages and Symbols (here: rcl.lbr)

The table of contents of this library is shown. 
显示了元件库的内容列表。
Three columns list all Devices, Packages and Symbols available in the library file. 
在库文件中可用的所有Devices, Packages and Symbols 在3列列表中。
Double­click on of the entries to start the editing mode.
双击进入开始编辑模式。
A right mouse­click opens a context menu offering a number of options, like Edit, Remove, Rename and Edit Description.
右键点击鼠标打开上下文菜单提供了更多选项，像是编辑、移除、重命名和编辑描述。
The context menu of a Device contains also the entries Used packages and Used symbols, of a Package or Symbol there is an entry Using DeviceSets. 
元件的上下文菜单也包含Used packages 和 Used symbols的入口，Package or Symbol 是进入DeviceSets。
This helps to understand where a Package or Symbol is used in a Device Set.
这有助于理解，使用 Package 或 Symbol 的元件组。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459386732390.png)
A Librarie's Table of Contents: Options of the context menu
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459386764568.png)

与原理图编辑器类似，元件库编辑器的主界面也是由菜单栏、操作工具栏、参数工具栏、命令工具栏、坐标栏与命令框识及绘图区组成， 下面将依次介绍这些内容。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387128138.png)

### 菜单栏
#### 文件 File
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387531271.png)
元件库编辑器的File 菜单与原理图编辑器类似，唯一不同的是，通过元件库编辑器File 菜单的Open 命令所打开的是某个元件库，而不是原理图或PCB 设计文件。在命令框中直接输入open命令也能够打开元件库。

#### 编辑
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387564952.png)
在新建元件库时打开的主界面上， Edit 菜单仅包含Stop command 命令。

#### 绘制
该菜单在主界面上无效，只有在编辑Symbol 、Package 或者Device 的时候才会显示相应的选项，这些选项将会在这3 种编辑模式中分别介绍。

#### 查看
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387748240.png)
该菜单与原理图编辑器相同。

#### 元件库
元件库编辑器的Librar y 菜单包含Description、 Device 、Package 、Symbol、Remove 、Rename 和 Update 等命令
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387832046.png)

##### 描述
等同于DESCRIPTION 命令，用于为当前的Device 、Package 或元件库添加描述信息。描述对话框的下半部分可以输入相应的描述信息，并且支持 HTML 语言格式。为Devlce、Package 和元件库输入的描述信息会显示在不同的地方，由于这里新建的对象是元件库，因此输入的信息会在选中Control Panel 的Libraries树形分支下的相应元件库时，出现在右边的对话框区域内。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459388196563.png)

##### Device
用于载入当前编辑器所打开的元件库中的元件。选择该命令后，如果编辑器已经通过 OPEN 命令打开了某个元件库，例如 40xx.lbr ，则在弹出的窗口中会显示该元件库中所有的元件，在窗口中选择需要载入的元件并单击OK 按钮，相应的元件所包含的原理图符号和PCB 设计中的封装
等信息就会显示在编辑器中。
New 文本框：新建一个元件， 在其中可以输入新建元件的名称， 单击OK 按钮后， 该元件则会保存在当前打开的元件库中。
**Dev 按钮**：在对话框中显示当前元件库中所有的元件。
**Pac 按钮**：在对话框中显示当前元件库中所有的封装。
**Sym 按钮**：在对话框中显示当前元件库中所有的原理图符号
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459388519785.png)
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459388900556.png)
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459388881042.png)

##### Package
该命令用于载入当前编辑器所打开的元件库中的封装，或者新建封装。选择该命令后所弹出的窗口上图中单击 Pac 按钮所显示的界面内容完全相同。

##### Symbol
该命令用于载入当前编辑器所打开的元件库中的原理图符号，或者新建原理图符号。选择该命令后所弹出的对话框与上图中单击 Sym 按钮所显示的界面内容完全相同。

##### 移除 Remove
该命令用于删除元件库文件以及元件库中的Device 、Package 和Syrnbol 。
需要注意的是，不论当前是否已经打开了某个元件库，该命令都可对任意元件库进行删除，例如在该命令的弹出对话框中输入40xx.lbr ， 确定后即可删除该元件库文件。
但是在单独删除Device 、Package 和Symbol 时则只对当前打开的元件库有效，而不能对其他元件库中的这三种元素进行删除，并且需要先删除Device 后才能删除相应的Symbol，否则系统会提示该Symbol 正在使用中，当前元件库中 Package 可以直接删除，例如在Remove 的弹出对话框中，输入该元件库中包含的某个元件4000.dev、或者某个原理图符号4000.sym、或者某个封装名称DIL08.pac，确定后即可删除相应的元素。
Remove 命令等同于 REMOVE 命令，在元件库编辑器命令框中，输入REMOVE 和对象的名称也能实现相同的功能。
例如运行REMOVE 40xx.lbr ，则可以删除该元件库的文件。
REMOVE 命令同样可以用于原理图和 PCB 编辑器中。可以删除指定的原理图和PCB设计文件，例如在原理图编辑器中运行REMOVE 1. sch 、或者在PCB 编辑器中运行REMOVE 1. brd ，则可以删除这两个文件。并且在原理图编辑器中还可以删除某个界面，例如运行REMOVE.s2( 请注意 s2 前面有点)则会删除第二个原理图界面。
注意: 如果不指定路径，则被删除的库文件必须位于安装目录的 lbr 根目录下， 例如40xx.lbr 必须保存在D : \EAGLE-7.5\ lbr\ 目录下，否则无法删除。如果路径不同，就需要指定路径(有空格的路径加引号)。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459389156045.png)

##### 重命名 Rename
该命令用于对当前打开的元件库中的Device 、Package 和Symbol 进行重新命名。例如在打开元件40xx.lbr 后，选择该选项并在命令行中(仅限于主界面，在其他对话框中会直接弹出新名称的输入对话框)输入修改目标的名称(需要扩展名) ，比如4001. sym 并按Enter ，然后在弹出对话框中输入新名称(不需要扩展名)。当然也可以
直接在命令框中运行RENAME 4001. dev 、或RENAME 4001. sym 、或RENAME DIL08. pac ，然后在弹出的对话框中输入新的名称即可对这三种元素进行重命令。也可以在命令后加上新名称来一步实现重命名，例如运行RENAME 400l. dev 4002 ，则该元件重新命名为4002.dev。注意，被重名的对象必须带有扩展名，而后面的新名称则可以省略扩展名。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459390400853.png)

##### 更新Update
该命令用于将指定的元件库作为更新源，对当前打开的元件库中类型相同的封装进行更新，以实现同类型封装的一致性。


#### 选项
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387871592.png)


#### 窗口
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387909674.png)

#### 帮助
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459387901871.png)

### 操作工具栏
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395403124.png)
元件库编辑器的操作工具栏中的大部分内容与原理图编辑器相同，下图中的四个图标分别对应元件库中的Table of contents/Device/Package/Symbol
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395480486.png)
From the left: Show table of contents, Load Device, load Package, load Symbol. 
These icons are shown in the action toolbar.
这些图标被显示在操作工具栏。
If you click on one of these icons with the right mouse button, or long­click with the left mouse button on one of theses icons (not show table of contents), a list with the recently最近 edited objects will pop-up.
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395510548.png)


### 参数工具栏
 元件库编辑器的参数工具栏与原理图编辑器相同。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395668744.png)
**注意**: 由于当前包括 EAGLE 在内的绝大部分 EDA 工具的原理图符号，即 Symbol 都是默认基于100mil 的标准栅格设置，因此为了实现兼容和避免错误，推荐在新建 Symbol 时将栅格设置为 100 mil 。

### 命令工具栏
#### Edit
Load Device or Package (if you only have the Layout Editor) for editing.
加载一个元件（Device）或者封装（如果您只有 PCB 编辑器）来编辑。

元件库编辑器的命令工具栏在编辑器还没有打开任何库文件时，仅显示 EDIT 命令按钮

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395820449.png)

单击该按钮后会弹出与元件库>Device同样的对话框，在该对话框中可以新建Device 、Package 和 Symbol ，关于新建这些元素的方法，在元件库创建实例中介绍。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459395985424.png)

与其他命令按钮相同， EDIT 命令按钮的功能也可以通过在命令框中执行EDIT 来实现，并且当编辑器已经打开了某个元件库时，也可以通过执行 EDIT 命令来弹出的对话框，选择该元件库中的任一种元素来进行编辑。
命令工具栏在编辑器载入了某个元件库的 Device、Package 或 Symbol 后，都会发生相应的变化。

### Library Description 描述
不仅仅是 Package 和 Device 需要描述，Library 库同样需要描述，该描述显示在 Control Panel 中 Library 分支下的该元件库所在的项。不管当前编辑模式（Symbol、Package、Device）是否处于活动状态，都可以使用元件库/描述菜单来添加描述，如果您需要还可以添加 HTML 格式的文本。

### 使用 Library
新创建的库可以在原理图编辑器和 PCB 编辑器中使用了（先用 USE 命令激活），也可以把该库标志到 Control Panel 的树形浏览区下，详情请参考帮助。现在，新建的库已经被 ADD 命令验证并能搜索。

## Symbol 编辑模式
定义一个 Symbol，也就是定义一个可以单独在原理图中使用的 Device 的一部分。比如，74LS00 就可以定义成一个非门（NAND），电源和地则定义成另外一个 Symbol。再比如电阻符号仅仅包含一个 Symbol 来表示电阻。使用 WIRE、ARC 或者其他命令，在第 94 层（Symbols 层）中设计一个原理图符号。

点击 Symbol 按钮，输入新建原理图符号的名称，并单击OK 按钮，进入Symbol 编辑界面。该 symbol 名称名词仅仅是用于程序内部，并不会在原理图中显示。

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459403804805.png)
Symbol 编辑界面与主界面大体相似，只有 Edit 菜单、Draw 菜单、View 菜单，以及命令工具栏和绘图区中增加了相应的内容。
Edit 、Draw 和View 菜单中增加的命令绝大部分都能够在编辑器的操作工具栏、参数工具栏和命令工具栏中找到相同的按钮，并且由于操作工具栏已经在元件库编辑器主界面中进行了介绍， 下面将着重介绍命令工具栏中增加的、之前没有接触过的命令按钮和参数工具栏中相应的参数项，以及Draw 工具栏中的Frame 命令。

### Menu bar 菜单栏
#### 绘制 Draw
##### Frame 框架
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459410317983.png)
用于自定义外框，当软件自带的 frames.lbr 库文件中包含的外框样式无法满足设计要求时，可以通过 Symbol 编辑界面中的Draw>Frame 命令，或者在命令框中运行FRAME 命令来自行创建一个外框库文件。
例如在编辑器中的 Symbols 层上自定义一个上下左右刻度都为5 ，并且带有设计项目名称、最后保存时间和界面数的外框，其步骤如下：

1. 选择Control Panel 上的File→ New→Library 菜单来打开元件库编辑器主界面。

2. 在主界面的操作工具栏中单击 Symbol 按钮，然后输入新建的符号名称，例如：FRAME_SYMBOL 并确定，进入原理图符号编辑界面。

3. 在命令框中运行 FRAME 命令或Draw/Frame，然后在参数工具栏中的层下拉菜单中选择 94 Symbols层， Columns 下拉菜单和Raws 下拉菜单中都选择5，负值翻转标签的方向。最后在绘图区按住鼠标左键并拖动鼠标，直至外框尺寸达到适当大小时，再次单击确定外框，也可在命令栏中输入框架角度坐标来确定。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461935633743.png)
行/列的值用来定位 Device 或者 Net 的位置，比如：使用 ULP 的帮助，或者经过计算后的 Cross-References（参考 LABEL 命令）。
可以使用 CHANGE 命令中的 Border、Rows、和 Columns 选项来确定 Frame 标签
位置和行/列数量。

因为 Frame 对象的固有特性，其本身不会旋转！FRAME 命令在原理图和 PCB 编辑器中仍然可以使用，但是它通常是用来在库中定义一个绘图区框架。

库 frames.lbr 同样包含可以和 Frame 一同使用的documentation fileds，当然，您可以设计自己的 documentation fileds。
档案记录区域包含文本变量`>DRAWING_NAME`、`>LAST_DATE_TIME` 和`>SHEET`，当然还有一些固定的文本，设计文件的文件名、最后修改日期和时间都会和设计文档页面（比如：2/3 = sheet 2 of 3）一起在原理图的档案记录区域显示。另外，变量`>PLOT_DATE_TIME` 也可以使用来记录最近打印输出的日期和时间。
所有的这些文本变量都可以放到原理图和 PCB 图（>SHEET 变量除外）中。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461938680760.png)

Frames 在 Device 编辑器中的 Addlevel 值为 Next，Documentation field 的 Addlevel 值 为 Must 。 意思是如果 Frame 存在绘图中 ， 则 Documentation field 不能被删除。
Frames 还可以定义 Package 来确保其原理图和 PCB 图保持一致，不过这些 Frames 并没有任何电器特性，因为它们没有任何引脚和焊盘。
变量>CONTACT_XREF 在电气原理图中具有特殊的含义，该变量并不在原理图中显示，但其位置却是作为触点的 Cross-Referneces 显示的保留区域。更详细的信息可以查看帮助功能中 Contact cross-references 章节。

4. 单击命令工具栏中的 WIRE 命令按钮，在外框的右下角绘制出信息标注区域。

5. 单击命令工具栏中的 TEXT 命令按钮，在弹出窗口中输入文本变量 >Drawing_Name 并确定，然后将其放置在信息标注区中。该文本变量将在外框符号放置到某个原理图中时显示该原理图的文件名，因此只要将原理图文件名定义为设计项目的名称，则外框的标注区域就会显示该项目的名称。而原理图的最后保存时间的显示，则可以通过创建外框符号时添加文本变量>Last Date Time 来实现，原理因界面数则可以用文本变量>Sheet 来实现（为了表达更清楚，可以在>Sheet 前面多添加一个纯文本 Sheet=）。
关于更多文本变量的使用方法，请在编辑器Help 菜单下General 命令的对话框中搜索关键字TEXT 。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459411315559.png)

6. 文本变量放置完成后，单击编辑器操作工具栏中的 Device 按钮，输入新建的元件名称，例如MY_FRAME 并确定. 进入元件编辑窗口。

7. 在元件编辑窗口中单击 ADD 命令按钮，从弹出对话框中选择刚才新建的FRAME_SYMBOL 符号并确定，将其放置到对话框绘图区中，单击绘图区下方的 Description 可以为该元件提供描述信息。然后单击操作工具栏中的保存按钮。输入例如 MyFrame 的名称后，将元件保存在 EAGLE 安装文件的lbr目录下，成为一个元件库文件，显示为MyFrarne.lbr 。这样便完成了自定义外框符号的创建过程。
注意: 由于外框符号不存在封装，因此并没有涉及创建封装的内容，而只包括了Symbol和Device 的创建。关于创建封装的详细内容将在本节后面通过具体的实例来进行介绍。


### Command toolbar 命令工具栏
#### Change
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459404289978.png)
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459470551761.png)

**Align**：text文字的对齐方式，Bottom底部、center中心、top顶部。

**Border**：Frame 标签边框的位置，例如四周均有边框或无右侧边框。

**Cap** : 该命令用于修改绘图中用 ARC 命令绘制的弧形的端点形状。鼠标指针指向该选项时会弹出子菜单，其中包含Flat平头和Round圆头两个选项，选择Flat 后通过左键单击某个圆弧，会将圆弧的两个端点变为平头形状;选择Round 则可以将端点变为圆头形状。

**Columns**：Frame 标签边框的列数量。

**Direction**：
NC 不连接
In 输入
Out 输出
I/O 输入/输出
OC 开集电极或开漏
Pwr 电源引脚（供电输入）
Pas 无源（比如：电阻）
Hiz 高阻输出
Sup 电源输出的地，或者电源符号

**Dline:**
Width：dimension 尺寸命令中箭头的宽度；
延长>Width：延长线的宽度，垂直于箭头的两段延长线的宽度。
延长>Length：延长线的长度，垂直于箭头的两段延长线的单位长度，以该单位为基准进行叠加。
延长>Offset：延长线的偏移，垂直于箭头的两段延长线和箭头之间的偏移量。

**Dtype**：dimension 尺寸命令中标尺类型。
平行、水平、垂直、半径、直径、角度、Leader。

**Dunit**：dimension 尺寸命令中的单位。
Unit：单位
precision：精度
show：显示单位

**Font**：该命令用于修改文本字体，包含Vector(向量字体)、Proportional (比例字体)和Fixed(固定字体)。向量字体能够在绘图缩放和打印时保持清晰并且不会变形，而比例字体和问定字体则有可能在缩放和打印时出现不清晰的问题，因此推荐采用向量字体，选择字体后单击需要修改的字体即可。
如果需要始终在绘图中采用向量字体，并且保证在不同设置的 EAGLE 中打开该绘图时不会改变字体设置，可以通过选中编辑器的Option→ User interface 菜单中的 Always vector font 命令和 Persistent in this drawing 命令来实现。

**Function**：设置引脚功能，这些功能指定了原理图符号是否显示为：简单的一个端点（None）、反向符号（Dot）、时钟符号（Clk）和反向时钟符号（DotClk）。下图给出了一个原理图符号中的 4 种表示方法：
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459405947615.png)

**Layer…** : 该命令用于选择当前的绘图层，也可用于显示当前被隐藏的层。选择该命令后会弹出一个层列表，如果其中某一层在DISPLAY 命令弹出窗口中设置为隐藏，则可以在该列表中选中这一层，确定后就会在绘图中显示该层，并且DISPLAY 命令的弹出窗口中该层也会标记为显示。

**Length**：引脚长度设置。
point: 0inch 表示引脚线不可见
short: 0.1inch
middle: 0.2inch
long: 0.3inch
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459406155538.png)

**Line distance**：行距，设置文本的行距

**Pour 敷铜**：指定敷铜类型，对一个区域进行敷铜，而不是焊盘。即实心填充（Solid）或者栅格填充（Hatch）。如果在绘图区中使用POLYGON（多边形）命令绘制了敷铜区，则可以通过该命令选择Solid (实心填充)或者 hatch(网格填充)样式。

**Ratio 比率** : 该命令用于修改字体的线宽，即字体粗细，以字体高度的百分比表示。选择该选项后，在弹出的文本框中指定需要的比例(范围为0 到31)，确定后左键单击需要修改线宽的文字即可。该选项虽然对前面提到的三种字体都能实现肉眼可见的效果，但是除了向量字体外，修改其他字体的线宽没有任何实际意义。

**Rows**：frame 标签的行数。

**Size 尺寸**: 该选项用于指定字体的高度，其单位与栅格单位相同。选择该命令后会弹出子菜单，其中列出了一系列的可选高度。也可以选择子菜单底部的” … “命令来自行输入需要的高度，最大允许高度为2inch。指定好高度后单击需要修改高度的文字即可。

**Spacing 间距**：如果敷铜类型选择为 Hatch栅格填充，则该值决定了栅格线的间距。

**Style 线样式** :该选项用于修改绘图中 WIRE、NET 和 BUS命令所绘制的线段风格，可选项有Continuous(连续)、LongDash(不连续长线)、ShortDash(不连续短线)以及DashDot(线段与点交错)。选择线段风格后单击需要修改的连线即可。在原理图编辑器中对于线段风格没有限制，但是在PCB编辑器中不允许在信号层中采用不连续的线形来绘制线路，否则DRC功能会报错。

**Swaplevel 交换等级**：Swaplevel 为 0 的意思是在同一个 Gate 中不能和其他引脚互换，除 0 以外的其他数字表示该引脚可以和其他引脚互换，前提条件是 2 个引脚的 Swaplevel 值相同，并且是处于在同一个 Symbol 中。PINSWAP 命令可以用于原理图和 PCB设计中的引脚互换。二极管的引脚是不能互换的，因此要把它们的 Swaplevel 设为 0。
电阻符号的 2 个引脚具有相同的 Swaplevel（比如：1），因此它们可以互换。
如果第 93 层（Pins 层）设置为显示，网络连接点上就会显示一个绿色圆环，Direction 和 Swaplevel 参数（Pas 和 1 ）在该层中显示。

**Text 修改文本**: 该命令用于修改绘图中采用TEXT 命令添加的文本。选择该命令后单击需要修改的文本，然后在弹出的文本框中输入新的文本并确认即可。

**Visible可见性**：引脚是否显示引脚名称、或焊盘名或同时显示两种名称，下图显示了一个原理图符号实例。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459407988303.png)
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459407705933.png)
其中引脚名称在元件符号内侧，焊盘名称在外侧编号，引脚的相关标签是固定的，文字高度也固定不变（60mil）。
如果您需要将一个引脚连接到多个焊盘上并且您在 Visible 设置项中选择了Both 选项，那么在原理图中将只会显示其中一个焊盘的名称（编号最小的那个焊盘）。焊盘名称后面有一个*号标志，说明有多个焊盘连接。

**Width 线宽**: 该命令用于修改绘图中采用WIRE 、NET 和BUS 等命令所绘制的线段宽度。选择该后弹出的子菜单中列出了当前可用的线宽，单位与当前绘图的栅格单位相同。选择需要的线宽或者通过”… “选项自定义一个线宽，然后单击需要修改的线段即可。

#### Pin 绘制引脚
用于在创建元件符号时添加引脚。命令只有在原理图符号编辑模式中才有效。name 命令用于修改引脚名。
在编辑器的参数工具栏会出现相应的参数项。
如果想一次更改多个pin的属性，可以先用 GROUP 命令定义一个对象组，然后输入 CHANGE 命令，按住 Ctrl 键，在绘图区表面单击鼠标右键来改变参数和值。
PIN 命令的参数工具栏包括了 16 个按钮和两个下拉菜单，其中左边的 16 个按钮以 4 个按钮为一组. 每一组按钮都具有不同的功能:
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459412863281.png)

1. **引脚方向 Orientation**，每个方向相差90°，也可以通过单击鼠标右键来实现旋转。

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459412877908.png)
2. **引脚的功能 Function**，其中包括普通引脚、反向信号引脚、时钟引脚、反向时钟引脚。通过编辑器命令工具栏 Change→ Function 选项可以修改已经放置的引脚的功能。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460008259394.png)

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459412886175.png)
3. **引脚线条的长短** 四个长度分别为（0，0.1inch，0.2inch，0.3inch）设置为‘ 0 ’表示引脚线不可见。
在原理图编辑器中使用 SHOW 命令来检查网络是否连接到引脚上，如果连接在一起，引脚线和网络线就会高亮显示。如果引脚长度设为‘ 0 ’或者是使用WIRE 命令画的引脚，则不会高亮显示。
~~对于电阻符号，引脚长度最好小于 0.1inch，在这种情况下，可以在第 94 层（Symbols 层）使用 WIRE 命令来为电阻画一条线作为引脚~~

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459412894403.png)
4. **Visible 可见性**是否在原理图中显示 Pad (直插式焊盘)名称和 Pin (引脚)名称，使用NAME命令改变引脚名称。Pad 在原理图中的外侧通常为1、2 、3 等数字；Pin 名称则表示为引脚的功能在元件的内侧，例如WRITE、JUM、RTN等。引脚的相关标签是固定的，文字高度也固定不变（60mil）。
如果您需要将一个引脚连接到多个焊盘上并且您在 Visible 设置项中选择了Both 选项，那么在原理图中将只会显示其中一个焊盘的名称（编号最小的那个焊盘）。焊盘名称后面有一个*号标志，说明有多个焊盘连接。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459413728012.png)

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459412908807.png)
5. **Direction 信号流向** 用于选择信号传输的逻辑方向，其中包括:
NC   不连接 
In     输入 
Out  输出 
I/O   输入/输出 
OC   集电极开路或漏极开路
Pwr 电源引脚（供电输入），Vcc、Gnd、Vss、Vdd 等
Pas  无源、被动连接(连接电阻、电容等)
Hiz 高阻抗输出 (例如三态式输出)
Sup 电源输出的地，或者电源符号，通用电源引脚(例如连接接地符号)，用于绘制独立的电源符号。
如果元件符号上带有 Pwr 引脚，并且在原理图中存在相应的Sup 引脚，则它们会自动连接。Sup 引脚不能用来作为新建元件的一个引脚，而是用于创建单独的电源符号。
通过编辑器命令工具栏中的 Change→Direction 选项可以修改已经放置的引脚的信号方向。

**ERC 电气规则检查**： 依靠这些引脚信号流向来做出不同的检查，ERC 依靠如下信号流：
NC 没有任何连接的引脚
In   一个网络连接到该引脚上，不仅仅是输入引脚连接到这个网络上
Out 不仅仅是输出引脚连接到一个网络上，该网络上不能连接Sup 或 OC 引脚
OC   在相同的网络中没有out引脚
Pwr 把该网络设置成 Sup 引脚的属性
I/O，Hiz，Pas 不作特殊的检查

6. **Swaplevel 引脚交换等级**，用于选择引脚(或gate) 的互换等级， 范围为0~255 。Swaplevel 为 0 的意思是在同一个 Gate 中不能和其他引脚互换，除 0 以外的其他数字表示该引脚可以和其他引脚互换，前提条件是 2 个引脚的 Swaplevel 值相同，并且是处于在同一个 Symbol 中。PINSWAP 命令可以用于原理图和 PCB设计中的引脚互换。
原理图编辑器的93 pin layer 可以查看到 Direction引脚方向 和 Swaplevel 参数（如Pas 和 1 ）。
**PINSWAP** 命令可以用于原理图和 PCB设计中的同一 gate中引脚互换。
通过编辑器命令工具栏中的 Change→Swaplevel 命令可以修改已经放置的引脚的互换等级。
二极管的引脚是不能互换的，因此要把它们的 Swaplevel 设为 0。 
电阻符号的 2 个引脚具有相同的 Swaplevel（比如：1），因此它们可以互换。 

#### pin name
如果是低电平有效的信号引脚，会在引脚名称的顶部画一条横线。使用感叹号可以确定横线的长度。
例如：
`bar_above_text!-normal`
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460098512235.png)


### Schematic Symbol 原理图元件符号
使用 WIRE 或者其他命令在 Symbol 层绘制 schematic Symbol 。
Place the texts >NAME and >VALUE in layers 95,Names, and 96, Values (TEXT command).
Place them where the name and value of the component are to appear显示 in the schematic.
在 TEXT 命令有效时，可以设置更细的栅格尺寸来更精确地放置文本，然后请一定记得把栅格尺寸改回原来的 0.1inches。
第 97 层（Info 层）可以用来添加更多的附加信息和提示。

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460076286452.png)






## Package 编辑模式
在元件库编辑器的操作工具栏中单击Package 按钮，，然后在弹出对话框中输入新建封装的名称并确定，即可以进入封装编辑界面。
Package 编辑界面与Symbol 编辑界面类似，只是 CHANGE 命令按钮中包含了更多内容，并且增加了 PAD直插式焊盘、SMD表面贴装焊盘、HOLE钻孔等命令功能，以及绘图区下方的封装描述框。
Use the WIRE, ARC, etc. commands to draw
使用 WIRE, ARC等命令绘图。
 the symbol for the silkscreen on layer 21, tPlace,
 丝印层的字符和符号必须放到第 21 层（tPlace 层）
 additional graphical information for the documentation print
into layer 51, tDocu.
附加的图形信息文档放到第 51 层（tDocu 层）
Draw restricted areas for the Autorouter, if needed, in layers 41, tRestrict, 42,bRestrict, or 43, vRestrict, or in layers 39, tKeepout, or 40, bKeepout, by using the commands CIRCLE, RECT, or POLYGON.

在必要的时候使用 CIRCLE，RECT 或者 POLYGON 命令在第 41 层（tRestrict层）、第 42 层（bRestrict 层）、第 43 层（vRestrict 层）、第 39 层（tKeepout 层），或者第 40 层（bKeepout 层）为自动布线提供限制区域。
Use the TEXT command to place
the string >NAME in layer 25, tNames, serving as a text variable containing the name of the component,
第 25 层（tNames 层）上的字符串>NAME 是包含了元件名称的文本变量。
the string >VALUE in layer 27, tValues, serving as a text variable containing the value of the component.
第 27 层（tValues 层）上的字符串>VALUE 是包含了元件的值的文本变量


### Command toolbar 命令工具栏

#### Change
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459471760359.png)
**Cream 焊膏**：修改 SMD 焊盘的焊膏层开关状态，，可以选择On、Off ，默认为On。将SMD 焊盘的焊膏层修改为Off 时，该封装放置到 PCB 编辑器中后，相应 SMD 上就不会出现焊膏层标记图案(通过 DISPLAY 命令选中第 31 层 tCrcam 层来显示标记图案) ，从而之后为焊膏层生成的 GERBER 文件中就不会在相应位置上涂刷焊膏。建议除了某些特殊情况以外，在建立封装时将所有 SMD 的焊膏层都设置为On 。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459472308504.png)

**Diameter 直径** : 该命令用于修改直插式焊盘 ( PAD 命令按钮所放置的焊盘 ) 的外径。单击该命令子菜单底部的" ..."符号可以自定义新的外径值，选择好适当的值后，单击绘图区中的直插式焊盘就能够对其外径进行修改。
- 外径(Diameter)是指Pad (直插式焊盘)或Via(过孔)上包含金属外圈厚度在内的直径
- 内径(Drill) 是指钻孔的实际大小。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459472964539.png)

**Drill** : 该命令用于修改 PAD 焊盘和非电镀孔( 即 hold 命
令放置的孔)的内径。单击该命令子菜单底部的" … "符号可以自定义新的直径。选择好适当的值后，单击绘图区中的PAD 焊盘或非电镀孔就能够对其直径进行修改。
EAGLE 在元件库编辑器和PCB 编辑器中采用不同的符号来标记不同内径范围的孔。如果需要查看这些符号，在 display 开启 44-Drill 层。EAGLE 会根据不同范围的钻孔直径自动分配不同的标记符号。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459473827105.png)

**First** : 用于对封装的第一个焊盘进行标记。在该命令的弹出菜单中选择On，然后单击封装的某个焊盘，则该焊盘会被标记成该封装的第一个焊盘。且只能标记一个first，若重复标记，则以最后一个为准。
如果在 DRC 命令弹出对话框上 Shape 标签内的 First 下拉菜单中选择了标记形状，例如Octagon(八角形)，则当该封装放置到PCB 设计中时，被标记的焊盘就会显示成八角形，以便与其他焊盘区别。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459474180915.png)

**Roundness 圆度**: 该选项用于修改 SMD 焊盘 4 个角的圆弧形状。单击该命令后在弹出对话框中输入0~100 之间的值，确定后再单击SMD焊盘即可完成修改。默认值为0 ，表示4 个角均为直角。输入的数值越大， 4 个角的弧形半径就越大。

**Shape 焊盘形状** : 该选项用于修改 PAD 命令放置的焊盘形状。一共有5 个子选项，包括Square(正方形)、Round( 圆形)、Octagon (八角形)、Long( 长条形)、Offset (偏移形)。选择需要的形状后单击焊盘即可以完成修改。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459481489588.png)

**Smd 焊盘尺寸** : 该命令用于修改SMD 焊盘的尺寸。单击该命令弹出的子菜单底部的" … "符号可以向定义新的SMD 尺寸。选择好适当的尺寸后，单击绘图区中的SMD 符号即可以实现修改。

**Stop 阻焊**: 该命令用于修改 PAD 和 SMD 焊盘的阻焊层开关状态，可以选择on(启用)或者off(禁用)命令，默认为On。将PAD 和SMD 焊盘的阻焊层修改为Off 时，该封装放置到 PCB编辑器中后，相应的 PAD 或SMD 上就不会出现阻焊层标记图案 (通过DISPLAY 命令选中第 29 层tStop 层来显示标记图案) ，从而之后为阻焊层生成的 GERBER 文件中就会在该 PAD 或SMD 的相应位置上涂刷阻焊漆。STOP 为 OFF 可以阻止自动为 Pad 产生阻焊层。

**Thermals 热焊盘** : 用于修改PAD 焊盘是否需要采用热焊盘敷铜，可以选择On( 启用 )或者Off( 禁用 )命令，默认为 On 。在PCB 设计中 PAD 可以通过热焊盘敷铜的方式连接相同信号的敷铜区，如果在建立封装时将PAD 的Thermals 命令设置为OFF，则当封装放置到PCB 设计中并且处于相同信号的敷铜区时， PAD 的四周会完全与敷铜区接触，这样在焊接元件时热量散发过快，不利于焊锡熔化，因此建议保持默认设置。
设置 Thermals flag 为 off 可以阻止在敷铜区产生一个热焊盘符号。

热焊盘指在大面积的接地（电）中，常用元器件的腿与其连接，对连接腿的处理需要进行综合的考虑，就电气性能而言，元件腿的焊盘与铜面满接为好，但对元件的焊接装配就存在一些不良隐患如：①焊接需要大功率加热器。
___
7.5版本中 change 没有以下选项
**Isolate 隔离**：该命令用于修改多边形敷铜区与不同信号的对象之间的间距。单击该命令弹出的子菜单底部的"..."符号可以自定义新的问距值，选择好适当的值后，单击绘图区中的多边形就能够实现修改。
如果在设计规则或网络簇中对特殊的对象规定了较高的值，则会在需要时采用该值。
在多边形敷铜区具有不同等级的情况下，Isolate 始终针对的是以外框轮廓形式显示的多边形敷铜区，即使所计算出的多边形敷铜区具有另一个不同的轮廓，例如由于线路超出多边形敷铜区而产生的轮廓。实际的间距可能比规定的 Isolate 值更大。

**Rank 等级**: 该命令用于修改多边形敷铜区的等级.可选等级为0 和7 。如果将封装中的多边形等级设置为0 ，则该封装放置到PCB 编辑器中后，其多边形不会被其他任何多边形覆盖。而如果将等级设置为7 ，则其多变形可以被PCB 设计中的任意多边形覆盖。
如果封装中的多边形等级设置为7 ，并且将该多边形作为一个异形SMD 焊盘，这样当封装放置到PCB 设计中时，就能够被PCB 上的敷铜层覆盖，这对于接地散热非常有用。
___

#### Pad 通孔焊盘
于添加直插式焊盘。这种焊盘是一种贯穿 PCB 板所有层的电镀过孔。每个焊盘具有独立的属性，比如 Shape 外形、Diameter 直径、 和 Drill 钻孔直径，可以使用的外形包括：Square 正方形、Round 圆形、Octagon 八角形、Long 长形、和 Offset（钻孔不在中心的长形焊盘）。

已经放到图中的 Pads 属性可以在后面使用 CHANGE 命令修改，单击 CHANGE 图标（或者输入 CHANGE 命令），然后选择属性和合适的值，选择需要修改的Pads 进行修改。CHANGE 命令也可以适用于 Groups（需要先用 GROUP 命令定义组），选择合适的特性后用鼠标右键点击组内任何地方就可以实现。
一旦放好了一个 Pad，EAGLE 会自动在第 29 层和第 30 层（t/bStop 层）产生一个阻焊符号，阻焊符号的直径由设计规则中 Mask 书签上的 Stop 参数定义。

通过编辑器命令工具栏中的 CHANGE 命令按钮中的Shape、Diameter、Drill、Angle，可以对已经放置的焊盘的形状、外径、钻孔直径和旋转角度进行修改。
另外也可以通过CHANGE命令按钮中的Stop、Cream、Thermal 以及 First命令，来启用或禁用向动生成阻焊符号、焊膏符号、散热符号以及First标记 ( 即使用特殊形状来将某个焊盘标记为封装的第一个引脚所连接的焊盘，特殊形状可以在PCB编辑器中运行DRC命令，进入Shapes选项卡，找到First下拉菜单进行设置 )。
设置 Thermals flag 为 off 可以阻止在敷铜区产生一个热焊盘符号。
设置 CHANGE 命令下 STOP 为 OFF 可以阻止自动为 Pad 产生阻焊层。

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459489929615.png)
1. **Shape 焊盘形状**：前 5 个用于设定焊盘形状，Square(正方形)、Round( 圆形)、Octagon (八角形)、Long( 长条形)、Offset (偏移形)。

2. **直径 Diameter**：设定焊盘的外径。通常使用标准值 Auto（respecitively 0）来定义 Pads 的直径，因为这样定义的直径值最后都由 PCB 编辑器中的设计规则选项中的 Restring 标签中的值来决定，元件库中的 Pads 直径默认值为 55mil。您也可以给 Pads 单独定义一个值，比如 70mil，这样的结果就是电路板上该元件的 Pads 直径不能低于70mil（此种情况不由设计规则来计算）。在 PAD 命令有效时（或者 Pad 已经附着在鼠标右键上的时候）可以使用参数栏来设置 Pads 的直径，同样可以定义钻孔直径和焊盘类型。

3. **钻孔 Drill**：设定焊盘的钻孔直径，即内径。

4. **角度 Angle**：设定焊盘的旋转角度，可通过右键来切换。

#### Pad 命名
当放置 Pad 到库中时，EAGLE 会自动为 Pads 分配名称：`P$1`，`P$2`，`P$3` ...分配的名称和数据手册中一致。
按顺序自动命名焊盘：选择 PAD 命令后在命令栏中输入第一个 Pad 的名称，比如 '1' ，然后就可以顺序放置 Pad 了。请注意，这里的单引号必须要输入。

#### 显示 Pad name
这些名称很容易在选项/设置/杂项菜单里面的显示焊盘名称选项中进行检查，所有的 Pad 的名称会在刷新屏幕（F2）后显示出来。
另外一种方式是在命令输入栏中输入：
SET PAD ON
要隐藏 Pad 名称，可以输入以下命令：
SET PAD OFF
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460081318283.png)


#### Smd 表面贴装焊盘
绘制表面贴装焊盘。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459490575523.png)
1. **layer 下拉菜单**：可通过中键切换，设置SMD焊盘符号所放置的层，SMD只能在顶层或底层上，因此下拉菜单值提供Top(顶层)和Bottom(底层)两项。
2. **尺寸 Smd**：焊盘尺寸。
3. **圆度 Roundness**: 该选项用于修改 SMD 焊盘 4 个角的圆弧形状。以百分比表示. 数字越大，圆弧的半径就越大，选0时，则表示直角。设置适当的尺寸，可以绘制圆形焊盘。
4. **角度 Angle**：设定焊盘的旋转角度，可通过右键来切换。
通过CHANGE命令按钮中的Layer、Smd、Roundness、Stop、Cream、Thermal命令也可以对已经放置的SMD焊盘进行相应的修改。

#### Smd 特殊标记
表面贴装元件通常都是焊在电路板顶层，SMD 通常也放在第 1 层 (Top层)。如果您想让元件焊在焊接层（底层），则需要在 PCB 布局时考虑使用 MIRROR命令，而不是在建封装时考虑。
当放一个 SMD 焊盘（在顶层）的时候，阻焊层和焊膏层符号会分别自动在第29 层（tStop 层）、第 31 层（tCream 层）创建。
如果创建的封装需要在 PCB 编辑器中使用 MIRROR 命令放到焊接层（底层），则相关的功能会自动修改，也就是会变成第 30 层（bStop 层）和第 32 层（bCream 层）。

SMDs 的特殊标记（Stop、Cream、 Thermals）均可使用 CHANGE 命令修改。设置 Thermals 为 off 时可以避免 SMD 焊盘和敷铜区产生热焊盘符号。设置 CHANGE STOP OFF 或 CHANGE CREAM OFF 可以阻止 EAGLE 自动为 SMD 焊盘产生阻焊层和焊膏层符号，可以参考帮助中的 CHANGE 和 SMD 了解更多。

如果您不得不设计一个很大的区域（比如散热区），此时使用 SMD 命令就无能为力了，必须使用 POLYGON 命令来画一个满足要求的多边形区域 ，该区域或多或少的覆盖相关的 SMD 焊盘则可，一定要谨记此时需要在 tStop 层和 tCream 层调整阻焊和焊膏区域。使用 DRC 检查时会在此位置出现“overlap重叠 error”错误，可以允许此处的错误。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460087176474.png)

#### 命名 SMD
使用 NAME 命令来校正名称以便和元件规格保持一致。
如果元件具有很多连续序号的引脚，可以使用另外一种方来放置 SMD 焊盘：
选择 SMD 命令，在命令栏中输入第一个数字（比如：’ 1’），然后按照正确的顺序放置焊盘。
比如：
smd 0.8 2 '1' ←
输入上面的命令后，鼠标右键上就会粘附上一个尺寸为 0.8 x 2.0mm，名称为1 的焊盘。

#### 显示 SMD 名称
如果 SMD 焊盘 上 没 有显 示 名 称 ， 请单击Option/Set/Misc 菜单 ， 并选择 Display pad names 选项。
另外一种替代方法是在命令栏输入下面的命令：
set pad_names on ←




#### Hold 孔洞
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459491259729.png)
添加不带任何电气属性的钻孔，如安装孔。
命令行：hold
**钻孔 Drill**：设定焊盘的钻孔直径，即内径。，选择不同的钻孔直径时，钻孔符号会发生相应的变化， 以便进行区别。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459491646781.png)
钻孔符号由两部分组成，一部分即中心位置的圆形，另一部分则是代表不同尺寸的标记符号。其中圆形符号放置在 20  Dimension 层上，其直径即就是钻孔的真实直径；而剩下的标记符号则放置在 45 Holes 层上，用于区分不同直径的孔。
如果需要修改已经放置的钻孔的直径，可以通过编辑器命令工具栏中change 命令按钮下的Drill 选项来实现。

### Description 描述
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459491977372.png)
绘图区下方的Description 用于为当前的封装添加描述信息。当在Control Panel 的Libraries树形分支中的相应元件库下选中封装时，这些信息将会显示在右方的对话框内。单击Description 或者在命令框中运行DESCRIPTION 命令后，在弹出对话框的下半部分输入描述。
输入 HTML 格式的文本，即允许输入格式化的文本。
这些文本的关键字可以在 PCB 编辑器中使用 ADD 命令弹出的对话框中搜索。
```
<b>R-10</b>
<p>
Resistor 10 mm grid.
```
```
<b>LCC-20</b>
<p>
FK ceramic chip carrier package from Texas
Instruments.
```

### Silkscreen 丝印
使用 WIRE/ARC/CIRCLE/RECT/ POLYGON 命令在第 21 tPlace 层( 丝印层)画需要在电路板上看得见的丝印符号，该层包含了打印到板上的一些信息。您可以选择符号的精细程度。
在需要时可以使用较细的栅格尺寸。
丝印层线宽通常设为 8mil（0.2032mm），更小的元件使用 4mil（0.01016mm）宽度。
可以从 library.txt 文件中得到更多的信息来作为设计元件的指南。

请确认丝印不要覆盖焊接区域，否则当电路板焊接时会出现问题。

必要的时候使用 GRID 命令来设置一个更合适的栅格尺寸或使用 Alt 键来选择两种栅格中的一种（参考 GRID 命令）。在屏幕打印的时候使用标准线宽（使用 CHANGE WIDTH 命令可以修改线宽）为 8mil 或 4mil，具体的需要取决于元件的尺寸。

**51 tDocu** ：有时候需要在第 51 层（tDocu 层）创建额外的看起来更好看的丝印，这些丝印看起来实际上覆盖了焊接区域，不过它们并不会在制造数据中输出，因此是可行的。该层上的内容本身不会打印到电路板上，但此内容是用于文档打印的一种补充。

请注意，在第 21 层（tPlace 层）放置内容时不要覆盖需要焊接的任何区域，而在第 51 层（tDocu 层）则没有这样的制。以前面的电阻为例，电阻的外形符号需要画在第 21 层（tPlace 层），但是连线因为要覆盖焊盘，就应该放到第 51 层（tDocu 层），请参考下图所示。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459999416086.png)

### Labeling 添加标签
`>NAME `：25 tNames 
`>VALUE`：27 tValues
TEXT 不会自动调整图层，需要手动调整到相应的图层。

推荐使用 0.07inch 的文字高度（尺寸）和 10%的比率（当使用矢量字体时，可以使用 CHANGE 命令设置文本宽度和高度之间的关系）。推荐使用矢量字体，这样在 PCB 编辑器中的文本看起来和实际打印的文本保持一致。

在 PCB 编辑器中可以使用 SMASH 和 MOVE 命令来改变这些和封装有关系的文本。对于示例 IC 来说，Value 表示 Device 的名称（比如：74LS00）。
如果想放一个和 Package 方向呈180°颠倒的字体，必须使用 Spin 标志(带旋转标志)

### Restricted area 元件的限制区域
39 tKeepout 层
应该使用 RECT 命令在第 39 层（tKeepout 层）创建一个覆盖整个元件的矩形区域（使用 RECT 命令），或者使用 WIRE 命令绕着 Package 画一个外框，这样便于使用 ERC 来检查 PCB 板上是否有元件相距太近甚至重叠在一起。

### Note 注意
CHANGE 命令 用来在后面阶段修改对象的属性，比如已经放好的对象线宽、文本高度、Pad 外形或者所在的层。
如果想一次更改多个对象的属性，可以先用 GROUP 命令定义一个对象组，然后输入 CHANGE 命令，按住 Ctrl 键，在绘图区表面单击鼠标右键来改变参数和值。
例如：
使用 GROUP 命令定义一个包含 2 个 Pads 的对象组，然后选择 CHANGE 命令下的 Shape/Square 子项，按住 Ctrl 键，用鼠标右键单击绘图区，2 个 Pads 的外形都会改变。

### Description 描述：
在窗口的描述区域单击 Description 可以打开一个描述窗口，输入描述文字或者 EAGLE 允许的 HTML 格式的文本（详情可以参考帮助功能中的 HTML）。
例如，我们创建的 DIL-14 封装的描述文本可以使用下面格式：
```
<b>DIL-14</b>
<p>
14-Pin Dual Inline Plastic Package, Standard Width
300 mil
```
```
<b>LCC-20</b>
<p>
FK ceramic chip carrier package from Texas
Instruments.
```
或者可以参考数据手册中的描述、邮件地址、或者其他信息均可，这样在 PCB编辑器的 ADD 对话框中很容易使用关键字搜索到该 Package。
元件库对象的描述中所包含的超链接可通过相应的应用程序打开。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460084133265.png)

### 定位点（Origin 原点）
一旦完成了封装的设计，请检查原点坐标的位置，最好是让原点坐标位于**封装的中心**，或者在封装的第一个引脚上。必要的时候需要使用更合适的栅格（比如：0.635mm 或 25mil），并使用 GROUP 和 MOVE 命令来把整个封装移到一个更适合的区域。
**在移动之前确保所有的层均可见**（使用 DISPLAY ALL），这是唯一一种可以确保所有对象均被移动的方式。

## Device 编辑模式
Device 包含了Symbol 的引脚和Package 的焊盘之间的对应关系，因此在完成Symbol 和Package 的创建工作后，需要在Device 编辑器界面中将两者关联起来。

### Command toolbar 命令工具栏
#### Change
1. Addlevel 
在原理图中使用 ADD 命令放置元件的 gate 时，该gate 的优先等级。如果需要查看某个元件的 Addlevel 和 Swaplevel 等级，可以在该元件的 Device 编辑器界面中右击原理图符号，并选择 Properties 命令即可。
**Must**: 表示该元件中任何gate放置到原理图中时，该gate也会自动出现在原理因中。如果要删除Addlevel为Must的gate，则必须先删除其他等级的gate。典型的例子是：一个继电器的线圈绕组，如果调用了继电器的触点，则继电器的线圈绕组必须被调用。
**Can**: 表示元件中具有该等级的gate(电源gate除外)需要使用INVOKE命令来放置到原理图中，该元件在必要的时候才使用。例如一个包含A 、B 、C 、D 共4 个gate 的逻辑元件符号，它们的Addlevel 通常都为Next ，放置该逻辑元件时，前一个gate 放置后会自动切换到下一个gate， 直至 4 个gate 放置完成；如果将第 4 个gate 的Addlevel 改为 Can，则前3 个 gate 放置完成后再次放置时，会从第一个 gate 重新开始，而不会自动放置第4 个 gate 。这时就需要使用INVOKE 命令手动选择来完成整个元件的放置。在一个继电器的原理图符号中，触点 Gate 的 Addlevel 就会被定义成 Can，这种情况下，在需要的时候可以使用 INVOKE 命令单独调出触点 Gate，并且可以使用 DELETE 命令删除。
**Next**: 表示具有该等级的 gate 依照名称顺序进行放置。例如 4 个ga忱的名称为A 、B 、C 、D ，并且它们的Addlevel 均为Next ，则放置元件时会依照建立元件库时各个gate 放置到元件库编辑器中的先后顺序来进行放置。对于具有单一 Gate 的 Device 来说也是一种很好的选择。使用 ADD 命令添加元件符号时，软件在“打开”一个新的元件符号之前总是首先调用已经存在于原理图中元件的 Next-Gates。
**Request**: 该等级专用于元件的电源gate 。通常电源符号都属于 Request 等级，不能自动添加，与 Can 等级一样需要使用 INVOKE 命令来进行放置。但与Can 等级不同的是，当元件由两个 gate 组成，并且其中一个的 Addlevel 是 Request 的电源 gate，则元件放置到原理图中后的名称通常为IC1、IC2 或IC3 等等，而不会在名称后加上gate 的名称。而电源 gate 被放置到原理图中时，其名称为前缀+ 数字+ gate 名称，例如IC1P。
**Always** : 该等级与Must 相似，不同的是该等级的 gate 可以单独删除，也可以通过INVOKE命令重新添加。比如：多触点继电器的触点，某些触点 Gate 可能偶尔不会被使用，如果这些触点 Gate 被定义成 Always，则他们可以使用 DELETE 命令删除。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459493347735.png)

2. **Swaplevel**：设置 gate 的交换等级。

#### ADD 添加
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459824980621.png)
为 Device 添加一个 Symbol。
如果一个 Device 包含几个可以单独依次放入原理图中的原理图符号（在EAGLE 中，称这样的符号为 Gates），这些 Gates 可以使用 ADD 命令单独放入原理图中。
在 ADD 命令下，通过参数栏可以定义 Swaplevel 和 Addlevel，输入 CHANGE 命令后可以重新定义。

- **Swaplevel**: Gate 的 Swaplevel 行为非常类似于引脚的 Swaplevel，值为 0 意味着在这个Device 中该 Gate 不能互换。不为 0 的其他值意味着具有相同值的同一Device 中的 Gate 可以在原理图中互换，使用 **GATESWAP** 命令即能实现。

- **Addlevel** 参数则指明了 Device 中的 Gate 是否可以根据用户的需求单独添加到原理图中，例如：逻辑电路或放大器中的电源 Gate 符号并不会在原理图中显示。
>The Addlevel of the Gates that have been fetched determines the manner in which these Gates are fetched into the schematic, and under what conditions it can be deleted from the schematic.

在 gate 被读取时，gates的addlevel 决定了gates 被读取到原理图中的方式，和在什么情况下该gate能从原理图中被删除。


#### NAME 命名
改变 Gate 的名称。
如果只有 1 个 Gate，则这个名称不重要，因为该名称并不会出现在原理图中。
如果 Device 中包含很多个 Gate，则 Gate 的详细名称就会添加到 Device 的名称中。
例子：
假如 Gates 被命名为：A、B、C 和 D，原理图中元件的名称为 IC1，在原理图中添加 Gate 后，名称就会变成：IC1A、IC1B、IC1C 和 IC1D。


### Description 描述
Device 编辑界面左下方的Description 设置项用于为当前Device 添加描述，该描述会在Control Panel 的Libraries 树形分支下相应的 Device 被选中时显示在旁边的Description 一栏中。这些文本的关键字可以在 PCB 编辑器中使用 ADD 命令弹出的对话框中搜索。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459495456834.png)

HTML 格式的文本如下：
```
<b>R-10</b>
<p>
Resistor 10mm package
```
元件库对象的描述中所包含的超链接可通过相应的应用程序打开。

### Technologies 制造工艺
用于为当前的Device 添加不同的技术标识。
EAGLE 使用单词 Technology 来表示不同的集成电路设计技术，比如TTL 、LVTTL 、CMOS 、ECL 等。
当某个元件可以通过几种设计技术进行制造时，就需要通过该命令来添加。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459495463982.png)
在 New 文本框中输入该元件的Technology 名称，例如AS 、HC 、LS 等，然后单击两次确定即可完成Technology 的添加工作。
这里添加的 Technology 名称会加入元件的名称中，例如当通过 ADD 命令在原理图中添加元件库74xx-cu. lbr 中的元件时，ADD 命令弹出对话框中该元件库下的74 * 00 元件内就能够找到诸如74HC00FK 和74HC00N 的元件， 其名称中间就包含了Technology 的名称HC。
如果在为新创建的 Device 输入名称时，在名称中加入" * "号，则Technology 的名称会取代"*"号的位置。如果不加入" * "号，则Technology 的名称会直接添加到Device 名称的后面，然后再加上Variant name ( 用于区分不同的封装) 。
Technology 命令等同于在Device 编辑界面中运行 TECHNOLOGY 命令，关于该命令的更多信息，请在编辑器 Help 菜单下 General 命令的对话框中搜索关键字TECHNOLOGY 。

### Attributes 定义属性
用于为选择的 Technology 添加附加信息，附加信息可以是生产商、分销商、器件高度等。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459816644270.png)
在该对话框中选中某个Technology ，然后单击 New 按钮。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459816688404.png)
**Name名称**：文本框中输入属性名称，例如Manufacturer生产商; 

**Value 值** ：文本框中输入值，例如NXP ; 在下方的下拉列表中选择 Variable ( 变量可修改)或者 Constant( 常数不可修改选项) ，如果选择 Variable，则可以在原理图中通过 ATTRIBUTE 命令来对该元件在上图中定义的 Value 进行修改，如果选择 Constant，则只能通过ATTRIBUTE 查看，而无法修改；

**Technologles 制造工艺**： 文本框内选择添加附加信息的对象， current（当前） 命令表示只为当前选中的 Technology 添加信息，也可以选择 all 来为该元件包含的所有Tcchnology 添加附加信息。

#### Attribute 操作实例
打开库 74xx-us.lbr，并在任一路经下另存为该库文件，我们不希望对原始的库文件进行修改。编辑封装 74*05。
让我们来为封装变量为 N（即 DIL14 封装）定义属性，单击 Device 编辑窗口右边封装列表中的 DIL14（封装变量 N），单击参数栏中的 ATTRIBUTE 命令图标或者在 Description 窗口中单击 Attribute 文本会弹出如下图所示的属性窗口：
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461852352869.png)

该对话框最初显示封装变量 N 中的可用到的 Technologies，单击 New 按钮打开一个新的属性窗口，在 Name 栏中输入属性 height (高度)，在 value 栏中输入值0.16in，下面的下拉列表中 variable 表示允许修改值，constant 表示不能修改值，本例中选择 constant。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461917612929.png)

现在可以定义该属性在哪一种 Technologies 中有效：选择 current 表示当前有效，选择 all 表示所有均有效。单击 OK 后，新的属性就会在列表中显示出来。

让我们来定义第二种属性：具有不同值的 Technologies。再一次单击 New 按钮，输入下面的参数：
Name 栏输入：Distributor分销商，Value 栏输入：Smith，选择variable，Technologies 定义为：all 单 击 OK 确 认 ，新的 Distributor 属性会增加并显示出来 ， 所有的Technologies 均有该属性值 Smith。

`属性名称会自动使用大写字母表示！`

但是在本例中，LS Technology 是由 Miller 独家发布的，选中 Distributor 区域中属于 LS 的那个单元格。
单击 Change 按钮，弹出 Change 对话框，使用下面的设置：
Name 栏输入：Distributor。Value 栏输入：Miller exclusively，constant。Technologies 定义为：current 单击 OK 确认后就修改了 LS 的 Distributor 属性，该值在原理图中也不会被修改。

Technologies 的 Change 对话框有 3 中可能的形式：current、all with same value、all。Current 意思是当前改变的属性只适用于当前的选择，all with same value 意思是和当前值相同的属性适用于所有的 Technologies，all 意思适用于所有的Technologies。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461917730155.png)

最后，让我们定义更多的备注属性，这些属性没有初始值，属于变量，因此，我们在必要的时候可以用于原理图和 PCB 图中。
在属性对话框中单击 New，输入下面设置：Name 栏输入：Remarks备注，Value 栏输入：-，variable。Technologies 定义：all
单击 OK 确认，这些定义的属性看起来如下图所示：
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461917872335.png)
`在表格中使用灰色来表示属性为固定值！`

现在，封装变量为 N 的属性定义已经完成，单击 OK 关闭属性窗口后，所有的属性就会在 Device 编辑窗口的 Technologies 后面显示出来。
如果您想定义封装变量 D（SO14）的属性，可以按照上面的步骤来实现。
也可以通过命令栏中输入命令或者使用脚本文件来定义属性，详情请参考帮助功能中的 ATTRIBUTE 命令。

#### 显示 attributes
如果您在原理图编辑器或者 PCB 编辑器中使用没有定义附加属性的 Device 74*05，它只会显示属于它本身的一些属性和值。附加的属性不会在绘图区中显示，可以使用 ATTRIBUTE 命令来检查。
请参阅用户手册第 115 页来操作如何在原理图编辑器或者 PCB 编辑器中显示属性的信息。

##### Symbol 和 Package 的占位符
在元件库中您已经定义了什么样的属性会和 Device 一起在原理图编辑器中显示，或者什么样的属性会和封装一起在 PCB 编辑器中显示，这些可以使用TEXT 命令在 Symbol 编辑器和 Package 编辑器中输入占位符文本来实现，占位符格式为：“>”加上“字符”，比如：>name 和>value。我们前面定义的属性就可以这样输入：

`>Distributor`
`>Height`
`>Remarks`

将上面的文本放到 Symbol 或者 Package 编辑器中合适的位置，并为每一个文本选择属于它们自己的层，不必在意大小写。一旦您在原理图或者 PCB 图中添加了具有预定义属性占位符的元件，并设置了值，该属性值就会显示在占位符所在的位置。

这些文本可以使用 SMASH 命令从 Device/Package 中拆分开，这些属性可以使用 Attribute 命令来查看显示效果，可能的选项有：Off，Value，Name 或Both。
关于属性显示效果更详细的描述，请参考用户手册第 115 页。


### 新建 NEW /PACKAGE 选择封装
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459817807237.png)
New 按钮等同于在 Device 编辑界面中运行 PACKAGE 命令。
用于将已经创建好的封装添加到元件中，在对话框中选择要添加的封装。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459818455637.png)

#### Variant name 变量名/变体名称
文本框中输入被选中封装的变量名，例如输入D ， 并单击确定即可。如果 封装的版本只有一个，通常会使用 2 个单引号( ' ' )来作为封装版本的名称，相当于分配了一个名称。
Variant name 用于区分不同的封装，如果定义了变量名并且将该变量名对应的封装与某个Symbol 进行了关联，那么在原理图中通过 ADD 命令添加这个 Symbol 时， ADD 命令的弹出窗口中与该Symbol 对应的 Device 名称后面就会添加这个变量名。如果该Symbol 与多个定义了变量名的封装进行了关联，则在ADD 命令对话框中能够找到多个相应的Device ，名称带有不同的封装变量名，例如ADD 命令对话框中74xx - eu. lbr 元件库中，74xx00分组下的元件74HC00FK 和74HC00N 分别带有封装变量名FK 和N ，代表不同的封装。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459818976416.png)

### Connect
用于将创建好的 Symbol 的引脚和 Package 的焊盘相互关联起来。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459819544697.png)
1. **Pin 栏**：Symbol 的引脚名
2. **Pad 栏**：Package 的焊盘名
3. **Connect**：选择需要关联的某个引脚和某个焊盘，然后点击Connect，即可将它们关联起来，并出现在右方的connection栏内引脚和焊盘的对应关系中。
4. **Disconnect**：用于取消关联，选中connection 中的某对引脚和焊盘，点击Disconnect 即可。
5. **Append 附加**：将同一个信号的多个焊盘与某一个引脚相连。首先在连接窗口中选中一个引脚和一个焊盘并单击 Connect 按钮。这时在Connection 一栏中会显示引脚/焊盘的连接。接下来选中该连接，然后在 Pad 一栏中选中某个焊盘，再单击 Append 按钮就可以将该焊盘添加到连接中。重复以上操作可以添加更多的焊盘。添加后焊盘的名称会显示在 Connection 一栏中。
EAGLE 能识别两种用于创建多个焊盘连接的方法在Connection 栏中点击图标切换两种连接方式：
All：所有的焊盘都必须用线路连接起来。在 PCB 编辑器中您会发现所有的焊盘都用鼠线进行了连接，即必须对其进行布线。
Any：只有其中一个焊盘会用鼠线进行连接，即仅需要对该连接进行布线。在布线过程中，您可以决定需要进行布线的那个焊盘。在这种模式下可以实现元件的内部连接。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459821196578.png)
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459821178932.png)
6. **Copy from 复制于**：下拉菜单中可以选择其他具有相同焊盘数量的封装，单击 OK 按钮后就能直接将引脚和焊盘的关联关系复制到当前选择的Symbol 和Packagc 上，免去多次进行引脚和焊盘关联的操作。

### Prefix 前缀
用于为元件或者元件的gate添加前缀字符。
单击该按钮并在弹出对话框中输入需要的前缀字符来进行添加。
定义了前缀后，当在原理图中放置该元件或元件的gate时，软件会自动将该字符作为该元件或元件gate名称的开头部分。例如将前缀定义为IC，则在原理图中放置该元件的Symbol时，软件会自动将其命名为"IC+数字(表示这是第几个同前缀名的元件)+gate名称"，比如IC5A，表示该Symbol是原理图中第5个前缀名为IC的原理图符号，gate名称为A。

### Value 值
在 Device 模式下，VALUE 命令用来定义一个元件的值在原理图或 PCB 设计中是否可以自由改动，或者该元件本身就是一个固定的值。
元件的值由包含 Technolog 和不同封装变量的Device 名称组成。
在原理图编辑器中，如果 Technology 或Package 版本通过 CHANGE PACKAGE 或 CHANGE TECHNOLOGY 命令进行了修改，则改变后的值保持不变。
1. **off**，则表示自动将 Device 的名称作为原理图中元件所显示的 Value 的值，包含 Technology 和 Package 信息，例如Device 的名称为74HC00FK ，则当该元件被放置到原理图中时，其Value 的值自动定义为 74HC00FK 。当在原理图编辑器中通过VALUE 命令对其进行修改时，系统会弹出询问框进行确认，这时需要确认后才能修改。
2. **on**，则当该元件被放置到原理图中时，不会自动定义其 Value 的值，而需要手动定义，这时通过VALUE 命令来进行定义时，则不会弹出询问框。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1459822157611.png)

![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1460077690659.png)


## Labeling 原理图符号的标签
变量>NAME 和>VALUE 可以用来作为 Package 和 Symbol 的标签，在原理图中还有 2 个参数变量：>PART 和>GATE。下图是一个关于>Name 的示意图，左边：Symbol 编辑器中显示，右边：原理图中显示。
在第一种情况下，所有的符号都使用>Name 来标注，而在第二种情况下，第一个 Gate 使用>Part 和>Gate 标注，其他 3 个仅仅只有>Gate。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1461919628212.png)

## Solder Side 元件的焊接面
表面贴装元件（直插也可以）可以放到电路板的顶层和底层。因此，EAGLE 软件预先定义了一组和顶层相关联的层（Top、tPlace、tOrigins、tNames、tValues 等），和另外一组和底层相关的层（Bottom、bPlace 等）。

表面贴装元件总是放到电路板的顶层。可以使用 MIRROR 命令来把这类元件放到相反的层，用鼠标单击需要镜像的元件或者在命令栏中输入该元件的名称即可。
这会导致该对象在顶层的属性会移到底层，所有 t 开头的层都会移动到相对应的 b 层。
当使用 ADD、COPY、MOVE 或者 PASTE 命令中任何一个时，单击鼠标中键同样可以实现镜像功能。

## 任意焊盘形状
如果软件自带的焊盘形状无法满足您创建封装的需要，您可以自行定义一个任意形状的焊盘。通过多边形或者附加的线段就可以绘制这种焊盘。只要 Pad 或者 SMD 焊盘的中心位置处于多边形区域内部或者从 Pad 的中心位置引出了一条线段形成多边形区域，该区域就能够被识别为 PAD/SMD 焊盘的一部分。
绘制任意形状焊盘的常用方法是：
1. 放置一个 PAD 或 SMD 焊盘；
2. 使用 POLYGON 命令绘制焊盘需要的形状；
- 对于SMD  焊盘来说一把在顶层绘制多边形；
- 对于 PAD 焊盘来说，需要在所有要使用的层上(顶层、底层、内部层)绘制多边形；
PAD/SMD 的中心必须处于多边形的内部。否则该多边形就无法被识别为焊盘的一部分。请根据设计规则中的设置选择合理的多边形外框线宽。
3. 另一种绘制多边形的方法是使用 WIRE 命令
从 PAD/SMD 焊盘的原点位置开始通过 WIRE 命令来绘制多边形的外框。需要在所有将要用到的层上绘制相同的区域。请根据设计规则中的设置选择合理的线宽。
4. 检测阻焊层：阻焊层数据只针对 PAD/SMD 焊盘区域。请先将第29 tStop 和第30 bStop设置为显示状态。如果您需要焊盘区域不涂抹阻焊漆，请在适当的层上手动绘制阻焊区。
检查焊膏层
5. 请先将第 31 层 tCream 和第 32 层 bCream 设置为显示状态。正如前面所说，封装的定义始终处于电路板的顶层，因此我们需要检查的层是第 31 层 tCream。焊膏层数据会自动生成并且仅针对 SMD 焊盘。如果自动生成的数据不能满足要求，请在焊膏层上进行手动绘制。请记住在 SMD 的属性窗口内可以关闭自动生成焊膏层数据的功能（即Cream on/off 选项）。

通过在帮助中查找 PAD 或 SMD 命令可以了解关于绘制任意形状焊盘的更多信息。

`如果某个任意形状的焊盘没有与任何信号连接，DRC 将会提示间距错误，这是因为用于绘制任意形状的多边形或者线段无法被识别为某个信号的一部分。`


## 不包含封装的外部设备
External Devices without Packages 
>A so­called所谓的 External Device can be used to represent表示 components or objects that need to appear显示 in the schematic but are not part of the board design.

一个所谓的外部设备被用于表示元件或对象，该元件或对象需要显示在原理图中，但是不会成为电路板设计的一部分。
>There can be additional额外的 components, measurement equipment, cables, mounting materials and so on. 

可以有额外的元件、测量设备、电缆、安装材料等。
>It could be used for testing or simulating purposes, or for an electric schematic, as well.

它可用于测试或模拟的目的，或电路原理图，以及
>An external device is created in the library the same way as any other component. 

一个外部设备在库中被创建的方式与任何其它部件相同。
>The symbol may have pins of any direction. 

symbol 可以有任何方向的引脚。
>Create the Device and ADD the symbol(s) as usual.

创建设备和天剑 symbol 像往常一样。
>For marking the device as an external device create an attribute with the name `_EXTERNAL_`. 

 创建一个名为`_EXTERNAL_`的属性，用于标记该设备是作为一个外部设备。
>This attribute has to be created in the library; creating the attribute in the schematic won't work! 

该属性在库中被创建；在原理图编辑器中创建的该属性是不能工作的。
>The attribute's value doesn't matter.

该属性的值并不重要。
>An external device is no longer treated as作为 external as soon as you assign a package. 

一旦你为外部设备分配一个package，那么该外部设备不再作为一个外部设备。
>In this case you have to CONNECT all the pins with pads.

在这种情况下你 CONNECT 所有的 pins 到 pads。

## 定义任何角度旋转的 Packages
在Package 编辑器中，元件封装的角度可定义成任意角度，最小分辨率为0.1度。通常情况下，封装会定义成一个正常的角度，然后整体进行旋转。
原理图的符号只能以每步90°的角度选装。

### 整体旋转 Package
使用命令 DISPLAY ALL 显示所有层来确保该封装的所有对象均被旋转，然后使用 GROUP ALL 命令将所有的对象定义成一个组。
使用 ROTATE 旋转命令旋转该组。
现在，在参数栏中的点中 Angle 角度栏，输入需要旋转的角度值，然后使用鼠标右键单击定义好的组来定义旋转基点。
封装就会按照所设置的角度旋转，并显示。
另外的方法是在命令栏中输入下面的命令：
ROTATE R22.5 （> 0 0）
上面命令的意思是：先前定义好的组绕着坐标位置（0 0）旋转 22.5°，大于符号‘>’到右括号之间的数字表示旋转的基点（和鼠标右键单击坐标基点（0 0）的意思相同）

### 使用径向排列焊盘（Radial Pad）的封装
如果封装中有径向排列焊盘（Radial Pad）的情况，使用极坐标可以很容易地放置 Pads 和 SMDs。首先使用 MARK 命令选择一个合适的参考点，比如封装的中心点，然后在命令栏中会显示鼠标位置信息。
![Alt text](0x06_Library_Editor(元件库编辑器).assets/.1462023196756.png)
上图中使用 R 标记的值表示相对以前参考点的值（相对坐标值），P 标志后面的值则是相对于参考点的极坐标值（相对极坐标值）。
例子：
有一个封装的 3 个焊盘分布在半径为 50mm 的圆周上，元件的中心位置在在坐标（0 0）处。
GRID MM;
MARK （0 0）;
PAD '1' （P 50 0）;
PAD '2' （P 50 120）;
PAD '3' （P 50 240）;
依照以前使用的焊盘形状，使用上述的命令行很容易实现旋转焊盘（比如：长形焊盘，或者表面贴装焊盘）。
当使用 PAD 或 SMD 命令时，可以通过在参数栏直接输入角度来放置焊盘。
例子：
GRID MM ;
MARK （0 0）;
PAD '2' LONG R120 （P 50 120）;