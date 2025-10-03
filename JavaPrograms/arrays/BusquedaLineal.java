import java.util.Scanner;

class BusquedaLineal{

    //Method main
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        BuscarPalabra(CrearArray(leer),leer.nextLine());     
        leer.close();
    }
    
    static String[] CrearArray(Scanner ola){
    
        String[] palabras = new String[5];
        for(int i = 0; i < palabras.length; i++){
            System.out.println("Ingresa la palabra Para el índice número: "+ (i));
            palabras[i] = ola.nextLine();
        }
    
        System.out.println("Ingresa la palabra a buscar");
        return palabras;
    }

    static void BuscarPalabra(String[] palabras, String palabraUser){
        int indice = 0;
        boolean bandera = true;
        for (String string : palabras) {
            if(palabraUser.equals(string)){
                System.out.println("Palabra "+ palabraUser+" Encontrada en el índice: "+ indice);
                bandera = false;
                break;
            }
            indice++;
        }
        if(bandera){
            System.out.println("Palabra "+ palabraUser+" No fue Encontrada");
            }   
    }
}