# 0x12_Layer
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库

**PCB 和 Package 编辑器中使用的层**

1 Top  Tracks路径, top side | 线路，顶层

2 Route2 Inner layer | 内部层

3 Route3 Inner layer

4 Route4 Inner layer

5 Route5 Inner layer

6 Route6 Inner layer

7 Route7 Inner layer

8 Route8 Inner layer

9 Route9 Inner layer

10 Route10 Inner layer

11 Route11 Inner layer

12 Route12 Inner layer

13 Route13 Inner layer

14 Route14 Inner layer

15 Route15 Inner layer

16 Bottom底部 Tracks跟踪, bottom side 底部侧 | 线路，底层

17 Pads Pads (through-hole) | 焊盘(通孔)

18 Vias Vias (through-hole) | 金属镀孔(穿过所有层)

19 Unrouted未布线 Airwires鼠线 (rubberbands伸缩线)

20 Dimension尺寸 Board outlines轮廓 (circles for holes圆孔) | 电路板外框（绝缘孔圆圈直径）*）

*） 在该层上绝缘孔以相应半径的圆圈表示。它们用于对 Autorouter（自动布线功能）进行限制。

21 tPlace  Silk screen, top side 丝印层，顶层

22 bPlace Silk screen, bottom side  丝印层，底层

23 tOrigins Origins原点, top side | 原点，顶层(自动生成)

24 bOrigins Origins, bottom side | 原点，底层(自动生成)

25 tNames Service print, top side 服务打印 | 用于打印，顶层（元件名称）

26 bNames Service print, bottom side | 用于打印，底层（元件名称）

27 tValues Component VALUE, top side | 元件值，顶层

28 bValues Component VALUE, bottom side | 元件值，底层

29 tStop Solder stop mask, top side | 阻焊层，顶层(自动生成)

30 bStop Solder stop mask, bottom side | 阻焊层，底层(自动生成)

31 tCream Solder cream, top side  焊膏层，顶层

32 bCream Solder cream, bottom side 焊膏层，底层

33 tFinish Finish表面处理, top side | 镀金专用阻焊层，顶层

34 bFinish Finish, bottom side | 镀金专用阻焊层，底层

35 tGlue Glue mask, top side | 粘接层，顶层

36 bGlue Glue mask, bottom side | 粘接层

37 tTest Test and adjustment inf. top side | 测试和修改信息

38 bTest Test and adjustment inf. bottom side| 测试和修改信息

39 tKeepout  No go areas区域 for components, top side | 元件限制区域

40 bKeepout No go areas for components, bottom side

41 tRestrict 限制 No go areas for tracks, top side | 敷铜限制区域| 针对顶层的线和多边形敷铜区的限制区域

42 bRestrict No go areas for tracks, bottom side|针对底层的线和多边形敷铜区的限制区域

43 vRestrict No go areas for via-holes通孔 | 金属镀孔限制区域

44 Drills Conducting through-holes | 导电过孔

45 Holes Non-conducting holes | 非导电空(安装、定位孔)

46 Milling Milling 铣加工 | 铣床切割轮廓绘制层 Milling

47 Measures Measures 测量 | 尺寸信息层

48 Document General documentation | 文档信息标注层 Documentation

49 Reference Reference marks | 基准标记

51 tDocu Part documentation, top side 部分文档，顶端 | 顶层打印时使用的详细

52 bDocu Part documentation, bottom side 部分文档，低端 | 底层打印时使用的详细

------

**Schematic、Symbol 和 Device 编辑器中使用的层**

90 Modules Module instances and ports 模块实例和端口

91 Nets Nets 网络 | 绘制具有电气属性的信号连线。

92 Busses Buses 总线 | 绘制总线形式的信号连线。

93 Pins Connection points for component symbols with additional information 元件 symbol 的连引脚，含有附加信息 | 元件符号的引脚，带有附加信息 | 放置元件引脚的连接点。

94 Symbols Shapes外形 of component symbols | 元件符号的外形 | 放置元件符号，同时也用来放置原理图外框。

95 Names Names of component symbols | 元件符号的名称 | 放置元件符号的名称。

96 Values Values/component types | 值/元件类型 | 放置元件的值。

97 Info General常规 information | 附加信息 | 放置用户添加的信息。

98 Guide Guide参考 lines | 为了符号对齐而提供的参考线 | 放置向导信息。

------

通过各层的名称或编号可以对其进行操作。

名称可以通过 LAYER 命令或 DISPLAY 菜单来修改，特殊层的功能不变。

如果您要建立自定义的层，请使用 100 以上的层编号。

通过 DISPLAY 菜单可以建立新的层（New 按钮）或者在命令框中输入 LAYER 命令来建立。

例如，您在建立名称为 Remarks 的第 200 层时，输入：

LAYER 200 Remarks

为该层设置颜色和填充方式请使用 DISPLAY 命令。