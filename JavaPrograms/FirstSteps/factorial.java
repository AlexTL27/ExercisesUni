package FirstSteps;
import java.util.Scanner;
public class factorial {
    public static void main(String[] args) {
        System.out.println("Ingresa un número: ");
        Scanner leer = new Scanner(System.in);
        int value = leer.nextInt();

        for(int a = value - 1 ; a > 1; a--){
            
            //value no se toca, a se disminuye

            value *= a;
            
        }
        leer.close();
            System.out.println("El factorial es: "+ value);


    }
}
