Polygon Area Calculator - freeCodeCamp
This repository contains my solution for the "Polygon Area Calculator" project, required to complete the Scientific Computing with Python Certification at freeCodeCamp.

📝 Description
The goal of this project is to use object-oriented programming to create a Rectangle class and a Square class. The Square class is a subclass of Rectangle and inherits its methods and attributes. The application allows users to calculate mathematical properties like area, perimeter, and diagonal, generate a text-based visual representation of the shapes, and determine how many times one shape can fit inside another.

🎯 Objective
Fulfill all the user stories provided by freeCodeCamp and make all the automated tests pass to complete the lab.

✨ Features
Rectangle Class: Create a rectangle initialized with width and height attributes.

Setters: Modify the dimensions using set_width and set_height methods.

Math Calculations: Compute the shape's properties using get_area, get_perimeter, and get_diagonal.

Visual Representation: Use get_picture to return a string of asterisks (*) that visually draws the shape (or returns an error message if the shape is too large).

Shape Fitting: Use get_amount_inside to calculate how many times a passed shape can fit completely inside the current shape (without rotations).

Formatted Output: Printing a Rectangle object displays a cleanly formatted string: Rectangle(width=X, height=Y).

Square Class: Inherits from Rectangle but initializes with a single side length. It overrides the setter methods (set_width, set_height, and introduces set_side) to ensure the width and height are always equal, and prints as Square(side=X).

🇧🇷 Versão em Português
Calculador de Área de Polígono (Polygon Area Calculator) - freeCodeCamp
Este repositório contém a minha solução para o projeto "Calculador de Área de Polígono" (Polygon Area Calculator), necessário para concluir a certificação em Computação Científica com Python do freeCodeCamp.

📝 Descrição
O objetivo deste projeto é usar programação orientada a objetos para criar uma classe Rectangle (Retângulo) e uma classe Square (Quadrado). A classe Square é uma subclasse de Rectangle e herda seus métodos e atributos. O aplicativo permite aos usuários calcular propriedades matemáticas como área, perímetro e diagonal, gerar uma representação visual das formas baseada em texto e determinar quantas vezes uma forma pode caber dentro da outra.

🎯 Objetivo
Cumprir todas as user stories fornecidas pelo freeCodeCamp e fazer todos os testes automatizados passarem para completar o laboratório.

✨ Funcionalidades
Classe Rectangle (Retângulo): Criar um retângulo inicializado com os atributos de largura (width) e altura (height).

Modificadores (Setters): Alterar as dimensões usando os métodos set_width e set_height.

Cálculos Matemáticos: Calcular as propriedades da forma usando get_area, get_perimeter e get_diagonal.

Representação Visual: Usar get_picture para retornar uma string de asteriscos (*) que desenha a forma (ou retorna uma mensagem de erro se a forma for grande demais).

Encaixe de Formas: Usar get_amount_inside para calcular quantas vezes uma forma passada como argumento cabe inteira dentro da forma atual (sem rotações).

Saída Formatada: Imprimir um objeto Rectangle exibe uma string formatada: Rectangle(width=X, height=Y).

Classe Square (Quadrado): Herda de Rectangle, mas é inicializada com o comprimento de apenas um lado (side). Ela substitui os métodos modificadores (set_width, set_height e introduz set_side) para garantir que a largura e a altura sejam sempre iguais, e sua impressão retorna Square(side=X).