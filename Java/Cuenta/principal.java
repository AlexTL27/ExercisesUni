package Cuenta;//NOmbre de la carpeta
import java.util.Scanner;

public class principal {
    public static void main(String[] args) {
        
        Scanner read = new Scanner(System.in);
        Cuenta Objcuenta = new Cuenta();


        System.out.println("El saldo es: "+Objcuenta.setSaldo(120.50f));

        //Nombre del cliente
        System.out.println("Introduce tu nombre");
        String nombre = read.nextLine();
        Objcuenta.setCLiente(nombre);
        System.out.println("Bienvenido de nuevo " + nombre);

        //retiro
        System.out.println("Cuánto deseas retirar? :");
        float retiro = read.nextFloat();
        
        System.out.println("Saldo despues del retiro: "+ Objcuenta.Retiro(retiro));

        read.close();
    }
}