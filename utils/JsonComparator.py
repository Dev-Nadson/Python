import json

def readJson(path01: str, path02: str):
    try:
        with open(path01, "r", encoding="utf-8") as file01:
            old_data = json.load(file01)

        with open(path02, "r", encoding="utf-8") as file02:
            new_data = json.load(file02)
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e.filename}")
        return

    old_codes = {item['code'].strip() for item in old_data if 'code' in item}
    new_codes = {item['code'].strip() for item in new_data if 'code' in item}

    added_codes = new_codes - old_codes
    removed_codes = old_codes - new_codes

    added_items = [item for item in new_data if item.get('code', '').strip() in added_codes]
    removed_items = [item for item in old_data if item.get('code', '').strip() in removed_codes]

    with open("./data/cleanData/Added.json", "w", encoding="utf-8") as f_added:
        json.dump(added_items, f_added, ensure_ascii=False, indent=2)

    with open("./data/cleanData/Removed.json", "w", encoding="utf-8") as f_removed:
        json.dump(removed_items, f_removed, ensure_ascii=False, indent=2)


    print(f"\nForam encontrados {len(added_items)} itens adicionados:")
    for item in added_items:
        print(f"  - {item}")

    print(f"\nForam encontrados {len(removed_items)} itens removidos:")
    for item in removed_items:
        print(f"  - {item}")


readJson("./data/procedures_antigo.json", "./data/tb_procedimento.json")