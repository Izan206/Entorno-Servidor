package com.example;

public class Ejercicio4 {
    public static void main(String[] args) {
        String palabra = "hola";
        boolean esPalindromo = false;
        String nuevaPalabra="";
        
        for (int i = palabra.length()-1; i>=0; i--) {
            char c=palabra.charAt(i);
            nuevaPalabra+=c;
            if (nuevaPalabra==palabra) {
                esPalindromo=true;
            }
        }
        System.out.println(nuevaPalabra);
        if (esPalindromo==true) {
            System.out.println(palabra + " es un palíndromo.");
        } else {
            System.out.println(palabra + " no es un palíndromo.");
        }
        
    }
}
