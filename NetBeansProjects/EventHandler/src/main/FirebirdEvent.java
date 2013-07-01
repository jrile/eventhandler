package main;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

import org.firebirdsql.event.DatabaseEvent;
import org.firebirdsql.event.EventListener;

public class FirebirdEvent implements EventListener {
	String eventName, subject, text, sender;
	ArrayList<String> emails = new ArrayList<String>();

	public FirebirdEvent(String eventName) {
		this(eventName, eventName, eventName
				+ " has been raised from the database.", "noreply@eastcor.com");
	}

	public FirebirdEvent(String eventName, 
			String subject, String text, String sender) {
		this.eventName = eventName;
		this.subject = subject;
		this.text = text;
		this.sender = sender;
	}

	@Override
	public String toString() {
		return eventName;
	}

	public boolean addEmail(String email) {
		return emails.add(email);
	}

	public boolean deleteEmail(String email) {
		return emails.remove(email);
	}

        @Override
	public void eventOccurred(DatabaseEvent arg0) {
		System.out.println(arg0.getEventName() + " occurred!");
		Properties properties = System.getProperties();
		Session session = Session.getDefaultInstance(properties);
		for (String recipient : emails) {
			try {
				MimeMessage msg = new MimeMessage(session);
				msg.setFrom(new InternetAddress(sender));
				msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
						recipient));
				msg.setSubject(subject);
				msg.setText(text);
				Transport.send(msg);

			} catch (MessagingException e) {
				System.out.println("\nError sending email to \'" + recipient
						+ "\'.\nReason:" + e.getMessage());
			}
		}

	}
        
        public void addToDatabase(Connection conn) throws SQLException {
            PreparedStatement ps = conn.prepareStatement("insert into events (event_name, email_title, email_text, sender_email) values (?, ?, ?, ?)");
            ps.setString(1, eventName);
            ps.setString(2, subject);
            ps.setString(3, text);
            ps.setString(4, sender);
            ps.executeUpdate();
            
        }
        
        public void removeFromDatabase(Connection conn) throws SQLException {
            PreparedStatement ps = conn.prepareStatement("delete from events where event_name = ?");
            ps.setString(1, eventName);
            ps.executeUpdate();
        }

	public String getEmails() {
		String out = "";
		for (String email : emails) {
			out += email + "\n";
		}
		return out;
	}
	
	public String print() {
		return eventName + "\n" + emails;
	}

}
