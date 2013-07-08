package eventhandler;

public class Driver {

    /**
     * Gets an instance of the event master and runs the program.
     *
     * @param args Unused
     */
    public static final boolean DEBUGGING = true;

    public static void main(String[] args) {

        String propPath = System.getProperty( "CONFIG.properties" );
        System.out.println(propPath);

        FirebirdEventMaster.getInstance();
    }
}