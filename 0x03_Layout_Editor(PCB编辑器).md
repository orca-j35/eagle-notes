# 0x03_Layout_Editor(PCB编辑器)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库

## PCB 编辑器主界面
在使用PCB 编辑器进行电路板绘制之前，首先需要检查元件库中的封装，与电路板制作厂商沟通，并定义设计规则。
虽然用EAGLE 集成的由资深工程师创建的元件库已经非常接近现在的标准了，但是由于不同的制造商对同一种元件有可能采用不同的封装，而且根据不同的焊接流程会要求不同的焊盘尺寸，因此在进行PCB 设计之前仍然需要对所用到的元件封装进行仔细的检查。
另外，为了顺利地制造出最终产品，在设计电路板之前还需要与电路板制作厂商沟通，询问是否能够满足电路设计要求，比如以下参数:
- 布线宽度;
- 焊接区外形;
- 焊接区直径;
- SMD 焊盘尺寸;
- 丝印文本的尺寸和线宽;
- 钻孔直径;
- 如果是多层电路板，则要说明盲孔和埋孔的制作方向，以及电路板的结构;
- 信号之间的间距;
- 关于阻焊层和焊膏层的参数;
- 需要提交的电路板制造数据。

最后还需要对设计规则进行设置，即DRC 设计规则。DRC 设计规则是针对电路板设计中包括层设置、信号层中各对象的间距和尺寸、焊盘形状、阻焊层和焊膏层大小等要素在内的一系列规则。在设计之前对这些规则进行严谨地定义后，能够极大地减少电路板设计中的错误。关于DRC 的详细内容，在原理图编辑器中章节中已有介绍。

完成以上准备后，就可以开始电路板的设计工作了。通过Control Panel 的File→ New→Board 菜单新建电路板可以打开PCB 编辑器，或者单击原理图编辑器操作工具栏中的 Board 按钮，在已经设计完成的原理图基础上生成一个相应的PCB 设计文件，并在编辑器中打开。

注意：PCB 编辑器的操作工具栏中也有一个外形相同的按钮，即 schematic 按钮。如果先行完成原理图的绘制并且与同名的PCB 设计文件保存的相同的目录下，则单击该按钮就可以从 PCB 编辑器切换到对应的原理图，但是如果存放PCB 设计文件的目录下不存在同名的原理图文件，则单击该按钮后会生成一个空白的同名原理图文件，不会包含PCB 设计中的任何元件或信号线路。
PCB 编辑器：
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462071559622.png)


## command toolbar 命令工具栏
虽然部分命令按钮的功能与原理图编辑中的按钮相同，但是针对 PCB 设计而言，却包含了不同的内容，因此要注意区别不同编辑器中按钮的功能。

### INFO 信息
显示所选对象的属性，在命令栏中输入 INFO IC1 就会弹出一个 IC1 的属性对话框。根据不同的对象，有些属性在这里可以修改。
参考原理图编辑器
### SHOW 高亮显示
高亮显示用鼠标选中的对象。
也可以在命令栏中输入对象的名称（甚至一次输入几个名称）来实现此功能。
*号和 ? 号可以作为通配符使用。
Ctrl + SHOW 可以固定被选对象的高亮状态，进行逐个选择。
参考原理图编辑器

### 层设置 DISPLAY
显示和隐藏电路板的各个层。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462072506098.png)
eagle 最多支持 16 个信号，默认为两层，即1 top 层和16 bottom 层。这些层用于电路板布线，其它层则用于放置焊盘、过孔等符号以及名称、外框、阻焊区等信息。
如果需要增加布线的层数，需要运行 DRC 设计规则命令，在设计规则对话框中的 Layer 选项卡下编辑 setup 文本框。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462078955478.png)

不能在 display 窗口中使用new按钮来创建，因为该按钮只能添加100以上的层，并且只能用于显示其他信息，不能用于布线。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462078933032.png)
仅在 Layer 23，tOrigins 被显示的情况下才能选中顶层的元件。
只有 Layer 24，bOrigins 层设置为显示状态，才能选中底层的元件。

DISPLAY 命令可以支持自定名称，可以将多个层的显示状态定义成为一个名称，然后作为 LAYER 命令的一个参数来使用，这样可以很快的从一种显示模式切换到另外一种显示模式。
DISPLAY LAST 命令用于返回到上次显示的模式。详细的 DISPLAY 命令信息请参阅帮助功能。

详细的层含义，参考相关笔记。

### MARK 标记
单击鼠标可以定义新的坐标原点。
在坐标显示区域中除了显示绝对坐标外，还会添加相对坐标（R x 值 y 值）和极坐标（P 半径 角度）显示。第一次单击MARK 图标然后单击后交通灯图标（Go 图标），只有绝对坐标会再次显示。

### MOVE 移动
移动任何可见的对象，单击鼠标右键会旋转对象。
MOVE 命令并不能把信号连接起来，就算把导线（或走线）移动到另外一条线或焊盘上也不能连接。要使用 ROUTE手工布线 或 WIRE 来走线。使用wire时，需要结合name命令同一信号名称。
当在选择对象时按下 Ctrl 键时会有一些特殊的使用方法。
详情请参阅帮助功能（其他命令也类似：CIRCLE、ARC、WIRE、MOVE、ROUTE 等）。
如果要移动一个对象组，请参考原理图编辑章节中的 MOVE 功能。

### COPY 复制
复制元件或者其他对象。
当复制对象时，名称会重新分配，但是值保持原来的不变。
当复制一条单独的走线时，走线的名称保持不变。
按住 Ctrl 键并单击某个对象时，该对象将会附着到鼠标的光标上。
这时该对象的原点与当前栅格对齐。
COPY 命令也可以用于复制对象组。
对象组将会复制到操作系统的剪贴板中，因此可以将其粘贴到另一个 EAGLE 编辑器中。
### MIRROR 镜像
镜像所选对象。
如果使用 MIRROR 命令来操作元件,元件会被放置到电路板的另外一面。
虽然 PCB 编辑器中 MIRROR 命令按钮与原理图编辑器中的相同，都是将所选对象进行镜像操作，但是其功能效果却不太相同。对PCB 编辑器中位于TOP 层和 Bottom 层上，或t???层(如 stop)和b???层(如bStop)上的对象进行镜像操作后，该对象将会翻转后移动到相反的那一面上。如对tStop层上的某对象镜像后，该对象会翻转并移动到 bStop 层上。而对2~15 层，以及新建编号 100 以上的层中的对象进行镜像操作后，不会改变其所在的层。

### ROTATE 旋转
旋转选择的对象（经常和 MOVE 命令一起使用）。
在move命令下，移动时单击右键会旋转被选中的对象，参数栏显示当前对象的角度。
同样的操作可以使用于对象组（使用 GROUP 命令和鼠标右键）。
ROTATE 命令也可以和对象组一起使用。在 ROTATE 命令有效时，按住 Ctrl 键，用鼠标右键在绘图区域中单击可以设置对象组的旋转中心，对象组就会按照一定的角度逆时针方向旋转。旋转的角度可以通过在命令栏中输入角度值或者在角度参数框中修改。
详细的语法结构可以在帮助功能中找到。

### GROUP 对象组
定义一个对象组以便进行移动、旋转、或者通过 COPY 和 PASTE 命令进行复制或粘贴到另一个绘图中、或者修改对象组的属性。

单击该图标，然后按住鼠标左键拖拽光标可以定义一个长方形的对象组覆盖区域。
如果想定义一个非长方形的对象组区域，可以用鼠标左键来确定多边形的每一个角，然后点击右键来形成封闭的多边形对象组。
在命令栏中输入 GROUP ALL 命令会选中所有的对象。
必须确保所有被选择的对象所在的层都全部被显示后，GROUP ALL 命令才能选择所有的对象。换句话说，可以取消某一些层的选择来让特定的某些对象不会被选择。
更详细的信息，请参考原理图编辑器中 GROUP 的介绍或者帮助功能。

### CHANGE 修改
改变对象的属性，比如改变走线的宽度，文本尺寸等。
如果改变一个属性后按下 Esc 键，先前使用过的属性值会以菜单的形式弹出，这种方式可以很方便的选择一个新的值。
请同时查看帮助功能。
另外，通过右键单击对象并选择属性可以查看对象的参数以及对参数进行修改。
鼠标右键单击对象可以弹出弹出菜单。
下面介绍 PCB 编辑器中特有的命令，其余命令参考原理图编辑器笔记。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462157058909.png)



