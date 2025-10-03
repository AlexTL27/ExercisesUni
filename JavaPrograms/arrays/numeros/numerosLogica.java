import java.util.Scanner;

public class numerosLogica {

        //LLenar arreglo
    static int[] Rellenar(int[] numeros, Scanner leer){
         for(int a = 0;a<numeros.length;a++ ){
            System.out.println("Ingresa el índice: "+a);

            numeros[a] = leer.nextInt();
        }
        return numeros;
    }
   
    //NUmero mayot metodo
    static void Mayor(int[] numeros){
        int numMax = 0;

        for(int a = 0;a<numeros.length;a++ ){
            if (numeros[a] > numMax){
                numMax=numeros[a];
            }
        }
        System.out.println("Número Mayor: "+numMax);    
    }

    //NUmero menor metodo
    static void Menor(int[] numeros){
        int numMen = numeros[5];

        for(int a = 5;a>=0;a-- ){
            if (numeros[a] < numMen){
                numMen=numeros[a];
            }
        }
        System.out.println("Número menor: "+numMen);

    }
}