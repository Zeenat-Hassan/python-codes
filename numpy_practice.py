#Given n numbers, find the runner up solution
if __name__ == '__main__':
 i=int(input())
 lis=list(map(int,input().strip().split()))[:i]
 z = max(lis)
 get_max_from_List= max(lis)
 while max(lis)==z:
  lis.remove(max(lis))
 print(max(lis))