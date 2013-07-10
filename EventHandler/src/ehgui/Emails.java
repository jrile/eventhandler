package ehgui;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.Serializable;
import javax.persistence.*;

/**
 * Email class that contains the default email text, email subject, and email to
 * "send" from.
 *
 * @author jrile
 */
@Entity
@Table(name = "EMAILS", catalog = "", schema = "")
@NamedQueries({
    @NamedQuery(name = "Emails.findAll", query = "SELECT e FROM Emails e"),
    @NamedQuery(name = "Emails.findById", query = "SELECT e FROM Emails e WHERE e.id = :id"),
    @NamedQuery(name = "Emails.findByEmailAddress", query = "SELECT e FROM Emails e WHERE e.emailAddress = :emailAddress"),
    @NamedQuery(name = "Emails.findByEventName", query = "SELECT e FROM Emails e WHERE e.eventName = :eventName")})
public class Emails implements Serializable {

    @Transient
    private PropertyChangeSupport changeSupport = new PropertyChangeSupport(this);
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @Column(name = "ID")
    private Integer id;
    @Column(name = "EMAIL_ADDRESS")
    private String emailAddress;
    @Column(name = "EVENT_NAME")
    private String eventName;

    public Emails() {
    }

    /**
     *
     * @param id The automatically assigned unique ID number from the database.
     */
    public Emails(Integer id) {
        this.id = id;
    }

    /**
     *
     * @return The automatically assigned unique ID number from the database.
     */
    public Integer getId() {
        return id;
    }

    /**
     * Sets ID number to 'id'.
     *
     * @param id The ID number to change to.
     */
    public void setId(Integer id) {
        Integer oldId = this.id;
        this.id = id;
        changeSupport.firePropertyChange("id", oldId, id);
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public void setEmailAddress(String emailAddress) {
        String oldEmailAddress = this.emailAddress;
        this.emailAddress = emailAddress;
        changeSupport.firePropertyChange("emailAddress", oldEmailAddress, emailAddress);
    }

    public String getEventName() {
        return eventName;
    }

    public void setEventName(String eventName) {
        String oldEventName = this.eventName;
        this.eventName = eventName;
        changeSupport.firePropertyChange("eventName", oldEventName, eventName);
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Emails)) {
            return false;
        }
        Emails other = (Emails) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return emailAddress;
    }

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.removePropertyChangeListener(listener);
    }
}
