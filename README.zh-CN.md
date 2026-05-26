# Autoresearch Skill 中文说明

<p align="center">
  <img src="./picture.gif@480w_480h.webp" alt="耄耋梗猫照片" width="280">
</p>

<h2 align="center">哈基米爱科研</h2>


`autoresearch` 是一个面向深度学习实验自动化的 Codex skill。

它适合处理那种一次实验要跑很久、网络可能中断、实验过程又必须严格记录的研究任务。它会在你的项目运行目录里创建并维护一个 `AUTORESEARCH.md` 文件，把“任务是什么、允许改哪里、运行什么命令、指标是多少、这次为什么这么改、结果好不好、要不要保留”全部记录下来。

一句话概括：

> `AUTORESEARCH.md` 是自动化科研循环的持久记忆。断网后也靠它恢复。

## 适用场景

你可以在这些深度学习任务中使用它：

- 提升医学图像分割的 Dice / IoU
- 提升分类任务的 Accuracy / F1 / AUC
- 降低验证集 loss 或 perplexity
- 重新设计 loss function
- 改进半监督、弱监督、自监督训练策略
- 把论文或 GitHub 仓库里的方法迁移到自己的代码里
- 使用 tmux 跑 4 到 7 小时甚至更久的实验
- 中断之后继续自动化迭代

它不绑定具体框架，可以用于 PyTorch、MONAI、TensorFlow、JAX、Lightning、自定义 trainer、Python 脚本或 shell 脚本。

## 它会做什么

调用后，这个 skill 会引导 Codex：

1. 询问深度学习项目运行目录。
2. 询问任务目标、主指标、当前最好结果和目标结果。
3. 询问每轮迭代前是否需要加入论文或 GitHub 仓库作为参考。
4. 如果用户提供论文或方法，优先寻找官方 GitHub 实现。
5. 询问具体运行哪个 Python 文件、shell 脚本或命令。
6. 如果有多个运行命令，询问是否生成统一 `.sh` 脚本。
7. 询问是否使用复用终端，默认使用 tmux。
8. 询问具体允许修改哪些文件、函数、loss、模块或代码区域。
9. 询问当前可用 GPU 编号。
10. 创建或更新 `AUTORESEARCH.md`。
11. 每次只提出一个主要实验 idea。
12. 要求每个 idea 写明新颖性，目标达到 NeurIPS、ICLR、CVPR、AAAI 等顶会级别的研究标准。
13. 只修改用户允许的代码范围。
14. 启动训练、检查日志、解析指标、记录结果。
15. 将实验标记为 `keep`、`discard`、`crash` 或 `running`。

## 为什么需要 AUTORESEARCH.md

深度学习实验很容易乱：

- 一次实验可能跑几个小时。
- 日志会不断追加，容易分不清是哪次实验。
- 网络中断后，聊天上下文可能丢失。
- 如果不记录失败原因，坏 idea 可能被重复尝试。
- 如果不记录改动范围，可能误改到不该动的代码。

`AUTORESEARCH.md` 用来记录：

- 项目目录
- 任务目标
- 主指标和方向
- 当前最好结果
- 目标结果
- 运行命令
- tmux session
- 日志文件
- 可用 GPU
- 允许修改范围
- 禁止修改范围
- 已经读取的文件
- 当前关键代码路径
- 每轮实验假设
- 顶会级新颖性说明
- 参考论文或官方 GitHub
- 具体代码改动
- 启动时间
- 最佳指标和最新指标
- keep / discard / crash 决策

如果断网或 Codex 重启，直接用这句话恢复：

```text
读取 /path/to/project/AUTORESEARCH.md，继续自动化 autoresearch 任务。
```

## 对 idea 的要求

这个 skill 不鼓励无意义地乱调参数。

每个实验 idea 都应该有一个清楚的机制和新颖性说明，目标是达到 NeurIPS、ICLR、CVPR、AAAI 等顶级会议级别的研究标准。它不一定要改很多代码，但必须能说明：

