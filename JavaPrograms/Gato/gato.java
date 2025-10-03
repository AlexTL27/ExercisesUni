import java.util.Scanner;
public class gato {
    
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        String player1 = "X";
        String player2 = "O";
        boolean empate = false;
        //Primero llenaremos la matriz
        String[][] mapa = gatoLogica.crearMapa(leer);

        //HACEMOS QUE LOS USUARIOS PUEDA INGRESAR DATOS PARA LA POSICION
        //Empieza el juego

        
        boolean turno = true;
        int numTirada = 0; //para tener un empate
        String tirada;

        while (true) {
            
            
            //Turno de player 1 tendra 11
            if(turno){
                do{
                    System.out.println("Turno de player 1");
                    tirada = leer.nextLine();
                }while(gatoLogica.llenarMapa(mapa,tirada , player1));
                
                if(gatoLogica.AlguienGano(mapa, player1)){
                    //Alguien a ganado, se rompera el while y saldra
                    break;
                    
                }
                turno =!(turno);

            }
            //Turno de player 2, //player 2 tendra 0
            else{
                do{
                    System.out.println("Turno de player 2");
                    tirada = leer.nextLine();
                }while(gatoLogica.llenarMapa(mapa,tirada , player2));

                
                if(gatoLogica.AlguienGano(mapa, player2)){
                    //Alguien a ganado, se rompera el while y saldra
                    break;
                    
                }
                turno =!(turno);
                
            }
            numTirada ++;
            //verificar si se ejecuta un empate
            if (numTirada >= 9){
                empate = true;
                break;
            }
           
        }

        //Verifiación del ganador
        if(empate){
            System.out.println("Empate, Nadie ganó");

        }
        else{
            if(turno){
                System.out.println("El jugador 1 a ganado");
            }
            else{
                System.out.println("El jugador 2 a ganado");
            }
        }
    }
}
   


