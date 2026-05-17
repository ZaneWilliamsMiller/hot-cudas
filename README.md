# 🔥 Hot CUDAs — CUDA/GPU 开源项目知识库

> 自动整理 2026-05-17 | 39 个热门项目 | 深度源码分析 · Git Submodules · 持续更新

## 📦 使用方式

```bash
# 克隆含所有子模块
git clone --recurse-submodules https://github.com/ZaneWilliamsMiller/hot_cudas.git

# 已克隆后初始化子模块
git submodule update --init --recursive

# 更新所有子模块到最新
git submodule update --remote
```

## 🍴 Submodule 索引

| # | 项目 | ⭐ | 子模块目录 | 上游仓库 |
|---|------|-----:|:----------:|---------|
| 1 | **PyTorch** | 100k | `pytorch/` | [pytorch/pytorch](https://github.com/pytorch/pytorch) |
| 2 | **vLLM** | 80k | `vllm/` | [vllm-project/vllm](https://github.com/vllm-project/vllm) |
| 3 | **DeepSpeed** | 42k | `deepspeed/` | [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) |
| 4 | **llm.c** | 30k | `llm-c/` | [karpathy/llm.c](https://github.com/karpathy/llm.c) |
| 5 | **SGLang** | 28k | `sglang/` | [sgl-project/sglang](https://github.com/sgl-project/sglang) |
| 6 | **FlashAttention** | 24k | `flash-attention/` | [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) |
| 7 | **Instant-NGP** | 17k | `instant-ngp/` | [NVlabs/instant-ngp](https://github.com/NVlabs/instant-ngp) |
| 8 | **Megatron-LM** | 16k | `megatron-lm/` | [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM) |
| 9 | **DeepLearningExamples** | 15k | `deep-learning-examples/` | [NVIDIA/DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) |
| 10 | **Horovod** | 15k | `horovod/` | [horovod/horovod](https://github.com/horovod/horovod) |
| 11 | **Deeplearning4J** | 14k | `deeplearning4j/` | [deeplearning4j/deeplearning4j](https://github.com/deeplearning4j/deeplearning4j) |
| 12 | **ZLUDA** | 14k | `zluda/` | [vosen/ZLUDA](https://github.com/vosen/ZLUDA) |
| 13 | **TensorRT-LLM** | 14k | `tensorrt-llm/` | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| 14 | **Open3D** | 14k | `open3d/` | [isl-org/Open3D](https://github.com/isl-org/Open3D) |
| 15 | **TVM** | 13k | `tvm/` | [apache/tvm](https://github.com/apache/tvm) |
| 16 | **TensorRT** | 13k | `tensorrt/` | [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT) |
| 17 | **GPU-Puzzles** | 12k | `gpu-puzzles/` | [srush/GPU-Puzzles](https://github.com/srush/GPU-Puzzles) |
| 18 | **Taskflow** | 12k | `taskflow/` | [taskflow/taskflow](https://github.com/taskflow/taskflow) |
| 19 | **HVM2** | 11k | `hvm2/` | [HigherOrderCO/HVM2](https://github.com/HigherOrderCO/HVM2) |
| 20 | **CuPy** | 11k | `cupy/` | [cupy/cupy](https://github.com/cupy/cupy) |
| 21 | **LeetCUDA** | 11k | `leetcuda/` | [xlite-dev/LeetCUDA](https://github.com/xlite-dev/LeetCUDA) |
| 22 | **cuDF** | 10k | `cudf/` | [rapidsai/cudf](https://github.com/rapidsai/cudf) |
| 23 | **CUTLASS** | 10k | `cutlass/` | [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass) |
| 24 | **DeepEP** | 10k | `deepep/` | [deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) |
| # | **LMDeploy** | 7.9k | lmdeploy/lmdeploy | [GitHub](https://github.com/InternLM/lmdeploy) |
| 25 | **Apex** | 9k | `apex/` | [NVIDIA/apex](https://github.com/NVIDIA/apex) |
| 26 | **cuda-samples** | 9k | `cuda-samples/` | [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples) |
| 27 | **OneFlow** | 9k | `oneflow/` | [Oneflow-Inc/oneflow](https://github.com/Oneflow-Inc/oneflow) |
| 28 | **LMCache** | 8k | `lmcache/` | [LMCache/LMCache](https://github.com/LMCache/LMCache) |
| 29 | **vid2vid** | 9k | `vid2vid/` | [NVIDIA/vid2vid](https://github.com/NVIDIA/vid2vid) |
| 30 | **jetson-inference** | 9k | `jetson-inference/` | [dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference) |
| 31 | **tensorrtx** | 8k | `tensorrtx/` | [wang-xinyu/tensorrtx](https://github.com/wang-xinyu/tensorrtx) |
| 32 | **DeepGEMM** | 7k | `deepgemm/` | [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) |
| 33 | **Warp** | 7k | `warp/` | [NVIDIA/warp](https://github.com/NVIDIA/warp) |
| 34 | **FasterTransformer** | 6k | `faster-transformer/` | [NVIDIA/FasterTransformer](https://github.com/NVIDIA/FasterTransformer) |
| 35 | **TileLang** | 6k | `tilelang/` | [tile-ai/tilelang](https://github.com/tile-ai/tilelang) |
| 36 | **Chitu** | 3k | `chitu/` | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) |
| 37 | **RTP-LLM** | 1k | `rtp-llm/` | [alibaba/rtp-llm](https://github.com/alibaba/rtp-llm) |
| 38 | **RAFT** | 1k | `raft/` | [rapidsai/raft](https://github.com/rapidsai/raft) |
| 39 | **UCC** | 307 | `ucc/` | [openucx/ucc](https://github.com/openucx/ucc) |

---

## 🗂️ 按领域分类

### 🔧 GPU 内核 & 算子
CUTLASS · FlashAttention · GPU-Puzzles · Taskflow · HVM2 · CuPy · OneFlow · DeepEP · cuda-samples · LeetCUDA · RAFT

### 🚀 推理引擎
vLLM · SGLang · RTP-LLM · Chitu · DeepGEMM · FasterTransformer · TensorRT-LLM · TensorRT

### 💾 缓存 & 存储
LMCache

### 📡 通信
UCC

### 🏋️ 分布式训练
DeepSpeed · Megatron-LM · Apex · llm.c · Horovod

### 🔬 编译 & 模拟
TileLang · Warp · TVM

### 🧠 深度学习框架
PyTorch · Deeplearning4J

### 🎨 神经图形学 & 3D
Instant-NGP · Open3D

### 📚 参考实现
DeepLearningExamples

### 🔀 GPU 兼容层
ZLUDA

---

## 🔗 项目关系

```
训练栈:    llm.c ─── Apex ─── DeepSpeed / Megatron-LM
               │         │     └── Horovod (Ring-AllReduce)
               └──── 内核层: CUTLASS + FlashAttention
                              │
推理栈:    FasterTransformer ──→ TensorRT ──→ TensorRT-LLM ── vLLM/SGLang
               ↓
          vLLM ←──→ SGLang ←── RTP-LLM ←── Chitu (国产GPU推理)
               │         │
缓存层:    LMCache (KV Cache 跨层共享)
               │
通信层:    UCC (统一 NCCL/UCP/SHARP) + DeepEP (MoE EP)
               │
基础库:    RAFT ─── RAPIDS 底层 (cuML/cuGraph/cuVS 公共原语)
框架层:    PyTorch (Dynamo/Inductor/FSDP/DTensor/Export)
           DL4J (JVM 深度学习全栈/SameDiff/ND4J)
编译层:    TileLang ─── TVM ─── CuTeDSL (CUTLASS)
图形层:    Instant-NGP (NeRF/SDF/Hash Encoding) + Open3D (3D全栈)
兼容层:    ZLUDA (CUDA→AMD GPU)
编排层:    Taskflow (DAG调度/CUDA Graph/Pipeline)
计算层:    HVM2 (Interaction Combinators GPU并行)
数值层:    CuPy (NumPy/SciPy GPU)
模拟层:    Warp (独立)
教学:     GPU-Puzzles (入门) ──→ LeetCUDA (实战) ──→ cuda-samples (官方)
参考:     DeepLearningExamples (50+ SOTA模型)
```

---

## 📈 项目演进时序

```
2015 ── Deeplearning4J (JVM深度学习)
2017 ── TVM (ML编译器, Apache孵化)
2018 ── Horovod, FasterTransformer, DeepLearningExamples, Open3D, Taskflow
2019 ── Apex (AMP 混合精度)
2020 ── DeepSpeed (ZeRO), Megatron-LM (TP/PP), ZLUDA (CUDA兼容层)
2021 ── CUTLASS 2.x (Ampere), UCC (统一通信)
2022 ── FlashAttention FA1/FA2, vLLM, Instant-NGP, GPU-Puzzles, HVM2
2023 ── SGLang, RTP-LLM
2024 ── CUTLASS 4.x, FA3, LeetCUDA, DeepEP, DeepGEMM
2025 ── FA4, llm.c, TileLang, LMCache dev, Chitu
2026 ── cuDF v26.06, PyTorch v2.13, TVM v0.25, TensorRT 10.16/11.0
```

