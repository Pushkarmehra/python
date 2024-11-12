def my():
     for i in range(200): 
         yield i
          
g = my()
print(next(g))


# for j  in g:
#     print(j)     
