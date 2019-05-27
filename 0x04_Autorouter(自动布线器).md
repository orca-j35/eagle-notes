# 0x04_Autorouter(自动布线器)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库

eagle 允许用户按照一定的设计规则进行自动布线或半自动布线(跟随布线)。


## 1.  自动布线器的基本特性
- 任意布线栅格（最小 0.02 毫米）Any routing grid (min. 0.02 mm)
- 任意布局栅格（最小 0.1 微米）Any placement grid
- 完全集成到基本程序中 Fully integrated into basic program
- TopRouter with gridless routing algorithm, which can be preceded by the Autorouter
无网络布线算法 TopRouter ，该算法在 autorouter 之前发生。
- Optional automatic selection of routing grid and preferred directions in the signal layers .在信号层中，可以选择自动设置栅格选项和自动设置首选方向。
- Support for multi­core processors to process multiple routing jobs simultaneously 支持多核处理器，以同时处理多个布线作业。
- 表面贴装元件可布置在电路板两面。SMDs are routed on both sides
- 整个绘图区域都可作为布线区域（前提是有足够使用的内存）The whole drawing area can be the routing area (provided enough memory is available)
- 可通过控制参数来选择布线策略 The strategy is selected via control parameters
- 能同时对定义了不同线宽和最小间距的各种不同信号簇进行布线 Simultaneous同时 routing of various各种 signal classes with various track widths and minimum clearances间隙
- 采用设计规则检查和自动布线器的通用数据设置（设计规则）Common data set (Design Rules) for the Design Rule Check and the Autorouter
- 支持多层电路板功能（能同时对多达 16 个层进行布线，而不仅限于一对/两层）Multilayer capability能力 (up to 16 layers can be routed simultaneously同时, not only in pairs)
- 支持盲孔和埋孔 Support of Blind and Buried vias
- 能独立设置每个层的首选走线方向：水平方向和垂直方向，正 45/135 度（对内部层非常重要！）The preferred track direction can be set independently for each layer: horizontal and vertical, true 45/135 degrees (important for inner layers!)
- 对 100%的布线进行取消和重新布线 Ripup and retry for 100 % routing strategy策略
- 通过减少过孔和平滑走线路径来进行优化 Optimization passes to reduce vias and smooth track paths 路径
- 不会改变预布线  Prerouted tracks are not changed
- 提供基本的 Follow-me 布线功能，它是布线命令的一个特殊操作模式，允许对所选信号进行自动布线。Serves a basis for the Follow­me router, a special operating操作 mode of the ROUTE command that allows automatic routing of selected signals

## 2.  What Can be Expected from the Autorouter 自动布线器给出怎样的期望

The EAGLE Autorouter is a "100%" router.
EAGLE 自动布线器是一个“100%”布线器

This means that boards which, in theory, can be completely routed will indeed真正的 be 100% routed by the Autorouter, provided - ­and this is a very important restriction -­ the Autorouter has unlimited无限的 time. 

如果 Autorouter 没有时间限制—这是一个非常重要的限制—那么意味着在理论上电路板能够通过  Autorouter 真正的完成 100% 布线。

This restriction限制 is valid for all 100% Autorouters whatsoever任何. 
这个时间限制对所有的 100%自动布线器都是有效的。

However, in practice实际, the required需要 amount数量 of time is not always available可获得, and therefore certain某些 boards will not be completed even by a 100% Autorouter.
但实际上所需要的时间并不能始终得到保证，因此一些电路板并不能通过 100% 自动布线器来完成所有布线。
-
The EAGLE Autorouter is based on the ripup/retry algorithm. 
EAGLE 自动布线器基于 ripup/retry 取消/重试算法。

As soon as it cannot route a track, it removes prerouted tracks (ripup) and tries it again (retry). 
当它无法为一条线路布线时，可以删除先前的布线然后重新布线。

The number of tracks it may remove is called ripup depth which is decisive决定 for the speed and the routing result. 
线路能够被删除的次数叫做取消深度，它对运行速度和布线结果起决定性作用。

This is, in principle原理, the previously mentioned提到的 restriction限制.
从原理上讲，这就是先前提到的限制。
-
In the Autorouter main dialog it is possible to choose a TopRouter variant.
在  Autorouter main dialog 可以选择 TopRouter 变体。

It uses a gridless algorithm with topological approach. 
TopRouter 使用了一个含拓扑方法的无栅格算法。

This algorithm calculates first the course of the signals and then uses the optimization runs of the traditional EAGLE Autorouter to meet the Design Rules. 
该算法首先计算信号过程，然后使用传统的 EAGLE 自动布线程序的优化运行，以满足设计规则。

Typically, the TopRouter requires需要 significantly明显 fewer vias than the traditional传统的 EAGLE Autorouter. 
通常情况下，TopRouter 需要比传统的 EAGLE 自动布线程序明显减少通孔。

The user has the option to select both methods方法 for a project and eventually最终 opt for one or the other routing result.
用户有一个选项，以对一个项目选择两种方法，并最终选择这种或其余布线结果。
-
Those who expect期望 an Autorouter to supply提供 a perfect board without some manual help will be disappointed失望. 
用自动布线器实现一个完美电路板而不需要手工帮助并不现实

The user must contribute贡献 his ideas and invest投入 some energy精力. 
用户必须同时
投入自己的智慧和精力。

If he does, the Autorouter will be a valuable宝贵 tool which will greatly reduce减少 routine work.
这样自动布线器将会是一个很有价值的工具，可以极
大的减少工作量。
-
Working with the EAGLE Autorouter requires要求 that the user places the components and sets control parameters which influence影响 the routing strategy策略.
使用 EAGLE 自动布线器前需要使用者放置元件和设置控制参数，因为它们会影
响到布线策略。

These parameters must be set carefully if the best results are to be achieved获得.
要达到最好的效果，必须谨慎的对这些参数进行设置。
They are therefore described in detail in this section.
本章节将对其进行详细的描述。

## 3. Controlling the Autorouter 控制自动布线器
The Autorouter is controlled by a number of parameters. 
自动布线器通过大量的参数进行控制。

The values in the current Design Rules, the net classes and special Autorouter control parameters all have an effect.
在当前设计规则 DRC、网络族 和专用 Autoroute 控制参数的值都对自动布线器有影响。
-
The Design Rules specify the minimum clearances (DRC commands for setting Clearance and Distance), the via diameter (Restring setting) and the hole diameter of the vias (Sizes setting). 
设计规则指定了最小间距（ DRC 命令用来设置间距和距离），过孔直径（Restring 设置），过孔内径（size 设置）。

The minimum track width is also specified.
最小线宽也需要设定。
-
The net classes ­ if any are defined ­ specify指定 special 特殊minimum clearances, track widths and the hole diameters for vias carrying particular signals.
如果定义了网络簇，则其规定了传输特定信号的过孔的最小间距、线宽和过孔内径。
-
There is also a range of special特定 cost factors因素 and control parameters that can be changed via the Autorouter menu. 
通过自动布线器菜单可以在一定范围内改变花销因数和控制参数。

They affect the route given to tracks during automatic routing. 
它们在自动布线时会影响布线。

Default values are provided by the program. 
程序会为这些参数提供默认值。

The control parameters are saved in the BRD file when the layout is saved. 
当保存 PCB 设计时这些控制参数会保存在 BRD 文件中。

You can also save these values in an Autorouter control file (*.ctl). 
您也可以将这些值保存在一个自动布线器控制文件（*.ctl）中。

This allows a particular特殊 set of parameters to be used for different layouts. 
这样可以把特殊设置的参数用到不同的 PCB 布局设计上。

Neither Design Rules nor the data for various各种 net classes are part of the control file.
控制文件中不包含针对各种网络簇的设计规则和数据。
-
A routing process involves a number of separate basic steps:
一个布线过程涉及到多个独立的基本步骤：

### 3.1 Bus Router
Normally the bus router starts first. 
正常情况下，首先启动总线布线。

It deals处理 with signals which can be routed in the preferred direction with only slight轻微 deviation偏离 in x and y direction allowed. 
Bus Router 处理那些在首选方向能布通的信号，并且首选方向只允许在 x 和 y 方向有少许偏差。

The bus router takes only those signals into consideration考虑 that belong属于 to net class 0.
总线布线仅考虑那些属于网络簇 0 的信号。

This step may be omitted.
这一步可以被省略。

`Buses, as understood by the Autorouter, are connections which can be laid as straight lines in the x or y direction with only a few deviations偏离.`
作为自动布线器所理解的总线，是能够在 x 和 y 方向上放置并且只带有少许偏差的直线。

`It has nothing in common with buses in the meaning of electronics, for example, address buses or the like.`
该总线和原理图意义上的总线没有任何共同之处，例如，地址总线等等。
和原理图中的类似地址总线不同，原理图中的总线在电路板图中并不会表现出来。

### 3.2 Routing Pass 布线过程
The actual实际 routing pass is then started, using parameters which make a 100% routing as likely as possible. 
总布线完成后开始实际的布线过程，尽可能的使用那些能达到 100%布线通过率的参数。

A large number of vias are deliberately故意 allowed to avoid paths路径 becoming形成 blocked阻塞.
特意使用大量的过孔来避免路径形成阻塞。


### 3.3 TopRouter
>Select a routing variant with upstream TopRouter, and the traces will be laid out with another routing algorithm算法, which tends to use less vias. 

选择一个布线变体
线路使用另外一种布线算法，
倾向于使用更少的过孔。
>Finally routing and optimization follows in order to trim all the traces to comply with the design rules.

在 TopRouter 之后的最终布线和优化是为了修剪所有线路以遵守设计规则。
![Alt text](0x04_Autorouter(自动布线器).assets/.1462977362373.png)

### 3.4 Optimization 优化
After the main routing pass, any number of optimization passes can be made.
在主要的布线工作完成后，可以进行数个优化 passes

The parameters are then set to remove superfluous多余的 vias and to smooth平滑 the track paths路径. 
随后设置参数以删除多余的过孔和平滑线路的路径。

In the optimization passes tracks are removed and rerouted one at a time. 
在优化过程中，每条线路的删除和重新布线会依次进行。

This can, however, lead to a higher degree度 of routing, since it is possible for new paths to be freed by the changed path of this track.
但这可能导致较高的布线难度，因为这条线路的改变可能造成新的路径断开。
-
The number of optimization passes must be specified before starting the Autorouter. 
在启动自动布线之前，必须对优化过程的数量进行指定。

It is not possible to optimize at a later stage. 
不能在后期再进行优化

Once the routing job has been completed all the tracks are considered考虑 to have been prerouted, and may no longer be changed.
一旦布线工作完成，所有的线路都会被认为是预布线，将不能再更改。
-
Any of the steps mentioned提到 above上述 may be separately 单独的 activated or deactivated.
以上提到的 3 个步骤可以单独激活或取消。


## 4. What Has to be Defined Before Autorouting

### 4.1 Design Rules  设计规则
>The Design Rules need to be specified指定 in accordance根据 with the complexity复杂性 of the board and of the manufacturing制造 facilities available. 

