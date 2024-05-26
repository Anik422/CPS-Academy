import re
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        # check mail
        if re.match(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]{2,3}", data[i]):
            try:
                val = int(data[i+1])
                with open("output.txt", "a", encoding="utf-8") as f:
                    f.write(data[i] + ":" + data[i+1] + "\n")
            except:
                pass            