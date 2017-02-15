# i=1
# while i<=10:
#     print(i, 'fish in the aquarium')
#     i += 1
#s=['wer', 'rew', 'ter', 4]
# i=0
# while i<len(s):
#      i -=1
#      print(s[i]+'!')
#      s.remove(s[i])
#      i += 1
# print(s)
# s=['wer', 'rew', 'ter', 'd']
#
# while s:
#      print(s.pop())

# l='writeln'
# while l:
#     print(l[-1])
#     l=l[:-1]
# print(l)
# s=0
# for i in range(1,101,2):
#     s +=i**2
# print(s)
#s="delete"
# for i in range(len(s)):
#     if type(i)!=str:
#         s[i]=str(s[i])
# print(s)
# d=0
# for i in s:
#     if type(s[d])!=str:
#         s[d]=str(s[d])
#     d +=1
# print(s)
input_file = open("test4.txt")
#all_read = input_file.read(1)
#print(all_read)
line = input_file.readline()
print(line)
lines = input_file.readline()
print(lines)
input_file.close()