设计规则需要按照电路板的复杂性和制造设备的可用条件来定义。

自动布线器在自动布线时必须遵循设计规则对信号网路的约束和设置，因此在自动布线之前确保设计规则满足自己的需求是必不可少的。

设计规则对PCB 设计中所有元件和信号网络的电气属性进行约束，并对其参数进行设置，这些属性和参数依然对自动布线产生作用， 比如相同或者不同网络的最小间距、最小布线宽度以及过孔直径等设置。


### 4.2 Net Classes 网络族
网路簇的设置优先级高于设计规则的设置，如果在电路设计中对特殊信号网络有特殊的布线间距、宽度、过孔直径等要求，建议对该特殊信号网络进行网路簇设置。
如果设计中定义了网路簇设置，自动布线器在布线的过程中仍然会遵循网路簇所定义的过孔的最小间距、线宽和过孔内径，因为优先级较高。

>If you have not already defined various各个 net classes in the schematic diagram图表 you now have the opportunity机会, before running the Autorouter, of specifying指定 whether particular 特定 signals are to be laid using special特殊 track widths, particular clearances are to be observed遵守, or whether certain某一 drill diameters are to be used for vias for particular signals. 

如果您还没有在原理图图表中定义各种网络簇，在运行自动布线器前您还有机会，
指明特殊信号是否使用特别的线宽来放置，
特殊间距需要被遵守，
或者对特殊信号所用的过孔是否采用某些钻孔直径。

Please consult the help pages (CLASS command) or the section on Specifying Net Classes on page 123 for information about the definition of net classes.
请参考帮助页面（CLASS 命令）或 在用户手册 110 页的定义网络簇 Net Classes（即网络分类）章节关于网络簇定义的信息。当然我已将其归纳为笔记

### 4.3 Track Width 线宽
>If no special net classes are defined, the values from the Design Rules apply.

如果没有特殊网络族被定义，那么会使用设计规则中的值。
>The value Minimum width in the Sizes tab determines决定 the track width, the values for minimum clearances/distances are taken from the Clearance and Distance tabs. 

在 Size 标签中的 Minimum width 值决定了线宽 ，最小间隙 /距离值取自于 Clearance 和 Distance 标签中的值。
>The diameter of vias is defined by the values in the Restring tab.
>过孔直径由 Restring 标签中的值定义。

`Did you set values in the Design Rules and for net classes? In this case the Autorouter follows the higher value.`
您在设计规则里设置了网络簇的值吗？如果已经设置，则自动布线器将依照这些更高的值来进行布线。

### 4.4 Grid
The Design Rules determine the routing and placement grid. 
设计规则决定布线栅格和布局栅格。
The minimum routing grid is 0.02 mm, which is about 0.8 mil.
最小布线栅格是 0.02 mm，大约 0.8 mil

#### 4.4.1 Placement Grid 布局栅格
应该是指在放置元件时只用的栅格。

>Although the Autorouter does permit允许 any placement grid, it is not a good idea to place the components on a grid that is too fine. 

尽管自动布线器允许任何布局栅格，但并不推荐将元件放在过于细小的栅格上。(避免增加自动布线时间和降低布线通过率)

Two good rules are:
- The placement grid should not be finer than the routing grid. 布局栅格不能小于布线栅格。
- If the placement grid is larger than the routing grid, it should be set to an integral multiple of the routing grid.如果布局栅格比布线栅格大，则它应当设置为布线栅格的整数倍。如果布线栅格为5mil，则布局栅格设置为10mil 或者15 mil 较为妥当。

>These rules make sense意义 if, for example, you consider认为 that it might be possible, within the Design Rules, to route two tracks between two pins of a component, but that an inappropriate不恰当 relationship关系 between the two grids could prevent阻止 this (see diagram).

例如，您认为在设计规则下可以在一个元件的两个引脚间布两条线，但在两个栅格间存在不适当关系的情况下该布线过程会被禁止（见图表）。这时这些规则对设计很有意义。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463448872373.png)

#### 4.4.2 Routing Grid 布线栅格

>Please note that the Autorouter grid has to be set in the AUTO command's Autorouter Main Setup Window. 

请注意自动布线器栅格必须在 AUTO 命令的自动布线器设置窗口中进行设置。
>This is not the same as the currently used grid in the Layout Editor window that you have selected with the GRID command.

这和您在 PCB 编辑器窗口中当前使用到的栅格是不同的，当前使用栅格是通过 GRID 命令来选择的。
>Bear in mind记住 that for the routing grid the time demand需求 increases增加 exponentially指数方式 with the resolution分辨率. 

请记住对于布线栅格来说，对时间的需求随着其分辨率的增大而按指数级增加。
>Therefore select as large a grid as possible.

因此尽可能选择大的栅格。
>The main question for most boards is how many tracks are to be placed between the pins of an IC. 

对大多数电路板来说，主要的问题是在一个 IC 的引脚之间有多少线路要放置。
>To answer this question, the selected Design Rules (i.e. the minimum spacing between tracks and pads or other tracks) must of course also be considered.

要回答这个问题，设计规则的选择（例如，在线路与焊盘或线路与线路之间的最小间隔）当然也需要考虑到。

>The result is: 实际效果：

`The two grids must be selected so that component's pads are located位于 on the routing grid.这两种栅格必须选择，以使元件的焊盘定位在布线栅格上。`

>There are of course exceptions例外, such as with SMDs to which the opposite相反 may apply应用, namely that a position outside of the routing grid leads to the best results. 

当然也有例外， 比如不使用布线栅格的 SMD，即布线栅格之外的位置上才能够得到最好的结果。
>In any event the choice of grid should be carefully considered in the light of参照 the Design Rules and the pad spacing.

在任何情况下，栅格的选择都应该参照设计规则和焊盘间距来仔细考虑。
-
![Alt text](0x04_Autorouter(自动布线器).assets/.1463448872373.png)
>The example above may clarify the situation:
>上面的例子能够阐述这种情况：
>For the component on the left, the pads are placed on the routing grid. 
>左边的元件，其焊盘放置在布线栅格上的。
>Two tracks can be routed between two pads. 
>两个焊盘之间可以放置两条线路。
>The pads of the component in the middle are not on the routing grid, and therefore only one track can be routed between them. 
>中间那个元件的焊盘没有放置在布线栅格上，因此在两个焊盘之间只能布一条线。
>On the right you see the exception from the rule shown for SMD pads, which are placed between the routing grid lines so that one track can be routed between them.
>在右边显示了 SMD 焊盘的例外情况，SMD 焊盘放置在两条布线栅格线之间，这时两个焊盘之间可放置两条线路。

-

>When choosing the grid, please also ensure确保 that each pad covers at least one grid point. 

当选择好栅格后，也请确保每一个焊盘至少覆盖一个栅格点。
>Otherwise it can happen that the Autorouter is unable to route a signal, even though there is enough space to route it.

 另外，尽管有足够的空间来为其布线，也可能发生自动布线器不能为一个信号进行布线的情况。
>In this case the Autorouter issues发出 the message Unreachable不能达到 SMD at x y as it starts. 

在这种情况下，自动布线器在其开始时就会给出 Unreachable SMD at x y 的提示信息。
>The parameters x and y specify the position of the SMD pad.

参数 x 和 y 表示 SMD 焊盘的位置。
-
>The default value for the routing grid is 50 mil. 

布线栅格的默认值是 50mil。
>This value is sufficient足够的 for simple through­hole layouts. 

这个值对简单的通孔布局来说足够了。
>Working with SMD components demands a finer routing grid.

SMD 元件要求较小的布线栅格。
>Usual values are 25, 12.5, 10, or 5 mil.

常用的值是 25、12.5、10 或 5mil。

`Please remember that finer routing grids require需要 significantly more routing memory.请记住较小的布线栅格需要更多的布线内存空间。`

>With the automatic grid selection option, the auto router determines决定 at its own heuristics试探 suitable适用 grid settings for each routing jobs.

使用 automatic grid 选项时，自动布线的栅格设置参数，由其自动试探每个布线作业适合的栅格设置得到。


### 4.5 Memory Requirement 内存需求
>The amount数量 of routing memory required depends决定于 in the first place on the selected routing grid, the area of the board and the number of signal layers in which tracks are routed.

布线内存数量需求首先取决于所选定的布线栅格、电路板面积和走线信号层的数量。
>The static memory requirement (in bytes) for a board can be calculated as follows:
>number of grid points x number of signal layers x 2

电路板需要的静态内存（字节）能够通过下面的公式来计算：
栅格点数 * 信号层数 * 2

-
>Space is also required for dynamic data, in addition增加 to the static memory requirement. 

除了需要静态内存空间外，动态数据也需要存储空间。
>The dynamic data require in a very rough粗略 estimate估算 about 10% up to 100% (in some cases even more!) of the static value. 

粗略估计大约为静态内存的 10%到 100%（在某些时候甚至更多！）。
>This depends heavily on the layout.

这很大程度上取决于 PCB 设计方式。
>Total memory requirement (rough粗略 approximation):
>static memory x (1.1..2,0) [bytes]

总的存储空间需求（粗略近似值）：
静态内存空间  X（1.1···2.0）[字节]
>This much RAM should be free before starting the Autorouter. 

在开始自动布线前应当释放这些 RAM 空间。
>If this is insufficient不足, the Autorouter must store data on the hard disk. 

如果空间仍然不足，则自动布线器需要把数据存储到硬盘上。(也就是启用虚拟存储器)
>This lengthens the routing time enormously, and should be avoided at all costs. 

这将极大地延长布线时间，应该尽可能的避免。
>Short accesses to the hard disk are normal, since the job file on the hard disk is regularly定期 updated.

短时间的访问硬盘是正常现象，因为硬盘上的工作文件需要定时更新。
`Try to choose the coarsest possible routing grid. This saves memory space and routing time!试着选择最宽的布线栅格。这能节省内存空间和布线时间!`

需要说明的是，使用Supply 层设置的电源层( $ name) 不会占用任何自动布线内存，而通过一个或多个多边形敷铜区来创建的电源层与其他任何信号层消耗的布线内存相同。


### 4.6 Layer 电路板层
>If you want to design a double­sided board, then select Top and Bottom as route layers. 
>如果您想设计一块双面电路板，则可以选择顶层和底层作为布线层。
>=
>You should only use the Bottom layer for a single­sided board.
>如果设计单面板，则只使用底层。
>=
>In the case情况 of inner layers, it is helpful to use the layers from the outside to the inside, i.e. first 2 and 15 and so on.
>在有内部层的情况下，以从外部层到内部层的顺序来使用层对设计有益，即从第 2 层开始到第 15 层或者其他层。

