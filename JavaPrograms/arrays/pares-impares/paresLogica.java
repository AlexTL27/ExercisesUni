import java.util.Scanner;

public class paresLogica {
    static void valores(int[] valores, Scanner leer){
        
        int pares = 0;
        int paresNum = 0;
        int impares = 1;
        int imparesNum = 0;

        for(int a = 0; a<valores.length;a++){
        System.out.println("Indica el valor "+a+":");

            valores[a] = leer.nextInt();

            //Sacar par
            if((valores[a] % 2) == 0){
                pares += valores[a];
                paresNum++;
            }
            else{
                impares *= valores[a];
                imparesNum++;

            }
        }
        
        System.out.println("Pares: "+ pares + "   Total de Pares: "+ paresNum);
        System.out.println("Impares: "+ impares + "   Total de impares: "+ imparesNum);
    }
}
