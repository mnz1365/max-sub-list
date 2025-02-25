# the function take list of numbers and output the sub-list with maximum total of numbers


import math



def maxList(myList):
       
    num_List = myList
    temporary_list = []
    max_subarray = []
    sum = 0
    bigNumber = -math.inf 
    list_scope = 1
    base_position = 0


    # finding biggest number in list
    for number in num_List:
        if number > bigNumber:
            bigNumber = number

    # finding biggest subarray
    for numbers in num_List:
        list_scope = list_scope + 1
        base_position = 0
        for numbers in num_List:
            for item in range(list_scope):
                if base_position+item >= len(num_List):
                    break
                temporary_list.append(num_List[base_position+item])
            # checking the new created sub list if greater then last greater sub list then replace it and hold this result for next test 
            for i in temporary_list:
                sum = sum + i
            if sum > bigNumber:
                bigNumber = sum
                sum = 0
                max_subarray = []
                for j in temporary_list:
                    max_subarray.append(j)
                temporary_list = []
            if sum <= bigNumber:
                sum = 0
                temporary_list = []
            
            base_position = base_position + 1
            
    return max_subarray
        
        
        
# num_List = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# num_List = [4,-1,2,0,-1,1,2,4,-5,-8,2,-1,4]

print(maxList([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    