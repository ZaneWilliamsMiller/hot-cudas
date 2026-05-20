# 🔥 Hot CUDAs — CUDA/GPU 开源项目知识库

> 自动整理 2026-05-20 | 99 个热门项目 | 深度源码分析 · Git Submodules · 持续更新

## 📦 使用方式

```bash
# 克隆含所有子模块（锁定版本）
git clone --recurse-submodules https://github.com/ZaneWilliamsMiller/hot-cudas.git

# 克隆最新版本（dev 分支每日同步上游）
git clone --recurse-submodules -b dev https://github.com/ZaneWilliamsMiller/hot-cudas.git

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
| 9 | **DeepLearningExamples** | 15k | `deep-learning-examples/deep-learning-examples` | [DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) |
| 10 | **Horovod** | 15k | `horovod/horovod` | [Horovod](https://github.com/horovod/horovod) |
| 11 | **Deeplearning4J** | 14k | `deeplearning4j/deeplearning4j` | [Deeplearning4J](https://github.com/deeplearning4j/deeplearning4j) |
| 12 | **Open3D** | 14k | `open3d/Open3D` | [Open3D](https://github.com/isl-org/Open3D) |
| 13 | **TensorRT-LLM** | 14k | `tensorrt-llm/TensorRT-LLM` | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| 14 | **ZLUDA** | 14k | `zluda/ZLUDA` | [ZLUDA](https://github.com/vosen/ZLUDA) |
| 15 | **TVM** | 13k | `tvm/tvm` | [TVM](https://github.com/apache/tvm) |
| 16 | **TensorRT** | 13k | `tensorrt/TensorRT` | [TensorRT](https://github.com/NVIDIA/TensorRT) |
| 17 | **GPU-Puzzles** | 12k | `gpu-puzzles/GPU-Puzzles` | [GPU-Puzzles](https://github.com/srush/GPU-Puzzles) |
| 18 | **Taskflow** | 12k | `taskflow/taskflow` | [Taskflow](https://github.com/taskflow/taskflow) |
| 19 | **CuPy** | 11k | `cupy/cupy` | [CuPy](https://github.com/cupy/cupy) |
| 20 | **HVM2** | 11k | `hvm2/HVM2` | [HVM2](https://github.com/HigherOrderCO/HVM2) |
| 21 | **LeetCUDA** | 11k | `leetcuda/LeetCUDA` | [LeetCUDA](https://github.com/xlite-dev/LeetCUDA) |
| 22 | **CUTLASS** | 10k | `cutlass/cutlass` | [CUTLASS](https://github.com/NVIDIA/cutlass) |
| 23 | **DeepEP** | 10k | `deepep/DeepEP` | [DeepEP](https://github.com/deepseek-ai/DeepEP) |
| 24 | **cuDF** | 10k | `cudf/cudf` | [cuDF](https://github.com/rapidsai/cudf) |
| 25 | **Apex** | 9k | `apex/apex` | [Apex](https://github.com/NVIDIA/apex) |
| 26 | **OneFlow** | 9k | `oneflow/oneflow` | [OneFlow](https://github.com/Oneflow-Inc/oneflow) |
| 27 | **cuda-samples** | 9k | `cuda-samples/cuda-samples` | [cuda-samples](https://github.com/NVIDIA/cuda-samples) |
| 28 | **jetson-inference** | 9k | `jetson-inference/jetson-inference` | [jetson-inference](https://github.com/dusty-nv/jetson-inference) |
| 29 | **vid2vid** | 9k | `vid2vid/vid2vid` | [vid2vid](https://github.com/NVIDIA/vid2vid) |
| 30 | **LMCache** | 8k | `lmcache/lmcache` | [LMCache](https://github.com/LMCache/LMCache) |
| 31 | **LMDeploy** | 8k | `lmdeploy/lmdeploy` | [LMDeploy](https://github.com/InternLM/lmdeploy) |
| 32 | **tensorrtx** | 8k | `tensorrtx/tensorrtx` | [tensorrtx](https://github.com/wang-xinyu/tensorrtx) |
| 33 | **DeepGEMM** | 7k | `deepgemm/deepgemm` | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) |
| 34 | **GPT-NeoX** | 7k | `gpt-neox/gpt-neox` | [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) |
| 35 | **GoCV** | 7k | `gocv/gocv` | [GoCV](https://github.com/hybridgroup/gocv) |
| 36 | **Warp** | 7k | `warp/warp` | [Warp](https://github.com/NVIDIA/warp) |
| 37 | **Chainer** | 6k | `chainer/chainer` | [Chainer](https://github.com/chainer/chainer) |
| 38 | **DALI** | 6k | `dali/DALI` | [DALI](https://github.com/NVIDIA/DALI) |
| 39 | **Deep Painterly** | 6k | `deep-painterly-harmonization/deep-painterly-harmonization` | [Deep Painterly](https://github.com/luanfujun/deep-painterly-harmonization) |
| 40 | **FasterTransformer** | 6k | `faster-transformer/faster-transformer` | [FasterTransformer](https://github.com/NVIDIA/FasterTransformer) |
| 41 | **FlashInfer** | 6k | `flashinfer/flashinfer` | [FlashInfer](https://github.com/flashinfer-ai/flashinfer) |
| 42 | **GPU MODE Lectures** | 6k | `lectures/lectures` | [GPU MODE Lectures](https://github.com/gpu-mode/lectures) |
| 43 | **TileLang** | 6k | `tilelang/tilelang` | [TileLang](https://github.com/tile-ai/tilelang) |
| 44 | **ethminer** | 6k | `ethminer/ethminer` | [ethminer](https://github.com/ethereum-mining/ethminer) |
| 45 | **ALIEN** | 5k | `alien/alien` | [ALIEN](https://github.com/chrxh/alien) |
| 46 | **Kaolin** | 5k | `kaolin/kaolin` | [Kaolin](https://github.com/NVIDIAGameWorks/kaolin) |
| 47 | **NCCL** | 5k | `nccl/nccl` | [NCCL](https://github.com/NVIDIA/nccl) |
| 48 | **Rust CUDA** | 5k | `rust-cuda/rust-cuda` | [Rust CUDA](https://github.com/Rust-GPU/rust-cuda) |
| 49 | **Thrust** | 5k | `thrust/thrust` | [Thrust](https://github.com/NVIDIA/thrust) |
| 50 | **cuML** | 5k | `cuml/cuml` | [cuML](https://github.com/rapidsai/cuml) |
| 51 | **Blitzar** | 4.9k | `blitzar/blitzar` | [spaceandtimefdn/blitzar](https://github.com/spaceandtimefdn/blitzar) |
| 52 | **torch2trt** | 4.9k | `torch2trt/torch2trt` | [NVIDIA-AI-IOT/torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt) |
| 53 | **ArrayFire** | 4.9k | `arrayfire/arrayfire` | [arrayfire/arrayfire](https://github.com/arrayfire/arrayfire) |
| 54 | **AITemplate** | 4.7k | `aitemplate/aitemplate` | [facebookincubator/AITemplate](https://github.com/facebookincubator/AITemplate) |
| 55 | **tiny-cuda-nn** | 4.5k | `tiny-cuda-nn/tiny-cuda-nn` | [NVlabs/tiny-cuda-nn](https://github.com/NVlabs/tiny-cuda-nn) |
| 56 | **CTranslate2** | 4.5k | `ctranslate2/ctranslate2` | [OpenNMT/CTranslate2](https://github.com/OpenNMT/CTranslate2) |
| 57 | **pytorch-YOLOv4** | 4.5k | `pytorch-yolov4/pytorch-YOLOv4` | [Tianxiaomo/pytorch-YOLOv4](https://github.com/Tianxiaomo/pytorch-YOLOv4) |
| 58 | **ExLlamaV2 (exllamav2)** | 4.5k | `exllamav2/exllamav2` | [turboderp-org/exllamav2](https://github.com/turboderp-org/exllamav2) |
| 59 | **HRNet (deep-high-resolution-net.pytorch)** | 4.5k | `hrnet/deep-high-resolution-net.pytorch` | [leoxiaobin/deep-high-resolution-net.pytorch](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch) |
| 60 | **lite.ai.toolkit** | 4.4k | `lite.ai.toolkit/lite.ai.toolkit` | [xlite-dev/lite.ai.toolkit](https://github.com/xlite-dev/lite.ai.toolkit) |
| 61 | **warp-ctc** | 4.1k | `warp-ctc/warp-ctc` | [baidu-research/warp-ctc](https://github.com/baidu-research/warp-ctc) |
| 62 | **SENet** | 3.6k | `SENet/SENet` | [hujie-frank/SENet](https://github.com/hujie-frank/SENet) |
| 63 | **cuda-course** | 3.6k | `cuda-course/cuda-course` | [Infatoshi/cuda-course](https://github.com/Infatoshi/cuda-course) |
| 64 | **StringZilla** | 3.5k | `StringZilla/StringZilla` | [ashvardanian/StringZilla](https://github.com/ashvardanian/StringZilla) |
| 65 | **SageAttention** | 3.4k | `SageAttention/SageAttention` | [thu-ml/SageAttention](https://github.com/thu-ml/SageAttention) |
| 66 | **ThunderKittens** | 3.4k | `ThunderKittens/ThunderKittens` | [HazyResearch/ThunderKittens](https://github.com/HazyResearch/ThunderKittens) |
| 67 | **LightSeq** | 3.3k | `lightseq/lightseq` | [bytedance/lightseq](https://github.com/bytedance/lightseq) |
| 68 | **FlowNet2-PyTorch** | 3.3k | `flownet2-pytorch/flownet2-pytorch` | [NVIDIA/flownet2-pytorch](https://github.com/NVIDIA/flownet2-pytorch) |
| 69 | **LYGIA** | 3.3k | `lygia/lygia` | [patriciogonzalezvivo/lygia](https://github.com/patriciogonzalezvivo/lygia) |
| 70 | **cuda-python** | 3.3k | `cuda-python/cuda-python` | [NVIDIA/cuda-python](https://github.com/NVIDIA/cuda-python) |
| 71 | **TransformerEngine** | 3.3k | `TransformerEngine/TransformerEngine` | [NVIDIA/TransformerEngine](https://github.com/NVIDIA/TransformerEngine) |
| 72 | **Jittor** | 3.2k | `jittor/jittor` | [Jittor/jittor](https://github.com/Jittor/jittor) |
| 73 | **MMDeploy** | 3.1k | `mmdeploy/mmdeploy` | [open-mmlab/mmdeploy](https://github.com/open-mmlab/mmdeploy) |
| 74 | **AresDB** | 3.1k | `aresdb/aresdb` | [uber/aresdb](https://github.com/uber/aresdb) |
| 75 | **HeavyDB** | 3.1k | `heavydb/heavydb` | [heavyai/heavydb](https://github.com/heavyai/heavydb) |
| 76 | **LichtFeld-Studio** | 3.1k | `lichtfeld-studio/LichtFeld-Studio` | [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) |
| 77 | **Chitu** | 3k | `chitu/chitu` | [Chitu](https://github.com/thu-pacman/chitu) |
| 78 | **Human Pose Estimation** | 3k | `human-pose-estimation-pytorch/human-pose-estimation.pytorch` | [microsoft/human-pose-estimation.pytorch](https://github.com/microsoft/human-pose-estimation.pytorch) |
| 79 | **Lc0** | 3k | `lc0/lc0` | [LeelaChessZero/lc0](https://github.com/LeelaChessZero/lc0) |
| 80 | **MinkowskiEngine** | 3k | `minkowski-engine/MinkowskiEngine` | [NVIDIA/MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) |
| 81 | **tensorRT_Pro** | 3k | `tensorrt-pro/tensorRT_Pro` | [shouxieai/tensorRT_Pro](https://github.com/shouxieai/tensorRT_Pro) |
| 82 | **how-to-optim-algorithm-in-cuda** | 2.9k | `how-to-optim-algorithm-in-cuda/how-to-optim-algorithm-in-cuda` | [how-to-optim-algorithm-in-cuda](https://github.com/BBuf/how-to-optim-algorithm-in-cuda) |
| 83 | **Model-Optimizer** | 2.7k | `model-optimizer/Model-Optimizer` | [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) |
| 84 | **CV-CUDA** | 2.7k | `cv-cuda/CV-CUDA` | [CVCUDA/CV-CUDA](https://github.com/CVCUDA/CV-CUDA) |
| 85 | **CUDALibrarySamples** | 2.4k | `cuda-library-samples/CUDALibrarySamples` | [CUDALibrarySamples](https://github.com/NVIDIA/CUDALibrarySamples) |
| 86 | **torch-ngp** | 2.2k | `torch-ngp/torch-ngp` | [torch-ngp](https://github.com/ashawkey/torch-ngp) |
| 87 | **cuGraph** | 2.2k | `cugraph/cugraph` | [cuGraph](https://github.com/rapidsai/cugraph) |
| 88 | **CCCL** | 2k | `cccl/cccl` | [CCCL](https://github.com/NVIDIA/cccl) |
| 89 | **PyCUDA** | 2k | `pycuda/pycuda` | [PyCUDA](https://github.com/inducer/pycuda) |
| 90 | **DeepMD-kit** | 1.9k | `deepmd-kit/deepmd-kit` | [DeepMD-kit](https://github.com/deepmodeling/deepmd-kit) |
| 91 | **PPQ** | 1.8k | `ppq/ppq` | [PPQ](https://github.com/OpenPPL/ppq) |
| 92 | **Aphrodite Engine** | 1.7k | `aphrodite-engine/aphrodite-engine` | [Aphrodite Engine](https://github.com/dphnAI/aphrodite-engine) |
| 93 | **PaddleSlim** | 1.6k | `paddleslim/PaddleSlim` | [PaddleSlim](https://github.com/PaddlePaddle/PaddleSlim) |
| 94 | **RAFT** | 1k | `raft/raft` | [RAFT](https://github.com/rapidsai/raft) |
| 95 | **RTP-LLM** | 1k | `rtp-llm/rtp-llm` | [RTP-LLM](https://github.com/alibaba/rtp-llm) |
| 96 | **DREAMPlace** | 998 | `dreamplace/DREAMPlace` | [limbo018/DREAMPlace](https://github.com/limbo018/DREAMPlace) |
| 97 | **llm_note** | 881 | `llm-note/llm_note` | [llm_note](https://github.com/harleyszhang/llm_note) |
| 98 | **cv-detect-robot** | 541 | `cv-detect-robot/cv-detect-robot` | [guojianyang/cv-detect-robot](https://github.com/guojianyang/cv-detect-robot) |
| 99 | **UCC** | 307 | `ucc/ucc` | [UCC](https://github.com/openucx/ucc) |
---

## 🗂️ 按领域分类

### 🔧 GPU 内核 & 算子
CUTLASS · FlashAttention · FlashInfer · GPU MODE Lectures · GPU-Puzzles · Taskflow · HVM2 · CuPy · OneFlow · DeepEP · DeepGEMM · cuda-samples · LeetCUDA · RAFT · Thrust · CCCL · PyCUDA · how-to-optim-algorithm-in-cuda (CUDA优化实战教程)

### 🚀 推理引擎
vLLM · SGLang · TensorRT-LLM · LMDeploy · RTP-LLM · Chitu · FasterTransformer · TensorRT · tensorRT_Pro · Model-Optimizer (量化/剪枝/蒸馏/推测解码) · Aphrodite Engine (大规模LLM推理, 多硬件后端)

### 💾 缓存 & 存储
LMCache

### 📡 通信

🔐 **密码学**: Blitzar
NCCL · UCC · DeepEP (MoE EP)

### 🏋️ 分布式训练
DeepSpeed · Megatron-LM · GPT-NeoX · Apex · llm.c · Horovod

### 🔬 编译 & 模拟
TileLang · Warp · TVM

### ⚡ 量化 & 压缩
PPQ (神经网络离线量化) · PaddleSlim (模型压缩/NAS) · Model-Optimizer

### 🧬 科学计算
DeepMD-kit (深度学习势函数/分子动力学) · DREAMPlace (深度学习VLSI布局)

### 📝 学习笔记
llm_note (LLM推理优化/CUDA编程笔记)

### 🧠 深度学习框架
PyTorch · Chainer · Deeplearning4J

### 🎨 神经图形学 & 3D
Instant-NGP · Open3D · vid2vid · MinkowskiEngine · LichtFeld-Studio (3D高斯泼溅训练/编辑/导出) · torch-ngp (PyTorch Instant-NGP, NeRF/SDF)

### 👁️ 计算机视觉
GoCV (Go+OpenCV+CUDA+OpenVINO) · Human Pose Estimation (ECCV2018, Simple Baselines, COCO/MPII) · cv-detect-robot (YOLO+DeepSort+DeepStream+TensorRT+ROS) · CV-CUDA (GPU加速图像处理/计算机视觉库)

### ⛏️ GPU 挖矿 (历史)
ethminer (Ethash CUDA/OpenCL, 已归档)

### ♟️ GPU 博弈 & 强化学习
Lc0 (AlphaZero棋类引擎, 神经网络+MCTS, CUDA/cuDNN/cuBLAS/CUTLASS)

### 📚 参考实现
DeepLearningExamples · tensorrtx · jetson-inference · cuda-course (CUDA编程课程) · CUDALibrarySamples (CUDA库官方示例)

### 🔀 GPU 兼容层
ZLUDA

### 📊 数据处理
cuDF · DALI · cuML · cuGraph (GPU图分析)

---

## 🔗 项目关系

```
训练栈:    llm.c ─── Apex ─── DeepSpeed / Megatron-LM
               │         │     └── Horovod (Ring-AllReduce)
               │         └── GPT-NeoX (Megatron+DeepSpeed+MoE/RWKV/Mamba)
               └──── 内核层: CUTLASS + FlashAttention + FlashInfer
                              │                    │