-
~~如果内部层重命名为$name，这里 name 表示有效信号名称，则该层会转变成电源层。这种层上不能布线。带有多个信号的电源层能够通过多边形敷铜区来实现。这些层将被视为正普通的信号层。~~
~~针对 Supply 电源层的自动布线考虑:层的名称指定了在该层上的信号(如: $ VCC 表示仅能够传输VCC 信号)。该层以负片的形式显示。自动布线时该层处于非活动状态(在General 标签中设置为N / A) 。布线完成后在PCB 板框周围话 一条非电气隔离线，可以防止电路板的边缘短路。没有其他信号或多边形敷铜区可以绘制。注意: 自动布线器不能在Supply 层上使用盲孔和埋孔，而是使用多边形敷铜区来代替! 自动布线器不能设置微型过孔 Micro vias ! 自动布线器允许设直盲孔，这种盲孔深度小于在层设置中定义的盲孔的最大深度。~~

针对使用Polygons 为电源层的自动布线考虑:
· 在运行自动布线前先定义多边形敷铜区。
· 为多边形敷铜区提供适当的信号名。
· 使用 RATSNEST 命令对多边形敷铜区敷铜。
· 在自动布线器设置中为层选择首选方向和基本花销(cfBase) 
· 为多边形敷铜区分配较高的 cfBase 值，可以让自动布线器更严格的避开这些层。
布线后，检查多边形敷铜区是否仍然和所有信号点连接，有可能多边形敷铜区被划分为孤立的几个部分，这时需要使用RATSNEST 重新敷铜。如果一切正常，则会在编辑器窗口底部的状态栏巾弹出提示信息 Ratsnest : Nothing to do !

-
>In the case of boards that are so complex that it is not certain确定 whether they can be wired on two sides, it is helpful to define them as multilayer boards, and to set very high costs for the inner layers. 

对那些非常复杂的电路板来说，无法保证在两个面上进行布线，这时推荐把它们定义为多层板，并将内部层的花销设置为很大的值。
=
>This will cause the Autorouter to avoid the inner layers and to place as many connections as possible in the outer layers.
>这将使得自动布线器尽量避开内部层而在外部层上放置尽可能多的连接。
>=
>It can, however, make use of an inner layer when necessary必须的.
>但在必要时还是有可能使用某个内部层。
>These settings are made in the Autorouter menu .
>这些设置可以在自动布线器菜单中实现（参考本笔记第 5 节）
>-
>The autorouter shows the message Unreachable不能到达 SMD in layer..., if a layer that contains SMDs is not active. 
>如果一个包含了 SMD 的层处于未激活状态，自动布线器会显示 Unreachable SMD in layer...提示信息。
>=
>Clicking OK starts the autorouter nevertheless任然.
>单击 OK 继续运行自动布线器。
>=
>If you want to change the autorouter setup click Cancel.
>如果您想改变自动布线器设置就单击取消。
>=

### 4.7 Preferred Directions 首选方向
>For each routing job you can specify individually各自 for each signal layer its own preferred direction. 

对于每个布线作业，你可以为每个信号层指定它们各自的首选方向。
>With the new Auto setting the Autorouter will choose different settings for preferred directions on its own.

关于新的 Auto 设置项，自动布线器将为各个层选择不同的首选方向设置。

-
>If you want to set preferred directions manually, the following considerations apply: On the two outside layers the preferred directions are normally set to 90 degrees from each other. 

假如你想手动设置首选方向，有以下注意事项：在两个外部层上，首选方向一般相互形成为 90°。
>For the inner layers it may be useful to choose 45 and 135 degrees to cover diagonal connections. 

对内部层来说，推荐选择45°和 135°的对角线。
>Before setting the preferred direction it is well worth值得 examining研究 the board (based on the airwires) to see if one direction offers提供 advantages优势 for a certain某一 side of the board. 

在设置首选方向前，推荐检查电路板（基于鼠线）是否在采用一个方向时能够为电路板的某一层带来许多优势。
>This is particularly特别 likely to be the case for SMD boards.

特别像是 SMD 板。

`Please also follow the preferred direction when pre-­placing tracks. 
The defaults are vertical for the Top (red) and horizontal for the Bottom (blue) layer.`
在预布线时，也请遵从首选方向。
顶层（红色） 默认的是垂直方向，底层（蓝色） 默认的是水平方向。

>Experience has shown that small boards containing mainly SMD components are best routed without any preferred direction at all (set * in the Autorouter setup). 

经验表明，对主要包含 SMD 元件的小型电路板来说，在没有任何首选方向的情况下能实现最佳的布线（在自动布线器设置中设置为*）。
>The router then reaches达到 a usable可用 result much faster.

这样布线能更快的得到可用的结果。
>Single sided boards should be routed without a preferred direction.

单面板应该在没有设置首选方向的情况下进行布线。

### 4.8 Restricted Areas for the Autorouter 自动布线器限制区域

>If the Autorouter is not supposed to route tracks or place vias within certain某一 areas, you can define restricted areas by using the commands RECT, CIRCLE, and POLYGON in the layers 41, tRestrict, 42, bRestrict, and 43, vRestrict.
>如果想要自动布线器在某个区域内不布线或不放置过孔，您可以通过在 41 层（tRestrict 层）、第 42 层（bRestrict 层）和第 43 层（vRestrict 层）上使用 RECT、CIRCLE 和 POLYGON 命令定义限制区域。
>=
>**tRestrict**: Restricted areas for Wires and Polygons in the Top layer.针对顶层的线和多边形敷铜区的限制区域
>**bRestrict**: Restricted areas for Wires and Polygons in Bottom layer.针对底层的线和多边形敷铜区的限制区域
>**vRestrict**: Restricted areas for Vias.针对过孔的限制区域

>Such restricted areas can already be defined in a Device or Package (around, for instance, the fixing holes for a connector, or for a flat-­mounted平面安装 transistor under which there should not be any tracks).

这样的限制区域也能够在一个元件或封装中定义（例如，一个连接器的安装孔周围，或下方不能存在任何线路的平面安装的三极管）。
-
>Wires drawn in layer 20, Dimension, are boundary lines for the Autorouter.
>在第 20 层（Dimension 层）上绘制的线路，是做为自动布线器的边界线。
>=
>Tracks cannot be laid beyond超过 this boundary范围.
>导线不能超出这个边界。
>=
>Typical application: board boundaries.
>典型应用：电路板的边界。
>=
>An area drawn in layer 20 can also be used as a restricted region区域 for all signals. 
>在第 20 层上绘制的区域，也可以做为所有信号的限制区域。
>=
>It should, however, be noted that this area should be deleted before sending the board for manufacture, since layer 20 is usually output during the generation生成 of manufacturing制造 data.
>但需要注意的是，这个限制区域在电路板制造前需要删掉，因为在生成制造数据时第 20 层通常会一起输出。
>=
>Cutout polygons which are used, for example, in inner layers in order to keep certain某一 areas of signal polygons free of copper, are not recognized by the Autorouter. 
>自动布线器不能识别内部层上用于禁止信号多边形中某个区域敷铜的 Cutout 多边形。
>=
>It may happen that the Autorouter draws wires in such an area.
>因此自动布线器有可能在该区域内绘制线路。


### 4.9 Cost Factors and Other Control Parameters
>All routing parameters are set in the Autorouter Variants dialog. 
>所有布线参数在  Autorouter Variants 对对话框中被设置。
>=
>They can be modified separately分别 for each routing variant.
>它们可以针对每个布线变体，分别进行修改。
>=
>The default values for the cost factors are chosen选择 on the basis of our experience in such a way as to give the best results.
>花销因数的默认值是基于我们的经验设置的，以便实现最好的效果。
>=
>The control parameters such as mnRipupLevel, mnRipupSteps etc. have also been set to yield the best results according to our experience.
>诸如 mnRipupLevel 和 mnRipupSteps 等的控制参数同样是根据我们的经验总结的最佳设置。
>=
>We want to emphasize, that we recommend working with the default values.
>我们强烈推荐您使用默认值。
>=
>If you nevertheless do want to experiment with these parameters, please consider the description of the cost factors in the following section. 
>但如果您想尝试修改这些参数，请参考下面章节中的关于花销因数的描述。
>In the case of many parameters even small alterations can have large effects.
>对这些参数做很小的改动都可能会产生很大的影响。



### 4.10 合理的元件布局
尽管自动布线器并不参与元件布局，但是合理的元件布局可以提升自动布线的布通率，并可减少布线时间，这点和手动布线必须依赖合理的元件布局是一个道理。

## 5. The Autorouter 自动布线器
>When running the Autorouter with the AUTO command, the setup menu appears出现 first. 

当使用 AUTO 命令运行 Autorouter ，最先出现 setup 菜单。

>All the necessary必须 settings are made there.

在那里进行所有必须的设置。

### 5.1. Autorouter Main Setup Dialog
>This is where you specify指定 the layers that may be used for routing and which preferred首选 directions apply. 

在这里你能指定可被用于布线的层，和该层上布线的首选方向。
>Click in the appropriate恰当的 combo box with the mouse, and select the desired需要 value.

使用鼠标点击恰当的组合框，并选择所需的值。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463124402807.png)
*Autorouter main setup: General settings*

#### 1.1 preferred directions 首选方向
`- horizontal` 水平
`| vertical` 垂直
`/ diagonal at 45°` 45°对角线
`\ diagonal at 135°` 135°对角线
`* none`没有首选方向
`N/A Layer not active` N/A 该层未激活
`Auto Automatic setting` auto 自动布线设置

#### 1.2 Effort 
>Setting Effort (Low, Medium or High) determines how many routing variants can be created.

设置 Effort (Low, Medium or High) 决定会创建多少种布线变体。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463130986105.png)

![Alt text](0x04_Autorouter(自动布线器).assets/.1463125227363.png)
*The Autorouter is routing the board with different sets of parameters depending on the Effort setting, if Routing Grid or Preferred Directions are set to Auto.*
如果布线栅格或首选方向被设置为 Auto ，Autorouter 对板卡布线工作不同参数设置取决于 Effort 工作量设置。
*Multiple-core processors are supported. *
多核处理器是被支持的。

#### 1.3 Auto grid selection
![Alt text](0x04_Autorouter(自动布线器).assets/.1463126092879.png)
![Alt text](0x04_Autorouter(自动布线器).assets/.1463126105314.png)
>If the automatic grid selection is on, the auto router chooses its own values.

假如开启自动栅格选择，自动布线器选择它自己的数值
>Turn off this option to choose your own suitable适当的 routing grid. 

关闭该选项，选择你自己适合的布线栅格。
>There is the opportunity机会 to examine the (automatically) selected grid settings and modify them later in the routing variants dialog.

在稍后的布线变体对话框中，还有机会检查(自动的)选择栅格设置和修改他们。

#### 1.4 Variant with TopRouter 
>Variant with TopRouter activates the new TopRouter that calculates the layout with another routing algorithm算法. 

TopRouter 变体，激活新的 TopRouter，使用另一种布线算法计算布局。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463131080783.png)
![Alt text](0x04_Autorouter(自动布线器).assets/.1463131097651.png)
选择该复选框后，会增加相应的布线变体。

>Typically, the computational effort is larger, but usually provides smoother results with fewer vias.

