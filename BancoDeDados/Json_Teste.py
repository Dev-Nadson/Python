index = "ArquivosManipulacao/batch.json"
with open(index, "r") as json:
    txt = json.readlines()
    for i in txt:
        print(i, end="")