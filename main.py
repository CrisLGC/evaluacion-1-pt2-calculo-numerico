import numpy as np
import flet as ft

def gauss_jordan(A, b):
        A = A.astype(float)
        Ab = np.hstack([A, b.reshape(-1, 1)])
        
        n = len(b)

        for i in range(n):
            Ab[i] = Ab[i] / Ab[i, i]
            
            for j in range(n):
                if i != j:
                    Ab[j] = Ab[j] - Ab[i] * Ab[j, i]
        x = Ab[:, -1]
        return x
    
     

def main(page: ft.Page):
    def resolver_clicked(e):
       
         A = np.array(eval(A_input.value))
         b = np.array(eval(b_input.value))
        
         x = gauss_jordan(A, b)
        
         t = ft.Text(value= str(x), color="green")
         page.controls.append(t)
         page.update()
    page.title = "Gauss-Jordan"

    A_input = ft.TextField(hint_text="Introduce la matriz A como una lista de listas")
    b_input = ft.TextField(hint_text="Introduce el vector b como una lista")
    

    resolver_button = ft.ElevatedButton("Resolver", on_click=resolver_clicked)

   
    page.add(A_input, b_input, resolver_button)

  

ft.app(target=main)



ft.app(main)