通常，该选项的计算工作量是很大的，但是通常提供较少过孔的平滑结果。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463126778954.png)
激活 Variant with TopRouter 复选框后，Routing Vaniants 中会增加更多的选项。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463126811969.png)
未激活时，只有三个。

#### 1.5 Maximum number of running threads
>The maximum number of running threads can be limited. 

运行的最大线程数可以被限制。
>The EAGLE Autorouter supports支持 the calculation of multiple Autorouter jobs at a time by using multi­core processors. 

EAGLE 自动布线器通过使用多核处理器， 使多个自动布线器的计算工作同时开展。
>The indicated指示 value depends on the number of available processor处理器 cores. 

指示值取决于可用的处理器核心数。
>It may be useful to reduce减少 the number of threads in order not to occupy占用 all processor cores with the EAGLE Autorouter.

该项可用于减少线程数，目的是为了不使 EAGLE 自动布线器占用所有处理器核心

####  1.6 Load... and Save as.... 
>You may use the Load... and Save as.... buttons to load a different parameter参数 set from an Autorouter control file (*.ctl) or to save the current settings for further未来的 projects.

您可 以使 用 Load... 和 Save as... 按 钮去加载 来自 自动 布线 器控 制文 件（*.ctl）中的不同的参数设置或保存当前设置，以便为其他的项目所用。
#### 1.7 Select  选择
![Alt text](0x04_Autorouter(自动布线器).assets/.1463366517980.png)
>Select this by clicking the corresponding相应的 signal lines.

通过点击相应的信号线进行选择。
>Clicking onto the Select button allows certain signals to be selected for autorouting. 

点击 选择 按钮，允许只选择某些信号用于自动布线。
>Select these with a mouse click onto the respective各自的 airwires.

通过在各自的鼠线上点击鼠标，以选择相应的信号线。
>Then click on the traffic-­light icon in the action toolbar in order to open the second part of the Autorouter setup; the routing variants dialog. 

然后在操作工具栏点击交通灯图标为了打开自动布线设置的第二部分， routing variants对话框。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463130330774.png)

>There you can check the configuration of the routing jobs and change some settings before the actual正式的 routing process过程 begins.

在这里，你可以在实际的布线过程开始之前，检查布线作业的配置和选择某些设置。

>It is, alternatively, possible to enter the signal names on the command line.

或者，可以在命令行中输入信号的名称。

>Examples:
>VCC GND ;

例如：VCC GND ;
>The signals VCC and GND will be routed.

信号 VCC 和 GND 将被布线。
>The semicolon分号 at the end of the line starts the Autorouter immediately立即. 

在行尾处的分号，立即启动自动布线程序。(如果行尾有分号，会直接启动routing variants dialog布线变体对话框; 如没有分号则启动 Autorouter Main Setup对话框)
>It is alternatively possible to click on the traffic­-light icon.

或者可以点击交通灯图标。
>If you type in the command line
>! VCC GND ;

假如你在命令行输入 ! VCC GND ;

>all signals except VCC and GND will be routed.

除了 VCC 和 GND 之外的所有信号将被布线。
>You may use wildcards for the signal selection, as well. 

你也可以使用通配符进行信号的选择。
>Allowed is
>`*`which matches any number of any characters.
>`?` which matches exactly one character.
>`[…]`which matches any of the characters between the brackets,for example [a-­f], for all characters from a to f.

允许：
`*` 匹配任意数量的任何字符。
`?`精确匹配一个字符。
`[…]`匹配两个括号间的任何字符，例如[a-f]，从a 到 f 的所有字符。

单击 OK 按钮后，自动布线器将开始为所有还没有布线的信号进行布线 。Cancel 菜单项能终止 AUTO 命令，并且不保存任何修改。

### 5.2. Routing Variants Dialog
>Click Continue... and a number of different routing variants are calculated, the Routing Variants Dialog opens.

点击 continue... 的同时会计算一些不同的布线变体，Routing Variants Dialog布线变体对话框将被打开。
>Here you can modify the parameter set of each variant or delete or add variants in the list. 

在这里你可以修改每个变体的参数设置，或者在列表中删除或添加变体
>Each parameter set corresponds to the known Autorouter parameter set from the previous versions of EAGLE.

该处每个参数设置对应于于之前 EAGLE 版本中已知的 Autorouter 参数设置。
>The calculation of the individual独立的 routing variants (routing jobs) is started from this dialog.

各自独立的布线变体(布线工程)计算从这个对话框开始。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463146214308.png)
*Autorouter: List of Routing Variants*

>Depending取决于 on the settings EAGLE shows a number of routing options for the board. 

对于板卡，会根据 EAGLE 中的设置显示数个布线选项。
>Click the Start button and the Autorouter starts processing the routing variants.

点击启动按钮，自动布线器开始处理布线变体。
>If you would like to check and maybe adjust the individual routing parameters before, click the >> button.

在这之前，如果你想要检查，并且也许调整个别布线参数，点击 >> 按钮。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463146764260.png)
*Autorouter Variants: List and Parameter settings*


>In the advanced高级 options dialog you can review and modify the routing parameters.

在高级选项对话框中，你可以查看并修改布线参数。
>Click Duplicate or Delete, in order to copy or delete the selected variant.

为了拷贝或删除选中的变体，点击 复制 或 删除 按钮。


>The parameters grouped in the sections Layer costs, Cost factors and Maximum can be set individually for each pass (Busses, Route, Optimize 1-­4).

这些参数归类到 Layer costs 、Cost factors 和 Maximum 各部分中，可以独立设置每个 pass  (Busses, Route, Optimize 1-­4)。
>For more information, see the following section.

更多信息，请参考笔记 “How the Cost Factors Influence the Routing Process  花销因数如何影响布线进程”

>You can insert additional额外的 optimization passes by clicking the Add button in the last optimization run.

在最终优化运行中，你可以通过点击添加按钮，以插入额外的优化 passes。
>The Autorouter starts for all the signals that have not yet been laid out by clicking on the OK button.

自动布线器开始为所有信号布线，这些信号是指没有通过点击 ok 按钮放置的信号。
>The Cancel menu button interrupts the AUTO command without storing any changes.

Cancel 菜单按钮会中断 AUTO 命令 不存储任何更改。

>You are not allowed to make any changes to the parameters, if you want to restart an interrupted routing job. 

假如你想重启一个被中断的布线作业，你是不被允许对参数做任何修改的。
>Use the Continue existing job check box to decide whether you want to continue with an existing job, or whether you want to choose new settings for the remaining剩下的 unrouted signals.

使用Continue existing job(继续现存作业复选框) 以决定是否需要继续一个现存作业，或者是否想要选择新的设置用于余下的未布线信号。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463150627128.png)
Autorouter Main Setup: Restarting an interrupted job

>The Autorouter's work can be undone by the UNDO command.

自动布线器的工作可以通过 UNDO 命令撤消。

Active激活复选框指定了这些设置是否执行。
更多的优化过程可以通过 Add 按钮来添加。
End job 结束作业按钮可以结束自动布线工作并加载以前的布线结果。

#### 2.1 General 常规设置
![Alt text](0x04_Autorouter(自动布线器).assets/.1463367762025.png)

1. **首选方向**
参考 “1.1 preferred directions 首选方向”

2. **Routing Gride**
参考 “1.3 Auto grid selection”
定义适合的布线栅格
越小的布线栅格代表越高的布线精密度，但同时花费的
时间也越多，选择合适的栅格可以在达到较高布通率的同时花费较少的时间。

3. **Via Shape** 
选择电镀过孔的形状，可以选择 圆形 round 和八角形 octagon。

#### 2.2 Busses 总线规则

这里需要特别说明的是，该总线规则设置中的总线并不是原理图中的总线，而是在 PCB 中可以用总线的形式布线的信号网络簇。

#### 2.3 Rout 布线规则
针对所有的信号网络均适用，是最重要的一个设置标签。
相较于其他的标签页，该标签页在 Costs 部分多了Avoid 设置项，在Maximum 部分多了RipupLevel、RipupSteps 和RipupTotal 这 3 个设置项。

#### 2.4 Optimize 优化规则
在EAGLE 中，优化总是在布线后进行。
EAGLE 中的优化以次数来计算，可以在界面中设置多个不同参数的优化选项卡， EAGLE 在执行完优化1 后继续执行优化2 ， 直到最后一个优化选项卡执行完毕。
优化是对布线的进一步调整，因此可以在不同的优化设置标签中针对部分参数进行严格设置，而忽略其他参数，这样可以降低优化时间，增加优化能力。
单击选项卡中的Add 按钮，可以添加新的优化选项卡。

### 5.3. How the Cost Factors Influence the Routing Process  花销因数如何影响布线进程

**花销**：是指自动布线器对一个或者一类操作的重视程度，也可以理解为自动布线器在这个操作上花费时间的多少。过低的花销可能使布线的结果达不到用户的要求，而过高的花销可能导致布线时间的无限延长。所以，需要用户根据实际情况，评估出需要重点照顾的地方，在这些地方允许EAGLE 使用高花销布线，而在剩余的地方使用合理的低花销布线。这样做的好处是可以在保证重要信号的同时，不会过分延长布线时间。EAGLE 采用数字来表示花销的多少，较小的数字代表低花销，较大的数字代表高花销。

花销因数的默认值是基于大量经验设置的，以便于实现最好的效果，其他 mnRipupLevel 和 mnRipupSteps 等也是基于经验总结的最佳设置，强烈建议使用默认值进行自动布线! 对这些参数做很小的改动往往会产生很大的影响!

>Values between 0..99 are possible for each cost factor (cfxxx), but the full range is not useful for all parameters. 

每个花销因数(cfxxx)的值可能在0 到 99 之间，但是不是所有参数都可以使用全部的数值范围。
>Sensible合理的 values are therefore因此 given with each parameter.

因此这里给出每个参数合理的值。
>The control parameters (mnxxx) accept values in the range 0..9999.

控制参数(mnxxx) 接受的值在0 到9999 的范围之间。
>Reasonable合理的 figures are also provided under each parameter.

在每个参数下也提供了合理的数字。
>The parameter can be set by the Autorouter Setup Menu. 

参数可以通过 Autorouter Setup Menu 进行设置。
>The settings for Route and the Optimize passes can be configured separately. 

对于布线过程和优化过程的设置，也可以分别进行。
>The menu is split分离 into three sections部分, Layer Costs, Costs, Maximum.

该窗口分成了三个部分：Layer Costs、Costs、Maximum。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463152254464.png)
Autorouter: Parameter for Route

>The following section部分 shows the available parameters and their effects效果

下面的章节展示了可用的参数和它们的作用。
>The names of the parameters are the same as they would be used in an Autorouter control file *.ctl. 

参数的名称与在自动布线器控制文件*.ctl 中使用的名称相同。
>Details about this can be found in Parameters of a Control File beginning with page 216.

详细信息可以在英文用户手册 216 页的控制文件的参数章节中找到。(我会在后面做相关笔记，总结用户手册中的内容)

![Alt text](0x04_Autorouter(自动布线器).assets/.1463217513639.png)


