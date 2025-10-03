import java.util.Scanner;
class arrayBidimensional{
    public static void main(String[] args) {
        
        Scanner leer = new Scanner(System.in);
        boolean romper = true;
        int[][] array = null;
        while (romper) {
            System.out.println("Selecciona una Opción\n1.-LLenar matriz\n2.-Sumar Matriz\n3.-Sumar Impares\n4.-Buscar un número\n5.-Salir");
            String op = leer.nextLine();

            switch (op) {
                case "1":
                    array = arrayLogica.llenarArray(leer);
                    System.out.print("===============\n");

                    for(int f = 0; f < array.length;f++){
                         for(int c = 0; c < array[0].length;c++){
                            System.out.print(array[f][c]);
                            
                        }
                        System.out.println(" ");
                    }       
                    System.out.print("===============\n");

                    break;
                case "2":
                    
                    System.out.println("Suma total: " + arrayLogica.sumarArray(array));
                    break;
                
                case "3":
                    System.out.println("Suma total de impares: " + arrayLogica.SumarImpares(array));
                    break;
                case "4":
                    System.out.print("Ingresa el número a buscar: ");
                    int numBuscar = leer.nextInt();
                    arrayLogica.BuscarNumero(array, numBuscar);
                    break;
                case "5":
                    romper = false;
                    break;
                default:
                    break;
            }

        }
        leer.close();

        //Antes de empezar, necesitamos llenar el array de 2x6
        
    }
}