1. **Diameter** 直径: 该命令用于修改PCB 设计中过孔 (  即VIA 命令按钮所放置的金属镀孔  ) 的外径。单击该命令弹出的子菜单底部的"..."符号可以向定义新的外径值。选择好适当的值后，单击绘图区中的过孔就能够对其外径进行修改。

2. **Drill**钻孔: 该命令用于修改PCB 设计中过孔via以及非电镀孔 Hole 的内径。
单击该命令弹出的子菜单底部的 "..." 符号可以自定义新的内径值。选择好适当的值后，单击绘图区中的过孔或非电镀孔就能够对其内径进行修改。

3. **Isolate** 隔离：该命令用于修改多边形敷铜区与不同信号的对象之间的间距。单击该命令弹出的子菜单底部的”…”符号可以自定义新的问距值，选择好适当的值后，单击绘图区中的多边形就能够实现修改。
如果在设计规则或网络簇中对特殊的对象规定了较高的值，则会在需要时采用该值。
在多边形敷铜区具有不同等级的情况下，Isolate 始终针对的是以外框轮廓形式显示的多边形敷铜区，即使所计算出的多边形敷铜区具有另一个不同的轮廓，例如由于线路超出多边形敷铜区而产生的轮廓。实际的间距可能比规定的 Isolate 值更大。

4. **Orphans** 孤岛: 该命令用于修改PCB 设计中的多边形敷铜区是否保留孤岛敷铜区。孤岛是指当某个敷铜区被另一个不同信号的线路截断时，被隔离在外的没有电气连接的那一部分敷铜区。选择On 或者Off 后单击需要修改的敷铜区即可实现修改。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462158542853.png)

5. **Rank**等级: 该命令用于修改 PCB 设计中多边形敷铜区的等级。等级最高为1，最低为6 。
当不同信号的高等级多边形与低等级多边形相互发生重叠的时，软件会对低等级多边形的相应区域进行裁剪，以避免短路。当然相同信号的多边形可以随意重合不会受到等级影响。如果不同信号的两个多边形等级相同，则最终会由DRC 命令所规定的设计规则来决定。

6. **Shape**形状: 该命令用于修改PCB 设计中过孔via的外形。其子菜单包含Square  (正方形) 、Round (圆形)、Octagon(八角形)三种形状，选择后单击过孔即可完成修改。

7. **Stop**阻焊层 : 该命令使用的情况较为特殊，即只有当PCB 设计中添加的过孔via 的内径小于 DRC 命令设置对话框中 Masks 标签下的Limìt 值时(请参考DRC 命令的相关笔记) ，软件不会自动为该过孔添加阻焊层，这时就需要用该命令来强行添加。
在该命令的子菜单中选择On ，然后单击过孔即可以添加阻焊标记。如果要取消添加的阻焊标记，选择off 再单击过孔即可(只能取消该命令所添加的阻焊标记，对于软件在其他过孔上自动添加的标记无效) 。

8. **Thermals**热焊盘：所绘制的 Polygon 多边形，是否开启热焊盘。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462179986000.png)

9. **Via**过孔 : 该命令用于修改PCB 设计中过孔所穿过的信号层。如果PCB 只有Top 层和Bottom 层，则该命令只有一个命令"1 - 16 " 。如果在DRC 命令的设置对话框中 Layers 标签下的Setup 框中设置了多个层，则该选项的子菜单中会包含其他不同的选项，表示穿过不同层数的孔。选择某种层数项(如1 - 2) ，然后单击PCB 设计中的过孔即可完成修改。

### PASTE 粘贴
该命令用于将剪贴板缓存中的对象粘贴到绘图区。
~~通过菜单栏的“编辑（Edit）/ 粘贴自（Paste from）”选项可以将整个 PCB设计（也可以是原理图）粘贴到您的当前绘图区中。~~
请参见帮助功能获取更多信息

### DELETE 删除
删除可见的对象。
使用 Ctrl + 鼠标右键可以删除被定义的一个对象组。
如果没有加载相关联的原理图，在 PCB 编辑器的命令栏中输入 DELETE SIGNALS 可以删除走线和信号。
按住 Shift 键，单击多边形敷铜区的轮廓线可以用 DELETE 命令删除整个多边形敷铜区。
按住 Ctrl 键，鼠标左键单击走线弯曲的地方可以删除掉弯曲线，在弯曲处会生成新的连接线，若是L 形状的连线，会删除拐角。
有些不能被删除的对象主要是和 DRC 命令有关，这些对象可以通过 ERRORS 命令 来 删 除 （ ERRORS CLEAR ） 。 
如果原点层，第 23  tOrigins 层或者第 24 bOrigins 层没有显示，则不能删除元件。

### ADD 添加
添加元件库中的封装到绘图区。该按钮提供了一种便捷的查找封装的功能。
使用 USE 命令可以加入需要使用的元件库。
鼠标右键单击 ADD 图标可以弹出一个最近放置 Devices 的列表。

### PINSWAP引脚互换
互换元件中 2 个等效焊盘的信号。该功能必须要求元件引脚具有相同的 Swaplevel。

### REPLACE 替换
从元件库中使用另外一个元件来更换某一个元件。
如果仅仅想更换不同的封装而不是整个 Device，可以使用 CHANGE PACKAGE 或 PACKAGE 命令。
鼠标右键单击 REPLACE 图标可以弹出一个最近被更换元件的列表。

### LOCK 锁定
lock 命令
用于锁定 PCB 编辑器中的元件，固定该元件的位置和方向。
元件被锁定后，其原点会由符号“+”变成符号“X”，表示该元件处于锁定状态。
被锁定后的元件不能move移动、镜像、旋转，该元件被复制和和粘贴后的新副本仍处于锁定状态。

如果试图移动某个含有锁定元件的元件组，这些被锁定的元件不会随元件组移动，而是停留在原来的位置上。
但是这些处于锁定状态的元件上的文本信息依然能够通过 SMASH 命令进行分离，并通过 MOVE 命令来移动分离后的文本信息。

- 解除锁定 ulock
使用 Shift + LOCK 可以对被固定的元件解除固定。
在被锁定的对象上右键，使用弹出菜单的 unLock 入口也可以达到此功能。

~~可以在属性对话框中输入一个新的坐标值来改变被固定元件的位置。~~

### NAME 命名
为元件、信号、过孔和多边形敷铜区命名。
使用 NAME 命令可以把多边形敷铜区从一个信号网络转移到另外一个信号网络中。

### VALUE 赋值
该命令为元件定义一个值，比如把一个电阻的值设为 100K。
鼠标右键单击该图标会弹出一个列表，其中包含之前使用过的值。
这时选中某一个值并单击一个或多个元件可以将该值应用到元件上。

### SMASH 拆分
把 Device 中的名称、值和其他任何属性文字拆分，以便能单独放置。
被拆分的文本尺寸可以单独改变。
该命令对于对象组仍然有效。执行该命令后，在按下 Ctrl 键的同时通过鼠标右键单击一个定义好的对象组可以对对象组进行拆分。
- 隐藏拆分后的文本
使用 DELETE 命令可以隐藏被拆分的文本，当执行 unSMASH 后，文本会自动显示在最初的位置。
- unSMASH
当使用 SMASH 命令时按下 Shift 键可以将文本转换成未拆分状态。刷新窗口后文本不可以再被编辑并且显示在原始位置（在弹出菜单中使用 unSmash 命令同样可以达到这样的效果）。
另外一种选择是单击弹出菜单的 Properties 属性入口可以打开或者关闭Smashed 选项。

### MITER 倒角
对 2 条走线的连接处（或多边形敷铜区轮廓）圆弧化或者斜角化。
不同的倒角半径表示不同的类别。
~~正半径值表示圆弧倒角，负半径值表示斜角倒角。~~
倒角半径大小也会影响到某些走线线的弯曲形式（请参见帮助功能：SET 命令，Wire_Bend）
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462182667107.png)

### SPLIT 折线
将一条走线中转换成弯折的形状。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462240782207.png)
用于对已经布好的线路重新布线。通过单击已布好的线可以插入一个弯折，然后移动鼠标重新布线。
使用 RIPUP 拆解已布线为鼠线。
Ctrl + DELETE 走线上的折角处。

- 更改走线所在层
如果想改变已经布好的走线段所在的层，可以使用 SPLIT 命令插入 2 个弯折，然后使用 CHANGE LAYER 命令改变弯折后形成的新线段所在的层，此时 EAGLE软件会在弯曲点上自动添加过孔 VIA。

