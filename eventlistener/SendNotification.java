package eventlistener;

import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SendNotification implements Runnable {

	private String recipient, sender, subject, text;

	/**
	 * Creates a new notification thread with default values.
	 * 
	 */
	public SendNotification() {
		this.recipient = "jrile@eastcor.com";
		this.sender = "noreply@eastcor.com";
		this.subject = "New insertion into table \'test\'";
		this.text = "A new insertion has been made into table \'test.\'\nWords and stuff";
	}

	/**
	 * Creates a new notification thread with specified values.
	 * 
	 * @param recipient
	 *            The recipient's email address to send to.
	 * @param sender
	 *            The sender's email.
	 * @param subject
	 *            The subject of the email.
	 * @param text
	 *            The text of the email.
	 */
	public SendNotification(String recipient, String sender, String subject,
			String text) {
		this.recipient = recipient;
		this.sender = sender;
		this.subject = subject;
		this.text = text;
	}

	/**
	 * Sends the email out with specified values.
	 */
	public void run() {
		Properties properties = System.getProperties();
		Session session = Session.getDefaultInstance(properties);
		try {
			MimeMessage msg = new MimeMessage(session);
			msg.setFrom(new InternetAddress(sender));
			msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
					recipient));
			msg.setSubject(subject);
			msg.setText(text);
			Transport.send(msg);
		} catch (MessagingException e) {
			System.out.println(e);
		}
	}
}