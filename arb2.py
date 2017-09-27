class Variable:
      def __init__(self, nombre, valor):
        self.nombre=nombre
        self.valor=valor

class Nodo():
    def __init__ (self, valor, izq = None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der

def evaluar(arbol):
    try:
        if arbol.valor == '+':
            return evaluar(arbol.izq) + evaluar(arbol.der)
        if arbol.valor == '-':
            return evaluar(arbol.izq) - evaluar(arbol.der)
        if arbol.valor == '/':
            return evaluar(arbol.izq) / evaluar(arbol.der)
        if arbol.valor == '*':
            return evaluar(arbol.izq) * evaluar(arbol.der)
        return int(arbol.valor)
    except AttributeError:
        return int(arbol)


class Pila(object):
    
    def __init__(self):
        self.items=[]

    def apilar (self,dato):
        self.items.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()

    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False
continuar = True

lista = []
while True:
    operacionpos =raw_input("Ingrese la operacion en posorden: ")
    operacion=operacionpos.split(" ")
    pila = Pila()
    for i in range(len(operacion)-1):
        if operacion[i+1] == '=':
            valor = evaluar(pila.desapilar())
            print(operacion[i] + ' = ' + str(valor))
            variable = Variable(operacion[i],valor)
            lista.append(variable)
        else:
            if(operacion[i]!='+' and operacion[i]!='-' and operacion[i]!='*' and operacion[i]!='/'):
                if (operacion[i].isalpha()):
                    for j in range (len(lista)):
                        if (lista[j].nombre==operacion[i]):
                            pila.apilar(lista[j].valor)                  
                else:  
                    pila.apilar(operacion[i])
            else:
                der=pila.desapilar()
                izq=pila.desapilar()
                nodo=Nodo(operacion[i],izq,der)
                pila.apilar(nodo)
