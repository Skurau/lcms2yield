# lcms2yield
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


This repository contains the data and code for the paper **"From Purification to Prediction: AI-Powered UV Spectral Prediction as a New Paradigm for Yield Quantification in Modern Chemical Synthesis"**.

该存储库包含了名为“从纯化到预测：基于人工智能的紫外光谱预测技术——现代化学合成中产量量化的新范式”的论文所涉及的数据和代码。

## Keywords
 **`AI-for-Science, Quantum-Chemistry-Computing, Deep-Learning, Pre-training and Fine-tuning, Reaction-Yield`**

## 📊 Data

This repository includes the following datasets:
- **`data/quantum_chemistry/data.csv`**: The SMILES and quantum chemistry calculated CFs for 22,609 compounds used at pre-training stage

  在预训练阶段，使用了 22,609 种化合物的 SMILES 和量子化学计算得出的构型信息。

- **`data/experiment/Fine_tuning.csv`**: The SMILES and LCMS/UV-derived experimental CFs for 1,845 compounds used at fine-tuning stage

  在微调阶段，对 1,845 种化合物进行了 SMILES 分析和 LCMS/UV 衍生光谱分析。

- **`data/experiment/FDA.csv`**: The SMILES and LCMS/UV-derived experimental CFs for 144 FDA approved drug compounds used for independent benchmark

  针对 144 种获得 FDA 批准的药物化合物所得到的 SMILES 和 LCMS/UV 衍生实验数据，这些化合物被用于独立的基准测试。

- **`data/experiment/Reaction.csv`**: The SMILES, LCMS/UV-derived experimental CFs for target products from 178 real-world reactions used for independent benchmark against calibrated reaction yields.

  针对 178 个实际反应过程，我们获得了目标产物的 SMILES、LCMS/UV 衍生实验数据。这些数据将被用于与校准后的反应产率进行独立比较。

- **`data/experiment/Isolated_Yields_Suzuki_34.csv`**: The SMILES, LCMS/UV-derived experimental CFs for target products from 34 Suzuki reactions used for independent benchmark against isolated reaction yields.

  通过 34 次 Suzuki 反应来制备目标产物的 SMILES、LCMS/UV 衍生实验数据。这些数据被用于独立基准测试，以评估反应的产率水平。
  
- **`data/experiment/Isolated_Yields_Minisci_26.csv`**: The SMILES, LCMS/UV-derived experimental CFs for target products from 26 Minisci reactions used for independent benchmark against isolated reaction yields.

  针对目标产物，通过 26 个 Minisci 反应得到了 SMILES、LCMS/UV 衍生的实验数据。这些数据被用于独立基准测试，以评估单独反应时的性能。



## 📦 Correction Factor Prediction

### Prerequisites
- Operating System​​: Ubuntu 20.04.2 LTS (recommended and tested)
- Python 3.11
- pip package manager
- NVIDIA GPU with CUDA support (optional, for GPU acceleration)

### Install Dependencies
#### CPU Version Installation
```bash
# Install PyTorch
pip3 install torch==2.3.0 torchvision==0.18.0 --index-url https://download.pytorch.org/whl/cpu

# Install PyTorch Geometric dependencies
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.3.0+cpu.html

# Install main packages
pip install torch_geometric==2.5.3 performer_pytorch==1.1.4 rdkit==2023.9.6

# Install additional dependencies
pip install pykan==0.2.7 pyyaml==6.0.2 matplotlib==3.9.0 pandas==2.3.2 numpy==1.26.4
```
#### GPU Version Installation (CUDA Acceleration)
```bash
# Install PyTorch with CUDA 11.8
pip3 install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118

# Install PyTorch Geometric dependencies
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.3.0+cu118.html

# Install main packages
pip install torch_geometric==2.5.3 performer_pytorch==1.1.4 rdkit==2023.9.6

# Install additional dependencies
pip install pykan==0.2.7 pyyaml==6.0.2 matplotlib==3.9.0 pandas==2.3.2 numpy==1.26.4
```


### Demo

