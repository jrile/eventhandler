package eventhandler;

import java.util.ArrayList;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SendMessage implements Runnable {

	private String sender, subject, text;
	private ArrayList<String> recipients;

	/**
	 * Creates a new notification thread with default values.
	 * 
	 */
	public SendMessage() {
		this("jrile@eastcor.com", "noreply@eastcor.com",
				"New insertion into table.", "A new insertion has been made.\n");
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
	public SendMessage(String recipient, String sender, String subject,
			String text) {
		this.recipients.add(recipient);
		this.sender = sender;
		this.subject = subject;
		this.text = text;
	}

	public SendMessage(ArrayList<String> recipients, String sender,
			String subject, String text) {
		this.recipients = recipients;
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
			for (String recipient : recipients) {
				MimeMessage msg = new MimeMessage(session);
				msg.setFrom(new InternetAddress(sender));
				msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
						recipient));
				msg.setSubject(subject);
				msg.setText(text);
				Transport.send(msg);
			}
		} catch (MessagingException e) {
			System.out.println(e);
		}
	}
}