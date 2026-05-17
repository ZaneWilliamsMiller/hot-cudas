# 🔥 Hot CUDAs — CUDA/GPU 开源项目知识库

> 自动整理 2026-05-18 | 41 个热门项目 | 深度源码分析 · Git Submodules · 持续更新

## 📦 使用方式

```bash
# 克隆含所有子模块（锁定版本）
git clone --recurse-submodules https://github.com/ZaneWilliamsMiller/hot_cudas.git

# 克隆最新版本（dev 分支每日同步上游）
git clone --recurse-submodules -b dev https://github.com/ZaneWilliamsMiller/hot_cudas.git

# 已克隆后初始化子模块
git submodule update --init --recursive

# 更新所有子模块到最新
git submodule update --remote
```

## 🍴 Submodule 索引

| # | **项目** | ⭐ | 目录 | 链接 |
|---|---------|-----|------|------|
| 1 | **PyTorch** | 100k | `pytorch/pytorch` | [PyTorch](https://github.com/pytorch/pytorch) |
| 2 | **vLLM** | 80k | `vllm/vllm` | [vLLM](https://github.com/vllm-project/vllm) |
| 3 | **DeepSpeed** | 42k | `deepspeed/deepspeed` | [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) |
| 4 | **llm.c** | 30k | `llm-c/llm.c` | [llm.c](https://github.com/karpathy/llm.c) |
| 5 | **SGLang** | 28k | `sglang/sglang` | [SGLang](https://github.com/sgl-project/sglang) |
| 6 | **FlashAttention** | 24k | `flash-attention/flash-attention` | [FlashAttention](https://github.com/Dao-AILab/flash-attention) |
| 7 | **Instant-NGP** | 17k | `instant-ngp/instant-ngp` | [Instant-NGP](https://github.com/NVlabs/instant-ngp) |
| 8 | **Megatron-LM** | 16k | `megatron-lm/Megatron-LM` | [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) |
| 9 | **DeepLearningExamples** | 15k | `deep-learning-examples/DeepLearningExamples` | [DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) |
| 10 | **Horovod** | 15k | `horovod/horovod` | [Horovod](https://github.com/horovod/horovod) |
| 11 | **Deeplearning4J** | 14k | `deeplearning4j/deeplearning4j` | [Deeplearning4J](https://github.com/deeplearning4j/deeplearning4j) |
| 12 | **ZLUDA** | 14k | `zluda/ZLUDA` | [ZLUDA](https://github.com/vosen/ZLUDA) |
| 13 | **TensorRT-LLM** | 14k | `tensorrt-llm/TensorRT-LLM` | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| 14 | **Open3D** | 14k | `open3d/Open3D` | [Open3D](https://github.com/isl-org/Open3D) |
| 15 | **TVM** | 13k | `tvm/tvm` | [TVM](https://github.com/apache/tvm) |
| 16 | **TensorRT** | 13k | `tensorrt/TensorRT` | [TensorRT](https://github.com/NVIDIA/TensorRT) |
| 17 | **GPU-Puzzles** | 12k | `gpu-puzzles/GPU-Puzzles` | [GPU-Puzzles](https://github.com/srush/GPU-Puzzles) |
| 18 | **Taskflow** | 12k | `taskflow/taskflow` | [Taskflow](https://github.com/taskflow/taskflow) |
| 19 | **HVM2** | 11k | `hvm2/HVM2` | [HVM2](https://github.com/HigherOrderCO/HVM2) |
| 20 | **LeetCUDA** | 11k | `leetcuda/LeetCUDA` | [LeetCUDA](https://github.com/xlite-dev/LeetCUDA) |
| 21 | **CuPy** | 11k | `cupy/cupy` | [CuPy](https://github.com/cupy/cupy) |
| 22 | **cuDF** | 10k | `cudf/cudf` | [cuDF](https://github.com/rapidsai/cudf) |
| 23 | **CUTLASS** | 10k | `cutlass/cutlass` | [CUTLASS](https://github.com/NVIDIA/cutlass) |
| 24 | **DeepEP** | 10k | `deepep/DeepEP` | [DeepEP](https://github.com/deepseek-ai/DeepEP) |
| 25 | **Apex** | 9k | `apex/apex` | [Apex](https://github.com/NVIDIA/apex) |
| 26 | **cuda-samples** | 9k | `cuda-samples/cuda-samples` | [cuda-samples](https://github.com/NVIDIA/cuda-samples) |
| 27 | **OneFlow** | 9k | `oneflow/oneflow` | [OneFlow](https://github.com/Oneflow-Inc/oneflow) |
| 28 | **vid2vid** | 9k | `vid2vid/vid2vid` | [vid2vid](https://github.com/NVIDIA/vid2vid) |
| 29 | **jetson-inference** | 9k | `jetson-inference/jetson-inference` | [jetson-inference](https://github.com/dusty-nv/jetson-inference) |
| 30 | **LMCache** | 8k | `lmcache/lmcache` | [LMCache](https://github.com/LMCache/LMCache) |
| 31 | **tensorrtx** | 8k | `tensorrtx/tensorrtx` | [tensorrtx](https://github.com/wang-xinyu/tensorrtx) |
| 32 | **LMDeploy** | 8k | `lmdeploy/lmdeploy` | [LMDeploy](https://github.com/InternLM/lmdeploy) |
| 33 | **GPT-NeoX** | 7k | `gpt-neox/gpt-neox` | [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) |
| 34 | **DeepGEMM** | 7k | `deepgemm/deepgemm` | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) |
| 35 | **Warp** | 7k | `warp/warp` | [Warp](https://github.com/NVIDIA/warp) |
| 36 | **FasterTransformer** | 6k | `faster-transformer/faster-transformer` | [FasterTransformer](https://github.com/NVIDIA/FasterTransformer) |
| 37 | **TileLang** | 6k | `tilelang/tilelang` | [TileLang](https://github.com/tile-ai/tilelang) |
| 38 | **Chitu** | 3k | `chitu/chitu` | [Chitu](https://github.com/thu-pacman/chitu) |
| 39 | **RTP-LLM** | 1k | `rtp-llm/rtp-llm` | [RTP-LLM](https://github.com/alibaba/rtp-llm) |
| 40 | **RAFT** | 1k | `raft/raft` | [RAFT](https://github.com/rapidsai/raft) |
| 41 | **UCC** | 307 | `ucc/ucc` | [UCC](https://github.com/openucx/ucc) |

---

## 🗂️ 按领域分类

### 🔧 GPU 内核 & 算子
CUTLASS · FlashAttention · GPU-Puzzles · Taskflow · HVM2 · CuPy · OneFlow · DeepEP · DeepGEMM · cuda-samples · LeetCUDA · RAFT

### 🚀 推理引擎
vLLM · SGLang · TensorRT-LLM · LMDeploy · RTP-LLM · Chitu · FasterTransformer · TensorRT

### 💾 缓存 & 存储
LMCache

### 📡 通信
UCC · DeepEP (MoE EP)

### 🏋️ 分布式训练
DeepSpeed · Megatron-LM · GPT-NeoX · Apex · llm.c · Horovod

### 🔬 编译 & 模拟
TileLang · Warp · TVM

### 🧠 深度学习框架
PyTorch · Deeplearning4J

### 🎨 神经图形学 & 3D
Instant-NGP · Open3D · vid2vid

### 📚 参考实现
DeepLearningExamples · tensorrtx · jetson-inference

### 🔀 GPU 兼容层
ZLUDA

### 📊 数据处理
cuDF

---

## 🔗 项目关系

```
训练栈:    llm.c ─── Apex ─── DeepSpeed / Megatron-LM
               │         │     └── Horovod (Ring-AllReduce)
               │         └── GPT-NeoX (Megatron+DeepSpeed+MoE/RWKV/Mamba)
               └──── 内核层: CUTLASS + FlashAttention
                              │
推理栈:    FasterTransformer ──→ TensorRT ──→ TensorRT-LLM ── vLLM/SGLang
               ↓                   │
          tensorrtx (TRT参考实现)   └── LMDeploy (TurboMind+PyTorch双引擎)
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
           vid2vid (视频翻译/FlowNet2/CUDA内核)
边缘层:    jetson-inference (Jetson/TensorRT/C++推理)
兼容层:    ZLUDA (CUDA→AMD GPU)
编排层:    Taskflow (DAG调度/CUDA Graph/Pipeline)
计算层:    HVM2 (Interaction Combinators GPU并行)
数值层:    CuPy (NumPy/SciPy GPU) · cuDF (DataFrame GPU)
模拟层:    Warp (独立)
教学:     GPU-Puzzles (入门) ──→ LeetCUDA (实战) ──→ cuda-samples (官方)
参考:     DeepLearningExamples (50+ SOTA模型) · tensorrtx (57模型TRT实现)
内核:     DeepGEMM (FP8/FP4 GEMM + MoE Mega-Kernel)
```

---

## 📈 项目演进时序

```
2015 ── Deeplearning4J (JVM深度学习)
2017 ── TVM (ML编译器, Apache孵化)
2018 ── Horovod, FasterTransformer, DeepLearningExamples, Open3D, Taskflow, vid2vid
2019 ── Apex (AMP 混合精度), jetson-inference
2020 ── DeepSpeed (ZeRO), Megatron-LM (TP/PP), ZLUDA (CUDA兼容层), GPT-NeoX
2021 ── CUTLASS 2.x (Ampere), UCC (统一通信), tensorrtx
2022 ── FlashAttention FA1/FA2, vLLM, Instant-NGP, GPU-Puzzles, HVM2, DeepGEMM
2023 ── SGLang, RTP-LLM, LMDeploy
2024 ── CUTLASS 4.x, FA3, LeetCUDA, DeepEP, Chitu
2025 ── FA4, llm.c, TileLang, LMCache dev
2026 ── cuDF v26.06, PyTorch v2.13, TVM v0.25, TensorRT 10.16/11.0
```