### OPTIMIZE 优化
用于将信号层中处于一条直线上的两条信号线段合并为一条信号线路。
单击该按钮或运行 optimize 命令，然后单击需要优化的线段，即可实现优化。
如果需要对整个 PCB 设计中的所有线段进行优化，则可在运行该命令后，单击操作工具栏中 GO 按钮来实现全部优化。
如果需要软件自动优化，需要开启 set 窗口中 misc 杂项 下的 optimize 复选框。

用于优化一条直线中的多条线段，以便减少会图中的对象的数量。例如。通过 wire 或者 route (手工布线 对鼠线进行布线)，由多次单击绘制了 3 条首尾相连的线段，形成一条直线，但该直线实际上包含了 3 个对象，这时运行 OPTIMIZE 并单击该直线后，就能够将它们合并成一条完整的直线，即减少为一个对象。这样不仅降低了软件的处理难度，而且能够对整条直线进行移动和旋转等操作，而不用每条线段重复操作。

### MEANDER 蛇形线
绘制蛇形线可以调整信号线路的长度，特别是差分线对的长度。
注：蛇形线不仅可以用于差分线对，也可以用于任何其他信号线路。
首先要绘制差分线对。参考相关笔记。

1. **差分线对的等长调整**：
在多数情况下，尽管您在对差分线对进行布线时尽量保证并行布线，但两条线路仍然会存在长度差。
MEANDER 命令能够用于对差分线对进行等长调整。
首先激活 MEANDER 命令，然后单击某一条差分线，并移动鼠标。鼠标离开起始点的垂直距离和平行距离分别决定了蛇形线的高度和宽度范围。
当两条差分信号线路存在长度差异时，并且鼠标光标位置与起始点之间的距离足够远，就可以生成蛇形线路。
蛇形线增加了较短那条差分线的长度。
鼠标光标附近显示的信息包括蛇形线调整的目标长度，即较长那条差分线的长度，以及两条差分线当前长度与目标长度的百分比。
如果添加蛇形线后长度仍然不够，您也可以在差分线上其他位置继续添加蛇形线。

2. **指定信号线路长度**
如果您需要指定差分信号线的长度，在 MEANDER 蛇形线命令下可以直接在命令框中输入数值并回车，例如输入 9.5in，然后左键单击差分线对。这时再用之前提到的方式移动鼠标来绘制蛇形线。
当针对指定信号线路长度的差分线进行布线时，软件首先会尽量保持两条线路在移动鼠标时长度始终相等，然后再考虑将两条线路延长到指定的长度。
通过重新执行 MEANDER 命令或者在命令框中输入 0  并回车，可以取消指定的长度。

3. **对称和非对称蛇形线**
默认情况下生成的是对称蛇形线，也就是蛇形线会向差分线对的两侧边伸展。
如果需要蛇形线仅向一个方向伸展（有可能因为只有一个方向有足够的空间布线，或者因为较长那条差分线不允许增加长度），您可以通过单击鼠标右键来切换到非对称模式。这时鼠标光标的位置决定了蛇形线的伸展方向。请移动鼠标来确定适当的蛇形线。
在设计规则窗口中“杂项”标签下的“差分线对中蛇形线的间距系数”用于设置蛇形线线段之间的间距。数值越大，线段间距越大。该系数的范围是 1 到20。默认为 2.5，是指单侧蛇形走线时，弯折一侧相对于自己的弯折间距。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462896233428.png)

![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462256438848.png)

4. **长度容差显示**
设计规则窗口“杂项”标签中的“差分线对最大长度差”决定了绘制蛇形线时鼠标光标附近所显示的百分比数值的颜色。当百分比数值显示为绿色时，相应的线路与目标长度的差异小于规定的值。否则百分比数值会显示为红色。该参数的默认值为 10mm。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462256654168.png)

5. **测量信号线路的长度**
按住 Ctrl 键并单击（或双击）某条线路就能够测量该信号线路的长度并显示在鼠标光标附近。
您可以使用该功能来测量某条信号线路的长度，并将测量到的长度作为另一条信号线路蛇形布线的目标长度。
如果在按住 Ctrl+Shift 的同时进行测量，则会同时显示目前为止测量过的最大长度和当前选中的信号线路长度。该功能可以用于确定多条总线中最长的总线，然后再通过蛇形线延长其他总线。



### ROUTE 布线
手动对信号进行布线。
布线完成后鼠线就转变成金属导线。
如果 EAGLE 软件支持自动布线模式，ROUTE 命令会支持 Follow-me 跟随布线功能，该功能能对所选择的信号进行自动处理。
ROUTE 命令和不同的鼠标按键一起使用可以提供不同的选项，同样，和 Ctrl  和 Shift 键结合使用也会有不同的功能。
1. Ctrl + Left 
起点：顺着任何一个 VIA 或 Wire 的给定点开始布线；
终点：当画一个圆弧终点时定义圆弧半径，此时使用 Ctrl + Right 切换圆弧的扇面。

2. Shift + Left 
起点：如果鼠线从一条已经存在的 Wire 上开始，并且这条 Wire 的线径宽度不同，则新的 Wire 将采用已存在的 Wire 的线径宽度。如鼠线的两层线宽不一致，会自动跟随点击处的线宽进行布线。
终点：在 Wire 的末端放一个 VIA。

3. Center 中键 在不同的信号层间切换
4. Right 右键 选择走线的弯曲类型
5. Shift + Right 反向切换导线的弯曲类型
6. Ctrl + Right 在相关联的弯曲类型间固定切换；

![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462244035657.png)
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462244044668.png)

1. **层选择下拉菜单**：用于选择布线的层，可以在布线过程中随时修改。在布线过程中单击鼠标中键可快速切换布线层。
2. **布线弯折形状**：布线过程中单击右键可轮流切换弯折类型。
3. **Follow-me 布线器**：布线弯折选项后面的两个按钮，分别是 Follow-me 布线器的两种模式：局部模式和全局模式，这两种模式相当于半自动的布线模式。
- **局部模式**：软件会自动对鼠标指针位置到最近的鼠线端点之间的信号线路进行布线计算。单击鼠标即可确定布线线路，然后再对余下的线路进行布线。
- **完全模式**：软件会同时对鼠标指针位置到鼠线两个端点之间的两段信号线路进行计算，这时能够看到鼠标指针两边的布线形状，移动鼠标时软件会同时计算并显示另一种布线形状，选定适合的布线后，单击鼠标即可完成这一段鼠线的布线工作
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462244477607.png)
Follow - me 布线器遵循 DRC 设计'规则和网路簇的设置，因此建议在使用该布线器之前先对这两种规则进行设置。
4. **Miter 半径和弯折选项**: 请参考原理图编辑器中 MITER 命令按钮笔记。
5. **Width 宽度**: 该选项用于设置布线宽度。可以从下拉菜单中选择一个值，或者直接在 Width 框中输入自定义值并回车来实现设置。
6. **过孔形状**：ROUTE 命令提供了三种过孔形状，依次分别是正方形、圆形和八角形。如果已经在某层上绘制了一段线路，并且该线路需要切换到另一层上继续布线，则软件会自动添加一个过孔，并采用选中的过孔形状。
7. **Diameter 和Drill** ：前者表示过孔的外径，后者表示内径。可以从两个下拉菜单中选择需要的值，或者直接在数值框中输入自定义值，并按Enter 键来实现设置。

注意: 当相同设计项目的原理图和PCB 设计同时打开时，只有在原理图中有相应的信号的情况下，才能在PCB 编辑器中进行对应的信号布线。如果需要在 PCB 中增加信号，则先要在原理图中添加对应的网络。

### RIPUP 取消布线
把 PCB 中已经布好的线（Tracks）转换成未布的鼠线（Airwires），把经过敷铜的多边形 RATSNEST 填充区域恢复到只有外轮廓的状态。
运行该命令，然后单击 PCB 中的信号线路或多边形即可。
在命令栏中输入信号名称可以只针对一定的信号进行 Ripup 操作。
RIPUP 命令可以将一条信号线路上两个PAD 或SMD (指元件库封装上的两个焊盘) 之间的布线和过孔都删除，并用一条细直线直接连接这两个焊盘。该命令主要用于设计中对布线进行修改。
DELETE 命令擦除走线，未连接到元件上的走线必须用 DELETE 命令来擦除。