#### 3.1 Layer Costs 布线花销/层花销
![Alt text](0x04_Autorouter(自动布线器).assets/.1463217662950.png)

1. **cfBase.xx: 0..20**

>Base costs for one step on the corresponding layer. 
>Recommendation: outside layers (Top, Bottom) always 0, inside layers greater than 0.

cfBase.xx: 0..20
对应层上任意步骤的基本花销。
推荐：外部层(Top, Bottom) 总是 0，内部层大于 0。

内部层采用比外部层高的花销。


#### 3.2 Costs 花销
![Alt text](0x04_Autorouter(自动布线器).assets/.1463227309979.png)

##### 3.2.1. **cfVia: 0..99** 过孔
控制过孔的使用


>Controls the use of vias. 
>A low value produces产生 many vias but also allows the preferred direction to be followed. 
>A high value tries to avoid避免 vias and thus因此 violates违反 the preferred direction. 
>Recommendation: low value for the routing pass, high value for the optimization.

控制过孔的使用。
较低的值会产生很多过孔，但是同样允许遵循首选方向。
较高的值试图避免过孔，但会因此违反首选方向。
推荐：低值用于布线过程，高值用于优化。

##### 3.2.2. **cfNonPref: 0..10** 未使用首选方向

>Controls following of the preferred direction. 
>A low value allows tracks to be routed against相反 the preferred direction, while a high value forces强制 them into the preferred direction.
>If cfNonPref is set to 99, track sections部分 can only be placed in the preferred direction. 
>Only select this value if you are certain确定 that this behaviour行为 is really wanted.

控制以遵从首选方向。
低值允许布线与首选方向相反，然而高值强制走线方向与首选方向一致。
如果 cfNonPref 设置到99，线路部分只能够顺着首选方向放置。
只有你真的很需要这种行为时，选择此值。

##### 3.2.3. **cfChangeDir: 0..25** 改变方向

>Controls how often the direction is changed. 
>A low value means many bends are allowed within a track. 
>A high value produces virtually几乎 straight直的 tracks.

控制方向改变的频率。
低值意味着在一条走线内允许有多个弯折。
高值产生几乎直线的走线。

##### 3.2.4. **cfOrthStep, cfDiagStep**
Orth正交步数：0°或90°方向上的步数
Diag对角步数：45°或135°方向上的步数

>Implements实现 the rule that the hypotenuse斜边 of a right-­angled直角 triangle三角形 is shorter than the sum of the other two sides. 

执行直角三角形的斜边小于另外两边之和的规则。
>The default values are 2 and 3. 

默认值值是 2 和 3。
>That means that the costs for the route using the two other sides are 2+2, as against相反 3 for the hypotenuse. 

这意味着使用另外两边的布线花销是 2+2，而斜边的布线花销是 3。
>These parameters should be altered改变 with great care!

改变这些参数要特别小心！


##### 3.2.5. **cfExtdStep: 0..30**  以45°背离首选方向的步数

>Controls the avoidance避免 of track sections which run at an angle角度 of 45 degree度 to the preferred direction, and which would divide the board into two sections. 

控制以避免与首选方向成 45°的走线部分的运行，它可以将电路板分成两部分。
> low value means that such sections are allowed while a high value tries to avoid them. 

较低的值意味着允许这种走线部分，而较高的值就会试图避免产生这种线段。
> In combination结合 with the parameter mnExtdStep you can control the length of these tracks. 

与参数 `mnExtdStep` 相结合，你可以控制走线的长度。
> If mnExtdStep = 0, each grid step at 45 degrees to the preferred direction causes costs that are defined in parameter cfExtdStep. 

假如 `mnExtdStep` = 0, 与首选方向成 45 度的每个栅格步 ，会导致在参数 `cfExtdStep` 中定义的花销。
> Choosing for example mnExtdStep = 5 allows a track to run five steps at 45 degrees without any additional额外 costs. 

挑选一个数值，例如 mnExtdStep = 5，会允许一条走线在 45 度的方向走 5 个栅格步，而没有额外的花销。
> Each further step causes costs defined in cfExtdStep.

之后的每一步会导致在 cfExtdStep 中定义的花销。
> In this way, 90 degree bends弯折 can be given 45 degree corners. 

这样，90 度的弯折能够被 45 度转角来实现。
> Settings like cfExtdStep = 99 and mnExtdStep = 0 should avoid tracks with 45 degree angles.

设置如 cfExtdStep = 99 和 mnExtStep = 0 时，将会避免 45°角走线。
> This parameter is only relevant有关 to layers which have a preferred direction.

这个参数仅和带有首选方向的层相关。
> Recommendation: use a lower value for the routing pass, and a higher value for the optimization.

推荐：低值用于布线过程，高值用于优化。

##### 3.2.6. **cfBonusStep, cfMalusStep: 1..3** 
在bonus 区域中的步数、在handicap 缺陷区域中的步数

>Strengthens the differentiation between preferred (bonus) and bad (malus) areas in the layout. 
>With high values, the router differentiates区分 strongly严格 between good and bad areas. 
>When low values are used, the influence影响 of this factor因数 is reduced减少. 
>See also cfPadImpact, cfSmdImpact.

加强布局编辑器中优先的（bonus）和坏的（malus）区域之间的差异。
当设置为较高值，布线器会严格区分好的区域和坏的区域。
当设置为低的值，该花销的影响降低。
另见参数 cfPadImpact, cfSmdImpact。

##### 3.2.7. **cfPadImpact, cfSmdImpact: 0..10**
Pad 焊盘周边区域的影响范围、SMD 焊盘周边区域的影响范围

>Pads and SMDs produce good and bad sections or areas around them in which the Autorouter likes (or does not like) to place tracks. 

在焊盘 Pads 和 SMDs 所产生的好的和坏的部分中，或在围绕它们的区域中，自动布线器会（或不会）在这些区域放置线路。
焊盘Pads 和SMDs 周围所产生的好的和坏的部分或区域， 自动布线器会(或不会)在这些区域放置线路
>The good areas are in the preferred direction (if defined), the bad ones perpendicular to it.

好的区域依照首选方向（如果已经定义），坏的区域的则与首选方向垂直。
>This means that tracks which run in the preferred direction are routed away from the pad/SMD. 

这意味着运行在首选方向上的走线的布线过程是从 pad/SMD 开始的。
>With high values the track will run `as far as possible`尽可能 in the preferred direction, but if the value is low it may leave the preferred direction quite soon. 

较高的值使线路尽可能在首选方向上进行布线，但如果是较低的值，则走线很快会偏离首选方向。
>It may be worth值得 selecting a somewhat有点 higher value for cfSmdImpact for densely 密集的 populated填入 SMD boards.

对密集安装贴片元件的电路板，推荐选择一个较高的 cfSmdImpact 值。

##### 3.2.8. **cfBusImpact: 0..10**偏离理想总线方向

>Controls whether the ideal line is followed for bus connections (see also cfPadImpact). 
>A high value ensures确保 that the direct line between start and end point is followed. >Only important for bus routing.

对是否为总线连接提供了理想的线路进行控制（参考 cfPadImpact）。
较高的值保证起点和终点用直线连接。
这仅针对总线布线。

##### 3.2.9. **cfHugging: 0..5**平行线距

>Controls the hugging of parallel tracks. 
>A high value allows for a strong hugging (tracks are very close to each other), a low value allows for a more generous distribution. 
>Recommendation: higher value for routing, lower value for the optimization.

控制平行线的接近程度。
较高的值允许较小的间距（线之间非常接近），较低的值允许更宽的间距。
推荐：低值用于布线过程，高值用于优化。

##### 3.2.10. **cfAvoid 0..10** 先前 ripup 时使用的区域
 ripup 取消布线命令
EAGLE 在布线时，可能会使用Ripup 功能取消布线。
 在该选项栏设置较高的值可以阻止线路取消。

>During the ripup, areas are avoided from which tracks were removed. 
>A high value means strong avoidance.
>Not relevant to the optimization passes.

在使用 ripup 功能时，需要避免线路取消的区域。
较高的值表示严格避免线路取消。
与优化过程不相关。

##### 3.2.11. **cfPolygon 0..30** 消除多边形
>If a polygon has been processed with the RATSNEST command and therefore is displayed as a filled area before you start the Autorouter, every step within the polygon is associated with this value. 

如果某个多边形敷铜区已经执行了 RATSNEST 命令，那么将在您启动自动布线器前显示为一个填充区域，多边形中执行的每一步都与该值 cfPolygon 相关。
>A low value makes it easier for the Autorouter to route traces inside the polygon area. 

较低的值使自动布线器很容易的在多边形区域内进行布线。
>The probability概率, however然而, that the polygon is broken into several pieces is higher. 

但多边形区域被分割成多个小块的可能性较高。
>A higher value causes the Autorouter to make fewer connections inside the polygon.

较高的值使自动布线器在多边形区域产生较少的连接。
>If a polygon is in outline mode and not processed by RATSNEST before you start the Autorouter, it won't be taken into consideration考虑 at all. cfPolygon does not play a role for such polygons.

如果一个多边形敷铜区处于外框模式并且在您启动自动布线器前没有执行 RATSNEST 命令，那么就不用考虑参数cfPolygon 对这些多边形敷铜区的影响。

#### 3.3 Maximum 最大
最大数量参数默认值
##### 3.3.1. **mnVia 0..30** 
每条连线的过孔数

>Controls the maximum number of vias that can be used in creating a connecting track.

控制能被用来创建连线的过孔的最大数量。

##### 3.3.2. **mnSegments 0..9999**
每条连线的线段数

>Determines the maximum number of wire pieces in one connecting track.

定义在一个连线中线段的最大数量

##### 3.3.3. **mnExtdSteps 0..9999**
与首选方向成45°的方向上的步数

>Specifies the number of steps that are allowed at 45 degrees to the preferred direction without incurring引发 the value of cfExtdStep.
>See also cfExtdStep.

指定与首选方向成 45°的方向上所允许的栅格步数，该步数之内不会激活 cfExtdStep 的值。
请参考 cfExtdStep

>Additionally此外 can be found the parameters mnRipupLevel, mnRipupSteps, and mnRipupTotal. 
>Those are described in the following section.
>另外还有这些参数：mnRipupLevel, mnRipupSteps 和 mnRipupTotal。
>它们将在下面的章节进行描述。

##### 3.3.4. **Number of Ripup/Retry Attempts** 
Ripup/Retry 取消/重试尝试的次数

mnRipupLevel 每条连线的 ripup 深度：设定自动布线器可以删除的已布线线路的最大数量。

mnRipupSteps 每条连线的 ripup 进程：每条无法重新布线并且被删除的线路会启动一个新的 Ripup 进程，该序列的最大数量在参数mnRipupSteps 中进行定义。

mnRipupTotal  同时可用  ripups 数：定义了可以同时被删除的线路数量。

 tracks 指一条线路中的某一段

>Due to the structure构成 of the Autorouter there are some parameters which influence影响 the ripup/retry mechanism机制. 

