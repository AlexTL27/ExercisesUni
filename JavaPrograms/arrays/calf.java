import java.util.Scanner;
public class calf {


    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        float[] calificaciones = new float[5];
        float total = 0;

        for (int i = 0; i < calificaciones.length; i++) {
            System.out.println("Ingresa la calificación número: " + (i + 1));
            calificaciones[i] = leer.nextFloat();
            total += calificaciones[i];
        }

        System.out.println("Promedio: " + (total / calificaciones.length));
        leer.close();
    }
}
