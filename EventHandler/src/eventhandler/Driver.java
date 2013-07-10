package eventhandler;

import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.JasperFillManager;

public class Driver {

    /**
     * Gets an instance of the event master and runs the program.
     *
     * @param args Unused
     */
    public static final boolean DEBUGGING = true;

    public static void main(String[] args) throws JRException {

        String propPath = System.getProperty( "CONFIG.properties" );
        System.out.println(propPath);

        FirebirdEventMaster.getInstance();
    }
}