由于自动布线器的构成中有一些参数会影响 Ripup/Retry 取消/重试机制。
>They are set in such a way that they offer提供 a good compromise妥协 between time demand and routing result. 

它们的设置能够在时间需求和布线效果之间实现平衡：使它们能在实际需求和布线结果之间有一个好的平衡 。
>The user should therefore因此 only carefully change the values for mnRipupLevel, mnRipupSteps and mnRipupTotal when needed.

因此用户在需要改变参数 mnRipupLevel, mnRipupSteps 和 mnRipupTotal 的值时要非常小心。

>As a rule, high parameter values allow for many ripups but result in increased增加 computing times.

较高的参数值允许多次 Ripup，但会增加计算时间。
>To understand the meaning of the parameters you need to know how the router works.

为了理解参数的意义，您需要知道布线器是如何工作的。
>To begin with the tracks are routed one after the other until no other path路径 can be found. 

开始时一条接一条的进行布线，直到找不到还没有布线的线路为止。
>As soon as this situation情况 occurs发生, the router removes up to the maximum number of already routed tracks (this number has been defined with mnRipupLevel) to route the new track. 

当出现这种情况时，自动布线器可以删除已布线的最大数量（这个数量使用参数 mnRipupLevel 来定义）以便放置新的线路。
>If there are eight tracks in the way, for example, it can only route the new track if mnRipupLevel is at least eight.

比如如果在一条路径中有 8 条线路需要布线，那么参数 mnRipupLevel 至少是 8。
>After routing the new track, the router tries to reroute all the tracks which were removed. 

在放置了新的线路后，自动布线器会尝试对所有被删除的线路进行重新布线。
>It may happen that a new ripup sequence must be started to reroute one of these tracks. 

可能发生这种情况：为了对这些线路中的一条进行重新布线而必须执行新的一轮 Ripup 进程。
>The router is then two ripup sequences away from the position at which, because of a track which could not be routed, it started the whole process. 

这时由于某个无法布线的线路，布线器将从该位置开始执行两个 Ripup 进程。
>Each of the removed tracks which cannot be rerouted starts a new ripup sequence. 

每条无法重新布线并且被删除的线路会启动一个新的 Ripup 进程。
>The maximum number of such sequences is defined with the mnRipupSteps parameter.

该序列的最大数量在参数 mnRipupSteps 中定义。
>The parameter mnRipupTotal defines how many tracks can be removed simultaneously. 

参数 mnRipupTotal 定义了多少条线路可以同时被删除。
>This value may be exceeded in certain cases.

在某些情况下可能超出这个值。
>If one of these values is exceeded, the router interrupts the ripup process and re-­establishes重新建立 the status which was valid有效的 at the first track which could not be routed. 

如果超出这些值中的某一个，布线器将中断 Ripup 过程，并在无法布线的第一条线路位置重新建立有效状态。
>This track is considered as unroutable, and the router continues with the next track.
>这条线路将被标记为无法布线，布线器将继续放置下一条线路。

---
 Follow-me 标签与自动布线过程本身并不相关。

## 6. Routing Multi-Layer Boards with Polygons
具有多边形敷铜区的多层板布线
>It is possible to create supply layers with polygons that contain包含 more than one supply voltage, and individual wires as well. 

通过多个不同电源信号的多边形和多条单独的线路可以创建电源层。

可以通过多边形创建电源层，该层包含多个电源电压，以及一些线路。
>Please note the instructions on page 172, Ground Planes and Supply Layers with Several Signals.

请注意中文用户手册第 145 页，英文手册 172 页中关于带有多个信号的接地层和电源层的内容。
- Define the polygons before running the Autorouter.
在运行自动布线器之前定义多边形。
- Give the appropriate signal names to the polygons.
为多边形分配一个适当的信号名称。
- Use the RATSNEST command to let EAGLE calculate the polygon.
使用 RATSNEST 命令来让 EAGLE 计算多边形。
- Select the preferred directions and base costs (cfBase) for the layer in the Autorouter setup. A higher value of cfBase for the polygon layer causes the Autorouter to avoid these layers more strongly.
在自动布线器设置窗口中为该层选择首选布线方向和基本花销（cfBasse）。数值较大的 cfBase 更能够确保自动布线器绕开这种信号层。
- After routing, check that the polygon still connects all the signal points. It is possible that the polygon was divided分割 as a signal was laid. RATSNEST recomputes polygons, and issues the message Ratsnest: Nothing to do!, if everything is in order.
完成布线后，请检查多边形是否连接到所有信号上。该多边形有可能在创建某条信号连接时被分割。这时 RATSNET 命令能够重新对多边形进行计算并显示计算结果。Ratsnest：如果没有需要处理的地方，软件会提示“未进行任何操作！”

`The Autorouter cannot set Micro vias!
自动布线器不能放置微型过孔！
The Autorouter is allowed to set Blind vias that are shorter 
than the maximum depth defined in the Layer Setup.
自动布线器可以放置盲孔，并且盲孔的最大深度小于 DRC 窗口中 Layers 标签内设置的最大深度。`

## 7. Backup and Interruption of Routing
>As, with complex layouts, the routing process may take several hours, a backup is carried out at intervals间隔 (approx大约. every 10 minutes). 

对复杂的 PCB 布局来说，布线过程可能需要几个小时，因此间隔一段时间（大约每 10 分钟）就进行一次备份。
>Depending on the number of routing jobs, there is a corresponding number of job files. 

取决于布线作业的数量，这里有一个相应作业量的文件。
>The file name_xx.job always contains the last status of the jobs, where xx stands代表 for the number of the variant, always beginning with 00.

文件 name_xx.job 通常包含最近的工作状态，xx 代表数字变体，通常从 00 开始。
>If the job is interrupted for any reason (power failure etc.) the computer time invested花费 so far is not lost, since you can recall the status saved in name.job.

如果工作因为一些原因（停电等）而中断，您可以重新调出保存在后缀为 .job 的文件中的状态，这样就不会浪费所投入的时间。

>Load your board file in the Layout Editor, and then enter: AUTO;

在布局编辑器中加载你的电路板，然后输入：AUTO
>Answer the prompt提示 as to whether the Autorouter should recall (Continue existing job?) with Yes. 

在询问是否继续运行自动布线的提示窗口上单击Yes（Continue existing job?）。
>The Autorouter will then continue from the position at which the job was last saved (a maximum of 10 minutes may be lost).

自动布线器将从上次工作最后保存的位置开始继续运行（最多可能丢失 10 分钟内的修改内容）。
>If the autorouting is interrupted via the stop icon, the files name_xx.job remain保持 intact完好 and can be recalled. 

如果通过单击 Stop 图标中断了自动布线，name_xx.job 文件也将保持原样，并能够继续调用。
>This may be useful when you have started a complex job on a slow computer and want to continue with it on a fast computer as soon as one is available.

当您在一台运行缓慢的计算机上进行复杂的工作，但希望在另一台更快的计算机上继续运行，这一功能则可能是非常有用的。
>Please note that changing the parameters before recalling will not influence the job, since it will have been saved together with the parameters which were valid有效的 at the time of the initial最初 Autorouter start.

请注意在重新调用前改变参数将不会对工作造成影响，因为工作参数已经进行了保存并且这些参数在最初的自动布线器开始时就已经生效了。
>When the Autorouter has finished, the routed board is saved as `name.b$$`.

当自动布线器完成布线，已布线的电路板以名称 name.b$$保存。
>You can rename it to name.brd and use it, for instance, if a power failure occurred after the autorouting run and you could not save the board file. 

您可以将它重命名为 name.brd 并可以使用它。例如，如果在完成自动布线后发生停电，并且您还没有保存这个电路板文件。
>This file is deleted automatically after the board has been saved.

那么这个电路板保存后将自动删除这个文件。

## 8. Information for the User
### 8.1 Status Display 状态显示
>During the routing, you are have the option to select different Variants from the list and observe观察 the routing progress进展.

在布线期间，你可以从列表中选择不同的布线变体，并观察布线的进展情况。

>The Autorouter displays information on the actual routing result of the selected Routing variant in the status bar.

自动布线器在状态栏中显示所选布线变体的实际布线结果

![Alt text](0x04_Autorouter(自动布线器).assets/.1463530714121.png)
Autorouter: Routing progress in the variants 变体中的布线进程。

>The displayed values have the following meaning:
>显示的值有如下含义
>![Alt text](0x04_Autorouter(自动布线器).assets/.1463531334825.png)

#### 1. Route:布线百分比2
Result in % (hitherto maximum, best data)。
结果用百分比显示。(该值越大，效果越好)

#### 2. Vias:过孔
Number of vias in the layout.
PCB 布局中使用的过孔数量。

#### 3. Conn:连线
Number of Connections *total/found/not routable*.

连线数量，包括全部连线数/已找到的连线数/无法布线的连线数。
Connections here means 2­ point connections.
连线在这里是指 2 点间的连接。

#### 4. Ripup:取消
Number of *Ripups/current RipupLevel/cur. RipupTotal*
Ripup 的次数/当前 Ripup 等级/当前所有 Ripup 等级。

- **Number of ripups**:
This indicates表明 the number of connections that have already been routed during the foregoing之前 routing procedure that have been (can be) removed in order to be able to route new signals.
表示在之前布线过程中产生的布线连接数量，这些连接已经或可以删除以便为新的信号布线。

- **Current RipupLevel**:
This indicates表明 the number of connections that have been removed or converted转换 in airwires in order to lay the track for the current signal.
表示已经删除的或者转变为鼠线的连线数量，以便为当前信号放置线路。

- **Current RipupTotal**:
After a signal's routes have been ripped up it can be broken down into a large number of two­-point connections. 
某个信号的线路被删除后，可能分解成大量的两点连接。
These connections are then routed again. 
些连接会再次进行布线。
This variable indicates the number of such two­-point connections still to be routed.
该变量表示等待布线的两点连接的数量。

#### 5. Signals:信号
Signals found/handled/prepared, if so followed by: (routing_time signalname)
找到的信号/已处理的信号/已准备好的信号，如果有那么后接(布线时间 信号名)
In case the Autorouter needs more than about 5 seconds to lay­out a connection, EAGLE shows in parenthesis括号 the routing time and the name of the currently processed signal.
在自动布线器放置一个连线需要超过 5 秒的情况时，EAGLE 在括号里显示出布线时间和当前处理的信号的名称。

### 8.2 Log file 日志文件
For each routing pass the Autorouter generates a file called name.pro, containing useful information. Example:
自动布线器为每一个布线过程生成一个 name.pro 的文件，它包括了一些有用的信息。例如：