### WIRE 画线
画线或者圆弧。
在第 1 层到第 16 层中使用 WIRE 命令会创建具有电气连接的连线。
Style 参数（CHANGE）决定了线段的类型。
不管线段属于什么类型，DRC 命令和自动布线功能始终将 Wire 作为一条连续的线段。
鼠标右键单击可以更改 Wire 的弯曲类型（SET WIRE_BEND）
请注意帮助功能中 WIRE 和 Ctrl、Shift 组合键的功能：
比如：在开始画线的时候按住 Ctrl 键，就会从最近的已经存在的线段的末端接着走线，即便这条线并不在当前设置的栅格点上，走线的宽度、类型和处于什么层上都会遵循已经存在的线段的属性。

### TEXT 文本
放置文本字符，使用CHANGE SIZE 命令来改变字体的高度。
如果采用矢量字体，可以通过 CHANGE RATIO 命令来改变字符宽度。
CHANGE TEXT 命令可以改变内容。
CHANGE FONT 命令可以改变字体。
在选项/用户界面菜单中的始终使用矢量字体选项可以使用矢量字体来显示和打印所有的文本，而不管针对某些文本的其他字体设置。
CHANGE ALIGN 命令可以定义文本的对齐方式（即文本原点的位置）。
如果想把文本转移到敷铜层， 则必须在 Layer 41，tRestrict 或Layer42，bRestrict 层中输入文本，然后在顶层或者底层使用 POLYGON 命令绕着文本的周围画一个多边形区域，该多边形区域能够保证限制区域（即以上两层中文本）不进行敷铜操作。

强烈推荐在敷铜层中使用矢量字体放置文本！这样才能确保 CAM 处理软件的输出和 PCB 编辑器中显示的字体一致，请参考帮助。

### CIRCLE 圆形
画圆命令。该命令如果使用在 Layer 41，tRestrict、Layer 42，bRestrict或 Layer 43，vRestrict 层中，则表示为 Autorouter/Follow-me Router 创建一个限制区域，如果圆的宽度设为 0，则画的是实心圆。

### ARC 圆弧
画圆弧命令（WIRE 命令也可以实现这个功能）输入 CHANGE 命令，在弹出菜单中选择 CAP/FLAT/ROUND 可以定义圆弧端点以平头或圆头结束。
如果圆弧是走线的一部分。或者圆弧两端都连接走线，则端点会是圆形。
当使用 CAM 处理软件产生 Gerber 格式的数据用于 PCB 制造时，会对平头的圆弧进行仿真。也就是说 CAM 程序会生成一条简短的直线，而圆头的端点则不会进行仿真。

### RECT 矩形
画一个矩形。
该命令如果使用在第 41 层（tRestrict 层）、第 42 层（bRestrict 层）或第43 层（vRestrict 层）中，则为 Autorouter/Follow-me Router 创建一个限制区域。

### POLYGON 多边形敷铜区
该命令用于在信号层上绘制覆铜区或者限制区域。

信号层的多边形敷铜区被作为信号对待。它们和其他信号保持一个可以调节的距离（敷铜，自动敷铜）。这样可以在同一信号层产生不同的信号区域，并在电路设计中生成隔离区。

多边形的轮廓线以点状线进行显示。如果在第 41 层（tRestrict 层）、第 42层（bRestrict 层）或第 43 层（vRestrict 层）中使用 POLYGON 命令绘制多边形，则可以为 Autorouter/Follow-me Router 创建一个限制区域。

请参见帮助功能了解 POLYGON 命令的其它用法。
- **cutout 填充类型**：
以 **cutout** 剪切 作为填充类型的多边形可以用作内部和外部层上针对信号多边形的限制区域。这种类型的多边形会对同一层上与其存在重叠的其他的信号多边形进行裁剪。并且这种多边形的点状外框会始终处于可见状态，外框的线宽也可以设置为 0。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462258073835.png)

### VIA 过孔
在电路板上放置一个电镀过孔，以便让信号从某一层传输到另一层上。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462258227221.png)
VIA 命令的参数工具栏与 ROUTE 命令的参数工具栏后面部分完全相同。

如果在 ROUTE 命令中改变层号会自动生成 VIA。

可以通过 NAME 命令把 VIA 的名称改成一个网络名称来把该 VIA 分配给这个网络。

VIA 在外部层（顶层和底层）可以有不同的外形（比如圆形、正方形和多边形），但是在内部层总是圆形的。

当PCB 设计中添加的过孔的内径小于 DRC 命令的设置对话框中Masks 选项卡中的 Limit 值时，软件不会自动为该过孔添加阻焊层，这时可以通过命令工具栏中 Change→Stop菜单项来添加阻焊层，或者在命令框中输入VIA 命令时在后面添加参数Stop 来加入阻焊层。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462258482828.png)

关于该命令的更多信息，请在编辑器Help 菜单下选择General 命令弹出的对话框中搜索
关键字VIA 。

### SIGNAL 信号
用于定义不同元件的焊盘之间的信号连接，这些连接都以鼠线的方式来表示。
在 VIA 过孔上无法添加信号连接。
如果启用了正反向标注（ Forward&Back Annotation）功能，则无法使用手动定义网络的功能。
这时必须先在原理图编辑器中使用 NET 命令来定义连接。
运行该命令时，命令工具栏中会显示 Net class 分类选项。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462259044787.png)
从 Net Class 下拉菜单中为当前正在绘制的信号连接选择一个网络簇。
网络簇是指信号线路所遵循的一组规则，主要作用是在手动布线和自动布线器布线时，软件会根据原理图中为相应信号分配的网络簇来决定PCB 绘图中的线宽、间距等参数。
请在编辑器Help 菜单下 Gencral 选项的窗口中搜索关键字SIGNAL 查询更多信息。

### HOLE孔
放置一个安装孔（非电镀孔）。

### ATTRIBUTE 属性
为元件定义属性。
通过菜单编辑/全局属性…定义的属性可以用于整个电路板。

### DIMENSION
该命令用于为电路板添加尺寸信息。
通过它可以为某个对象添加尺寸信息，也可以计算任意两点的距离。
当您选中某个对象时，EAGLE 会自动选择一种适当的标尺类型（dtype）。如果该标尺并非所需要的类型，可以通过单击鼠标右键来切换。测量任意两点的距离可以通过按住 Ctrl 键并单击左键来实现。
标尺具有多种不同的类型：平行（Parallel）、水平（Horizontal）、垂直（Vertical）、直径（Radius）、半径（Diameter）、角度（Angle）、和箭头（Leader）。在“选项（Options）/ 设置（Set）/ 标尺（Dimensions）”菜单中可以配置标尺线和文字尺寸单位等。请参见帮助功能页面获取更多信息。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462259266004.png)
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462259281785.png)

### RATSNEST 鼠线轨迹跟踪

用于对鼠线连接的最短距离以及多边形的填充进行计算。
鼠线：指电路板中还没有进行布线的信号连接，此种信号的电气连接关系以细线表示。
当连接某个元件和其它元件的焊盘的鼠线长度发生变化时。(如，当某个元件移动后) 这时运行 ratsnest 就能将各个信号连接的鼠线计算为最短的连接方式。
手动连接鼠线
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462626848785.png)
运行 ratsnest 后
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462626893965.png)

该命令能够对整个 PCB 设计中所有鼠线进行重新计算，并且同时对其中多边形进行计算和填充。如果某些焊盘已经由某个多边形敷铜区连接在一起，则这些焊盘之间就不需要进行布线，从而软件不会对这些焊盘之间的鼠线进行计算，而是直接计算和填充多边形。

1. 计算某个信号的鼠线：
在命令框中指定鼠线的信号名称。
如：RATSNEST VCC
则会对信号名称为 VCC  的鼠线一个多边形进行计算。

2. 对某些鼠线进行计算：
可以在信号名称中使用通配符。
通配符“ * ”表示信号名称中任意一个或多个字符(V* 表示首字母为V，后面为任意单个或多个字符的信号名称)；
“？”表示信号名称中任意单个字符(V？表示首字母为V，后面为任意一个字符)；
“[···]”表示多个信号名称中相互之间具有一定规律的字符，如 RATSNEST V [a-z]C 会对信号名称中首字符为V 、尾字符为C 、并且中间字符为 a~z 范围内的鼠线和多边形进行计算

3. 显示或隐藏鼠线
使用符号" ! "来将指定的鼠线隐藏起来。隐藏鼠线的主要作用在于让某些通过多边形敷铜区连接的信号不可见，例如电源信号，使得绘图更加清晰，容易辨认其他信号。例如在命令框中运行:
RATSNEST ! VCC 
会隐藏 VCC 信号的鼠线。感叹号的两侧均有空格。
如果需要再次显示，在命令框中执行一次不带感叹号的命令即可，这时软件会对该鼠线重新计算。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462630822960.png)