```python
from predict import predict_by_smiles_list

# Example SMILES strings
SMILES_list = [
    'CN(N=C1)C=C1CC2(CC(F)(F)C2)NC(CC3=CC(C=C(Br)C=N4)=C4C=C3)C5=C(O)C=CC=N5', 
    'Nc1[nH]c(=O)nc[c:1]1[N:1]1CSC[C@H]1C(=O)O'
]

# Get predictions
res = predict_by_smiles_list(SMILES_list)
model_pth = res['model_pth']
preds = res['preds']

print('Predicted CFs:', preds)
# Output: Predicted CFs: [1.1300693  0.43467927]
```


### 🔧 API Reference

### `predict_by_smiles_list(smiles_list)`
Predict correction factors for a list of SMILES strings.

**Parameters:**
- `smiles_list` (List[str]): List of SMILES strings

**Returns:**
- `dict`: Dictionary containing:
  - `model_pth` (str): Path to the model used
  - `preds` (List[float]): Predicted correction factors






## 📄 License

This project is licensed under the Apache-2.0 License.



---
# 使用方法
**当前项目使用现成权重，根据分子的 SMILES 预测校正因子 CF，无需重新训练。** 

固定使用：

- 项目：`E:\CodexProjects\lcms2yield`
- Python 环境：`D:\Anaconda3\envs\lcms2yield`
- 工作目录：`E:\CodexProjects\lcms2yield\model`
- 测试文件：`predict.py`

**1. 在 Anaconda Prompt 中运行**

```bat
conda activate lcms2yield
cd /d "E:\CodexProjects\lcms2yield\model"
python -X utf8 predict.py
```

这会预测项目自带的两个分子。结果应接近此前实测值：

```text
preds CFs: {
    'model_pth': './model_pth/20250721.pth',
    'preds': array([1.1300694, 0.43467924], dtype=float32)
}
```

`preds` 的顺序与输入 SMILES 顺序一致。**CF 是模型预测的校正因子，不是产率百分比。**

**2. 在 VS Code 中运行**

1. 打开文件夹 `E:\CodexProjects\lcms2yield`。
2. 打开 `model\predict.py`，取消文字选中。
3. 按 **Ctrl + Alt + N**，使用已经配置好的 Code Runner 运行。

也可以使用 **Python: Run Python File in Terminal**，但应确认所选解释器是：

```text
D:\Anaconda3\envs\lcms2yield\python.exe
```

两种运行入口都已配置为从脚本所在目录启动。F5 调试使用另一套启动配置，目前这些设置不控制它。

**3. 在 PowerShell 中直接运行**

使用明确的解释器路径，可以不依赖 `conda activate`：

```powershell
Set-Location -LiteralPath 'E:\CodexProjects\lcms2yield\model'

& 'D:\Anaconda3\envs\lcms2yield\python.exe' -X utf8 predict.py
```

**4. 预测自己的分子**

在项目的 `model` 文件夹中新建一个独立脚本，例如 `run_example.py`：

```python
from rdkit import Chem
from predict import predict_by_smiles_list


def main() -> None:
    # 将需要预测的分子放入同一个列表。
    smiles_list = [
        "CCO",       # 乙醇
        "c1ccccc1",  # 苯
    ]

    if not smiles_list:
        raise ValueError("SMILES 列表不能为空。")

    # 先检查输入，避免原项目将无效 SMILES 转为空分子。
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None or mol.GetNumAtoms() == 0:
            raise ValueError(f"无效或空的 SMILES：{smiles!r}")

    result = predict_by_smiles_list(
        smiles_list,
        batch_size=32,
        num_workers=0,
    )

    for smiles, cf in zip(smiles_list, result["preds"]):
        print(f"{smiles}\t预测 CF：{float(cf):.6f}")


if __name__ == "__main__":
    main()
```

激活环境并进入 `model` 目录后，执行：

```bat
python -X utf8 run_example.py
```

这段代码展示自定义输入方式，乙醇和苯的具体预测数值尚未实测。

**目前修改后的行为：**

- 自动使用可用的 NVIDIA GPU；GPU 不可用时回退到 CPU。
- Windows 默认 `num_workers=0`，避免启动多个进程重复导入依赖。
- 两类警告已处理，正常预测不需要再添加 `-W` 过滤参数。
- `checkpoint directory created`、`saving model version 0.0` 是普通日志，可能仍会显示。

此前双分子示例总耗时约 **23–28 秒**，主要是依赖导入。多个分子放在同一个列表中批量预测，可以分摊这部分启动开销。
