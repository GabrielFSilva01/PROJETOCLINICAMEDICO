#//~~~[CLASSE NÓ]~~~\\
class No:
    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None

#//~~~[CLASSE ÁRVORE BINÁRIA]~~~\\
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None


    #----------[Inserção de um nó na árvore]----------
    #//-[FUNCAO INSERIR]-\\
    def inserir(self, info):
        if self.raiz is None:
            self.raiz = No(info)
        else:
            self._inserir_recursivo(self.raiz, info)


    #//-[FUNCAO INSERIR RECURSIVO]-\\
    def _inserir_recursivo(self, no, info):
        if info.codigo < no.info.codigo:
            if no.esquerda is None:
                no.esquerda = No(info)
            else:
                self._inserir_recursivo(no.esquerda, info)
        else:
            if no.direita is None:
                no.direita = No(info)
            else:
                self._inserir_recursivo(no.direita, info)


    #----------[Busca de um nó pelo código]----------
    #//-[FUNCAO BUSCAR]-\\
    def buscar(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)


#//-[FUNCAO BUSCAR RECURSIVO]-\\
    def _buscar_recursivo(self, no, codigo):
        if no is None:
            return None
        
        if codigo == no.info.codigo:
            return no.info
        elif codigo < no.info.codigo:
            return self._buscar_recursivo(no.esquerda, codigo)
        else:
            return self._buscar_recursivo(no.direita, codigo)

    #----------[Exclusão de um nó pelo código]----------
    #//-[FUNCAO EXCLUIR]-\\
    def excluir(self, codigo):
        self.raiz = self._excluir_recursivo(self.raiz, codigo)


#//-[FUNCAO EXCLUIR RECURSIVO]-\\
    def _excluir_recursivo(self, no, codigo):
        if no is None:
            return no

        if codigo < no.info.codigo:
            no.esquerda = self._excluir_recursivo(no.esquerda, codigo)
        elif codigo > no.info.codigo:
            no.direita = self._excluir_recursivo(no.direita, codigo)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            
            temp = self._min_valor_no(no.direita)
            no.info = temp.info
            no.direita = self._excluir_recursivo(no.direita, temp.info.codigo)

        return no


    #----------[Método auxiliar para encontrar o menor valor]----------
    #//-[FUNCAO MIN VALOR NO]-\\
    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual