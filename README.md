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

