# arvore.py

# --- Classe Nó da árvore ---
class No:
    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None

# --- Classe Árvore Binária ---
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # Inserção de nó
    def inserir(self, info):
        if self.raiz is None:
            self.raiz = No(info)
        else:
            self._inserir_recursivo(self.raiz, info)

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

    # Busca por código
    def buscar(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, no, codigo):
        if no is None:
            return None
        if codigo == no.info.codigo:
            return no.info
        elif codigo < no.info.codigo:
            return self._buscar_recursivo(no.esquerda, codigo)
        else:
            return self._buscar_recursivo(no.direita, codigo)

    # Exclusão de nó
    def excluir(self, codigo):
        self.raiz = self._excluir_recursivo(self.raiz, codigo)

    def _excluir_recursivo(self, no, codigo):
        if no is None:
            return no

        if codigo < no.info.codigo:
            no.esquerda = self._excluir_recursivo(no.esquerda, codigo)
        elif codigo > no.info.codigo:
            no.direita = self._excluir_recursivo(no.direita, codigo)
        else:
            # Nó encontrado
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            # Substitui pelo menor nó da subárvore direita
            temp = self._min_valor_no(no.direita)
            no.info = temp.info
            no.direita = self._excluir_recursivo(no.direita, temp.info.codigo)
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    # Percorrer em ordem (in-order)
    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, no):
        if no is not None:
            self._percorrer_em_ordem_recursivo(no.esquerda)
            print(no.info)  # chama __str__ da classe
            self._percorrer_em_ordem_recursivo(no.direita)