使用 SET 命令可以禁用多边形的计算，也可以通过菜单 Options/Set/Misc 或者输入命令 SET POLYGON_RATSNEST ON | OFF 或简短命令: SET POLY ON |OFF 来实现相同的功能。
当使用 ROUTE 命令画线时自动执行 RATSNEST 命令。
当 RATSNEST 命令有效时，PCB 编辑窗口的状态栏会显示当前计算的网络。
更多的信息请参阅帮助功能。


### Autorouter 自动布线
如果在命令栏中输入 AUTO FOLLOWME 命令会打开 Follow-me 模式下的 Autorouter Setup 设置窗口，在该窗口中可以设置 Follow-me 模式下的一些参数。

启动自动布线器，以便对 PCB 设计进行自动布线处理。
也可针对指定的信号线路布线，例如 AUTO VCC 
软件会对信号名称为 VCC 的所有对象进行布线连接。
如果需要对PCB 设计中的大部分信号进行自动布线，而仅有少部分信号需要手动布线，则可以在命令中加入符号"! "，在后面指定需要手动布线的信号名称，例如在命令框中运行:
AUTO ! GND VCC
则软件会对除了GND 和VCC 信号以外的其他信号进行布线。
AUTO 命令中的信号名称中也可以使用通配符。通配符" * "表示信号名称中任意一个或多个字符(如V *表示首字母为V ，后面为任意单个或多个字符的信号名称) ；
" ? "表示信号名称中任意单个字符(如V?表示首字母为V ，后面为任意一个字符)
" [ ... ] "表示信号名称中的一部分字符与方括号中的字符完全相同，该通配符在指定一系列具有规律的信号名称时非常有用，例如命令" AUTO V[ a - z]C"会对信号名称中，首字符为V ，尾字符为C ，并且中间字符为a~z 范围内的信号进行布线。

自动布线器以 PCB 设计中第20 层(Dimension 层)上WIRE 命令绘制的外框为布线边界，并且布线涉及的层仅为顶层、底层和第2~15 层。如果在自动布线的中途需要停止布线，可以单击操作工具栏中的Stop 按钮中断布线。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462632340031.png)

参考自动布线相关笔记

### ERC 电气规则检查
为原理图和 PCB 图提供一致性检查。
详细介绍参考原理图编辑器笔记。

### DRC 设计规则检查
定义电路板设计及制造相关的参数的设计规则，然后基于这些规则对 PCB 进行检查。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462688185875.png)

DRC 窗口包含了File 、Layers、Clearances 、Distance 、Sizes 、Restring 、Shapes、Supply、Masks 、Misc 10个选项卡，分别对应PCB 设计'中的各种设置。

当设置完成后，单击对话框下方的 

**Check** 检查按钮，即可立即对当前PCB 设计进行检查； 
**Select** 选择按钮后，在PCB 编辑器的绘图区按住左键，并拖曳一个长方形阴影区域，然后放开左键，软件将对该阴影区域进行检查；
**Cancel** 取消按钮用于取消对设计规则所作的修改; 
**Apply** 应用按钮用于将规则应用到当前的PCB 设计上。比如和 Restring 相关的设置，单击 Apply 按钮会立即在 PCB 编辑器中显示。
这4 个按钮不会随选项卡切换而变化，因此在任意选项卡下都可以使用。

大多数参数都配有相应的小图示来进行解释，当单击不同的参数项，窗口左边就会显示相关的图示。

下面将对每个选项卡下的内容进行介绍：

#### **File 文件**
管理设计规则。
File 选项卡下的文字为当前设计规则的描述，不同的设计规则设置可以定义不同的描述，这些描述与当前设计规则一起以文件的形式(文件名为.dru)保存在 EAGLE 安装目录下的 dru 文件夹中，以便在需要时载入。
1. **Edit Descripton 编辑描述** ：该按钮可以对该选项卡下显示的描述进行修改。保存设计规则后，这些描述会在该设计规则再次载入时显示出来。该描述通常出现在 File 书签页。
2. **Load 载入**：用于载入需要的设计规则文件。
3. **Save as 另存为**：该按钮用于将当前设置的规则保存为. dru 扩展名的文件，这样就可以很容易的吧本次的设计规则设置应用到另外的 PCB 文件中。建议将DRC设计规则文件保存在 EAGLE 安装目录下的dru 文件夹中，这样在Control Panel 的Design Rules 树形分支下就能够看到这些文件和右方的描述(即File 标签下的描述)。通过在某个设计规则文件上右击即可以对该规则进行打开、重命名、复制、删除以及应用到某个PCB 设计等操作。也可以把 Control Panel 的树形浏览区中的 Design Rules 分支下的任何 dru 文件拖到一个 PCB 文件中来快速设置设计规则，或者在设计规则窗口中单击File 书签页中的 Load…按钮。
4. **merge into current setting** 合并到当前设置

>The default Design Rules have been set to cover a wide range of applications. 
>Your particular design may have different requirements, so please make the necessary adjustments and save your customized design rules under a new name.

默认设计规则被设置为覆盖宽泛的应用范围。
你的特定设计可能有不同的要求，所有请进行必要的调整，并保存你的自定义设计规则为一个新的名字。

#### **Layers**
定义电路板所使用的层和层叠方式，每个信号层的镀铜厚度，以及信号层之间隔离层的厚度层，VIA 的类型和长度，多层板结构，计算敷铜层数，等参数。
定义信号层数量，过孔的种类（盲孔或者埋孔）。

![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462691349557.png)
1. **Nr**：数值。
2. **Copper** 镀铜：设置每个信号层的镀铜厚度，默认单位为毫米。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462692401342.png)
3. **Isolation** 隔离：设置信号层之间隔离层的厚度，默认单位为毫米。
 ![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462692719906.png)
当鼠标选中下方文本框时，左边的示意图会做出相应的变化，让用户能直观地观察到不同设置项在真实的电路板上的意义。同样的，其他选项卡下也能够看到这样的示意图。Copper项与 Isolation 项文本框下方的 Total 值是当前设置下电路板的总厚度，单位同样为毫米。
4. **Setup**设定：在此栏输入适当的数学表达式，可设置电路板的结构，包括信号层的层数、层叠方式、via 过孔的类型和长度。定义**电路基板 core**，**绝缘板Prepreg** 和实际制造的过孔。
根据设置的层数和层叠方式不同，窗口左边的电路板横切面示意图会做出相应变化。这里默认显示的是两面镀铜电路板和其中的通孔。
在多层板的情况下，需要通过更复杂的表达式来定义多个信号层。
命令 DISPLAY、LAYER、WIRE 和 ROUTE 仅仅工作在 Layer Setup 中定义了的信号层。
当加载一个老版本的电路图时，EAGLE 会检查哪些信号层包含走线，包含走线的信号层会在 Layer Setup 中显示。必要的时候可以修改。

下面是多层板定义中需要用到的符号：

- **星号 * ** : EAGLE 采用"层编号*层编号"来表示两面镀铜的电路板原料(中间的星号可以看做原料板的隔离层) ，而单面镀铜的电路板原料则只需要输入编号即可。
这些原料在电路板制造中称为 Core 核 ，例如1 或者1*16 即为一个Core 。通过这种Core 的层叠即可以制造多层电路板。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462694626093.png)

- **加号 + **：表示粘合层(英文称为Prepreg) 。用于将两个或两个以上的Core 相互粘接，例如1 * 2 + 15 * 16 表示将1 * 2 和15 * 16 两个Core 通过粘合层粘合在一起成为一个4 层板。
 ![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462694747765.png)

- **小括号 ()**: 埋孔和通孔用两个括号表示，例如(1 * 2 + 15 * 16) 表示该电路板存在通孔; 1 + (2 * 3) + 16 表示中间两层存在埋孔。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462694811120.png)
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462694846626.png)

- **方括号与冒号[内部层: 顶层…底层: 内部层]** : 电路板两面的盲孔可以通过这个公式来设置，其中电路板顶层的盲孔表达式为"内部层: 顶层"，底层盲孔表达式为" 底层: 内部层"，输入各个盲孔后在整个表达式的首尾加上方括号即可。例如表达式[ 2:1 `[2:1+2*3+4*15+16:15]`中的"2 : 1" 和" 16 : 15"分别表示顶层到第2 层的盲孔以及底层到第15 层的盲孔。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462695667791.png)

