# matrix-multiplication

This is a Python program that performs matrix multiplication. The program prompts the user to enter the dimensions and values of two matrices, checks if they can be multiplied, performs the multiplication, and prints the resulting matrix.

## Table of Contents
* Introduction
* How it Works
* Error Handling

## Introduction
Matrix multiplication is a fundamental operation in linear algebra, and is used in a wide range of applications, such as computer graphics, physics simulations, and machine learning. This program provides an easy-to-use tool for performing matrix multiplication, without the need for complex mathematical calculations.

## How it Works
This program consists of three functions:

enter(): This function prompts the user to enter the dimensions of the matrices and checks if they can be multiplied. If the matrices can be multiplied, it returns a list containing their dimensions.

matrix(): This function prompts the user to enter the values of the matrices, and returns two matrices as lists of lists.

mult(): This function performs the matrix multiplication using nested loops and the zip() function, and returns the resulting matrix as a list of lists.

The program uses these functions to perform the matrix multiplication, and prints the resulting matrix using nested loops.

## Error Handling
This program handles errors gracefully and provides clear prompts and error messages to the user. The enter() function checks if the dimensions of the matrices are valid, and prompts the user to enter them again if they are not. The matrix() function prompts the user to enter the values of the matrices, and handles errors if the input is not a valid integer. If the matrices cannot be multiplied, the program prints an error message and prompts the user to enter the dimensions again.

