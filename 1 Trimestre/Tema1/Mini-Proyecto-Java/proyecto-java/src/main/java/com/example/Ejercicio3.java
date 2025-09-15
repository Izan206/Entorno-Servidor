package com.example;

public class Ejercicio3 {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};
        int[] nuevoArray={};

        for (int i = numeros.length-1; i >=0 ; i--) {
            nuevoArray[i]=numeros[i];
            
        }
        for (int i = 0; i < nuevoArray.length; i++) {
            System.out.print(nuevoArray[i] + " ");
        }
    }
}
