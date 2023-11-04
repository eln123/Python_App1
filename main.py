columns = [["hello"], "world", "hi"]
testNum = 10

def print_testing(columns):
        print(f" testNum is {testNum}")
        for i, column in enumerate(columns):
           print(i, column)

        for column in columns:
              print(column)

        for i in range(10, 15):
              print(i)
        
        for _ in range(5, 10):
              print("hello")

print_testing(columns)