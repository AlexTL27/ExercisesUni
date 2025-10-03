import java.util.Scanner;

public class gatoLogica {
    
    public static boolean AlguienGano(String[][] mapa,String player){
        //verificar si alguien ya gano
        if((mapa[0][0].equals(player) & mapa[0][1].equals(player) & mapa[0][2].equals(player)) || (mapa[1][0].equals(player) & mapa[1][1].equals(player) & mapa[1][2].equals(player)) || (mapa[2][0].equals(player) & mapa[2][1].equals(player) & mapa[2][2].equals(player)) || (mapa[0][0].equals(player) & mapa[1][0].equals(player) & mapa[2][0].equals(player)) || (mapa[0][1].equals(player) & mapa[1][1].equals(player) & mapa[2][1].equals(player)) || (mapa[0][2].equals(player) & mapa[1][2].equals(player) & mapa[2][2].equals(player)) || (mapa[0][0].equals(player) & mapa[1][1].equals(player) & mapa[2][2].equals(player)) || (mapa[2][0].equals(player) & mapa[1][1].equals(player) & mapa[0][2].equals(player))){
             return true;

        }
        return false;
    }

    public static String[][] crearMapa(Scanner leer){
        //Primero llenaremos la matriz
        String[][] mapa = new String[3][3];
        int index = 1;
        for(int a = 0; a < mapa.length;a++){
            for(int b = 0; b < mapa[1].length;b++){
                mapa[a][b] =  Integer.toString(index) ;

                index++;
            }
        }
         //Imprimir mapa
        for(int c = 0; c < mapa.length;c++){
            System.out.println("---------------");            
            System.out.println(mapa[c][0] +"   |   " +mapa[c][1] + "   |   " + mapa[c][2]  );
        }
        return mapa;
    }

    public static boolean llenarMapa(String[][] mapa, String posicion, String player){
        
        

        for(int a = 0; a < mapa.length;a++){
            for(int b = 0; b < mapa[1].length;b++){
                
                if ((mapa[a][b].equals(posicion) ) && (Integer.parseInt(mapa[a][b]) > 0 && Integer.parseInt(mapa[a][b]) <= 9)){
                
                   
                    mapa[a][b] = player;

                         //Imprimir mapa
                    for(int c = 0; c < mapa.length;c++){
                        System.out.println("---------------");            
                        System.out.println(mapa[c][0] +"  |  " +mapa[c][1] + "  |  " + mapa[c][2]  );
                    }
                    return false;

                }
                    
            }         
            }
            System.out.println("Lugar inválido");
             //Imprimir mapa
            for(int c = 0; c < mapa.length;c++){
                System.out.println("-----");            
                System.out.println(mapa[c][0] +"  |  " +mapa[c][1] + "  |  " + mapa[c][2]  );
            }
            return true;
        }
}
