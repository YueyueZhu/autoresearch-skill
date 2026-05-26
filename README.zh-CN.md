# Autoresearch Skill 中文说明

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9b/Mao_Tse_Tung.jpg" alt="毛泽东主席照片" width="260">
</p>

<h2 align="center">世界是你们滴</h2>

<p align="center">
  图片来源：<a href="https://commons.wikimedia.org/wiki/File:Mao_Tse_Tung.jpg">Wikimedia Commons, Mao Tse Tung.jpg</a>。
</p>

`autoresearch` 是一个面向深度学习实验自动化的 Codex skill。

它会在你的项目运行目录中创建并维护 `AUTORESEARCH.md`，把任务目标、运行命令、日志、指标、允许修改范围、每次实验的假设和结果全部记录下来。这样即使网络中断、Codex 重启，也可以从这个文件恢复。

## 功能

- 启动时询问工作目录、任务、指标、运行命令、GPU、tmux、允许修改的代码范围。
- 创建持久化的 `AUTORESEARCH.md`。
- 当用户提供论文、方法或 GitHub 仓库时，优先查看官方 GitHub 实现。
- 每个实验 idea 都要求写明新颖性，目标是达到 NeurIPS、ICLR、CVPR、AAAI 等顶级会议级别的研究标准。
- 只修改用户允许的文件或代码区域。
- 默认使用 tmux 运行长时间训练。
- 从日志中解析最新指标和最佳指标。
- 将实验标记为 `keep`、`discard`、`crash` 或 `running`。
- 记录每次实验的假设、代码修改、结果和决策。

## 典型使用方式

```text
使用 autoresearch skill 处理这个深度学习项目。
工作目录：/path/to/project
任务：提升验证集 Dice。
指标：mdice，越高越好。
当前最好结果：0.824。
运行命令：sh train.sh。
使用 tmux session 0。
允许修改范围：只修改 loss.py 里的 consistency_loss()。
可用 GPU：0,1。
```

## 中断恢复

如果网络中断或 Codex 重启，使用：

```text
读取 /path/to/project/AUTORESEARCH.md，继续自动化 autoresearch 任务。
```

## 文件说明

- `SKILL.md`：Codex 使用的 skill 主说明。
- `references/AUTORESEARCH_TEMPLATE.md`：完整 `AUTORESEARCH.md` 模板。
- `references/INTERVIEW_QUESTIONS.md`：启动时必须询问的问题。
- `references/ITERATION_PROTOCOL.md`：每轮实验迭代协议。
- `references/LOG_PARSING_GUIDE.md`：日志和指标解析指南。
- `scripts/init_autoresearch.py`：可选脚本，用于生成初始 `AUTORESEARCH.md`。
- `scripts/append_experiment.py`：可选脚本，用于追加实验记录。

## 适用范围

适用于任意深度学习工作流，例如医学图像分割、分类、检测、语言建模、半监督学习、自监督学习等。

它不是只能用于原始的 `karpathy/autoresearch` 仓库，而是把 autoresearch 思想泛化到本地任意项目。
