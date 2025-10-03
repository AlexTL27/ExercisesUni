package Cuenta;

public class Cuenta {

    private float saldo = 0;
    String cliente = "";

    float setSaldo(float nvoSaldo){
        saldo = nvoSaldo;
        return saldo;
    }

    float Retiro(float cant){
        saldo -= cant;
        return saldo;
    }
    void setCLiente(String nvoCliente){
        cliente = nvoCliente;
    }
    
}