import java.util.Scanner;
public class pares{
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int[] valores = new int[5];

        paresLogica.valores(valores, leer);
        leer.close();

    }
}