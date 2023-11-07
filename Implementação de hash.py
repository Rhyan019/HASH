import tkinter as tk
from tkinter import messagebox
#Vitor Rodrigues 185707
#Mateus Delucas Theobald 190379
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  

    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next

class HashTableGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hash Table GUI")

        self.hash_table = HashTable(size=10)

        self.label = tk.Label(master, text="Nome da Linguagem:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insert_button = tk.Button(master, text="Inserir", command=self.insert_language)
        self.insert_button.pack()

        self.search_button = tk.Button(master, text="Buscar", command=self.search_language)
        self.search_button.pack()

        self.remove_button = tk.Button(master, text="Remover", command=self.remove_language)
        self.remove_button.pack()

    def insert_language(self):
        language_name = self.entry.get()
        if language_name:
            self.hash_table.insert(language_name, "Descrição da linguagem")
            messagebox.showinfo("Inserção", f"{language_name} inserida com sucesso.")
        else:
            messagebox.showwarning("Inserção", "Por favor, insira um nome de linguagem.")

    def search_language(self):
        language_name = self.entry.get()
        if language_name:
            description = self.hash_table.search(language_name)
            if description:
                messagebox.showinfo("Busca", f"{language_name}: {description}")
            else:
                messagebox.showwarning("Busca", f"{language_name} não encontrada.")
        else:
            messagebox.showwarning("Busca", "Por favor, insira um nome de linguagem.")

    def remove_language(self):
        language_name = self.entry.get()
        if language_name:
            self.hash_table.remove(language_name)
            messagebox.showinfo("Remoção", f"{language_name} removida com sucesso.")
        else:
            messagebox.showwarning("Remoção", "Por favor, insira um nome de linguagem.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableGUI(root)
    root.mainloop()

