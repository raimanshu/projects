content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        # print(content)
        if "python" in content.lower():
            print(f"Yes python is present is present in {i}")
        # else:
        #     print("No python is not present")
        i+=1
        

