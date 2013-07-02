package eventhandler;


public class Driver {

/**
 * Gets an instance of the event master and runs the program.
 * @param args
 * @throws InterruptedException If the user types a command to interrupt the program.
 */
    public static void main(String[] args) throws InterruptedException {
        FirebirdEventMaster.getInstance();
        while (true) { }
    }
}