/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ehgui;

import eventhandler.Driver;
import eventhandler.FirebirdEventMaster;
import java.awt.Dimension;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.File;
import java.io.PrintWriter;
import java.io.Serializable;
import java.io.StringWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.Message;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import javax.persistence.*;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import org.firebirdsql.event.DatabaseEvent;
import org.firebirdsql.event.EventListener;

/**
 *
 * @author jrile
 */
@Entity
@Table(name = "EVENTS", catalog = "", schema = "")
@NamedQueries({
    @NamedQuery(name = "Events.findAll", query = "SELECT e FROM Events e"),
    @NamedQuery(name = "Events.findByEventName", query = "SELECT e FROM Events e WHERE e.eventName = :eventName"),
    @NamedQuery(name = "Events.findByEmailTitle", query = "SELECT e FROM Events e WHERE e.emailTitle = :emailTitle"),
    @NamedQuery(name = "Events.findByEmailText", query = "SELECT e FROM Events e WHERE e.emailText = :emailText"),
    @NamedQuery(name = "Events.findBySenderEmail", query = "SELECT e FROM Events e WHERE e.senderEmail = :senderEmail"),
    @NamedQuery(name = "Events.findByAttachPurchaseOrderReport", query = "SELECT e FROM Events e WHERE e.attachPurchaseOrderReport = :attachPurchaseOrderReport")})
public class Events implements Serializable, EventListener {

    @Transient
    private PropertyChangeSupport changeSupport = new PropertyChangeSupport(this);
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @Column(name = "EVENT_NAME")
    private String eventName;
    @Column(name = "EMAIL_TITLE")
    private String emailTitle;
    @Column(name = "EMAIL_TEXT")
    private String emailText;
    @Column(name = "SENDER_EMAIL")
    private String senderEmail;
    @Column(name = "ATTACH_PURCHASE_ORDER_REPORT")
    private Short attachPurchaseOrderReport;

    public Events() {
    }

    public Events(String eventName) {
        this.eventName = eventName;
    }

    public String getEventName() {
        return eventName;
    }

    public void setEventName(String eventName) {
        String oldEventName = this.eventName;
        this.eventName = eventName;
        changeSupport.firePropertyChange("eventName", oldEventName, eventName);
    }

    public String getEmailTitle() {
        return emailTitle;
    }

    public void setEmailTitle(String emailTitle) {
        String oldEmailTitle = this.emailTitle;
        this.emailTitle = emailTitle;
        changeSupport.firePropertyChange("emailTitle", oldEmailTitle, emailTitle);
    }

    public String getEmailText() {
        return emailText;
    }

    public void setEmailText(String emailText) {
        String oldEmailText = this.emailText;
        this.emailText = emailText;
        changeSupport.firePropertyChange("emailText", oldEmailText, emailText);
    }

    public String getSenderEmail() {
        return senderEmail;
    }

    public void setSenderEmail(String senderEmail) {
        String oldSenderEmail = this.senderEmail;
        this.senderEmail = senderEmail;
        changeSupport.firePropertyChange("senderEmail", oldSenderEmail, senderEmail);
    }

    public Short getAttachPurchaseOrderReport() {
        return attachPurchaseOrderReport;
    }

    public void setAttachPurchaseOrderReport(Short attachPurchaseOrderReport) {
        Short oldAttachPurchaseOrderReport = this.attachPurchaseOrderReport;
        this.attachPurchaseOrderReport = attachPurchaseOrderReport;
        changeSupport.firePropertyChange("attachPurchaseOrderReport", oldAttachPurchaseOrderReport, attachPurchaseOrderReport);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (eventName != null ? eventName.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Events)) {
            return false;
        }
        Events other = (Events) object;
        if ((this.eventName == null && other.eventName != null) || (this.eventName != null && !this.eventName.equals(other.eventName))) {
            return false;
        }
        return true;
    }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.removePropertyChangeListener(listener);
    }

    @Override
    public void eventOccurred(DatabaseEvent de) {
        if (Driver.DEBUGGING) {
            DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
            System.out.print("\n[Notifcn]: " + df.format(new Date()) + "--" + de.getEventName() + " occurred. \n\n\tSending emails to:\n\t");
        }
        Session session = Session.getInstance(FirebirdEventMaster.config);
        List emails = new EmailEditor().getEmailsByEventName(eventName);
        MimeMessage msg = new MimeMessage(session);
        int recordId = 0;
        try {
            MimeMultipart mp = new MimeMultipart();
            if (attachPurchaseOrderReport == 1) {
                Connection listenConn = FirebirdEventMaster.getInstance().getConnection();
                String query = "select recordid from eventreports where eventname = ? order by id desc";
                PreparedStatement getPONumber = listenConn.prepareStatement(query);
                getPONumber.setString(1, eventName);
                ResultSet rs = getPONumber.executeQuery();
                rs.next();  //get latest occurrence of event
                Map params = new HashMap();
                recordId = rs.getInt(1);
                params.put("poNum", recordId);
                JasperPrint report = JasperFillManager.fillReport(FirebirdEventMaster.getInstance().getPoReportPath(), params, listenConn);
                JasperExportManager.exportReportToPdfFile(report, recordId + "_report.pdf");
                MimeBodyPart attachment = new MimeBodyPart();
                DataSource ds = new FileDataSource(recordId + "_report.pdf");
                attachment.setDataHandler(new DataHandler(ds));
                attachment.setFileName(recordId + "_report.pdf");
                mp.addBodyPart(attachment);
            }
            MimeBodyPart textPart = new MimeBodyPart();
            textPart.setText(emailText);
            mp.addBodyPart(textPart);
            msg.setContent(mp);
            msg.setFrom(new InternetAddress(senderEmail));
            msg.setSubject(emailTitle);

            for (Object recipient : emails) {
                if (Driver.DEBUGGING) {
                    System.out.print(recipient.toString() + " ");
                }
                msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
                        recipient.toString()));
            }
            Transport.send(msg);
        } catch (Exception e) {
            StringWriter sw = new StringWriter();
            PrintWriter pw = new PrintWriter(sw);
            e.printStackTrace(pw);
            JFrame temp = new JFrame();
            temp.setAlwaysOnTop(true);
            temp.setVisible(true);
            temp.setTitle("Email error!");
            JTextArea error = new JTextArea("Event " + eventName + " has occurred, but there was an error.\n\n\nStack:\n"+sw.toString());
            error.setLineWrap(true);
            error.setWrapStyleWord(true);
            JScrollPane sp = new JScrollPane(error);
            sp.setPreferredSize(new Dimension(400,300));
            JOptionPane.showMessageDialog(temp,
                    sp,
                    "Event Listener Error!",
                    JOptionPane.ERROR_MESSAGE);
            temp.dispose();
        } finally {
            if (attachPurchaseOrderReport == 1) {
                // delete report locally after it has been sent.
                File file = new File(recordId + "_report.pdf");
                file.delete();
            }
        }
        if (Driver.DEBUGGING) {
            System.out.println("\n");
        }
    }

    @Override
    public String toString() {
        return eventName;
    }
}