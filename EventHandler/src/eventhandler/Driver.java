package eventhandler;

public class Driver {

    /**
     * Gets an instance of the event master and runs the program.
     *
     * @param args Unused
     */
    public static final boolean DEBUGGING = false;

    public static void main(String[] args)  {
        FirebirdEventMaster.getInstance();
    }
}
