/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ehgui;

import eventhandler.Driver;
import eventhandler.FirebirdEventMaster;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.Serializable;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.persistence.*;
import javax.swing.JOptionPane;
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
    @NamedQuery(name = "Events.findByPurchaseOrder", query = "SELECT e FROM Events e WHERE e.purchaseOrder = :purchaseOrder"),
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
    @Column(name = "PURCHASE_ORDER")
    private Short purchaseOrder;
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
        if(purchaseOrder==1 && attachPurchaseOrderReport==1) {
            // attach report here
            this.emailText+="\n\nblablabla";
        }
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

    public Short getPurchaseOrder() {
        return purchaseOrder;
    }

    public void setPurchaseOrder(Short purchaseOrder) {
        Short oldPurchaseOrder = this.purchaseOrder;
        this.purchaseOrder = purchaseOrder;
        changeSupport.firePropertyChange("purchaseOrder", oldPurchaseOrder, purchaseOrder);
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
        // TODO: Warning - this method won't work in the case the id fields are not set
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
        Session session = Session.getInstance(FirebirdEventMaster.getInstance().config);
        List emails = new EmailEditor().getEmailsByEventName(eventName);
        MimeMessage msg = new MimeMessage(session);
        try {
            msg.setFrom(new InternetAddress(senderEmail));
            msg.setSubject(emailTitle);
            msg.setText(emailText);
            for (Object recipient : emails) {
                if (Driver.DEBUGGING) {
                    System.out.print(recipient.toString() + " ");
                }
                msg.addRecipient(Message.RecipientType.TO, new InternetAddress(
                        recipient.toString()));
            }

            Transport.send(msg);

        } catch (MessagingException e) {
            JOptionPane.showMessageDialog(FirebirdEventMaster.getInstance().parent,
                    "Event " + eventName + " has occurred, but there was an error sending the email(s).\n\nReason: " + e.getMessage(),
                    "Email error!",
                    JOptionPane.ERROR_MESSAGE);
            e.printStackTrace();
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