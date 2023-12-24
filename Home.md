---
bibliography: papers.bib
csl: 'chinese-gb7714-2005-numeric.csl'
fignos-cleveref: True
fignos-plus-name: 图
fignos-caption-name: 图
---

### 如何写论文

根据**“广大科研工作者应该将论文写在大地上”**的号召。

* 论文可发表于网络
* 论文发表于期刊

#### 论文常用到的形式：

##### (一)文章评注标记critic-markup：

Don’t go around saying{-- to people that --} the world owes you a living. The
world owes you nothing. It was here first. {~~One~>Only one~~} thing is
impossible for God: To find {++any++} sense in any copyright law on the
planet. {==Truth is stranger than fiction==}{>>true<<}, but it is because
Fiction is obliged to stick to possibilities; Truth isn’t.


##### （二）文章交叉引用Biblatex citation:

学术大咖陈见着[^1]

[^1]: 文章作者： 陈见着 ORCID -XX.XXXXX.XX

爱因斯坦的理论研究[@einstein1950meaning]

智能车结构制作设计入门[@臧海波2016机器人制作入门]

如何用markdown写论文[@YuShuZhiLan]

esp32引脚如{@fig:esp32}所示

![esp32引脚](esp-32x.png){#fig:esp32 height=150px}

![大数据海报](Big-Data.jpg){#fig:bigdata height=150px}

大数据海报如{@fig:bigdata}所示

##### （三）PlantUML图表：
<!--```{.plantuml caption="This is an image, created by **PlantUML**." width=50%}-->
@startmindmap
* Debian
** Ubuntu
*** Linux Mint
*** Kubuntu
*** Lubuntu
*** KDE Neon
** LMDE
** SolydXK
** SteamOS
** Raspbian with a very long name
*** <s>Raspmbc</s> => OSMC
*** <s>Raspyfi</s> => Volumio
@endmindmap
<!--```-->

 <!-- ```{.py2image caption="This is an image, created by **Python**."}  -->
<!--  import matplotlib
matplotlib.use('Agg')

import sys
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

fig.tight_layout()
plt.savefig("$DESTINATION$", dpi=300, format="png")  -->
<!-- ```  -->

[[/image/plot.png|height=450px]] 

##### （四）数学公式：
$a+b$ # Recommended syntax!

$$2^2$$ # Recommended syntax!

$\frac{(x+y)}{[\alpha+\beta]}$

$\begin{matrix} 1&x&x^2\\\\ 1&y&y^2\\\\ 1&z&z^2 \end{matrix}$

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

#### 论文发表场合：
* 网络(wiki) ：markdown gollum[@zotero-26]
```
gollum -c config.rb
```

* 期刊： markdown 、pandoc[@zotero-25]
```
pancritic Home.md -t markdown -m m | pandoc -F pandoc-fignos -C --bibliography=papers.bib --csl=chinese-gb7714-2005-numeric.csl -s --metadata title="假论文"  -o output.docx
```

##### 相关插件介绍 [@zotero-23]：
* pandoc-fignos [@zotero-29]
* pancritic [@zotero-27]
* lua-filters [@zotero-31]
```
pandoc Home.md -f markdown -t docx --self-contained --standalone --lua-filter=diagram-generator.lua --metadata=plantumlPath:"plantuml.jar" --metadata=javaPath:"java" -o README.docx

```

```
pancritic Home.md -t markdown -m m | pandoc -f markdown -t docx --self-contained --standalone -F pandoc-fignos -C --bibliography=papers.bib --csl=chinese-gb7714-2005-numeric.csl -s --metadata title="假论文"  --lua-filter=diagram-generator.lua --metadata=plantumlPath:"plantuml.jar" --metadata=javaPath:"java" --metadata=pythonPath:"/usr/bin/python3" -o README.docx

```

```
pandoc -s -o test.docx --resource-path=.:image README.html
```

# Refercnce

::: {#przibram1967letters}
:::
