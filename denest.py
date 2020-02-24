# recursive array denesting function
def denest(List):
    for item in List:
        if type(item) ==  list:
            for i in item:
                List.append(i)
            List.remove(item)
            denest(List)
    return List

# testing and command prompt
if __name__=="__main__":
    test_list = [[[['1'], '2'], '3'], '4', ['5', '6', ['7']], ['8']]
    print("test list:", test_list)
    print("denested list:", denest(test_list))
    while True:
        exec(input())