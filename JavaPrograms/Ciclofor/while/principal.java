class principal{
    public static void main(String[] args) {
        
        MostrarWhile(1);
    }


    static void MostrarWhile(int a){
        while(a <= 5){
            System.out.println("SOy a vuelta número: "+ a);
            a++;
        }
    }
}