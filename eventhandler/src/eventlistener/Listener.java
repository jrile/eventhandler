package eventlistener;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;

public class Listener {

	/**
	 * @param args
	 * @throws InterruptedException
	 * @throws SQLException
	 */
	public static void main(String[] args) throws InterruptedException,
			SQLException {

		EventManager em = new FBEventManager();
		em.setHost("localhost");
		em.setUser("SYSDBA");
		em.setPassword("masterkey");
		em.setDatabase("/var/lib/firebird/data/testing.fdb");
		em.connect();
		Thread t = new Thread() {
			public void run() {
				Connection conn;
				try {
					conn = DriverManager
							.getConnection(
									"jdbc:firebirdsql:localhost/3050:/var/lib/firebird/data/testing.fdb",
									"SYSDBA", "masterkey");
					Statement stmt = conn.createStatement();
					for (int i = 0; i < 5; i++) {
						// add the values to the table 5 times.
						stmt.execute("insert into test (a, b) values (99, 200)");
					}
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		};
		t.start();

		int count = em.waitForEvent("test_inserted", 5 * 1000);
		if (count != -1) { // means we have recieved an event.
			Properties properties = System.getProperties();
			Session session = Session.getDefaultInstance(properties);
			try {
				MimeMessage msg = new MimeMessage(session);
				msg.setFrom(new InternetAddress("test@test.com"));
				msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
						"jrile@eastcor.com"));
				msg.setSubject("Test");
				msg.setText("Table has been updated!!");
				Transport.send(msg);
			} catch (MessagingException e) {
				System.out.println(e);
			}

		}

	}

}