- **过孔分类**：
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462695497248.png)

5. Layers 选项卡下的文字说明
>Layers are combined through either core or prepreg material.

层通过 core 或 预浸材料被组合到一起。
>a*b combines layers a and b with a core,with a+b does the same with prepreg.

a*b 使层 a 和 b 结合为一个 core，a+b 使用预浸材料结合 a/b 两层。
>Buried and through vias are defined by writing (...).

埋孔和通孔通过编写 (...) 来定义。

>Blind vias are defined by writing [t:...:b], which defines a blind via from top to layer t and from bottom to layer b.

盲孔通过编写 [t:...:b]来定义，该公式定义一个从顶层到 t 层，和一个从底层到 t 层的盲孔。

Example : 
>`[2:(1+(2*3)+(14*15)+16):15]` is a multilayer setup with two cores, combining layers 2/3 and 14/15, respectively ,with buried vias going through both cores. 

`[2:(1+(2*3)+(14*15)+16):15]`是含有两个 cores 的多层设置，将2/3 层和14/15 结合为两个cores，分别有两个埋孔穿过这两个 cores 。
>The cores are combined through a prepreg and buried vias are produced through the resulting stack. 

cores 通过一个 预浸材料层接合在一起，埋孔是通过产生的叠层生成的。
>Finally layers 1 and 16 added, with blind vias going from layer 1 to 2 and 15 to 16.

最后层 1 和16被添加盲孔在层 1/2 和 15/16 间.
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462697756787.png)

#### Clearance 最小间隙
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462707825592.png)
Clearance 选项卡下可以对PCB 设计中信号层上元件、线路、钻孔和焊盘相互之间的最小间距进行设置，其中包括属于不同信号的对象之间的间距和属于相同信号的对象之间的间距，
该选项卡下的内容主要分为两个部分，即Different Signals (不同信号的对象)以及Same Signals (相同信号的对象)。
1. **Different Signals** 
可对属于不同信号的 Wire 线路、Pad 直插式焊盘和Via 过孔之间的最小间距进行设置，推荐采用默认单位 mil。梯形的参数排列方式能够很清楚地表示各种对象之间的间距关系。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462708285867.png)
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462708651635.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462708667613.png)


2. **Same Signals** 
表示属于同种信号的 SMD 表面贴片焊盘、Pad和Via 之间的最小间距。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462708385379.png)
对象之间的间距单位可以直接输入，推荐采用默认的栅格单位mil 。
如果希望不对某一项进行检查，可以将该项的值设置为 0mil ，这样通过DRC 命令检查PCB 设计时就会自动忽略对该选项的检查。
可以把同一网络的间距值设置为 0 来取消对该网络的检查。

#### Distance 距离
Distance 选项卡用于设置信号层上的对象与电路板边缘的最小距离，这些对象包括Pad、SMD 和任何连接到这些焊盘上的铜线或敷铜。并且还可以设置钻孔边缘之间的最小距离。
Distance 标签允许在第 20 Dimension 层对对象的最小距离进行设置，该层主要用于电路板外框和孔间距。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462708869785.png)
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462709239123.png)

- **Copper/ Dimension** : 设置信号层上的对象与电路板边缘的最小距离，推荐使用默认单位mil 。如果将该项设置为0 ，则 DRC 在检查 PCB 设计时会自动忽略对该项的检查，取消敷铜和外框之间距离的检查。如果这样设置，EAGLE  将不在对孔是否和走线重叠进行判断，Polygon 敷铜也不再和第 20 层（Dimension 层）的对象保持一定距离。
- **Drill / Hole**: 设置钻孔边缘之间的最小距离，即某两个钻孔相互距离最近的边缘的两条平行切线之间的垂直距离。推荐使用默认单位mil。
如果一个网络属于某一特定的网络簇，该网络的间距和钻孔尺寸（ Drill）则由 Class 命令定义。需要注意到是，此时设定的值需要比设计规则中定义的要高（Sizes 标签中的间距和最小钻孔尺寸设置）

#### Size 尺寸
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462711232226.png)
用于设置信号层中线路的最小尺寸、钻孔的最小内径、微型过孔的最小内径，以及盲孔的最小钻孔直径。
如果网络簇中定义的间距、宽度或者钻孔直径高于此设置中的值才会被设计规则认可。

>Minimum Sizes of objects in signal layers and drill of holes.

信号层和钻孔中的对象的最小尺寸。
>Minimum Width and Minimun Drill may be overwritten by larger values in the Net classes for specific signals.

特定信号的最小线宽和最小钻孔直径可能会被 网络族交大的值覆盖。

Min. Micro Via applies to blind vias that are exactly one layer deep. 

Min. Micro  过孔适用于恰好一层深度的盲孔。
>Typical values are in the range 50 . . 100 micron.

 典型值的范围在50~100微米。
>The value has to be smaller than Minimum Drill; otherwise (e.g. with the default value of 9.99mm) there are no micro vias defined.

该值小于最小钻孔直径，否则该处没有微型过孔被定义(例如，默认值9.99毫米)

>Min. Blind Via Ratio defines the minimum drill diameter d a blind via must have if it goes through a layer of thickness t.

最小盲孔比定义最小钻孔直径 d ，一个盲孔必须有一个深度值 t ，假如它所穿过的层的深度为 t。
>Board manufacturers usually give this "aspect ratio" in the form 1:0.5 would be the value that has to be entered here.

主板制造商通常给窗体 1: 0.5 这"宽高比"会有要在此处输入的值。

- **Minimum Width**: 设置信号层上的最小线宽。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462711270863.png)
- **Minimum Drill** : 设置最小钻孔直径。如果网络簇中设置的最小线宽和最小钻孔直径大于 DRC 规则设置中的值，则软件会以网络簇中的设置为准来处理与该网络簇相关联的对象的线宽和钻孔直径。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462711278255.png)
- **Min. Micro Via**: 设置微型过孔的最小直径。
微型过孔其实是特殊类型的盲孔，只不过其直径很小， 一般来说处于50~ 100mm ，并且这种孔只能够从顶层到第2 层截止，或者从底层到上一层截止， 而不像普通盲孔能够穿过多个内部层。
如果这里设置的最小直径大于 Mimimum Drill 中设置的最小钻孔直径(比如图中该设置项设置的9.99 mm 就大于Minimum Drill 设置项的24mil) ，则表示PCB 中不存在任何微型过孔。换句话说，如果钻孔直径介于 Min.MicroVia 和 Minimum Drill 之间，则该过孔将被看作微型过孔。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462711286765.png)
- **Min. Blind Via Ratio** : 该项的含义是最小盲孔比， 用于定义连接顶层和第2 层或者连接底层和相邻上一层的盲孔必须采用的最小钻孔直径，该直径即由该比率决定。计算
公式是Ratio = t/ d ， 其中t 表示从顶层铜箔下表面到第2 层铜馅下表面之间的距离， d
表示盲孔的最小钻孔直径。PCB 制造商通常将都采用这个比值，并表示为"1 : 0.5" ，即如果 t 为1 ，则最小盲孔直径d 为0.5 ，因此建议不对该项进行修改。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462711297386.png)

#### Restring 焊盘和过孔圆环的直径
该设置决定了 Pads、VIAs 和 Micro Via 上围绕在电镀孔外圈的圆环形铜区的宽度。
环形铜区指当 Pads、VIAs 和 Micro Via 钻孔后围绕该钻孔还剩余的铜区。
可以在电路板内部层和外部层设置不同的圆环形铜区宽度，Pads 在顶层和底层同样可以有不同的设置。
通常情况下，该值用孔径的百分比表示，最大值和最小值还可以另外定义。
一旦修改了参数并单击 Apply 按钮后，修改后的设置马上就会在 PCB 图中表现出来。

如果想在上一层和下一层使用不同的值（比如：用Shapes标签配置不同的焊盘外形，使顶层焊盘和底层焊盘的拥有形状不同），需要对第 17 层（Pads 层）和第 18 层（Vias 层）设置颜色，使其和背景颜色设置一样（黑色或者白色），这样就可在 Pads 层和 Vias 层看到焊盘和过孔的真实尺寸和外形。推荐将第 17 层（Pads 层）和第 18 层（Vias层）设置为与背景色相同的颜色（黑色或白色）。这样您就能在相应的层中分辨焊盘/过孔的真实尺寸和形状。
下图中带斜线的圆圈，就是过孔在第二层中的显示效果(已将17/18层设置为背景色)。在非背景色的情况下，看不大斜线。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462762644615.png)

