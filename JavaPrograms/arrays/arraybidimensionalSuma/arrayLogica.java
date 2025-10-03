import java.util.Scanner;

public class arrayLogica {

    //LLenamos el array
    static int[][] llenarArray(Scanner leer){
    
        int[][] array = new int[2][6];

        for(int f = 0; f < array.length;f++){
            for(int c = 0; c < array[0].length;c++){
                System.out.print("Introduce los valores "+f+"-"+c+":");
                array[f][c] = leer.nextInt();
            }
        }
        return array;
    }

    //Sumar matriz
    static int sumarArray(int[][] array){

        if (array == null){System.out.println("Array aún no a sido inicializado");return 0;}

        int suma = 0;
        for(int f = 0; f < array.length;f++){
            for(int c = 0; c < array[0].length;c++){
                
                suma += array[f][c];

            }
        }
        return suma;
    }
    //Impares
    static int SumarImpares(int[][] array){
        if (array == null){System.out.println("Array aún no a sido inicializado");return 0;}

        int impares = 0;
        for(int f = 0; f < array.length;f++){
            for(int c = 0; c < array[0].length;c++){
                
                if( array[f][c] % 2 != 0){
                    impares += array[f][c];
                    
                }

            }
        }
        return impares;
    }
    
    static void BuscarNumero(int[][] array, int buscado){
        if (array == null){System.out.println("Array aún no a sido inicializado"); return;}

        int TotalEncontrado = 0;
        for(int f = 0; f < array.length;f++){
            for(int c = 0; c < array[0].length;c++){
                
                  if(array[f][c] == buscado){
                    TotalEncontrado ++;
                  }

            }
        }
        if (TotalEncontrado == 0){
            System.out.println("El número "+ buscado+" no fue encontrado ");
        }
        else{
            System.out.println("El número "+ buscado+" fue encontrado un total de: " + TotalEncontrado +" veces" );

        }
       
    }
    
}