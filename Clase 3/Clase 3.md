
Tuplas 

```Python

llista1 = [6,9]  
llista2 = ["josep", "dani"]  
  
llista_final = []  
  
for nota, nom in zip (llista1, llista2):  
   conjunt = (nota, nom)  
   llista_final.append(conjunt)  
  
for t in llista_final:  
   nota = t[0]  
   nom = t[1]  
   print(nom,nota)



```