EAGLE AutoRouter Statistics:
Job : d:/eagle4/test-design/democpu.brd
Start at : 15.43.18 (24.07.2000)
End at : 16.17.08 (24.07.2000)
Elapsed time : 00.33.48
Signals : 84 RoutingGrid: 10 mil Layers: 4
Connections : 238 predefined: 0 ( 0 Vias )
Router memory : 1121760
Passname: Busses Route Optimize1 Optimize2 Optimize3 Optimize4
Time per pass: 00.00.21 00.08.44 00.06.32 00.06.15 00.06.01 00.05.55
Number of Ripups: 0 32 0 0 0 0
max. Level: 0 1 0 0 0 0
max. Total: 0 31 0 0 0 0
Routed: 16 238 238 238 238 238
Vias: 0 338 178 140 134 128
Resolution: 6.7 % 100.0 % 100.0 % 100.0 % 100.0 % 100.0 %
Final: 100.0 % finished

## 9. Evaluate the Results 评估结果
>If all routing variants are 'completed', you can select one of them and end up with a job to complete the routing process过程. 
>The selected variant is then saved as a board file.

假如所有布线变体都已 “完成”，你可以选择它们中的一个，并作为最终作业以完成布线进程。
这个被选中的变体随后被保存为电路板文件。
>If you want to examine检查 the individual routing results in more detail, select one of the variants in the list and then click Evaluate.
>You are now directly in the Layout Editor and can examine and even edit this variant.

如果你想检查个别布线结果的更多细节，在列表中选择一个变体，然后点击 Evaluate。
现在你可以在布局编辑器中直接编辑该变体，并可详细检查，甚至可以编辑变体。
>In the status bar of the Layout Editor there is displayed the Autorouter icon, indicating表示 that the routing process for the current board is not yet completed.
>By clicking this icon, you obtain the following options:
>Click Evaluate and you will return to Autorouter Variants dialog for evaluating further routing results.

在布局编辑器的状态栏会显示 Autorouter 图标，表示当前板卡的布线过程尚未完成。
通过点击该图标，你获得如下选项：
点击 Evaluate 你将返回 Autorouter Variants 对话框以评价更多的布线结果。
>Click End Job and the current variant will be saved including all changes you have made while evaluating this board. 
>All the other routing variants and their results will be discarded丢弃.

点击 End Job 按钮，当前变体将被保存，其中包括你在评估该板卡是所作出的改变。
所有其余的布线变体和他们的结果将被丢弃。
![Alt text](0x04_Autorouter(自动布线器).assets/.1463534655701.png)
 Autorouter: Evaluating the routing results

## 10. Parameters of a Control File 控制文件参数
We see here how the individual单个 parameters in an Autorouter control file (name.ctl) are used.
以下解释了自动布线器控制文件（name.ctl）中每个参数的含义及应用。

```
Parameter参数   Default默认值  Meaning含义 
RoutingGrid= 50Mil Grid used by the Autorouter for tracks and via-holes Cost factors for...自动布线器用于放置线路和过孔的栅格花销参数
cfVia = 8 Vias 过孔
cfNonPref = 5 Not using preferred direction 未使用首选方向
cfChangeDir = 2 Changing direction 改变方向
cfOrthStep = 2 0 or 90 deg. Step 0 或 90°方向上的步数
cfDiagStep = 3 45 or 135 deg. Step 45 或 135°方向上的步数
cfExtdStep = 30 Deviation 45 deg. against preferred direction 以 45°背离首选方向
cfBonusStep = 1 Step in bonus area 在 bonus 区域中的步数
cfMalusStep = 1 Step in handicap area 在 handicap 区域中的步数
cfPadImpact = 4 Pad influence on surrounding area Pad 焊盘周边区域的影响范围
cfSmdImpact = 4 SMD influence on surrounding area SMD 焊盘周边区域的影响范围
cfBusImpact = 4 Leaving ideal bus direction 偏离理想总线方向
cfHugging = 3 Wire hugging 平行线距
cfAvoid = 4 Previously used areas during ripup 先前 ripup 时使用的区域
cfPolygon = 10 Avoiding polygons 消除多边形
cfBase.1 = 0 Basic costs for a step in the given layer 在特定层中每一步产生的花销
cfBase.2 = 1
...
cfBase.15 = 1
cfBase.16 = 0

**Maximum number of...**最大数量
mnVias = 20 Vias per connection 每条连线的过孔数
mnSegments = 9999 Wire segments per connection 每条连线的线段数
mnExtdSteps = 9999 Steps 45 deg. against preferred direction 与首选方向成 45°的方向上的步数
mnRipupLevel = 100 Ripups per connection 每条连线的 ripup 次数
mnRipupSteps = 300 Ripup sequences per connection 每条连线的 Ripup 进程
mnRipupTotal = 200 Ripups at the same time 同时可用 Ripups 数

**Track parameters for...** 线路参数
tpViaShape = Round Via shape (round or octagon)过孔外形（圆形或八角形）
PrefDir.1 = |
PrefDir.2 = 0 
PrefDir.15 = 0  
PrefDir.16 = -  

Preferred direction in the given layer Symbols: 0 - /  \ * 
0 : Layer not used for routing 该层不进行布线
* : No preferred direction 没有首选方向
- : X is preferred direction X 轴为首选方向
| : Y is preferred direction Y 轴为首选方向
/ : 45 deg. is preferred direction 45°方向为首选方向
\ : 135 deg. is preferred direction 135°方向为首选方向
```

## 11. Practical Hints
>This section presents展现 you with some tips that have, over a period of time, been found useful when working with the Autorouter.

本章节为您介绍一些小技巧，这些技巧经过了一段时间的验证，能够为自动布线器的使用提供帮助。
>Look on these examples as signposts指导 suggesting提示 ways in which a board can be routed. 
>None of these suggestions建议 guarantee保证 success.

这些范例演示了电路板布线的方式，但并不保证每一种方式都能成功。

### 1. General 概要
>The layer costs (cfLayer) should increase增加 from the outer to the inner layers or be the same for all layers. 
>It is unfavourable不推荐 to use lower values in the inner layers than in the outer layers. 
>This could increase the needed routing memory enormously巨大.

从外部层到内部层的层花销（cfLayer）会逐渐增加，或者所有层的层花销都一样。
不推荐使用内部层中花销较低的层来替代外部层中花销较高的层。
否则可能增加布线存储空间的需求。

`The Autorouter can't layout wires as arcs!
The Autorouter can't set micro vias!`
自动布线器不能放置圆弧线！
自动布线器不能放置微型过孔！

### 2. Single-Sided Boards 单面板
>There are two procedures, depending依据 on the kind of layout:

根据 PCB 布局类型分为两种情况：
>In the simplest case, only layer 16, Bottom, is active. 
>No preferred direction is defined. 
>Select a suitable grid and run the Autorouter.


在最简单的情况下，只有第 16 层即底层处于活动状态。
无需定义首选方向。
只需要选择合适的栅格，然后运行自动布线器。
>If the layout is rather相当 more complex, it may be possible to achieve获得 a usable result with special parameter settings. 
>Please take a look at the project named singlesided, which can be found in the eagle/projects/examples directory. 
>This example project comes with various control files (*.ctl), which are optimized for singlesided routing.

如果 PCB 设计比较复杂，就可能要用到特殊的参数设置来实现可用的结果。
请查看 EAGLE/projects/examples 目录下名称为 singlesided 的项目。
该项目范例带有各种控制文件（*.ctl），这些文件都针对单面板布线进行了优化。
>The Autorouter may use the Top layer as well. 
>The tracks laid there will be realized实现 as wire bridges on the board. 
>In layer 41, tRestrict, you can define restricted areas around the components and in regions区域 where wire bridges are not allowed.

自动布线器也可以使用顶层。
该层上的线路将作为电路板上的桥接线。
在第41 层（tRestrict 层）上，您可以在元件周围和不允许放置桥接线的范围中定义限制区域。
>Feel free to experiment尝试 with the parameter settings for your layout.

请尽量在您的 PCB 设计中尝试各种参数设置。

### 3. SMD Boards With Supply Layers 含有电源层的 SMD 电路板
>The following procedure程序 has been found effective:

下面方法已证实有效：
>The supply signals are routed first. 
>In general, a short track is wanted from a SMD component to a via that connects to the inner layer.

电源网络会首先进行布线。
通常从 SMD 元件到连接内部层的过孔需要较短的线路。
>Before altering改变 the parameters, save the current (default) values in an Autorouter control file (CTL file). 
>Click on the button Save as.. in the General tab of the Autorouter setup window and input any name, for example, standard.ctl.


在改变参数前，请将当前（默认）值保存在自动布线器控制文件（CTL 文件）中。
在自动布线器设置窗口中的 General 标签下单击 Save as..按钮，并输入任意名称，例如：standard.ctl。

>Now switch off the bus router and all the optimization passes in the Autorouter setup. 
>Only the routing remains active. 
>Alter改变 the following cost factors:
>cfVia = 0 Vias are welcome
>mnVia = 1 Max. one via per connection
>cfBase.1/16 = 30..99 Fewer tracks in Top/Bottom
>mnSegments = 2..8 Short tracks


现在关掉自动布线器设置中的总线布线和所有的优化过程。
只将布线功能设置为活动状态。
cfVia = 0 允许过孔
mnVia = 1 每条连线最多一个过孔
cfBase.1/16 = 30..99 在顶层/底层上放置较少的线路
mnSegments = 2..8 较短线路

>Start the Autorouter, using the Select button, and choose the signals to be routed. 
>After the routing pass it is possible, if appropriate适当, to optimize the result manually.

启动自动布线器并单击 Select 按钮，然后选择需要布线的信号。
布线完成后，在适当的情况下可以对结果进行手工优化。

>The rest of其余 the connections are routed after this. 
>Use AUTO to open the Autorouter setup menu, and load the previous stored control parameters with the Load.. button (standard.ctl). 
>Adjust the values to any special wishes you may have, and start the Autorouter.

剩下的连接都要在完成该步骤后进行布线。
使用 AUTO 命令来打开自动布线器设置菜单，并单击 Load.. 按钮来加载以前保存的控制参数文件（standard.ctl）。
然后根据您的要求调整参数值，并启动自动布线。

### 4. What can be done if not all signals are routed?如果并非所有的网络都进行了布线，那还需要做什么？
If this happens, check your settings.
如果发生这种情况，请检查您的设置：

- Has a sufficiently足够 fine routing grid been selected?
是否选择了足够细的布线栅格？
- Have the track widths got appropriate适当 dimensions尺寸?
线宽尺寸是否合适？
- Can the vias have smaller diameters?
过孔直径能否能更小些？
- Have the minimum clearances been optimally chosen?
是否选择了最佳的最小间距？

If it is either impossible不可能 or unreasonable不合理 to optimize these values any further, an attempt尝试 to achieve实现 a higher level of routing may be made by increasing增大 the ripup删除 level. 

如果无法对这些值进行进一步的合理优化，则需要通过提高 Ripup 等级来实现更高等级的布线。


Observe查看 the notes in the section on the Number of Ripup/Retry Attempts on page 211.

请参考 177zn/211en 页上的 Ripup/Retry 取消/重试的次数章节中描述。或直接查看本笔记，已对这两处进行总结。

## 12. The Follow-me Router 跟随布线器

