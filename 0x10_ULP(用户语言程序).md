# 0x10_ULP(用户语言程序)
> GitHub@[orca-j35](https://github.com/orca-j35)，所有笔记均托管在 [eagle-notes](https://github.com/orca-j35/eagle-notes) 仓库



## 1. ULP 用户语言程序简介
用户可以通过编写和使用 ULP 来访问 EAGLE 软件底层的模块，从而达到实现无线扩展的目的。
EAGLE 的 ULP 用一种类 C 的语法编写，熟悉 C 语言的用户可以很快地掌握。ULP 文件的扩展名为.ulp，可以用任意的文本编辑器创建并编写。
ULP 程序主要包含两个部分：定义和内容。
定义部分可以定义在内容中需要使用到的常量、变量、函数。
内容部分中可编写实现功能所需要的语句。
帮助文件中搜索 User Language 可查看 ULP 的详细解释及应用。

## 2. ULP 的语法(Syntax)
主要有下列语法：
### 2.1 Whitespace 空白
*Before a User Language Program can be executed, it has to be read in from a file.* 
在一个 ULP 被执行前，EAGLE 需要从一个文件中读入该程序。

*During this read in process, the file contents is parsed into tokens and whitespace.* 
在此读取过程中，文件内容被解析成符号和空白区域。

*Any spaces (blanks), tabs, newline characters and comments are considered whitespace and are discarded.* 
任何空格(空白)符、制表符、换行符和注释被识别为空白区域，并且会被丢弃。

*The only place where ASCII characters representing whitespace are not discarded is within literal strings, like in* 
只有在文本字符串内，用 ASCII 字符表示的空白区域不会被丢弃，例如：
```
string s = "Hello World";
```
*where the blank character between 'o' and 'W' remains part of the string.* 
在 o 和 w 之间的空白字符任然是字符创的一部分。
*If the final newline character of a line is preceded by a backslash (\), the backslash and newline character are both discarded, and the two lines are treated as one line:* 
```
"Hello \
World" 
```
*is parsed as "Hello World"* 
如果某行最后的换行符由反斜线(\)开头，反斜线和换行符都被丢弃，两行被视为一行：
"Hello \
World"
被处理为"Hello World" 

### 2.2 Comments 注释
*When writing a User Language Program it is good practice to add some descriptive text, giving the reader an idea about what this particular ULP does.* 
编写 ULP 时，添加一些描述性文本是很好的做法，告诉读者该特定 ULP 的编写思路。

*You might also want to add your name (and, if available, your email address) to the ULP file, so that other people who use your program could contact you in case they have a problem or would like to suggest an improvement.* 
你可能还需要添加你的姓名(如果可以，添加你的 email 地址)到 ULP 文件，其它使用你的程序的人可以联系到你，他们可能会有问题，或是想要提出改进意见。

There are two ways to define a comment. 
有两种方式定义注释。

The first one uses the syntax 
```
/* some comment text */
```
*which marks any characters between (and including) the opening / * and the closing */ as comment.* 

第一种使用如下语法
/* some comment text */
这标志在任何在开启 / * 和结束 */ 之间的字符被作为注释。

*Such comments may expand over more than one lines, as in* 
```
/* This is a
   multi line comment
*/
```
*but they do not nest.*
*The first */ that follows any / * will end the comment.* 

一些注释可能扩展超过一行，如
/* This is a
   multi line comment
*/
但是他们不做另外的嵌套。
在 / * 之后的第一个 */ 将会结束注释。

*The second way to define a comment uses the syntax *
```
int i; // some comment text
```
*which marks any characters after (and including) the // and up to (but not including) the newline character at the end of the line as comment.*

 第二种定义注释的方式使用下面这种语法：
 int i; // some comment text
 这标志着任何//之后，并在这一行结束的换行符之前的字符作为注释。

### 2.3 Directives 指令
*The following directives are available: *
下面的指令是可用的：

#### 1. **#include**：
*A User Language Program can reuse code in other ULP files through the #include directive.* 
*The syntax is* 
`#include "filename"`
某个 ULP 程序可以通过 #include 指令，重用其它 ULP 文件中的代码。
语法如下：
`#include "filename"`

*The file filename is first looked for in the same directory as the current source file (that is the file that contains the #include directive). *
*If it is not found there, it is searched for in the directories contained in the ULP directory path. *
*The maximum include depth is 10. *

filename 文件首先在当前原文件的相同目录中被寻找(原文件是指包含 #include 指令的文件)
假如在这里没有发现，它会搜索包含在 ULP 目录路径中的目录。
最大包含 10 的深度。

*Each #include directive is processed only once. *
*This makes sure that there are no multiple definitions of the same variables or functions, which would cause errors. *
每个 #incloud 命令只处理一次。
这可以确保这里没有相同变量或函数的多重定义，多重定义会引起错误。

*Portability note*
*￼If filename contains a directory path, it is best to always use the forward slash as directory separator (even under Windows!). *
*Windows drive letters should be avoided. *
*This way a User Language Program will run on all platforms.* 

假如 filename 包含一个目录路径，最好始终使用正斜杠嘴稳目录分割(即便是在 windows 下)
windows 驱动器字母应该被避免。
这样 ULP 可以在所有平台上运行。

#### 2. **#require**
Over time it may happen that newer versions of EAGLE implement new or modified User Language features, which can cause error messages when such a ULP is run from an older version of EAGLE. 
- 随着时间的推移可能会发生，EAGLE的新版本实现新的或修改用户语言的功能，当这样的 ULP 是从旧版本的EAGLE的运行，这可能会导致错误消息。

In order to give the user a dedicated message that this ULP requires at least a certain version of EAGLE, a ULP can contain the `#require` directive. 
The syntax is `#require version`
The version must be given as a real constant of the form `V.RRrr` where V is the version number, RR is the release number and rr is the (optional) revision number (both padded with leading zeros if they are less than 10). 
For example, if a ULP requires at least EAGLE version 4.11r06 (which is the beta version that first implemented the #require directive), it could use 
`#require 4.1106`
The proper directive for version 5.1.2 would be 
`#require 5.0102 `

- 为了给用户一个专门的消息(ULP 至少需要某一版本的 EAGLE) ，ULP 可以包含 #require 指令。
语法是 `#require version`
版本必须作为实型常量被给出，常量的结构是`V.RRrr`，V是版本号，RR是发布版本号，rr (可选)修订号(如果 RR 和 rr 小于少于10，用前导零填充)。
例如，假如 ULP 要求至少是 EAGLE 版本 4.11r06(这时测试版，首先执行 #require 指令)，可以使用
`#require 4.1106`
对于 5.1.2 版本的正确指令是：
`#require 5.0102 `

#### 3. #usage 

Every User Language Program should contain information about its function, how to use it and maybe who wrote it.
The directive 
 #usage text [, text...]
 implements a standard way to make this information available. 

每个用户语言程序应包含有关其功能，如何使用它，也许有作者的信息。
 #usage text [, text...]
实现了一个标准的方式来提供这方面的信息。
详细信息参考 帮助文件。

### 2.4 Keywords
The following keywords are reserved for special purposes and must not be used as normal identifier names: 

In addition, the names of builtins and object types are also reserved and must not be used as identifier names

- 以下关键字被保留用于特殊目的，不得作为普通标识符名称：
break
case
char
continue
default
do
else
enum
for
if
int
numeric
real
return
string
switch
void
while
此外，内建名称或对象类型的名称也被保留，一定不能用作标识符名称。
具体参考帮助内容。

### 2.5 Identifiers 标识符
An identifier is a name that is used to introduce a user defined constant, variable or function. 
Identifiers consist of a sequence of letters (a b c..., A B C...), digits (1 2 3...) and underscores (_). 
The first character of an identifier must be a letter or an underscore. 
Identifiers are case-sensitive, which means that 
int Number, number;
would define two different integer variables. 
The maximum length of an identifier is 100 characters, and all of these are significant. 

- 标识符是一个用来引入用户定义的常数、 变量或函数的名称。
标识符包括一系列的字母 （b c.......，A B C.......），数字 (1 2 3...) 和下划线 (_)。
标识符的第一个字符必须是字母或下划线。
标识符区分大小写，这意味着
int Number, number;
将定义两个不同的整数变量。
标识符的最大长度为 100 个字符，并且所有这些字符都是有意义的。

### 2.6 Constants 常量
Constants are literal data items written into a User Language Program. 
According to the different data types, there are also different types of constants. 
Character constants 
Integer constants 
Real constants 
String constants 

- 常量是写入到 ULP 的文本数据项。
根据不同的数据类型，也有不同类型的常量。
字符常量
整型常量
实数常量
字符串常量

常量的详细信息参考帮助信息。

### 2.6 Punctuators 标点符号
The punctuators used in a User Language Program are 
[] Brackets 方括号
() Parentheses 括号
{} Braces 大括号
, Comma 逗号
; Semicolon 分号
:Colon 冒号
= Equal sign 等号
Other special characters are used as operators in a ULP. 
其它特殊字符，在 ULP 中被用作运算符。
详见帮助文件。

## 3. 对象类型(Object Types)
在 EAGLE 中，ULP 可操作的对象分为元件库对象(Library) 、原理图对象(Schematic) 和 PCB 对象(Board) ，在这 3 个对象中右分别有很多小的可操作对象，例如栅格、层、网络、过孔等。
用户可以通过操作这些对象，实现相应的功能。
对对象的操作，可以单独操作，即只操作一个对象，也可以组合操作， 一次操作多个对象， 下面列举几个有代表意义的可操作对象来说明。

### 3.1 元件库对象(Library)
- area : 通过编写坐标，确定 Device 的区域。
- description : 通过字符串的形式添加Device 的描述。
- headline : 用户可以在该项中编辑 Device 的标题显示，用字符串形式表示。
- name : 用户可以在该项中编辑 Device 的位号，用字符串形式表示，既编辑元件 >name 的内容。
- package : 用户可以在该项中调用已经设计'好的器件封装。
- prefix : 用户可以在该项编写 Dcvice 的前缀，比如 IC 、U 、R 、L 、C 等，用以表示不同类别的器件。
- technologies: 用户可以在该项选择 Device 使用的技术类型，技术类型包括封装和包装类别。
- value：用户可在该项编写 Device 中 >value 的值，用字符串形式表示。
- SYMBOL：有下面 3 个数据：
	- area：编写坐标，确定 Symbol 的区域。
	- library：通过该项目，用户可以选择该 symbol 需要保存在哪个元件库中。
	- name：在该项中编辑 symbol 的位号，用字符串形式表示。

### 3.2 原理图对象(Schematic)
- SHEET : 在SHEET 中，只有两个数据成员。
• area : 在 area 项中，通过编写坐标，确定Sheet 的区域。
• number : 该项用于编辑 Sheet 的页码，用整数形式表示。

- BUS : 有一个数据成员。
• name : 顾名思义，在该项中，可以确定Bus 的名称。

- NET : 有4 个数据成员。
• class : 在该项中，可以选择 Net 属于哪一个网络簇。
• name : 在该项中，可以定义 Net 的名称，用字符串形式表示。
• column : 该项与 row 一同解释。
• row : row 与 column 项组合，用于Net 在 Sheet 中定位，主要用于 X-ref 功能。在Sheet 的四周， 有类似于栅格坐标的标号，通过横纵的组合，确定 Net 在Sheet 的位置。
row 表示行的标号， column 表示列的标号。

### 3.3 PCB 对象(Board)
- **HOLE** : 在 HOLE 中，有4 个数据成员。
• diameter : 在diameter 中，可以设置 Hole 的外径直径，用整数表示。
• drill : 在drill 中，设置Hole 的内径，也就是实际钻孔的直径，用整数表示。
• drillsymbol : 可以得到该 Hole 可选择的钻孔形状的数量， 0 表示没有钻孔形状分配给这一个 Hole 。
• x, y : 该项表示 Hole 的中心坐标。

- **VIA** : 在VIA 中，有8 个数据成员。
• diameter : diameter 中，可以设置Via 的外径直径，用整数表示。
• drill : 在drill 中，设置 Via 的内径，用整数表示。
• drillsymbol : 可以得到该 via 可选择的钻孔形状的数量， 0 表示没有钻孔形状分配给这一个 Hole。
• start：与 end 一同解释。
• end：start 与 end 表示 via 的开始层和结束层。由于 eagle 的层由数字排列，所以开始层总是小于结束层。
• shape：可以设置 via 外径的形状，可以分成设置。
•flage：用于返回end 标志，该标志可以用于生成 via 的阻焊区域。
•x,y：表示 via 的中心坐标。

## 4. 语句(Statement)
语句用于指定ULP 中的控制流程。
在没有特殊控制语句的 ULP 中， ULP 中的语句按顺序执行，这一点与 C 语言也一致。


### 4.1 复合语句(Compound Statement)
复合语句的含义是一组声明通过{ } 符号集中在一起，在语法上讲，整个块声明属于一个声明，块声明可以被嵌套在程序的任意深度。

### 4.2 控制语句(Control Statement)
控制声明用于控制程序的流程，包括循环声明、选择声明和跳转声明。

#### 4.2.1. 循环语句
1. **do...while**
>The do...while statement has the general syntax 
>`do statement while (condition);`
>and executes the statement until the condition expression becomes zero. 
>The condition is tested after the first execution of statement, which means that the statement is always executed at least one time. 
>If there is no break or return inside the statement, the statement must affect the value of the condition, or condition itself must change during evaluation in order to avoid an endless loop. 

- **do...while** 语句具有通用语法
 `do statement while (condition);`
 执行该语句直到条件表达式变为 0.
 条件在第一条语句执行后被测试，这意味着该总是至少被执行一次。
 假如语句中没有 break 或 return ，该语句的值必须要影响条件的值，或条件本身必须在平定过程中被改变，以避免一个无尽的循环。
```
string s = "Trust no one!";
int i = -1;
do {
   ++i;
   } while (s[i]); 
```

2. **while**
The while statement has the general syntax 
`while (condition) statement`
and executes the statement as long as只要 the condition expression is not zero. 
The condition条件 is tested before the first possible execution of statement, which means that the statement may never be executed if condition is initially zero. 
If there is no break or return inside the statement, the statement must affect the value of the condition, or condition itself must change during evaluation in order to avoid an endless loop. 
Example
```
string s = "Trust no one!";
int i = 0;
while (s[i])
      ++i; 
```

3. **for**
>The for statement has the general syntax 
>for ([init]; [test]; [inc]) statement
>and performs the following steps: 
>If an initializing expression init is present, it is executed. 
>If a test expression is present, it is executed. 
>If the result is nonzero (or if there is no test expression at all), the statement is executed. 
>If an inc expression is present, it is executed. 
>Finally control returns to step 2. 
>If there is no break or return inside the statement, the inc expression (or the statement) must affect the value of the test expression, or test itself must change during evaluation in order to avoid an endless loop. 
>The initializing expression init normally initializes one or more loop counters. It may also define a new variable as a loop counter. The scope of such a variable is valid until the end of the block which encloses the for loop. 

- for 语句有通用语法
for ([init]; [test]; [inc]) statement
执行以下步骤：
如果初始化表达式 [init] 存在，它将被执行。
如果[ test ]表达式存在，它将被执行。
如果结果非零(或者如果在所有情况下，没有 test 表达式)，语句被执行。
假如 inc 表达式存在，它被执行。
最后控制返回第二步。
假如在语句中没有 break 或 return，inc 表达式(或语句中)必须影响test表达式的值，或者 test 自身在评价过程中必须改变，以此避免一个无线循环。

```
Example

string s = "Trust no one!";
int sum = 0;
for (int i = 0; s[i]; ++i)
    sum += s[i]; // sums up the characters in s 
```

#### 4.2.2 选择语句
1. **if...else**
The if...else statement has the general syntax 
```
if (expression)
   t_statement
[else
   f_statement]
```
The conditional expression is evaluated评估, and if its value is nonzero the t_statement is executed. 
Otherwise否则 the f_statement is executed in case there is an else clause. 
An else clause is always matched to the last encountered if without an else. 
else 从句总是匹配到最近遇到的 if ，且该 if 没有 else。
If this is not what you want, you need to use braces括号 to group the statements, as in 
```
if (a == 1) {
   if (b == 1)
      printf("a == 1 and b == 1\n");
   }
else
   printf("a != 1\n"); 
```

2. **switch**
The switch statement has the general syntax 
```
switch (sw_exp) {
  case case_exp: case_statement
  ...
  [default: def_statement]
  }
```
and allows for the transfer of control to one of several case-labeled statements, depending on the value of sw_exp (which must be of integral type). 
并允许控制权转移到一些case- 标签语句之一，取决于 sw_exp 的值(必须为整型)
Any case_statement can be labeled by one or more case labels. 
任何 case_statement 能被标记在一个或多个 case labels 下。
The case_exp of each case label must evaluate to a constant integer which is unique within it's enclosing switch statement. 
每个 case_exp 标签的 case _exp 必须赋值到一个整型常量，并且该常量在闭合的 switch 语句内是唯一的。
There can also be at most one default label. 
还可以有最多一个 default 标签。
After evaluating sw_ exp, the case_exp are checked for a match. 
赋值 sw _exp 后，case _exp 进行匹配检查。
If a match is found, control passes to the case_statement with the matching case label. 
如果发现匹配，控制被传递给含有匹配 case 标签的 case_statement。
If no match is found and there is a default label, control passes to def_statement. 
如果没有发现匹配，并有一个默认的标签，控制权传递给def_statement。
Otherwise none of the statements in the switch is executed. 
否则在 switch 中没有任何语句被执行。
Program execution is not affected when case and default labels are encountered. 
当 case 标签和default 标签被遇到时，程序的执行不会受到影响。
Control simply passes through the labels to the following statement. 
控制仅是通过标签传递到下面的语句中。
To stop execution at the end of a group of statements for a particular case, use the break statement. 
在一个特定case的一组语句的结尾停止执行，使用break语句

Example
string s = "Hello World";
int vowels = 0, others = 0;
for (int i = 0; s[i]; ++i)
    switch (toupper(s[i])) {
      case 'A':
      case 'E':
      case 'I':
      case 'O':
      case 'U': ++vowels;
                break;
      default: ++others;
      }
printf("There are %d vowels in '%s'\n", vowels,s); 

#### 4.2.3. 跳转语句
1. **break**
The break statement has the general syntax 
`break;`
and immediately立即 terminates结束 the nearest enclosing封闭 do...while, for, switch or while statement. 
立刻结束最近的封闭语句，如do...while, for, switch，while
This also applies to loop members of object types. 
也使用于对象类型的循环部分。
Since all of these statements can be intermixed混合 and nested嵌套 to any depth, take care to ensure确保 that your break exits from the correct statement. 
由于所有这些语句可以被混合和被嵌套任意深度，因此要特别小心，以确保你的 break 从正确的语句退出。

2. **continue**
The continue statement has the general syntax 
`continue;`
and immediately transfers control to the test condition of the nearest enclosing do...while, while, or for statement, or to the increment expression of the nearest enclosing for statement. 
立刻把控制权交给最近的封闭语句的测试条件，如 do...while, while, for 语句；或者把控制权交给最近的闭合的 for 语句的增量表达式。
Since all of these statements can be intermixed and nested to any depth, take care to ensure that your continue affects the correct statement.
由于所有这些语句可以被混合和被嵌套任意深度，因此要特别小心，以确保你的 continue 从正确的语句退出。

3. **return**
A function with a return type other than void must contain at least one return statement with the syntax 
一个有返回类型的函数，且返回类型不是 void ，则该函数至少包含一个返回语句的语法。
`return expression表达式;`
where expression must evaluate to a type that is compatible with the function's return type. 
表达式必须复制给一个类型，该类型和函数的返回类型兼容。
The value of expression is the value returned by the function. 
表达式的值是函数返回的值。
If the function is of type void, a return statement without an expression can be used to return from the function call. 
如果函数的返回类型是 void ，return 语句无需使用从调用函数返回值的表达式。

### 4.3 Expression Statement 表达式语句
An expression statement is any expression followed by a semicolon. 
An expression statement is executed by evaluating the expression. 
All side effects of this evaluation are completed before the next statement is executed. 
Most expression statements are assignments or function calls. 
A special case is the empty statement, consisting of only a semicolon. 
An empty statement does nothing, but it may be useful in situations where the ULP syntax expects a statement but your program does not need one.
表达式语句是任何表达式后跟一个分号。
表达式语句是通过计算表达式执行。
在下一条语句被被执行前，该赋值的所有副作用被完成。
大多数表达式语句是赋值或函数调用。
一种特殊的情况是空语句，仅包括一个分号。
一个空语句不做任何事，但是在某些情况下是有用的，例如 ULP 语法期望一条语句，但是你程序在该处不需要语句。

### 4.4 Builtin Statements 内建指令语句
在笔记的第 5 节进行讲解

### 4.5 Constant Definitions 定义常量
Constants are defined using the keyword enum, as in 
常量使用关键词 enum 枚举进行定义，例如：
`enum { a, b, c };`
which would define the three constants a, b and c, giving them the values 0, 1 and 2, respectively各自的. 
Constants may also be initialized初始化 to specific特定 values, like 
`enum { a, b = 5, c };`
where a would be 0, b would be 5 and c would be 6.

### 4.6 Variable Definitions 定义变量
The general syntax of a variable definition is 
`[numeric] type identifier [= initializer][, ...];`
where type is one of the data or object types, identifier is the name of the variable, and initializer is a optional initial value. 
type 是一个数据类型会对象类型，identifier 标识符是变量的名称，initializer 初始化时一个可选的初始化值
Multiple variable definitions of the same type are separated分开 by commas (,). 
多个相同类型的变量的定，可以通过逗号分开。
If identifier is followed by a pair of brackets ([]), this defines an array of variables of the given type. 
假如标识符后跟一对方括号，将定义一组给定类型的变量。
The size of an array is automatically adjusted at runtime. 
数组的大小在运行时自动调整。
The optional keyword numeric can be used with string arrays to have them sorted alphanumerically by the sort() function. 
可选关键词 numeric 可被用于字符串数组，以使他们通过 sort() 函数排序字母
By default (if no initializer is present), data variables are set to 0 (or "", in case of a string), and object variables are "invalid". 
默认情况下（如果没有初始化是存在的），数据变量被设置为0（或“”，在一个字符串的情况下），对象的变量是“无效”。
```
Examples
int i; 
defines an int variable named i

string s = "Hello"; 
defines a string variable named s and initializes it to "Hello"

real a, b = 1.0, c; 
defines three real实型 variables named a, b and c, initializing b to the value 1.0

int n[] = { 1, 2, 3 }; 
defines an array of int, initializing the first three elements to 1, 2 and 3

numeric string names[]; 
defines a string array that can be sorted排序 alphanumerically字母

UL_WIRE w; 
defines a UL_WIRE object named w
```

The members of array elements of object types can't be accessed directly: 
对象类型数组元素中的成员不能被直接访问
```
UL_SIGNAL signals[];
...
UL_SIGNAL s = signals[0];
printf("%s", s.name); 
```

## 5. Builtins 内建指令

内建指令可以附加信息，还可以方便地对数据进行操作，内建指令可以理解为EAGLE 独有的、一种封装好的软件接口，用户可以操作这些接口，完成多样的功能。
内建指令包括常量、变量、函数和声明。


Builtins are Constants, Variables, Functions and Statements that provide additional information and allow for data manipulations. 
内建指令是常量、变量、函数和语句，提供附加信息并允许数据操作。

### 5.1 Builtin Constants 内建指令常量
Builtin constants are used to provide information about object parameters, such as maximum recommended name length, flags etc. 
内建指令常量是被用于提供有关对象参数的信息，例如最大的推荐名称长度、标志等。
Many of the object types have their own Constants section which lists the builtin constants for that particular object (see e.g. UL_PIN). 
许多对象类型有它们自己的 Constants 常量部分，该部分列出了特定对象的内建常量。 (see e.g. UL_PIN)
The following builtin constants are defined in addition to the ones listed for the various object types: 
下面显示内建常量以不同的对象类型被定义在一个附加列表中。
EAGLE_VERSION 
EAGLE program version number (int)

EAGLE_RELEASE 
EAGLE program release发布 number (int)

EAGLE_SIGNATURE 
a string containing EAGLE program name, version and copyright information
字符串，包含 EAGLE 程序名、版本和版权信息。
EAGLE_PATH 
a string containing the complete path of the EAGLE executable
字符串包含 eagle 的可执行文件的完整路径
EAGLE_DIR 
a string containing the directory of the EAGLE installation (`$EAGLEDIR`)
字符串包含 eagle 的安装目录 (`$EAGLEDIR`)
EAGLE_HOME 
a string containing the user's home directory when starting EAGLE (`$HOME`)
字符串，包含在启动 ealge 时用户的主目录 (`$HOME`)。
OS_SIGNATURE 
a string containing a signature of the operating system (e.g. Mac..., Windows... or Linux)
字符串，包含操作系统的签名(e.g. Mac..., Windows... or Linux)
REAL_EPSILON 
the minimum positive real number such that 1.0 + REAL_EPSILON != 1.0
eagle 可以识别的最小正实数，如 1.0 + REAL_EPSILON != 1.0
REAL_MAX 
the largest possible real value
最大正实数
REAL_MIN 
the smallest possible (positive!) real value
the smallest representable number is `-REAL_MAX`
最小正实数
最小正实数表示数字是 `-REAL_MAX`
INT_MAX 
the largest possible int value
最大整数
INT_MIN 
the smallest possible int value
最小整数
PI 
the value of "pi" (3.14..., real)
π值 (3.14...,实数)
usage 
a string containing the text from the #usage directive
字符串，包含从 #usage 指令中得到的字符串。

These builtin constants contain the directory paths defined in the directories dialog, with any of the special variables (`$HOME` and `$EAGLEDIR`) replaced by their actual values. 
Since each path can consist of several directories, these constants are string arrays with an individual directory in each member.
The first empty member marks the end of the path: 
这些内置常量包含的目录地址定义在目录对话框中，并用一些特别的变量 (`$HOME` and `$EAGLEDIR`) 代替它们的实际值。
因为每个路劲可以包含多个目录，在各个部分中这些常量是含有单个目录的字符串。
path_doc[] 
Documentation
文档路劲
path_lbr[] 
Libraries
库路径
path_dru[] 
Design Rules
设计规则路径
path_ulp[] 
User Language Programs
ULP 路径
path_scr[] 
Scripts
脚本路径
path_cam[] 
CAM Jobs
CAM 路径
path_epf[] 
Projects
工程路径
When using these constants to build a full file name, you need to use a directory separator, as in 
当用这些常量建立完整文件名时，你需要目录分隔符。例如
`string s = path_lbr[0] + '/' + "mylib.lbr";`
The libraries that are currently in use through the USE command: 
当前正在使用的库，通过命令 USE 
`used_libraries[] `

### 5.2 Builtin Variables 内建变量
Builtin variables are used to provide information at runtime. 
内建变量被用于在程序运行时提供信息。
int argc 
number of arguments given to the RUN command
为 RUN 命令提供参数的数量。
string argv[] 
arguments given to the RUN command (argv[0] is the full ULP file name)
给 RUN 命令提供参数(argv[0] 是全部 ULP 文件名)

### 5.3 Builtin Functions 
内建函数是预定义好的函数，用户只需要调用就可以实现相应的功能。
由于内建函数的数量庞大，限于篇幅的局限，在这里不一一介绍，只在每一类中挑选具有代表意义的函数举例介绍。对于内建函数，在EA GLE的帮助文件中有详细的说明。

Builtin functions are used to perform specific tasks, like printing formatted strings, sorting data arrays or the like. 
You may also write your own functions and use them to structure your User Language Program.
内建函数被用于执行特定任务， 如打印格式化字符串，排序数组或类似
你也可以编写你自己的函数，并用它们来构建你自己的 ULP 程序。

The builtin functions are grouped into the following categories: 
内建函数可分为以下几类：
#### 1. Character Functions 字符函数
Character functions are used to manipulate操作 single characters. 
The following character functions are available: 
字符函数被用于操作单个字符。
如下的字符函数是可用的：
isalnum() 
isalpha() 该函数可以判断字符是否属于字母(a 至z) ，如果属于字母，函数返回非0值，否则返回0 。
iscntrl() 
isdigit() 
isgraph() 
islower() 
isprint() 
ispunct() 
isspace() 
isupper() 
isxdigit() 
tolower()  该函数可以把字符从大写转换为小写状态。
toupper() 


#### 2. File Handling Functions 文件处理函数
Filename handling functions are used to work with file names, sizes and timestamps时间戳. 
The following file handling functions are available: 
fileerror() 
fileglob() 
filedir() 用于返回相应文件的路径
fileext() 
filename() 
fileread() 
filesetext() 
filesize() 
filetime() 用于返回相应文件的名称
See output() for information about how to write into a file. 


#### 3. Mathematical Functions 数学函数
Mathematical functions are used to perform mathematical operations. 
The following mathematical functions are available: 
abs() 执行该函数可以返回又的绝对值。
acos() 
asin() 
atan() 
ceil() 执行该函数返回不小于 x 的最小整数。
cos() 
exp() 
floor() 
frac() 
log() 
log10() 
max() 执行该函数返回又: 和y 中的较大值。
min() 
pow() 
round() 
sin() 
sqrt() 
trunc() 
tan() 
Error Messages
If the arguments of a mathematical function call lead to an error, the error message will show the actual values of the arguments. Thus the statements 
real x = -1.0;
real r = sqrt(2 * x);
will lead to the error message 
Invalid argument in call to 'sqrt(-2)' 

#### 4. Miscellaneous Functions 杂项函数
Miscellaneous functions are used to perform various tasks. 
The following miscellaneous functions are available: 
country() 
exit() 
fdlsignature() 
language() 执行该函数，可以返回当前系统使用的语言的代码。
lookup() 
palette() 
sort() 
status() 
system() 
Configuration Parameters 
Unit Conversions 

#### 5. Network Functions 
Network functions are used to access remote sites on the Internet. 
用于在英特网上访问远程站点。
The following network functions are available: 
neterror() 执行该函数后，返回最近的网络呼叫错误信息。
netget() 在网络上执行一个 GET 请求
netpost() 在网络上执行一个 POST 请求

#### 6. Printing Functions 
Printing functions are used to print formatted strings. 
The following printing functions are available: 
printf() 按括号内规定的格式，打印出相应信息。
sprintf() 

#### 7. String Functions 
String functions are used to manipulate处理 character strings. 
The following string functions are available: 
strchr(): strchr (s , x) 会扫描ns 字符串内是否有与x相同的字符。如果有，则返回这个字符在字符串中的偏移位置，否则返回- 10
strjoin() 
strlen() 执行该函数，可以得到字符串的长度。
strlwr() 
strrchr() 
strrstr() 
strsplit() 
strstr() 
strsub() 
strtod() 
strtol() 
strupr() 该函数可以把字符串内的小写字母转换为大写字母。
strxstr() 

#### 8. Time Functions 
Time functions are used to get and process time and date information. 
The following time functions are available: 
sleep() 
t2day() 
t2dayofweek() 
t2hour() 
t2minute() 
t2month() 
t2second() 
t2string() 
t2year() 
time(): time (void)执行该函数，可以得到当前的系统时间。
timems(): timems(void)  执行该函数，可以得到自从开始执行ULP 后，到现在的毫秒数。最大值86400000 ，超过最大值后从0 开始重新计数。

#### 9. Object Functions 
Object functions are used to access common information about objects. 
对象的函数用于访问对象的公共信息。
The following object functions are available: 
clrgroup()  清除对象的组标志。
ingroup() 检查在组里是否有对象
setgroup() 舍子对象的组标志
setvariant() 
variant() 

#### 10. XML Functions 
XML functions are used to process XML (Extensible Markup Language) data. 
The following XML functions are available: 
xmlattribute() 该函数可以用于提取XML 标签的属性。
xmlattributes() 
xmlelement() 
xmlelements() 
xmltags() 执行该函数，可以在 XML 代码中提取标签名称的列表。
xmltext() 


Builtin Statements 
### 5.3 Builtin Statements 内建指令语句
在通常意义上来讲，内建指令声明可以打开一个特定的文本编辑环境，在这个环境中，文件的数据结构可以进人，也就是可以以文本的方式编辑各种文件的一些属性，包括PCB 和原理图。
内建指令声明的类别有board 、deviceset 、library 、output 、package 、schcmatic 、sheet 、symbol 。

Builtin statements are generally used to open a certain context in which data structures or files can be accessed. 
内建指令语句通常用于在被访问的数据结构或文件中，打开某一上下文菜单。
The general syntax of a builtin statement is 
内建指令语句的一般语法是：

`name(parameters) statement`

where name is the name of the builtin statement, parameters stands for one or more parameters, and statement is the code that will be executed inside the context opened by the builtin statement. 
name 是内建指令语句的名称；parameters 代表一个或多个参数；statement 通过内建指令语句打开的上下文菜单中，将要被执行的代码。
Note that statement can be a compound statement, as in 
注意，语句可以是复合语句，例如：
```
board(B) {
  B.elements(E) printf("Element: %s\n", E.name);
  B.Signals(S)  printf("Signal: %s\n", S.name);
  }
```
The following builtin statements are available: 
有以下内建语句是可用的：
board() 
deviceset() 
library() 
module() 
output() 
package() 
schematic() 
sheet() 
symbol() 

board (): 针对PCB 板的内建指令声明。在当前的编辑窗口有PCB 设计时，可以打开
PCB 板的文本编辑环境。
```
if (board)
board(B) {
B.elements(E)
printf("Element: %s\n",E.name) ;
```
上面代码的意思是，如果board 存在，就打开board 的文本编辑环境，并且打印出相应的信息。

deviceset () : 在当前的编辑窗口有device 打开时，可以打开device 的文本编辑环境。
```
if (deviceset)
deviceset(D) {
D.gates(G)
printf("Gate: %s\n",G.name) ;
```
上面代码的意思是，如果当前的编辑窗口中有device ，那么打开该device 的文本编辑环境，并且打印出Gate D 的名字。

library () : 在当前的编辅窗口有library 打开时， 打开library 的文本编辑环境。
```
if (library)
library(L) {
L.devices(D)
printf("Device : %s\n ",D.name) ;
```
上面代码的意思是，在当前编辑有 library 打开时，打开library 的文本编辑窗口，并打印出Device D 的名字。

output () : 为随后的打印请求，打开一个输出文件，也就是打开一个文件，够打印语句输出，当执行完output 函数后，文件会立刻被关闭。
```
output("file.txt"."wt"){
printf("Directly printed\n");
PrintText("via function call");
}
```
上面的代码的意思是，打开一个名 为file 的文本文件，并且写入"Directly printed 和"via function call"到该文件中。

package () : 在当前的编辑窗口有package 打开时，打开package 的文本编辑环境。
```
if(package)
package(P) {
P.contacts(C)
printf("Contact:%s\n",c.name) ;
}
```
上面代码的意思是，在当前的编辅环境中有package 打开时，打开package 的文本编辑环境，并且提取 Contacts-C 的名称，并且打印出来。

schematic () : 在当前的编辑窗口有schematic 打开时，打开schematic 的文本编辑环境。
```
if (schemat i c)
schematic(S) {
S.parts(P)
printfC ("Part:%s\n ",P.name) ;
}
```
上面代码的意思是，在当前的编辑环境中有schematic 打开时，打开schematic 的文本编辑环境，并且打印出part-P 的名称。

sheet () : 在当前的编辑窗口有sheet 打开时，打开sheet 的文本编辑环境。
```
i f (sheet)
sheet(S) {
S.parts(P)
printfC"Part : %s\ n"， P.name) ;
}
```
上面代码的意思是，在当前的编辑环境中有sheet 打开时，打开sheet 的文本编辑环境，并且打印出 part-P 的名称。

symbol () : 在当前的编辑窗口有symbol 打开时，打开symbol 的文本编辑环境。
```
if (symbol)
symbol(S) {
S. pins(P)
printf(" Pin : %s\n " , P. name) ;
}
```
上面代码的意思是，在当前的编辑环境中有symbol 打开时，打开symbol 的文本编辑环
境，并且打印出 pin-P 的名称。

## 6. 对话框(Dialogs)
EAGLE 的 ULP 的对话框，可以让你自己定义与ULP 相连的前端界面，通过单击或者选
择按钮，可以实现 ULP 的窗口化操作。
EAGLE 预定义了一些对话框，可供ULP 调用，也可以通过编写对话框的各个元素， 自己构建一个对话框。

### 6.1 预定义的对话框(Predefined Dialogs)

#### 1.  dlgDirectory ( ) : 
显示目录对话框，语法如下:
```
string dirName ;
dirName = dlgDirectory( "Select a directory" , "" );
```
运行后的结果如图所示。
![Alt text](0x10_ULP(用户语言程序).assets/.1465136312636.png)

#### 2. dlgFileOen ( ) : 
打开文件对话框，语法如下:
```
stringfileName;
fi1eName = d1gFi1eOpen( "Se1ect afi1e"," ","*.brd");
```
运行后的结果如图
![Alt text](0x10_ULP(用户语言程序).assets/.1465136425585.png)

#### 3. dlgFileSave ( ) : 
保存文件对话框，语法如下:
```
string fileName ;
fileName=dlgFileSave( " select a file " ," " , " *. brd" ) ;
```
![Alt text](0x10_ULP(用户语言程序).assets/.1465136558620.png)

#### 4. dlgMessageBox () : 
运行该预定于的对话框，会显示一个信息窗口，这个窗口在用户对其有下一步操作之前一直存在。
```
if(dlgMessageBox("! Are you sure? " , " &Yes" , " &No") == 0 ) {
// let's do it!}
```
![Alt text](0x10_ULP(用户语言程序).assets/.1465136692164.png)

### 6.2 对话框对象(Dialog Object)
对话框对象指的是在 ULP 的对话框中可以操作的对象。
对话框可操作的对象几乎包括 EAGLE 的各种元素，例如网格、按钮等。
由于对话框的操作对象很多，这里仅列举出几个对象来说明。
具体的对话框操作对象，请阅读 EAGLE 的帮助文件。

#### 1. dlgcell () : 
dlgcell 操作的对象是对话框中的单元。
该对话框函数与 dlgGridLayout 配合，定义了对话框单元在对话框中的相对位置，对话框的左上方是行与列的起始位置，所以坐标为(0,0) ，单元的相对位置以对话框的左上方为原点。
Dlgcell 的语法为: dlgCell ( int row ,int column[ , int row2 , int column]) statement，在该表达中，可以看到第二个行列坐标为可选项。当只有一个行列坐标时，单元开始于该坐标；当有两个行列坐标时，单元开始于第一个坐标，结束于第二个坐标。
```
string Text;
dlgGridLayout {
dlgCell(0,0) dlgLabel( "Cell 0,0" ) ;
dlgCell(1,2,4,7 ) dlgTextEdit(Text) ;
}
```
上面代码的意思是，在对话框坐标为(0,0) 的地方，定义一个单元，显示信息为" Cell , 0 " ；在对话框坐标(1,2)~(4,7) 的地方，定义一个单元，显示文本信息"Text" 。

#### 2. dlgGridLayout () : 
dlgGridLayout 可以打开一个网格布局的环境，在该环境内，可以定义一个一个的单元，通过这些单元可以把对话框分为很多个部分。
唯一的可以进入该网格布局环境的就是上面介绍的dlgcell。 
所以dlgGridLayout()和dlgcell()总是同时出现。
```
dlgGridLayout {
dlgCell(0,0) dlgLabel ( "Row 0/Col 0");
dlgCell(1,0) dlgLabel ( "Row 1/Col 0");
dlgCell(0,1) dlgLabel ( "Row 0/Col 1");
dlgCell(1,1) dlgLabel ( "Row 1/Col 1");
```
上面代码的意思是，在对话框相对坐标(0 , 0) 的地方示"Row 0/ Col 0" ，在对话框相对坐标(1,0 )的地方显示"Row 1/Col 0"，在对话框相对坐标(0 ，1)的地方显示" Row 0/Col 1" ，在对话框相对坐标(1,1)的地方显示"Row 1 / Col 1" 。

### 6.3 布局信息(Layout Information)
在介绍布局信息前，需要知道一个概念: EAGLE 的 ULP 的所有对象都被放置在布局环境中，并且该环境可以细分为网格环境、横向环境和纵向环境。

网格布局环境(Grid Layout Context) : 网格布局环境dlgGridLayout 函数设置，前面已经详细介绍了该函数，所以这里不再说明。

横向布局环境( horizontal layout context ) : 横向布局环境中的对象总是由左向右排列，dlgStretch 和 dlgSpacing 可以更加灵活的在可利用的空间内分配位置，由横向布局环境定义
的元素在对话框内部占用横向的空间。
```
dlgHBoxLayout {
dlgStretch(1) ;
dlgPushButton("+OK") dlgAccept();
dlgPushButton( "Cancel") dlgReject();
```
Accept 同意 reject 拒绝
上面的代码，定义了一个横向的布局，由左到右放置了两个元素: OK 和 Cancel 。

纵向布局环境(vertical layout context) : 纵向布局环境对操作对象的操作方式和横向布局环境完全一致。唯一不同的是，纵向布局环境使用 dlgVBoxLayout ，并且占用对话框内部的
纵向空间。

### 6.4 对话框函数(Dialog Functions)
关于对话框，还有一些函数，可以实现对话框的特殊功能。
对话框函数包括dlgAccept 、dlgRedisplay 、dlgReset 、dlgReject 、dlgSelectionChanged 这5 个。
#### 1. dlgAccept (int Result) : 
该函数的功能是在当前的指令序列执行完成后，关闭对话框，用户对对话框做的任何改变都会被接受。

#### 2. dlgRedisplay (Void) : 
该函数的功能是刷新对话框，可以在对话框有改变的情况下使用，当对话框没有改变或者对话框结束时，不需要使用dlgRedisplay 函数，因为在对话框的最后，会自动刷新对话框。
```
string Status ="Idle";
int Result = dlgDialog("Test") {
dlgLabel(Status,1) ; // note the '1' to tell the label to be updated !
dlgPushButton(" + OK") dlgAccept(42);
dlgPushButton("Cancel") dlgReject();
dlgPushButton("Run" ) {
Status = "Running...";
dlgRedisplay() ;
// some program action here...
Status ="Finished . ";
}
}
```
上面的代码中，在 runnmg 后执行了dlgRedisplay ， 其目的是在改变了程序的状态为'Run'后，刷新对话框，然后再执行下面的代码。

#### 3. dlgReset () : 
执行该函数后，复位对话框中的所有对象到初始值。
```
int Number = 1;
int Result = dlgDialog("Test") {
dlgIntEdit(Number);
dlgPushButton("+OK")    dlgAccept(42);
dlgPushButton("Cancel") dlgReject();
dlgPushButton("Reset")  dlgReset();
               }; 
```
上面的代码中，定义了3 个按钮，分别是OK 、Cancel 和Reset ，单击 Reset 按钮会调用dlgReset 函数，使对话框中的所有对象恢复初始值。

#### 4. dlgReject () :
执行该函数，可以关闭对话框，任何改变都会被忽略。
在上面的例子中，Cancel 按钮调用了dlgReject 函数，当单击Cancel 后，对话框会关闭，并且对对话框所作的修改都不会被接受。

#### 5. dlgSelectionChanged () : 
该函数可以用在一个列表环境中，用来确定是否 dlgListView 或者 dlgListBox 函数被调用。
还有一个功能是可以确定是否在当前列表的选择有改变，当有改变时，函数返回非0 值，否则返回0 。
```
string Colors[] = { "red\tThe color RED", "green\tThe color GREEN", "blue\tThe color BLUE" };
int Selected = 0; // initially selects "red"
string MyColor;
dlgLabel(MyColor, 1);
dlgListView("Name\tDescription", Colors, Selected) {
  if (dlgSelectionChanged())
     MyColor = Colors[Selected];
  else
     dlgMessageBox("You have chosen " + Colors[Selected]);
  } 
```

在上面的代码中，使用digSelectionChanged 函数来确定用户对于颜色的选择是否改变，当改变时，把显示的颜色改变为用户选择的颜色，否则输出信息栏" You have chosen + (当前
选择的颜色)" 。

### 6.5 对话框实例
A Complete Example
Here's a complete example of a User Language Dialog. 

```
int hor = 1;
int ver = 1;
string fileName;
int Result = dlgDialog("Enter Parameters") {
  dlgHBoxLayout {
    dlgStretch(1);
    dlgLabel("This is a simple dialog");
    dlgStretch(1);
    }//在这一段，程序定义了两个变量 hor 和 ver，并同时为它们定义了初始值 1，还定义了一个字符串"fileName"，最后利用横向布局环境定义了在对话框上端显示"This is a simple dialog"的字样。
  dlgHBoxLayout {
    dlgGroup("Horizontal") {
      dlgRadioButton("&Top", hor);
      dlgRadioButton("&Center", hor);
      dlgRadioButton("&Bottom", hor);
      }
    dlgGroup("Vertical") {
      dlgRadioButton("&Left", ver);
      dlgRadioButton("C&enter", ver);
      dlgRadioButton("&Right", ver);
      }
    }//上面这段在第一段的后面执行，所以在对话框中的显示也是紧跟着第一段程序。这一段通过一个横向布局环境定义了很想的空间，在这个空间内有定义了两个名为"Horizontal"和"Vertical"的显示组。在 Horizontal 组里面，有 3 个单选按钮，分别为 Top、Center、Bottom；
在 Vertical 组中，也有 3 个单选按钮，分别为 Left、Center、Right
  dlgHBoxLayout {
    dlgLabel("File &name:");
    dlgStringEdit(fileName);
    dlgPushButton("Bro&wse") {
      fileName = dlgFileOpen("Select a file", fileName);
      }
    }//这段代买中，有一个横向空间可供操作，在该空间内的最左边显示"File &name:"字样，然后有一个字符串编辑窗口，可以手动设计超级文件路径，最右边是一个名为 Browes 的按钮，单击该按钮后，弹出打开文件窗口，可以选择需要打开的文件。
    dlgGridLayout {
    dlgCell(0, 0) dlgLabel("Row 0/Col 0");
    dlgCell(1, 0) dlgLabel("Row 1/Col 0");
    dlgCell(0, 1) dlgLabel("Row 0/Col 1");
    dlgCell(1, 1) dlgLabel("Row 1/Col 1");
    }//该段代码定义了一个网络布局空间，然后在该空间相对坐标(0,0)的地方显示"Row 0/Col 0",在相对坐标(1,0)的地方显示"Row 1/Col 0",在相对坐标(0,1)的地方显示"Row 0/Col 1",在相对坐标(1,1)的地方显示"Row 1/Col 1"。
    
  dlgSpacing(10);
  dlgHBoxLayout {
    dlgStretch(1);
    dlgPushButton("+OK")    dlgAccept();
    dlgPushButton("Cancel") dlgReject();
    }
  }; 
  最后，定义了一个横向的操作空间，该空间内有两个按钮，分别是 OK 和 Cancel。单击 OK 按钮调用 dlgAccpet 函数，关闭并保存所作的修改。但是 Cancel 按钮调用 dlgReject 函数，关闭对话框并忽略修改。
```

执行后，得到如下对话框
![Alt text](0x10_ULP(用户语言程序).assets/.1465175960613.png)
名字为"EAGLE : Enter Parameters" ，在标题的下面显示" This is a simple dialog" 。然后在 Horizontal 区域有 3 个单选按钮，分别为Top 、Center 和Bottom ; 在Vertical 区域有3 个单选按钮，分别为Left 、Center 和Right 。
在这两个区域的下面，是一个文件选择的空间，可以手动输入文件路径，也可以浏览需要打开的文件。随后在对话框内出现了按网格坐标显示的 4 个字符串。
在对话框的最后，有两个按钮，分别是 OK 和 Cancel ，提供相应的功能。

## 7. 常用 ULP 说明

### 7.1 Bom.ulp
使用 Bom. ulp 文件可以快速地导出原理图设计文件的元件清单，如图所示。
![Alt text](0x10_ULP(用户语言程序).assets/.1465176868945.png)

所有的元件，还包括了元件的一些属性，例如数量、封装、规格等。
~~在元件列表下面，有Load 和New 两个按钮。单击Load 可以为原件加入更多的属性，单击New 编辑新的元件属性。~~
在 List type 区域，可以选择列表的显示格式是以元件还是以元件的规格，
~~单击 Eidt 按钮，可以编辑选定元件的属性，~~
单击View 按钮可以在一个更大的对话框中预览元件清单，
单击 Save 按钮可以保存元件清单。
在Output format 区域可以选择文件输出的格式。

### 7.2 exp - project - Ibr. ulp
在原理图和 PCB 图中执行exp - project - lbr. ulp ，能将原理图和PCB 图中使用的所有元件库提取出来生成一个或者多个元件库供以后设计使用。
![Alt text](0x10_ULP(用户语言程序).assets/.1465177771069.png)
按照不同的需求选择输出一个还是多个元件库并修改文件输出路径后，单击 Collect data 按钮先收集原理图或者PCB 图的库，完成后再单击 Create library 按钮，即可生成需要的库
文件。

好像在新版本中改为 exp-lbrs.ulp。
![Alt text](0x10_ULP(用户语言程序).assets/.1465180005577.png)

### 7.3 Change prefix sch. ulp
在原理图中，会把元件分为很多个大类，比如U、IC 、R 、L 、C ，它们分别代表了不同种类的元件。
这样做的目的是为了在阅读原理图时可以很容易地判断元件的类别，而不是一定要去看元件的 part number 。
这样的符号在 EAGLE 里面称为元件的前缀(prefix)。
Change prefix sch 函数可以方便地修改元件的前缀。

在左边的输入栏输入想要修改的原前缀，在右边的对话框中输入新的前缀，单击 OK 按钮完成修改。这样的修改是全局性的，它不只针对某一个元件，对拥有相同前缀的元件都起作用。
![Alt text](0x10_ULP(用户语言程序).assets/.1465177914037.png)

### 7.4 Renumber sch. ulp
在绘制原理图时，有可能有频繁的删除和复制操作，这样可能会造成原理图的元件序号混乱，甚至出现缺失，从而会使最终的 PCB 难以焊接。

为了避免这样的情况，在完成了原理图后，需要重新对元件进行排序，使用 renumbcr sch 可以非常快速地完成重排序工作。
renumber sch 函数的运行界面如图10 . 9 所示，在窗口的上半部分， 是一些说明文本，提醒在进行重排序之前，要确定PCB 文件已经打开。
如果没有打开PCB 文件，进行了原理图重排序后， PCB 和原理图将不再同步。
在下面有两个选择区域，分别选择横向和纵向的排序方式，
在 X 区域，选择 Ascending 意味着从左到右的排序，选择D escending 则是从右到左的排序，在Y 区域，选择Ascending ，排序从下到上执行排序，选择Descending 从上到下执行排序。
![Alt text](0x10_ULP(用户语言程序).assets/.1465179225846.png)

该 ULP 好像有更新，新版本如下：
![Alt text](0x10_ULP(用户语言程序).assets/.1465179923712.png)
![Alt text](0x10_ULP(用户语言程序).assets/.1465179950556.png)

### 7.5 length. ulp
length. ulp 文件只能在 PCB 编辑环境当中使用，作用是计算某一个或者某几个信号的布线长度，还可以计算信号布线的长度差。
Length 可以用来计算差分信号的信号线是否等长。
直接运行 length. ulp ，会计算PCB 板所有信号的长度和差距，所以一般使用 run 命令来运行 length. ulp ，格式为run length name namel name2. . . 其中 name 为信号的名称。
比如在命令输入窗口输入: run length RA3 RA4 ，可以计算RA3 和RA4 的布线长度，以及两者的走向长度差。
![Alt text](0x10_ULP(用户语言程序).assets/.1465180299755.png)
对话框的第一列为信号名称，第二列为信号的布线长度，第三列为布线的长度差，第四列为该布线长度差占布线长度的比例。如果所计算的信号存在没有完成的鼠线，那么会显示在最后一列。

![Alt text](0x10_ULP(用户语言程序).assets/.1465180079055.png)
![Alt text](0x10_ULP(用户语言程序).assets/.1465180175018.png)

### 7.6 drillcfg. ulp
用作生成 PCB 钻孔工具列表，该列表会在 PCB 加工时使用，是 PCB 加工的必须文件之一。
执行后会弹出一个对话框，可选钻孔列表单位。
![Alt text](0x10_ULP(用户语言程序).assets/.1465180570982.png)
单击OK 按钮后，对话框会把相应 PCB 文件的钻孔列表显示出来。可以通过该对话框修改钻孔列表，但是除非有十足的把握，否则不要修改列表里的任何内容。
![Alt text](0x10_ULP(用户语言程序).assets/.1465180593109.png)

### 7.7 Import-bmp.ulp
![Alt text](0x10_ULP(用户语言程序).assets/.1465180688811.png)
Import bmp. ulp 可以在PCB 文件中导人位图文件，在设计PCB 时，可能需要加入一些符号或图表，例如公司 logo 或者电气警告符号，但这些符号大多比较复杂，用手工绘制比较浪费时间，且效果不佳。

这时使用 EAGLE 自带的import bmp 文件可以很方便地导人位图文件。
执行 import bmp. ulp 后，会弹出一个说明对话框，在里面描述了EAGLE 支持的位图规格，该部分需要仔细阅读，单击OK 按钮进入下一步，弹出文件选择对话框，选择所需要导人的位图文件，选择后单击OK 按钮，进入颜色选择界面，选择文件需要显示的颜色，选择完成后，单击OK 按钮，进入最后一步设置。
![Alt text](0x10_ULP(用户语言程序).assets/.1465181190938.png)

file data 显示出了文件的像素，
右边的 format 对话框可以设置导人后的格式，分别有 DPI、scaled 和 Aspect/Ratio m 三种格式。
在 format 下面是单位界面，可以选择 inch 、mil 、mm 和 Micron 4 个单位。
界面的下半部分有两个文本输入框，上面的文本输入框可以设置导人图片与原图片的比例，
 下面的文本输入框可以选择放置位图第一个颜色的开始层。单击 ok 按钮，完成导如工作。
![Alt text](0x10_ULP(用户语言程序).assets/.1465182947590.png)

### 7.8 find.ulp
使用find . ulp 可以搜索到当前编辑窗口中的有关信息，包括pin 、pad 、device 、gate 和 value 等都可以被搜索
![Alt text](0x10_ULP(用户语言程序).assets/.1465183084896.png)
name 一栏处输出想要搜索的信息，
在find options 一栏，可以选择想要搜索的信息是属于哪一个类别的，可以为引脚、焊盘、device 、gat e 和数值。
当搜索的类别是数值时，勾选 change to 复选框，并在value 一栏中填入新的数值，可以在搜索的同时把数值替换为新的数值。



本节介绍了一些常用的ULP 文件，但没有介绍的占大多数。
EAGLE 自带的 ulp 文件保存在EAGLE 安装目录下的ULP 文件夹下。
除了自带的ULP 文件，在EAGLE 的官方网站上，还提供了更多的ULP 文件供下载，进入EAGLE 的官方网站: http://www.cadsoftusa.com/downloads/ ，单击页面左边的Download 链接，再单击新页面中的 ULPs 链接，就可以下
载更多的ULP 文件。