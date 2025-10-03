import java.util.Scanner;

public class numeros {
    public static void main(String[] args) {
        int[] numeros = new int[6];
        Scanner leer = new Scanner(System.in);

    
        boolean bandera = true;
        String opc = "0";
        numeros = Rellenar(numeros,leer);

        while (bandera) {
             System.out.println("Bienvenido a Buscador de Número\nIngresa el número dado para\n1.-LLenar arreglo\n2.-Saber Número Mayor\n3.-Saber número menor\n4.-Salir");
        
             opc = leer.nextLine();       
        
            switch (opc) {
                
            case "2":
                numerosLogica.Mayor(numeros);
                break;
            case "3":                
                numerosLogica.Menor(numeros);
                break; 
            case "4":
            bandera = false;
            System.out.println("Adiosss");
            break;
            default:
                System.out.println("No indico nada");
                break;
        }       
    
        

    }
    leer.close();

    }
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