- 为什么这个想法不是普通调参？
- 它解决了什么机制问题？
- 它为什么可能泛化？
- 它如何被一次实验验证？
- 如果失败，能说明什么？

比较合适的方向包括：

- 不确定性感知一致性学习
- 动态 curriculum
- teacher-student disagreement 建模
- 边界感知或拓扑感知 loss
- 类别不平衡下的伪标签过滤
- 表征对齐的 contrastive objective
- 弱监督中的置信度校准
- noisy label 或 mixed sample 下的鲁棒训练

小改动也可以做，但必须服务于一个更大的研究机制。

## 仓库结构

```text
autoresearch-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── references/
│   ├── AUTORESEARCH_TEMPLATE.md
│   ├── INTERVIEW_QUESTIONS.md
│   ├── ITERATION_PROTOCOL.md
│   └── LOG_PARSING_GUIDE.md
└── scripts/
    ├── init_autoresearch.py
    └── append_experiment.py
```

## 文件说明

- `SKILL.md`：Codex 使用的 skill 主说明。
- `references/AUTORESEARCH_TEMPLATE.md`：完整的 `AUTORESEARCH.md` 模板。
- `references/INTERVIEW_QUESTIONS.md`：启动时必须询问的问题。
- `references/ITERATION_PROTOCOL.md`：每轮实验的 keep / discard 协议。
- `references/LOG_PARSING_GUIDE.md`：常见指标和日志解析方式。
- `scripts/init_autoresearch.py`：生成初始 `AUTORESEARCH.md` 的辅助脚本。
- `scripts/append_experiment.py`：追加实验记录的辅助脚本。

## Prompt 模板

开始新项目时，可以复制下面的模板：

```text
使用 autoresearch skill 处理这个深度学习项目。

工作目录：
/absolute/path/to/my/project

任务：
提升 <指标或具体效果>。实验 idea 要尽量达到 NeurIPS、ICLR、CVPR、AAAI 等顶会级别的新颖性标准。如果我提供论文或方法，请优先查找官方 GitHub 实现，再把相关思想迁移到当前允许修改的代码范围内。

指标：
主指标是 <metric_name>，越 <高/低> 越好。
当前最好结果是 <current_best>。
目标结果是 <target_result>。

运行命令：
<python train.py ... 或 sh train.sh>

日志文件：
/absolute/path/to/log.txt

复用终端：
默认使用 tmux，tmux session 是 <session_name_or_id>。

GPU：
当前可用 GPU 编号是 <gpu_ids>。

允许修改范围：
只允许修改 <file/function/loss/module/code region>。

禁止修改：
不要修改 <dataset/evaluation metric/model/shell args/optimizer/etc.>。

自动化要求：
在改代码前，先在工作目录创建 AUTORESEARCH.md。把上下文、假设、代码修改、日志、指标、keep/discard 决策全部记录进去。如果中断，之后通过读取 AUTORESEARCH.md 恢复。
```

## 最小使用例子

```text
使用 autoresearch skill。
工作目录：/home/user/projects/segmentation-exp
任务：提升验证集 mdice。当前最好结果是 0.824，目标超过 0.83。
指标：mdice，越高越好。
运行命令：sh train.sh。
日志文件：/home/user/projects/segmentation-exp/train.log。
使用 tmux session 0。
可用 GPU：0,1。
只允许修改 losses.py 里的 consistency_loss()。
每轮迭代前问我是否要加入新的论文或 GitHub 仓库参考。
```

## 安装方式

把这个目录复制到 Codex skills 目录：

```bash
cp -a autoresearch-skill ~/.codex/skills/autoresearch
```

之后在 Codex 请求中提到 `autoresearch` 即可触发。

## 说明

这个仓库打包的是一个本地 Codex skill。它的工作流受 `karpathy/autoresearch` 启发，但已经泛化为适合任意深度学习项目的自动化科研流程。