INFO 命令和右键弹出菜单的属性选项一样具有相同的对话框，从中可以了解 Via 在外部层和内层的尺寸，以及最初的用户设定值，参考下面的图：
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462762837798.png)
~~上图中参数的意义：~~

~~预定义值外径（使用 CHANGE DIAMETER 命令）：0.7~~

~~外部层中实际计算的直径： 0.9~~

~~内部层直径实际修改过的值： 0.8~~

~~根据设计规则的 Restring 标签设置中对过孔的最小值设置，实际的过孔直径比预设的值大。~~

下图是设置 Restring 的模板，Restring 标准值为过孔直径的 25%，如果按照这样的算法，小型孔的 Restring 值很容易就低于最低的制造工艺值，因此，必须在此设定最小值（Pads:10mil，Vias：8mil，Micro Vias：4mil），当然，在此定义最大值也是可行的。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462757841973.png)
下面以一个实例来解释 Restring 的设置：
如果有一个直径为 40mil 的过孔，则该过孔的 Restring 值应该为 10mil（25%），10mil 的宽度刚好位于最大值（20mil）和最小值（10mil）之间。
如果该过孔直径仅仅只有 24mil（比如是 VIA），按照 25%的比例计算，该孔的 Restring 值应该仅仅只有 6mil，以标准 PCB 制作工艺来衡量，6mil 的宽度相当精细，制作难度很大，并且可能会增加额外的成本。因此，此时的Restring 值就会按照设计规则规定的最小值 10mil 来设定。
如果想定义一个固定的 Restring 值，可以设置最小值和最大值为同一值，这样上图中的百分比计算将不再有效。
**Diameter 复选框**：
如果您需要在元件库中为一个 Pads 定义直径，或者在 PCB 编辑器中为 Via 定义直径，并且您想把这个直径值应用到电路板内部层，请先激活 Diameter 选项。如果预定义的 Pad 或者 Via 的直径超越了设计规则计算后的直径，那就相当有趣了。否则 Pad 或者 Via 的内部层直径应该比外部层直径小。如果想让Pad 或者 Via 的内部层直径和外部层直径相同，请设置 Diameter 选项。
默认情况下，新创建的电路板中该选项设为 Off 状态，但是从 3.5 版后可以被设置，因为这些版本中的 Pad 或者 Via 在所有层的直径相同。因此，更新处理不会改变原始的电路板设计。
~~所有给定的值是以毫米为单位（比如：0.2mm）。~~

当选项卡单击Vias 和Micro Vias 设置项右方的设置框，该示意图会发生相应的变化来表明不同类型的孔的Restring 宽度定义。

1. **Pads**: 该项右方包含了对直插式焊盘在电路板顶层Top 、内部层Inner和底层Bottom上的Restring 的设置框。
每种层提供了3 个设置框，第一个和最后一个设置框分别表示焊盘 Restring 的最小值和最大值，中间的设置框表示 PCB 中焊盘的 Restring 宽度与内径的百分比。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758157865.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758169163.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758176616.png)

2. **Vias**: 该项有方包含了过孔在外部层(Outer ，即顶层或底层)和内部层上的Restring宽度设置框。各项设置框意义同上。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758650427.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758658591.png)


默认情况下， Pads 和 Vias 项中的内部层的 Restring 宽度与焊盘和过孔的内径没有任何
比率关系，并且总是小于外部层的Restring 。如果选中Inner 项右边的Diameter 直径复选框，则内部层上的Restring 由Inner 项和过孔内径决定。

3. **Micro Vias**: 微型过孔实际上就是仅连接外部层和相邻内部层的盲孔， 其内径比 Siz e 标签下 Minimum Drill 项规定的值还要小。在这里可以对微型过孔在外部层和内部
层的 Restring 宽度设置。各项设置框意义同上。可能会被网络分类中更大的 Drill 值覆盖。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758675292.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462758683574.png)

当Min 和Max 的值都为0 时，百分数无效，这时以实际设定的 Pad 或 Via 内外径为准，外层尺寸和外径相同，内层尺寸和内径相同。

在某些情况下， Pad 和 Via 的外径尺寸较大，从而使得Restring 宽度超过了Max 的值，这时软件会将这个 Restring 宽度作为外部层上实际应用的宽度。这些情况包括:
**第一种情况：** 当内径和百分比相乘的结果小于Min 或者大于Max ，Restring 宽度应为 Min 或 Max 的值。这时如果(手动设置的外径 - 内径)/2 的值小于 Min，则 Restring 宽度不做改变，因而实际显示的外径会比手动设置的外径更大；如果大于Max，则软件会采用这个较大的数值作为 Restring 的宽度。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462774630002.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462774648534.png)


**第二种情况：**当内径和百分比相乘的结果处于 Min 和Max 之间时，Restring 的宽度应为相乘后得出的结果，这时如果 (手动设置的外径 - 内径)/2 值小于相乘的结果，则 Restring 宽度不做改变，因而实际显示的外径会比手动设置的外径更大；如果大于相乘的结果，则软件会采用这个较大的数值作为 Restring 的宽度。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462775031003.png)![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462775061369.png)
如果需要设定一个固定的 Restring 宽度值，则需要把 Min 和 Max 项设置为某一个相同的值，这时 Restring 的宽度即等于这个值，不会受中间的百分比的影响，但仍然遵循第一中情况描述的规则。

#### Shapes 形状
可对 SMD 和 Pad 焊盘的形状进行设置。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462796642541.png)

1. **Smds**：设置表面贴片焊盘的转角弧形的大小。
为Smd 焊盘定义圆形因数。因数值在 0%（不需要圆形）到 100%（最大圆形）之间，参考下图：
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462801497501.png)
上图最右边是用一个正方形来代替矩形的 SMD 焊盘，当圆形比率设置为 100%时，SMD 焊盘就变成了圆形。

**Min** ：表示弧形的最小半径。
**Max**： 表示最大半径。
**%** ：文本框为从 0~100 的百分数，表示转角的当前直径与 SMD 焊盘最短边的比值，即该比值乘以 SMD 焊盘的最短边长度，结果等于当前转角直径。该直径除以2 后不能小于Min 项的值，或大于Max 项的值，否则以 Min 或 Max 的值为准。边长包含弧形部分。

如果 Min 和 Max 值都为0 ，则表示转角为直角，中间的百分数不产生作用。如需固定转角大小，可在 Min 和 Max 中输入相同的转角半径，这时软件也会自动忽略中间的百分数。

2. **Pads**：这是一种特别定义的直插式焊盘，该焊盘在顶层和底层可以有不同的形状。
**Top 和 Bottom** ：下拉菜单中可选择：As in library 保持原状、square正方形、round 圆形、octagon 八角形，用于设定封装被放置到 PCB 设计中时，焊盘在顶层和底层上所显示的形状。
值 As in library 表示 Pads 的格式由封装编辑器定义，单击 Apply 按钮马上就会在 PCB 编辑器中改变。
注：Pad 和 Via 在内部层的焊盘总是圆形，无论它们在顶层或者底层是什么形状，其直径由 Restring 的设置来决定。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462799180633.png)
**First** ：用于为封装上的第一个焊盘选择一个形状，以便和其它焊盘进行区分。如果在元件库中的封装上的第一个焊盘定义为首选，则当该封装放置到 PCB 设计中时，第一个焊盘就会以这里选中的形状表示。可选项有 not special 不区分、square 用正方形表示、round 用圆形表示、octagon 用八角形表示。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462800905829.png)
**Elongation延长** ：定义了焊盘长度和宽度的比率，以及焊盘长度和偏移的比率。单击图中的比率值，会在左边的窗口中看到对应的计算公式。
设置项用于设置长条形(Long) 和偏置形 (Offset) 直插式焊盘在PCB 设计中的长度，文本框中的数值为百分数。该百分数表示焊盘上"除去外径后的长度" 与外径d 的比值。
文本框一：100%表示长宽比为2:1；0%表示一个长宽比为1:1的正常八角形焊盘；最大设置为200%，比率4:1.
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462801082333.png)
文本框二：
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462801090939.png)

**PCB 编辑器显示的注意事项：**
如果 Pads 或 Vias 在不同层定义了不同的外形，当前信号层中可见的外形（使用 DISPLAY 命令）会出现在其他外形的上面。
如果第 17 层（Pads 层）和第 18 层（Vias 层）定义的颜色和背景色相同，并且它们以它们所代表的层的颜色和填充样式来显示，如果信号层不可见，此时Pads 和 Vias 不会显示。
如果第 17 层（Pads 层）和第 18 层（Vias 层）定义了和背景色不同的颜色，并且信号层不可见，此时 Pads 和 Vias 的外形会在顶层或者底层显示。
上面的应用也可以使用 PRINT 命令来打印。