推理栈:    FasterTransformer ──→ TensorRT ──→ TensorRT-LLM ── vLLM/SGLang
               ↓                   │                        │
          tensorrtx (TRT参考实现)   └── LMDeploy (TurboMind) └── FlashInfer (默认注意力后端)
               ↓                        └── Model-Optimizer (量化/剪枝/蒸馏/推测解码 → TRT/vLLM部署)
               ↓
          vLLM ←──→ SGLang ←── RTP-LLM ←── Chitu (国产GPU推理)
               │         │
          Aphrodite Engine (多硬件推理, CUDA/ROCm/TPU)
               │
缓存层:    LMCache (KV Cache 跨层共享)
               │
通信层:    NCCL (GPU集合通信标准) + UCC (统一通信) + DeepEP (MoE EP)
               │
基础库:    CCCL (Thrust+CUB+libcudacxx) ←── Thrust (归档, 并行算法, 启发C++17)
           RAFT ─── RAPIDS 底层 (cuML/cuGraph/cuVS 公共原语)
量化层:    PPQ (离线量化, ONNX/PyTorch/Caffe) · PaddleSlim (压缩/NAS, PaddlePaddle生态)
桥梁层:    PyCUDA (Python CUDA Driver API 桥梁, GPUArray, SourceModule)
视觉层:    GoCV (Go+OpenCV+CUDA+OpenVINO, 单二进制部署)
           Human Pose Estimation (ECCV2018 Simple Baselines, ResNet+3Deconv, OKS-NMS, Cython+CUDA NMS)
           cv-detect-robot (YOLO+DeepSort+DeepStream+TensorRT+ROS, 边缘部署)
           CV-CUDA (GPU加速图像处理/计算机视觉, 云规模)
