word=input("Enter your word:")
print("original word:",word)
size=len(word)
for i in range(0,size-1,2):
   print(f"index-{i}:", word[i])