严格地说，Follow-me 跟随布线并不属于自动布线范围。但是， Follow-me 布线却与自动布线使用相同的规则，也就是在进行Follow-me 布线时，元件对布线的约束与自动布线时
类似。
要准确的设置Follow-me 布线的规则，就必须要了解Follow-me 布线的功能。
Follow-me 是 EAGLE 的半自动布线功能，能够对选定的信号网络进行半自动布线。该布线器根据用户鼠标指针悬停的位置，寻找合适的路径进行布线，线路以信号连线的起点为起
始点，以用户鼠标指针的位置为终点。Follow-me 这个名字可以很形象地表示这一功能。

在 Follow-me 布线模式下，需要设定开始布线的层，该层被布线器选定为优先布线层，但是当首选层元法完成布线时， Follow-me 布线器会向动添加过孔，换到另一层继续布线。要使用Follow-me 布线功能，先要通过 ROUTE 命令进入手动布线模式。


>To simplify the routing of airwires on the board, the ROUTE command offers two follow-­me operating操作 modes that can route a selected signal automatically. 
>The position of the mouse cursor in the layout determines决定 the trace of the connection. 

为了简化电路板上的鼠线的布线，ROUTE 命令提供了两种 follow-me 操作模式，这些模式能自动的对选中的信号进行布线。
光标停留在电路图中的位置决定了连线的轨迹。
>For this function your license must provide the Autorouter module.

要实现该功能，需要您的软件许可能够提供自动布线器。

### 1. Partial and Full Mode

>To start the Follow­-me router, activate激活 the ROUTE command and select the wire bend弯折 mode 8 or 9 from the parameter toolbar.

要启动 Follow-me 布线，请使用 ROUTE 命令并在参数栏中选择线的弯折模式 8或者 9。（弯折模式从 0 开始）
![Alt text](0x04_Autorouter(自动布线器).assets/.1463550599261.png)
Parameter toolbar of the ROUTE command

>After clicking onto an airwire, EAGLE calculates an appropriate适当 trace and displays the connection. 
>Moveing the mouse cursor will change the current trace. 
>Trace processing处理 depends依赖 on the complexity of the layout and may last some moments.
>It is recommended推荐 not to move the mouse cursor until the connection is displayed.

然后单击一条鼠线，EAGLE 会计算出合适的轨迹和显示出连线。
移动光标将改变当前轨迹。
轨迹的处理速度取决于 PCB 的复杂度，因而有可能需要一些时间。
建议在连线显示出来之前不要移动光标。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463551293641.png)

>If you select wire bend mode 8 , the so­-called partial mode, EAGLE calculates the trace of the selected signal, beginning with the mouse cursor position to the nearer end of the airwire, and display it. 
>Fix the result with a mouse click. 
>The remaining余下 part of the airwire will be calculated dynamically.
>This means, that the airwire may point to another object that belongs属于 to the signal, depending依赖 on the current mouse cursor position.

如果您选择线路弯折模式 8 ，即局部模式，EAGLE 会计算所选信号的轨迹，该轨迹从鼠标光标的位置开始到最近的鼠线端点，并会显示出该轨迹。
通过点击鼠标左键可以确认结果。
鼠线的剩下部分将进行动态的计算。
也就是说，根据当前光标的位置，该鼠线可能指向属于这个信号的另一个对象。

![Alt text](0x04_Autorouter(自动布线器).assets/.1463552020123.png)

>With wire bend mode 9 , the full mode, the Follow-­me router calculates the trace in both directions方向 simultaneously同时. 
>A complete connection will be established建立. 
>As soon as you are clicking onto an airwire, EAGLE begins to calculate the trace of the connection from the nearer end of the airwire to the current mouse position. 
>It is not mandatory强制的 that the farer end of the airwire points always to its original原始 position. 
>Depending on the mouse cursor position this end point may direct引导 you to another (nearer) location.

当使用线路弯折模式 9 ，即完全模式时，Follow-me 布线器在两个方向上同时计算线路轨迹。
一条完整的连接将被建立。
一旦您单击某条鼠线时，EAGLE 就从最近的鼠线端点开始到当前光标位置来计算连线的轨迹。
鼠线的远端端点的位置并不一定总是处于其原始位置。
根据光标的位置不同，该端点有可能指向另一个位置。

>If it is not possible to draw a connection from the current mouse cursor position, the cursor turns into a small prohibition禁止 sign. 
>Move the mouse and try to find a possible way for the connection. 
>Maybe it is sufficient足以 to change the layer at the current position. 
>It could also be advice able to adjust调整 the Design Rules. 
>Please keep in mind that restricted areas in the layers t/bRestrict or wires in the Dimension layer can hinder阻碍 EAGLE to establish建立 a connection.

如果不能从当前光标位置来绘制一条连接，光标会变成一个小的禁止符号。
这时请移动光标并尝试找可以连线的位置。
在需要时可能要在鼠标当前位置上改变使用的层。
也可能会建议调整设计轨迹。(修改设计规则也是一种可行的方法)
请记住在 t/bRestrict 层中的限制区域或者在20 Dimension 层中的线路有可能对 EAGLE 建立连线造成阻碍。

### 2. Configuration 配置
>The Follow-­me router respects遵从 Design Rules settings:
>Values for Clearance, Distance, and Size will be taken in consideration考虑, as well as particular特定 values for net classes, if defined. 
>Please be sure that the Layer setup in the Layers tab is properly正确的 set.

Follow-me 布线遵从设计规则的设置：
Clearance、Distance 和 Size 的值都需要考虑，另外，如果已经定义的情况下，也需要考虑特定的网络簇的值。
请确保在 Layer 标签中对层设置进行正确的配置。
>The current grid setting in the Layout editor serves as routing grid. 
>Use the GRID command in order to change it. 
>If there is already a signal assigned指定 to mouse cursor, drop it, and select it again. 
>Otherwise the grid change does not affect影响 the connection

在 PCB 编辑器中的当前栅格设置被作为布线栅格。
可使用 GRID 命令来对其进行修改。
如果鼠标已经选中了一个信号，请取消选中，并再一次选择改信号。
否则，栅格的修改不会对连线产生效果。
>The layer setting, which can be checked and changed in the parameter toolbar of the ROUTE command, displays the layer which has to be used at the mouse cursor position.

可在 ROUTE 命令的参数栏中进行检查和修改的层设置，在鼠标当前位置被使用的层会被显示在层设置中。
>The Follow­-me router reacts反应 immediately立即 on changes concerning涉及 wire width or drill diameter of vias. 
>If the option Auto set route width and drill in the Options/Set/Misc menu is set, the Follow-­me router adapts适应 the given values for wire width and via drill diameter from the Design Rules and from the net classes as soon as an airwire is selected.

Follow-me 布线器会对涉及线路宽度或钻孔直径的改变立即发生响应。
如果设置了选项/设置/杂项标签中的自动设置布线宽度及钻孔选项，Follow-me 布线器将会在鼠线被选中时，依照设计规则和网络族中线路宽度和过孔钻孔直径进行特定值的调整。

### 3. Routing Parameters 布线参数
>Parameters that affect the routing strategy策略 are set by clicking onto the AUTO icon , which is available in the parameter toolbar after entering one of the follow-­me modes.
>Click this icon in order to open the known *Autorouter Setup* window.

影响布线策略的参数是通过单击 AUTO 图标来设置的，该图标在进入任一个 Follow-me 模式后就会显示在参数工具栏中。
单击这个图标为了打开 *Autorouter Setup* 窗口。
General 和 Follow-me，会对 Follow-me 布线器产生影响
![Alt text](0x04_Autorouter(自动布线器).assets/.1463555965222.png)

> Alternatively you can open this setup window from the command line. Type:  AUTO FOLLOWME

或者你可以从命令行打开设置窗口。输入 AUTO FOLLOWME
>In the General tab you decide决定 about preferred directions in the signal layers (| vertical, ­- horizontal, / diagonal 45°, \ diagonal 135°, or * no preferred direction). 
>In many cases it makes sense for the Follow­-me router to choose no preferred direction in the signal layers.

选择 General 标签来定义信号层的首选方向。 (| vertical, ­ -horizontal, / diagonal 45°, \ diagonal 135°, or * no preferred direction). 
在许多情况下，合理的 Follow­-me 布线是在信号层中选择* 没有首选方向。 
>Settings that influence影响 the way how traces will be routed in the layout are defined in the *Follow-­me* tab.

在 *Follow-­me* 标签中的设置，会在布局编辑器中影响布线的方式。在 follow-me 标签中可以进行与布线特征有关的设置
![Alt text](0x04_Autorouter(自动布线器).assets/.1463557347547.png)
>The effects效果 of these parameters are explained解释 in section 7.6, beginning with page 208.

设置效果的解释参看本条笔记关于自动布线器参数的设置。
>In the Maximum section, you can define the number of Vias the router may use for one connection. 
>If this value is set to 0, the Follow­me router is not allowed to set vias automatically. 
>However, you are able to manually set a via by changing the layer.

在 Maximum 部分中，，您可以定义布线器用于某一条连线的过孔数量。
如果这个值设置为 0，则不允许 Follow-me 布线器自动放置过孔。
但您能够通过改变层来手动放置过孔。
>The value for Segments defines the maximum number of wire segments a connection may consist组成 of. 
>If you choose it too small, it may happen that no connection will be established.

Segments 的值定义了组成一条连线的最大线段数量。
如果您选的值太小，可能发生无法建立连线的情况。


Laycr Costs 部分设置的是各个层之间的花销等级， 
Costs 部分设置的是PCB 各种元素的花销等级， 
Maximum 部分设置的是在布线时自动产生的一些元素的最大值。

### 5. Notes
>The Follow­me router supports round and octagon via shapes外形 only. 
>Square shaped vias are not possible.

Follow-me 布线器仅支持外形为圆形和八角形的过孔。
不支持正方形外形的过孔。
>If you are working in Full mode, the Follow­-me router works in both directions independently独立, beginning with the mouse cursor position. 
>So it could happen that the router places two vias very close to or even overlapping重叠 each other near the current position of the mouse cursor. 
>In this case move the mouse cursor slightly, until the vias are optimized and the trace looks good.

如果您工作在完全模式，则 Follow-me 布线器在光标位置的两个方向上分别布线。
因此可能发生布线器放置两个与光标位置非常接近的过孔，或者甚至两个孔在光标当前位置附近相互重叠的情况。
这种情况下，请轻微的移动鼠标光标，直到优化过孔并且达到较好的布线效果为止。
>It's recommended to draw a Dimension line in layer 20 in order to limit the board area and therefore required time and memory.
>Depending on the complexity of your design, it may be wise明智的 to increase增加 the cost factor for Vias and decrease减少 it for NonPref. 
>This avoids frequent频繁 layer changes.

推荐在第 20 层上绘制一条 Dimension  外框线，以限制电路板区域，从而限制因此而需要的时间和内存。
根据您的设计复杂程度不同，将 Via 的花销提高并将 NonPref 的花销降低可能会是明智的选择。
这样可以避免频繁的变换层。