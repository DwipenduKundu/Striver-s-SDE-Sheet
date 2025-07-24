class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        if numRows==1:
            arr.append([1])
        elif numRows==2:
            arr.append([1])
            arr.append([1,1])
        else:
            arr.append([1])
            arr.append([1,1])
            counter=3
            for row in range(2,numRows):
                temp=[]
                for col in range(counter):
                    if col==0:
                        temp.append(1)
                    elif col==counter-1:
                        temp.append(1)
                    else:
                        temp.append(arr[row-1][col-1]+arr[row-1][col])
                counter+=1
                arr.append(temp)
        return arr