package FirstSteps;
import java.util.Scanner;
class CrearClase{
    public static void main(String[] args) {
        
        Scanner leer = new Scanner(System.in);
        Operaciones oper = new Operaciones();

        System.out.println("Selecciona el número para: \n1.-Sumar \n2.-Restar \n3.-Multiplicar \n4.-Dividir");
        
        int opcion = leer.nextInt();
        System.out.println("Ingresa el primer Valor");
        oper.suma1 = leer.nextInt();

        System.out.println("Ingresa el Segundo Valor");
        oper.suma2 = leer.nextInt();

   

        switch (opcion) {
            case 1:
                System.out.println(oper.Sumar());
                break;
            case 2:
                System.out.println(oper.Restar());
                break;
            case 3:
                System.out.println(oper.Multiplicar());
                break;
            case 4:
                System.out.println(oper.Dividir());
                break;
            default:
                System.out.println("No seleccionaste algo válido");

                break;
        }

        
        leer.close();
        
        
        
    }

    static class Operaciones{
        int suma1 = 0;
        int suma2 = 0;

        int Sumar(){
            return suma1 + suma2;
        }
        int Restar(){
            return suma1 - suma2;
        }
        int  Multiplicar(){
            return suma1 * suma2;
        }
        int Dividir(){
            if(suma2 == 0){ 
                System.out.println("Error");
                return 0;
            }
            else{
                return suma1 / suma2;

            }
        }
    }

    
}

