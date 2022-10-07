lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
agregar =[ i for i in  lis if (type(i)== str)]
print(agregar)

# for element in lis:              #no entiendo porque no elimina los elementos de tipo str
                                    # la unica solucion que encontre es hacer lo mismo dos vecs    
#      if (type(element)==str):
#       lis.remove(element)
      
    
for element in lis:

      if (type(element)==str):
       lis.remove(element) 
       break
    
for element in lis:
      if (type(element)==str):
       lis.remove(element)
       break


lis.append(agregar)
print(lis)