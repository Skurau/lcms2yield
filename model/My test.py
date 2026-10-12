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
