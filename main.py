inputList = []

for i in range(10):
    inputList.append(int(input("Enter number: ")))

wanted = int(input("What are you searching: ")) 

def search(arr,wanted):
    for i in range(len(arr)):
        if arr[i] == wanted:
            return i
    return "Not here"

print(search(inputList,wanted))