框架层:    PyTorch (Dynamo/Inductor/FSDP/DTensor/Export) ←── Chainer (define-by-run先驱,CuPy母项目)
           DL4J (JVM 深度学习全栈/SameDiff/ND4J)
编译层:    TileLang ─── TVM ─── CuTeDSL (CUTLASS)
图形层:    Instant-NGP (NeRF/SDF/Hash Encoding) + Open3D (3D全栈) + MinkowskiEngine (稀疏张量卷积)
           vid2vid (视频翻译/FlowNet2/CUDA内核)
           LichtFeld-Studio (3DGS训练/编辑/导出, 原生桌面应用)
           torch-ngp (PyTorch Instant-NGP, NeRF/SDF实时渲染)
边缘层:    jetson-inference (Jetson/TensorRT/C++推理) + tensorRT_Pro (C++/Python TensorRT封装, YOLO推理)
兼容层:    ZLUDA (CUDA→AMD GPU)
编排层:    Taskflow (DAG调度/CUDA Graph/Pipeline)
计算层:    HVM2 (Interaction Combinators GPU并行)
数值层:    CuPy (NumPy/SciPy GPU, 源自Chainer) · cuDF · DALI · cuML (DataFrame GPU) · cuGraph (GPU图分析)
科学层:    DeepMD-kit (深度学习势函数, LAMMPS/ASE集成, TensorFlow/PyTorch/JAX) · DREAMPlace (深度学习VLSI布局, PyTorch加速)
博弈层:    Lc0 (AlphaZero棋类引擎, CUTLASS Fused MHA, cuBLAS/cuDNN FP16, ResNet+SE+Attention)
历史层:    ethminer (Ethash GPU挖矿, SHFL+DAG, 已归档)
教学:     GPU-Puzzles · GPU MODE Lectures (34讲全栈) (入门) ──→ LeetCUDA (实战) ──→ cuda-samples (官方) ──→ cuda-course (系统课程)
           how-to-optim-algorithm-in-cuda (CUDA优化实战, Reduce/Softmax/GEMV/Elementwise)
