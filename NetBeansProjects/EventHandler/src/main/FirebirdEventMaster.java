package main;

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
import java.io.File;
import java.io.FileNotFoundException;
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
import java.util.Scanner;
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
    // TODO: will the username/password combinations be different or the same?
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
            readConfig("/home/colgado/NetBeansProjects/EventHandler/src/eventhandler/ehconfig");
            read();
            createGUI();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }


    private void createGUI() {
        final JFrame parent = new JFrame();
        SystemTray systray = SystemTray.getSystemTray();
        Image image = Toolkit.getDefaultToolkit().getImage("EventHandler/src/eventhandler/firebird.jpeg");
        PopupMenu menu = new PopupMenu();
        MenuItem events = new MenuItem("Edit Events");
        menu.add(events);
        events.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parent.setTitle("Firebird Event Editor");
                parent.setContentPane(new EventEditor());
                parent.pack();
                parent.setVisible(true);
            }
        });

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

    private void readConfig(String path) {
        //TODO: change to java Properties...
        try {
            Scanner sc = new Scanner(new File(path));
            eventHost = sc.nextLine().substring(11);
            eventPort = Integer.parseInt(sc.nextLine().substring(11));
            eventDatabase = sc.nextLine().substring(15);
            eventUser = sc.nextLine().substring(11);
            eventPass = sc.nextLine().substring(11);
            listenHost = sc.nextLine().substring(12);
            listenPort = Integer.parseInt(sc.nextLine().substring(12));
            listenDatabase = sc.nextLine().substring(16);
            listenUser = sc.nextLine().substring(12);
            listenPass = sc.nextLine().substring(12);
            sc.close();
            System.out.println(eventHost + eventPort + eventDatabase + eventUser + eventPass);
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        }
    }
    public static ArrayList<FirebirdEvent> getList() {
        return events;
    }
}