>If pads or vias have different shapes on different layers, the shapes of the currently visible (activated with DISPLAY) signal layers are displayed on top of each other.

如果 pads 和vias 在不同的层有不同的形状，当前可见的信号层中的焊盘形状被显示在彼此的顶部。使用了 DISPLAY 激活相关层。
>If the color selected for layer 17, Pads, or 18, Vias, is 0 (which represents the current background color), the pads and vias are displayed in the color and fill style of their respective各自 layers. 
>If no signal layer is visible, pads and vias are not displayed.

如果17, Pads, 或 18, Vias 层选择颜色 0 (表示当前背景颜色)，pads和vias 在各自层的颜色和填充类型中显示。
如果没有信号层可见，pads 和 vias 不会被显示。
>If the color selected for layer 17, Pads, or 18, Vias, is not the background color and no signal layers are visible, pads and vias are displayed in the shape of the top and bottom layer.

假如 17, Pads, 或 18, Vias 层所选择的颜色，不是背景颜色并且没有信号层是可见的， pads 和 vias 显示在顶层和底层的形状。
>This also applies to printouts made with PRINT.

这也使用于打印输出，使用 PRINT 命令。

#### Supply 电源标签
>Specifies the settings for Thermal symbols.
>设定热焊盘符号。
>![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462885540636.png)
>The value for Thermal isolation determines决定 the distance between a polygon and the restring of the pad or via that is joined连接 to the polygon through a Thermal symbol.

Thermal isolation 指散热隔离的值，该值决定了多边形敷铜区与pad/via 的 restring 之间的距离，pad/via 通过一个热焊盘符号连接到多边形敷铜区。

>The Generate thermals for vias flag permits Thermal symbols at through-­holes.

Generate thermals for vias 选项允许在过孔上生成热焊盘符号。
>Otherwise vias are fully connected to the copper plane. 

如果不选中该复选框，vias 被完全连接到敷铜区域。
>This applies also for polygons. 

该选项也适用于多边形敷铜区。
>But you can disable this option for individual个别的 polygons with CHANGE THERMALS OFF and a mouse click onto the polygon's contour轮廓.

但你可以为个别多边形禁用该选项，适用 CHANGE THERMALS OFF 命令并鼠标单击多边形的轮廓。

Inside hatched polygons EAGLE doesn't generate产生 Thermal symbols for vias that do not have a direct contact to one of the polygon lines.

vias 没有直接连接任何一个多边形的连线，此时在以 Hatch 模式填充的多边形内部，eagle 不会为该 via 生成热焊盘符号。

>Pads or SMDs marked with the flag NOTHERMALS (CHANGE THERMALS OFF) in the Package Editor will be connected basically without Thermal symbols.

在封装编辑器中含有 NOTHERMALS (CHANGE THERMALS OFF)标记的 Pads 或 SMDs 将不会使用热焊盘符号连接。

**Thermal isolation**散热隔离：设定热焊盘隔离区的宽度。
**Generate thermals for vias** 选项允许在过孔上生成热焊盘符号。该选项也适用于多边形敷铜区

#### Mask 阻焊层和焊膏层的值
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462888414588.png)

设置阻焊层和焊膏层中针对 Pad / SMD 焊盘的阻焊漆与焊膏。
对阻焊层 Solder Stop Mask （ Stop）和焊膏层 Solder Cream Mask（Cream）的余量值进行设置。
将 Package 定义中 Pad 或 SMD 的 STOP 或 CREAM（仅针对 SMD）选项设置为 OFF时，可以禁止 EAGLE 生成阻焊层或焊膏轮廓。


1. **Stop**阻焊：表示阻焊符号，其数值是斜线阴影部分超出焊盘的距离。阻焊漆将会围绕阴影区域进行上漆，而不会进入该区域，以免阻碍焊盘的焊接。该距离以 SMD 焊盘的短边或直插焊盘的外径的百分比表示，并且该距离只能在 Min 和 Max 的范围之间。设置 long 或 offset 型的 smd 和pad 的余量值时，百分比的关键值是其中较小的值。阻焊层位于第 29 层（tStop 层），或者第 30 层（bStop 层）。
当 min 和 max 的值相等时，例如默认值 4mil，最小值和最大值都为 4mil。这时百分比值没有作用，这时阻焊符号超出焊盘的距离确定为4 mil 。

2. **Cream**焊膏 : 表示焊膏符号，使用正值，仅适用于SMD 焊盘，并且显示在第31 tCream 或32 bCream，其数值即 SMD 焊盘超出斜线阴影的距离。焊膏将被限制在斜线阴影部分内，而不会超出该区域，以免焊锡溢出。该距离以 SMD 焊盘短边的百分比捷示。默认 Cream 的值等于0 时，则表示焊膏涂抹范围覆盖整个SMD 焊盘。
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462890455399.png)

3. **Limit**限制 : 该项用于设置一个限制值，默认值为0 ，表示所有在PCB 设计中放置的Via( 过孔)都向动添加阻焊符号，即所有过孔都不涂抹阻焊漆。
当Limit 的值大于0 时，则所有内径小于或等于该值的Via 都不添加阻焊符号(即都要涂抹阻焊漆) ，只有大于该值的Via 才会带有阻焊符号。如果需要强行为内径小于该值的过孔添加阻焊符号，可以通过CHANGE 命令按钮菜单下的 stop 项来修改。
设置 Limit = 24：
所有直径小于或等于 24mil 的电镀过孔都不带有阻焊符号（它们都覆盖阻焊漆），直径大于该限制的过孔则带有阻焊符号。
对于直径小于 Limit 的过孔可以设置 STOP 选项（命令 CHANGE STOP ON）。然后 EAGLE 会生成一个阻焊层。

#### Misc 其他检查项
![Alt text](0x03_Layout_Editor(PCB编辑器).assets/.1462892590460.png)

1. **Check grid 检查栅格**：用于检查PCB 设计中所有的Pad 、SMD 、Via 和线路是否处于当前栅格上。由于PCB 设计中常常会同时用到米制单位栅格和英制单位栅格上建立的元件，因此不可能找到同时适合这两种元件的栅格设置，所以该检查并非必不可少。

2. **Check angle 检查夹角**：检查线路夹角，以便确保所有夹角都是45°的倍数。默认为禁用状态，在需要检查时可以启用该复选框。
3. **Check font 检查字体**：启用该复选框后， DRC 会检查PCB 设计中是否使用了向量字体，所有非向量字体都会被标记为错误。由于CA M 程序生成制造数据时不能采用非向量字体，否则会造成线路长度随文本尺寸而变化，因此该项检查非常必要。建议启用该复选框。
假设您在底层上使用了按比例变化字体的文本，并把它放在两条走线之间，然后使用 CAM 处理程序来生成 Gerber 文件，走线有可能随着文本尺寸而缩短（文本的高度和长度可能发生变化）！

4. **Check restrict 检查约束**：由于第41 层( tRestrict) 和第42 层( bRestrict) 中绘制的限制区域不允许在顶层和底层正对应的区域内放置任何铜质对象(如过孔、线路和焊盘等) ，因此需要启用该复选框对限制度域进行检查。但是在某些情况下不需要对限制区域中的铜质对象进行检查，也可以禁用该复选框。另外， 如果限制区域和铜质对象是在建立封装时进行定义的，则EAGLE 会自动忽略对它们的检查。
通过 cutout 多边形实现的限制区域不会被 DRC 功能检查！
对于设计规则的设置操作同样可以使用 UNDO/REDO 功能进行撤销和恢复。
默认设置为：启用。

5. **差分对最大长度差值**：参考蛇形线笔记
6. **差分对中蛇形线部分的间隙因子**：参考蛇形线笔记

### ERRORS 错误报警
显示 DRC 检查的错误报警。
当 PCB 板还没有执行设计规则检查时，如果系统发现有任何的错误就会在显示错误报警信息列表之前自动检查。

PCB 编辑器中的ERRORS 命令按钮与原理图编辑器中的同名按钮功能相似，用于显示绘图中最后一次执行检查后所发现的错误。不同的是，该按钮显示的是 DRC 命令所发现的错误，而不是原理图编辑器中的 ERC 命令。
请同时参考原理图编辑器中 ERRORS 命令按钮章节的内容。