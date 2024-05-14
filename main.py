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

def eliminacion_gausseana(A, b):
    n = len(b)

    for i in range(n):
        A[i] = A[i] / A[i, i]

        for j in range(i+1, n):
            A[j] = A[j] - A[i] * A[j, i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i] - sum(A[i, j]*x[j] for j in range(i+1, n))

    return x


def main(page: ft.Page):
    def resolver_clicked(e):
        validate_input(str(A_input.value))
        validate_input(str(b_input.value))

        if dd.value=="Gauss-Jordan":
            A = np.array(eval(A_input.value))
            b = np.array(eval(b_input.value))
            x = gauss_jordan(A, b)
            t = ft.Text(value= str(x), color="green")
            page.controls.append(t)
            page.update()
        elif dd.value=="Eliminacion Gausseana":
            A = np.array(eval(A_input.value))
            b = np.array(eval(b_input.value))
            x = eliminacion_gausseana(A, b)
            t = ft.Text(value= str(x), color="green")
            page.controls.append(t)
            page.update()

        
    page.title = "Gauss-Jordan"
    def elegirop(e):
        A_input.value=""
        b_input.value=""
        A_input.focus()
        A_input.update()
        b_input.update()

    def validate_input(input_text):
        allowed_chars = set("[] ,.0 1 2 3 4 5 6 7 8 9 -")
        if input_text.strip() == "":
            indicacion.value = "El campo de texto no puede estar vacío."
            indicacion.update()

        elif set(input_text) - allowed_chars:

            indicacion.value="invalido"
            indicacion.update()

        else:
            indicacion.value="INGRESAR MATRICES Y VECTORES COMO UNA LISTA DE LISTAS. EJEMPLO: matriz: [[0, 0], [0, 0]] vector: [0, 0]"
            indicacion.update()
        



    A_input = ft.TextField(hint_text="Introduce la matriz A como una lista de listas")
    b_input = ft.TextField(hint_text="Introduce el vector b como una lista")
    indicacion = ft.Text(value="INGRESAR MATRICES Y VECTORES COMO UNA LISTA DE LISTAS. EJEMPLO: matriz: [[0, 0], [0, 0]] vector: [0, 0]", color="yellow300", italic=True)
    

    resolver_button = ft.ElevatedButton("Resolver", on_click=resolver_clicked)

   
    page.add(A_input, b_input, indicacion, resolver_button)
    dd = ft.Dropdown(width=300, hint_text="Elige el tipo de operacion",
                     options=[
            ft.dropdown.Option("Gauss-Jordan", on_click=elegirop),
            ft.dropdown.Option("Eliminacion Gausseana", on_click=elegirop),

        ],
    )
    page.add(dd)

  

ft.app(target=main)



ft.app(main)


