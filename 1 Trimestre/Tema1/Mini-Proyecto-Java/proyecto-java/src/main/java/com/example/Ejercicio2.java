package com.example;

public class Ejercicio2 {
    public static void main(String[] args) {
        int[] numeros = {3, 4, 7, 10, 12, 15, 18};
        
        
        int contadorPares = 0;

        for (int i = 0; i < numeros.length; i++) {
            int num=numeros[i];
            if (num%2==0) {
                contadorPares++;
            }
        }

        System.out.println("Cantidad de números pares: " + contadorPares);
    }
}
