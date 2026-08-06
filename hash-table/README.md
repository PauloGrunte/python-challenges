Build a Hash Table - freeCodeCamp
This repository contains my solution for the "Build a Hash Table" project, required to complete the Scientific Computing with Python Certification at freeCodeCamp.

📝 Description
The goal of this project is to build a hash table data structure from scratch. A hash table works by taking a key as input, applying a hash function, and storing the associated value. For this lab, the hash function is simple: it sums the Unicode (ASCII) values of each character in the key. This computed hash is then used to store, retrieve, and delete the key-value pairs.

🎯 Objective
Fulfill all the user stories provided by freeCodeCamp and make all the automated tests pass to complete the lab.

✨ Features
HashTable Class: Create a class initialized with a collection attribute (an empty dictionary) to store the data.

Hash Method (hash): Takes a string and returns a hash value calculated as the sum of the Unicode values of each character using the ord function.

Add Method (add): Takes a key-value pair, computes the key's hash, and stores a dictionary containing the pair inside the collection. Handles collisions by storing multiple key-value pairs in a nested dictionary under the same hash value.

Remove Method (remove): Computes the hash of a given key and safely removes the corresponding key-value pair from the table. If the key does not exist, it does nothing (avoids throwing errors).

Lookup Method (lookup): Takes a key, computes its hash, and returns the corresponding value stored in the table. Returns None if the key is not found.

🇧🇷 Versão em Português
Construir uma Tabela Hash (Build a Hash Table) - freeCodeCamp
Este repositório contém a minha solução para o projeto "Construir uma Tabela Hash" (Build a Hash Table), necessário para concluir a certificação em Computação Científica com Python do freeCodeCamp.

📝 Descrição
O objetivo deste projeto é construir uma estrutura de dados de tabela hash do zero. Uma tabela hash funciona pegando uma chave como entrada, aplicando uma função de hash e armazenando o valor associado. Para este laboratório, a função de hashing é simples: ela soma os valores Unicode (ASCII) de cada caractere na chave. Esse hash calculado é então usado para armazenar, recuperar e excluir os pares chave-valor.

🎯 Objetivo
Cumprir todas as user stories fornecidas pelo freeCodeCamp e fazer todos os testes automatizados passarem para completar o laboratório.

✨ Funcionalidades
Classe HashTable: Criar uma classe inicializada com um atributo collection (um dicionário vazio) para armazenar os dados.

Método Hash (hash): Recebe uma string e retorna um valor hash calculado como a soma dos valores Unicode de cada caractere usando a função ord.

Método Adicionar (add): Recebe um par chave-valor, calcula o hash da chave e armazena um dicionário contendo o par dentro da collection. Lida com colisões armazenando vários pares chave-valor em um dicionário aninhado sob o mesmo valor de hash.

Método Remover (remove): Calcula o hash de uma chave fornecida e remove de forma segura o par chave-valor correspondente da tabela. Se a chave não existir, não faz nada (evita gerar erros).

Método Buscar (lookup): Recebe uma chave, calcula seu hash e retorna o valor correspondente armazenado na tabela. Retorna None se a chave não for encontrada na coleção.