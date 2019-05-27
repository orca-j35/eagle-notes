# 1x02_Technical_Terms(技术术语)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库



>In this manual, in the help function, and in EAGLE itself we frequently频繁的 use some technical terms术语 that should be explained讲解 here in a few words.

这里简要介绍在该手册中、帮助功能中以及 EAGLE 软件中经常用到的某些技术术语。

## 1. Airwire:
>Unrouted connection on a board, displayed in the unrouted layer (= rubber band).

Airwire 鼠线：
电路板上未经布线的连接，它显示在未布线层中（=rubber 伸缩线）。
这些线以笔直的细线形式表示，处于电路板的第 19 unrouted 层上。在 PCB 设计中通过 SIGNAL 命令可以添加鼠线。

## 2. Blind Via:
>A plated­-through hole for changing the layer of a track which has not been drilled through all layers in the production process of a multilayer board.

Blind Via 盲孔：
在多层电路板设计中用于顶层或底层与中间某一层之间实现电气连接的电镀孔，该孔并未贯穿电路板的所有分层。
![Alt text](1x02_Technical_Terms(技术术语).assets/.1465276514854.png)

## 3. Buried Via:
>A plated­trough hole, which has been drilled through the current layer stack in the production process like a normal (through) via, but does not connect all layers of the whole board.

Buried Via 埋孔：
在多层电路板设计中实现中间两层或多层电气连接的电镀孔，该孔并未贯穿顶层和底层。
![Alt text](1x02_Technical_Terms(技术术语).assets/.1465276532997.png)

## 4. Core:
>Two copper镀铜 layers applied应用 to a solid固定 substrate基底.

Core 基板：
带有一层或上下两层未蚀刻敷铜层的固化基板。
带有一层或上下两层未蚀刻的敷铜层的固化板，层设置中用 * 号表示。例如 1 * 2 + 15 * 16 ，表示第1层和第2层所组成的部分，以及第 15 和 16 层所组成的部分，分别是两个 core。
core 通常用于叠层起来制造多层电路板，一般不会直接制作为双层板，因为双层电路板有专门的成品板可供使用，其规格与 core 不同。
![Alt text](1x02_Technical_Terms(技术术语).assets/.1465276606150.png)

## 5. Design Rule Check (DRC):
>EAGLE can identify the violation of certain Design Rules (e.g. if two different tracks overlap or are too close) with the DRC.

Design Rule Check 设计规则检查（DRC）：
EAGEL 软件可以通过 DRC 识别某些违反设计规则的错误（例如两条不同的线路相互重叠或者距离太近的情况）。

## 6. Device:
>A fully defined element in a library. 
>Consists of at least one Package and one Symbol.

Device 元件：
元件库中完整定义的元件。至少包含一个封装符号和一个原理图符号。

## 7. Device Set:
>Consists of Devices that use the same Symbols for the Schematic but have different Package variants or technologies.

Device Set 元件组：
元件组包含相同的原理图符号，但同时提供多个不同的封装符号。

## 8. Drill:
Plated­through drilling in the layout (in pads and vias)

Drill 钻孔：
PCB 设计中在焊盘或过孔上钻孔。
直插式焊盘和过孔上钻的孔的直径(即中间钻空部分的直径)，用于焊接电容等原件或者改变布线所在的层。

## 9. Electrical Rule Check (ERC):
>EAGLE can identify the violation of certain electrical rules (e.g. if two outputs are connected) with the ERC. 
>It also checks the consistency of the schematic and the layout.

Electrical Rule Check 电气规则检查（ERC）:
EAGLE 软件可以通过 ERC 识别某些违反电气规则的错误（例如两个输出端相互连接的情况）。
该软件还可以检查原理图和 PCB 设计的一致性。

## 10. Follow­me Router:
>The manual ROUTE command offers an operating mode that calculates and displays the connection of a selected signal automatically. 
>The current position of the mouse cursor determines the trace of the connection. 
>Only available with the Autorouter module.

Follow-me Router 跟随布线器：
手动 ROUTE 命令提供了一种能够自动计算和显示某个被选信号连接的工作模式。
鼠标的当前位置决定了连接的线路。
只有安装了自动布线器时才能使用该功能。
随着鼠标指针的移动，软件会进行实时计算并提供不同的参考。

## 11. Forward&Back Annotation:
>Transforms all the actions one makes in a schematic online into the layout (and with limitations from layout into schematic). 
>Both files are consistent all the time.

Forward&Back Annotation 正反向标注:
将原理图中所作的修改反映到 PCB 设计中的功能叫做正向标注（反之叫做反向标注，反向标注有一定的限制）。
该功能可以保证原理图和 PCB 设计在任何时候都是一致的。

## 12. Gate:
>The term Gate is used in this manual for a part of a component which can be individually placed on a schematic. 
>This can be one Gate of a TTL component, one contact pair in a relay, or an individual resistor from a resistor array.

Gate:
本手册中所用的术语 Gate 是指可以单独放到原理图中的某个元件的一部分。
它可以是 TTL 元件的一个逻辑门、或者继电器的一对触点、或者电阻阵列中的一个单独的电阻。
隐藏的 GATE 通过 invoke 放置。

## 13. Hole:
>Non plated­through drilling in the layout (e.g. a mounting hole).

Hole 孔:
PCB 设计中的非电镀孔（比如安装孔）。

