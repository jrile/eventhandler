package eventhandler;

import java.io.FileNotFoundException;
import java.sql.SQLException;
import main.FirebirdEventMaster;


public class Listener {

	/**
	 * @param args
	 *            Unused.
	 * @throws InterruptedException
	 *             If the user interrupts program, simply print stack and quit.
	 * @throws SQLException
	 *             If there is an error using Firebird.
	 * @throws FileNotFoundException
	 */
	public static void main(String[] args) throws InterruptedException,
			SQLException, FileNotFoundException {
        
		FirebirdEventMaster fem = new FirebirdEventMaster();
		try {
			fem.read();
			System.out.println(fem);


		}
		catch(SQLException e) {
			e.printStackTrace();
		}
		
		for(;;) { }
	}
}