参考:     DeepLearningExamples (50+ SOTA模型) · tensorrtx (57模型TRT实现) · CUDALibrarySamples (CUDA库官方示例)
内核:     DeepGEMM (FP8/FP4 GEMM + MoE Mega-Kernel) · FlashInfer (推理内核库, JIT生成, 多后端)
```

---

## 📈 项目演进时序

```
2009 ── Thrust (C++并行算法, 启发C++17标准), PyCUDA (Python CUDA桥梁)
2013 ── ArrayFire
2015 ── Chainer (define-by-run首创), Deeplearning4J, ethminer, NCCL
2017 ── DALI, TVM (ML编译器), GoCV, CuPy (从Chainer分离独立)
2018 ── ALIEN, cuML, Deep Painterly, Horovod, FasterTransformer, DeepLearningExamples, Open3D, Taskflow, vid2vid, Human Pose Estimation, Lc0
2019 ── Apex, jetson-inference, MinkowskiEngine, Chainer进入维护模式
2020 ── DeepSpeed, Megatron-LM, ZLUDA, GPT-NeoX
2021 ── CUTLASS 2.x, UCC, tensorrtx, tensorRT_Pro
2022 ── Blitzar ·  FlashAttention, vLLM, Instant-NGP, GPU-Puzzles, HVM2, DeepGEMM
2023 ── CCCL (Thrust+CUB+libcudacxx合并), SGLang, RTP-LLM, LMDeploy, Thrust归档, FlashInfer
2024 ── GPU MODE Lectures, CUTLASS 4.x, FA3/FA4, LeetCUDA, DeepEP, Chitu, FlashInfer MLA/POD
2025 ── llm.c, TileLang, LMCache dev, CCCL v3.5, FlashInfer FP4/Blackwell
2026 ── cuDF · DALI · cuML v26.06, PyTorch v2.13, TVM v0.25, TensorRT 10.16/11.0, CV-CUDA, LichtFeld-Studio, Model-Optimizer, cuda-course, Aphrodite Engine, DeepMD-kit, PaddleSlim, PPQ, torch-ngp, cuGraph, how-to-optim-algorithm-in-cuda, CUDALibrarySamples, DREAMPlace, llm_note
```
