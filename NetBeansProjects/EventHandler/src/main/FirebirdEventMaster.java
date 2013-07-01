package main;

import ehgui.EmailEditor;
import ehgui.EventEditor;
import java.awt.AWTException;
import java.awt.Image;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.Query;

import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;
import org.firebirdsql.jdbc.FBSQLException;
import javax.swing.JFrame;

public class FirebirdEventMaster {
    // singleton:

    private static FirebirdEventMaster instance = null;

    public static FirebirdEventMaster getInstance() {
        if (instance == null) {
            instance = new FirebirdEventMaster();
        }
        return instance;
    }
    // TODO: read from XML file
    static String eventHost = "localhost";
    static int eventPort = 3050;
    static String eventDatabase = "/var/lib/firebird/data/events.fdb";
    static String eventUser = "sysdba";
    static String eventPass = "masterkey";
    static String listenHost = "localhost";
    static int listenPort = 3050;
    static String listenUser = "sysdba";
    static String listenPass = "masterkey";
    static String listenDatabase = "/var/lib/firebird/data/testing.fdb";
    static ArrayList<FirebirdEvent> events = new ArrayList<FirebirdEvent>();
    private Connection conn;
    private EventManager em = new FBEventManager();

    protected FirebirdEventMaster() {
        
        
        

        try {
            // TODO: make config file an argument
                    this.conn = DriverManager
      .getConnection(
      "jdbc:firebirdsql:" + eventHost + "/" + eventPort + ":/" + eventDatabase, eventUser, eventPass);
            em.setHost(listenHost);
            em.setUser(listenUser);
            em.setPassword(listenPass);
            em.setDatabase(listenDatabase);
            em.connect();
                    
        EntityManager entityManager = java.beans.Beans.isDesignTime() ? null : javax.persistence.Persistence.createEntityManagerFactory("events.fdbPU").createEntityManager();
        Query query = java.beans.Beans.isDesignTime() ? null : entityManager.createQuery("SELECT e FROM Events e");
        List<ehgui.Events> list = java.beans.Beans.isDesignTime() ? java.util.Collections.emptyList() : org.jdesktop.observablecollections.ObservableCollections.observableList(query.getResultList());
        for (ehgui.Events event : list) {
            System.out.println(event.toString());
            listen(event);
        }
        
            //read();
            createGUI();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }


    private void createGUI() {
        final JFrame parent = new JFrame();
        parent.setTitle("Firebird Event Handler");
        SystemTray systray = SystemTray.getSystemTray();
        Image image = Toolkit.getDefaultToolkit().getImage("EventHandler/src/eventhandler/firebird.jpeg");
        PopupMenu menu = new PopupMenu();
        MenuItem events = new MenuItem("Edit Events");
        menu.add(events);
        events.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parent.setContentPane(new EventEditor());
                parent.pack();
                parent.setVisible(true);
            }
        });
        
        MenuItem emails = new MenuItem("Edit Emails");
        menu.add(emails);
        emails.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parent.setContentPane(new EmailEditor());
                parent.pack();
                parent.setVisible(true);
            }
        });

        menu.addSeparator();
        
        MenuItem exit = new MenuItem("Exit");
        menu.add(exit);
        exit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        TrayIcon icon = new TrayIcon(image, "Firebird Event Listener", menu);
        try {
            systray.add(icon);
        } catch (AWTException ex) {
            ex.printStackTrace();
        }
    }
    
    public void listen(ehgui.Events event) {
        try {
            em.addEventListener(event.toString(), event);
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    private void read() throws SQLException {
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
                
                System.out.println(event_name);
                getEmails.setString(1, event_name);
                ResultSet emails = getEmails.executeQuery();
                FirebirdEvent event = new FirebirdEvent(event_name, email_title, email_text, sender);
                events.add(event);
                while (emails.next()) {
                    event.addEmail(emails.getString(1));
                }
                em.addEventListener(event.toString(), event);

            }
        } catch (FBSQLException e) {
            // result set is closed, ignore
            e.printStackTrace();
        } finally {
            stmt.close();
            getEmails.close();
        }


    }


    public void addEvent(FirebirdEvent event) {
        try {
            event.addToDatabase(conn);
            events.add(event);
            em.addEventListener(event.toString(), event);
            
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    public boolean removeEvent(String eventname) {
        for (FirebirdEvent event : events) {
            if (event.toString().equals(eventname)) {
                try {
                    event.removeFromDatabase(conn);
                    em.removeEventListener(event.toString(), event);
                    return events.remove(event);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
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
    public static ArrayList<FirebirdEvent> getList() {
        return events;
    }
}
