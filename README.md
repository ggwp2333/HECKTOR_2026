# HECKTOR 2026 · nnU-Net 训练流程（Shiman 分支）

这个分支是 Shiman 负责的部分：在 Google Colab 上，用 nnU-Net v2 对 HECKTOR 2026 的 PET/CT 数据做头颈部肿瘤分割（原发肿瘤 GTVp 和淋巴结 GTVn）的完整训练流程。

## 文件

| 文件 | 内容 |
| --- | --- |
| `HECKTOR_nnUNet_train.ipynb` | 从数据准备到训练、看结果的完整 notebook，每一步都有中文说明 |

## 流程概览

1. **安装 nnU-Net**（`nnunetv2`），检查 GPU。
2. **挂载 Google Drive**，设置 `nnUNet_raw` / `nnUNet_preprocessed` / `nnUNet_results` 三个路径。原始数据只读；训练结果存在 Drive 上，断线不丢。
3. **选病人**：在有完整 CT、PET、标签的病人里，排除层数超过 350 的大扫描（免费 Colab 内存不够），用固定随机种子抽 50 个。
4. **整理成 nnU-Net 格式**：CT 为通道 `_0000`，PET 为通道 `_0001`。
5. **写 `dataset.json`**：标签 0 = 背景，1 = GTVp，2 = GTVn。
6. **规划 + 预处理**：`nnUNetv2_plan_and_preprocess --no_pp` 只做规划；预处理改成逐个病人进行、可断点续跑，避免 Colab 内存溢出。
7. **训练**：`3d_fullres` 配置，`nnUNetTrainer_50epochs`，第 0 折（40 个训练 / 10 个验证）。支持 `--c` 断线续训。
8. **看结果**：训练曲线 `progress.png` 和验证集上 GTVp、GTVn 的 Dice。

## 怎么跑

在 Colab 里打开 notebook，运行时选 GPU（T4 即可，T4 上 50 个 epoch 大约 5–6 小时），然后从上到下逐格运行。需要先把共享的 `HECKTOR_2026` 文件夹添加快捷方式到「我的云端硬盘」。

如果用内存更大的机器跑，可以把 `MAX_SLICES` 调大或去掉，第 6 步也可以直接用 `nnUNetv2_plan_and_preprocess` 一次完成预处理。

## 数据

HECKTOR 2026 数据需要向挑战赛官方申请，**本仓库不包含任何影像数据**。

## 已知局限

- 只训了 1 折、50 个 epoch、50 个病人，结果是初步的。
- 排除大扫描后，抽到的病人大部分来自 MDA，医院分布不均衡。
