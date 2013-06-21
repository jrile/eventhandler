package main;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;
import org.firebirdsql.jdbc.FBSQLException;

import main.FirebirdEvent;





public class FirebirdEventMaster {
	// TODO: will the username/password combinations be different or the same?
	final String eventDatabase = "jdbc:firebirdsql:localhost/3050:/var/lib/firebird/data/events.fdb";
	final String eventUser = "sysdba";
	final String eventPass = "masterkey";
	final String listenHost = "localhost";
	final String listenUser = "sysdba";
	final String listenPass = "masterkey";
	final String listenDatabase = "/var/lib/firebird/data/testing.fdb";
	
	ArrayList<FirebirdEvent> events = new ArrayList<FirebirdEvent>();

	public void read() throws SQLException {
		Connection conn = DriverManager
				.getConnection(
						eventDatabase, eventUser, eventPass);
		Statement stmt = conn.createStatement();
		PreparedStatement getEmails = conn
				.prepareStatement("select email_address from emails where event_name = ?");
		ResultSet rs = stmt
				.executeQuery("select event_name, email_title, email_text, sender_email from events");
		try {
			while (rs.next()) {
				String event_name = rs.getString(1);
				String email_title = rs.getString(2);
				String email_text = rs.getString(3);
				String sender = rs.getString(4);
				getEmails.setString(1, event_name);
				ResultSet emails = getEmails.executeQuery();
				ArrayList<String> emailList = new ArrayList<String>();
				while (emails.next()) {
					emailList.add(emails.getString(1));
				}
				events.add(new FirebirdEvent(event_name, emailList,
						email_title, email_text, sender));
			}
		} catch (FBSQLException e) {
			// result set is closed, ignore
		
		} finally {
			stmt.close();
			getEmails.close();
		}
		
		listen();

	}

	private void listen() throws SQLException {
		EventManager em = new FBEventManager();
		em.setHost(listenHost);
		em.setUser(listenUser);
		em.setPassword(listenPass);
		em.setDatabase(listenDatabase);
		em.connect();
		for (FirebirdEvent event : events) {
			em.addEventListener(event.toString(), event);
		}
	}

	public void addEvent(FirebirdEvent event) {
		events.add(event);
	}

	public boolean removeEvent(String eventname) {
		for (FirebirdEvent event : events) {
			if (event.toString().equals(eventname)) {
				return events.remove(event);
			}
		}
		return false;
	}

	@Override
	public String toString() {
		String out = "";
		for (FirebirdEvent event : events) {
			out += event.print() + "\n";
		}
		return out;
	}

}
