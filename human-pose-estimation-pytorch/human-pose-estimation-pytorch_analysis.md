# Human Pose Estimation (PyTorch) — 深度源码分析

> **项目**: [microsoft/human-pose-estimation.pytorch](https://github.com/microsoft/human-pose-estimation.pytorch) | ⭐ 3,005 | MIT License | 已归档
> **论文**: ECCV2018 — *Simple Baselines for Human Pose Estimation and Tracking*
> **语言**: Python 97.5k行, CUDA 5,062行, Cython 3,484行, C++ 146行

## 核心成果
- **COCO val2017 AP**: 0.743 (ResNet-152, 384×288)
- **MPII PCKh**: 90.2%
- **COCO 2018 Keypoint Detection**: 第2名
- **PoseTrack2018 Multi-Person Pose Tracking**: 冠军

## 架构设计：极简即 SOTA

### ResNet Backbone + 3层反卷积（核心创新）
```
Input Image → ResNet (无修改) → [256×H/4×W/4] → Deconv(256,k4,s2,p1) × 3 → [17×H×W] Heatmaps
```
- 整个姿态估计头只有3个反卷积层（配置驱动 `d256d256d256`）
- Caffe-style Bottleneck（stride 放 conv1）比 PyTorch-style（stride 放 conv2）在 COCO 上 AP 更高
- 支持 ResNet-{18,34,50,101,152}，通过 `resnet_spec` 字典驱动

### 模型关键组件
- **PoseResNet**: BasicBlock/Bottleneck/Bottleneck_CAFFE 三种块；init_weights 从 ImageNet 预训练加载（处理 DataParallel `module.` 前缀）
- **3层反卷积头**: `nn.ConvTranspose2d(256, 256, 4, 2, 1, bias=False)` + BN + ReLU，逐层 2× 上采样

## 训练与推理

### 训练循环 (function.py)
- DataParallel 多 GPU 训练
- 验证时 **Flip Test** + **shift_heatmap**（翻转输出偏移1像素对齐）
- TensorBoard 日志记录

### 损失函数 (loss.py)
- **JointsMSELoss**: 逐关节 MSE，`target_weight` 掩码忽略不可见关节
- 归一化: `0.5 * crit / norm`

### 后处理 (inference.py)
1. `get_max_preds`: argmax 获取粗定位
2. **泰勒展开**: `sign(diff) * 0.25` 亚像素精度修正
3. `transform_preds`: 仿射变换回原图坐标

## 数据处理

### COCO 数据集 (coco.py)
- 17 个关键点，8 对 flip pairs
- `_xywh2cs`: 保持宽高比的仿射变换中心+尺度计算
- **OKS-NMS**: 17 个关节 sigma 归一化

### 仿射变换 (transforms.py)
- `get_affine_transform`: 3 点仿射（src→dst 三角对应）
- `flip_back`: 翻转热图 + 交换对称关节
- `fliplr_joints`: 水平翻转关节坐标

## NMS 实现（CUDA 加速）

### OKS-NMS (nms.py)
- 贪心算法，17 个关节各有 sigma 归一化
- `oks_iou`: 基于关键点距离的 IoU，是姿态估计标准评估指标
- CPU/GPU 双实现包装

### CUDA NMS 内核
- **gpu_nms.pyx**: Cython 封装 `_nms` C++ CUDA 内核（源自 py-faster-rcnn）
- **cpu_nms.pyx**: Cython 加速 CPU NMS，suppressed 数组
- **gpu_nms.hpp**: `void _nms(int*, int*, const float*, int, int, float, int)`

## 环境与配置
- Python 3.6, PyTorch ≥0.4.0
- 需禁用 `cudnn.benchmark` + `cudnn.deterministic`
- 4× P100 GPU, Adam + MultiStepLR
- experiments/ 目录含 COCO/MPII 完整 YAML 配置

## 历史地位
- 证明了**极简架构**（ResNet + 反卷积）即可达到 SOTA，后续 HRNet 等复杂架构在此基础上继续提升
- HRNet 系列: COCO AP 77.0, MPII PCKh@0.5 92.3%
- OKS 指标和泰勒展开后处理成为姿态估计领域的标准实践