## 14. Layer Stack:
>Current number and order of copper and isolation layers which are used to build up a printed circuit board.

Layer Stack 电路板层叠:
用于制造印刷电路板的敷铜层和隔离层的当前层号和序号。
表示电路板制造过程中由多个 core 和隔离层堆叠在一起组成的部件。

## 15. Micro via:
>A plated­through hole (like Blind via) with a relatively small drill diameter which connects an outer layer with the next reachable inner layer.

Micro via 微型过孔:
一种直径相对较小的电镀孔（与盲孔相似），用于连接某一外层和另一个需要连接的内部层。
微型过孔是一种直径非常小的电镀过孔，通常直径为 0.05~0.1mm,并且只连接顶层与第二层或者底层与上一层，因此也可以看做是一种特殊的盲孔，不同之处在意普通盲孔可以连接内部层并且直径较大。
![Alt text](1x02_Technical_Terms(技术术语).assets/.1465276914624.png)

## 16. Module:
>A subunit of the hierarchical schematic that contains a smaller part of the schematic

模块：
层次化电路原理图的子部分，模块用于连接原理图的一小部分。
## 17. Module instance:
>A simple symbol in a superior level in the hierarchical schematic that represents the usage of a module.

模块实例：
在层次化的原理图中的上一级中的一个简单符号，用于表示一个模块的使用。
## 18. Net:
>Electrical connection in a schematic.

Net 网络:
原理图中的电气连接。

## 19. Package:
>Component footprint stored in a library.

Package 元件封装:
保存在元件库中的元件封装，即 Footprint覆盖区。

## 20. Pad:
>Through­hole pad associated with a Package.

Pad 通孔焊盘:
元件封装上的电镀通孔。表示该元件为直插式元件。
## 21. Pin:
>Connection point on a Schematic Symbol.

Pin 引脚:
原理图符号上的一个引脚。
## 22. Port:
>Similar to a pin, the port connects module instances in the hierarchical diagram with nets.

端口
类似于一个引脚，在层次化的示意图中端口用于连接模块实例和网络。

## 23. Prepreg:
>Used in a compound of inner and outer layers for multilayer boards.

Prepreg 半固化片：
用于多层电路板内层和外层间的化合物。
多层电路板中用于连接两个内部层并提供绝缘功能的一种半固化树脂。2 和 15 层间为半固化片。
![Alt text](1x02_Technical_Terms(技术术语).assets/.1465277093134.png)

## 24. Rack:
>Configuration table for a drilling machine. 
>Needed for generating drill data.

Rack 钻孔数据配置表:
PCB 制作时钻孔设备的配置表，用来产生钻孔数据。

## 25. Ratsnest:
>Command for calculating the shortest airwires and for hiding or displaying certain airwires for a better overview.

Ratsnest 鼠线轨迹跟踪 :
该命令用于计算最短鼠线，或用于隐藏或显示某一鼠线以获得更好的显示效果。
当元件被移动后，可以使用 Ratsnest 命令来重新计算鼠线的最短路径，并刷新以前的鼠线。
更详细的解释请参考软件帮助菜单中关于 Ratsnest 命令的内容
## 26. Restring:
>Pronunciation: rest­-ring. 
>Setting that determines the width of the copper ring around a plated­through hole of a pad or via.

Restring 圆环宽度:
发音为“rest-ring”，设置焊盘或者过孔的电镀孔铜箔的圆环宽度。
## 27. Signal:
>Electrical connection in a board.

Signal 信号网络:
电路板上的电气连接。
通过 singal 命令可以绘制信号线段，并以鼠线的形式表示。

## 28. Supply Symbol:
>Represents a supply signal in the schematic. 
>Causes the ERC to run special checks.

Supply Symbol:
表示原理图中的一个电源符号。
ERC 会对该符号进行专门的检查。

## 29. Symbol:
Schematic representation of a component, stored in a Library.

Symbol 原理图符号:
保存在元件库中元件示意图的一种表示方式。

## 30. User Language:
>Freely programmable, C­like language for data import and export.

User Language 用户语言:
可以自由编程的一种类 C 语言，便于数据的输入和输出。
## 31. Via:
>Plated­through hole for changing the layer of a track. See also Micro via, Blind via, and Buried via.

Via 过孔:
用来改变 PCB 布线层的一种金属孔，有不同的类型：微型过孔、盲孔和埋孔。

## 32. Wheel:
>Aperture configuration file. Generated with Gerber data for board manufacturing.

Wheel 光圈配置文件:
光圈配置文件，用来产生 PCB 制作时的 Gerber 数据文件。

## 33. Wire:
>Electrical connection in a board, or a line (since lines are drawn with the WIRE command).

Wire 金属连线:
电路板上具有电气特性的连线（或者使用 WIRE 命令画出来的线）。
原理图或 PCB 设计中的无电气属性的线段或带电气属性的线段(是否带电气属性取决于所在的层，一般不推荐用 WIRE 命令来绘制带电气属性的线段 )。

## Annolus Symbol (环形符号)
在敷铜区或电源层中存在的环形隔离符号，该符号用于将某个信号与敷铜区或电源层完全隔离开来。

## Technology
EAGLE 使用单词 Technology 来表示不同的集成电路设计技术，如TTL 、LVTTL 、CMOS 、ECL 等。