/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ehgui;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.persistence.Transient;

/**
 *
 * @author colgado
 */
@Entity
@Table(name = "EVENTS", catalog = "", schema = "")
@NamedQueries({
    @NamedQuery(name = "Events.findAll", query = "SELECT e FROM Events e"),
    @NamedQuery(name = "Events.findByEventName", query = "SELECT e FROM Events e WHERE e.eventName = :eventName"),
    @NamedQuery(name = "Events.findByEmailTitle", query = "SELECT e FROM Events e WHERE e.emailTitle = :emailTitle"),
    @NamedQuery(name = "Events.findByEmailText", query = "SELECT e FROM Events e WHERE e.emailText = :emailText"),
    @NamedQuery(name = "Events.findBySenderEmail", query = "SELECT e FROM Events e WHERE e.senderEmail = :senderEmail")})
public class Events implements Serializable {
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

    @Override
    public String toString() {
        return "ehgui.Events[ eventName=" + eventName + " ]";
    }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.removePropertyChangeListener(listener);
    }
    
}
