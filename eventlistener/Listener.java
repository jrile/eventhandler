package eventlistener;

import java.sql.SQLException;
import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;

public class Listener {

	/**
	 * @param args
	 *            Unused.
	 * @throws InterruptedException
	 *             If the user interrupts program, simply print stack and quit.
	 * @throws SQLException
	 *             If there is an error using Firebird.
	 */
	public static void main(String[] args) throws InterruptedException,
			SQLException {

		EventManager em = new FBEventManager();
		em.setHost("localhost");
		em.setUser("SYSDBA");
		em.setPassword("masterkey");
		em.setDatabase("/var/lib/firebird/data/testing.fdb");
		em.connect();
		while (true) {
			if (em.waitForEvent("test_inserted") != -1) { // means we
															// have
															// received
															// an event.
				System.out
						.println("test_inserted has been raised! Sending email...");
				/* customize message: */
				new Thread(new SendNotification("jrile@eastcor.com", "test@eastcor.com",
						"Overloaded test", "Howdy!\nTest \ttest")).start();
				/* or send generic message: */
				// new SendNotification().start();
			}
		}
	}
}