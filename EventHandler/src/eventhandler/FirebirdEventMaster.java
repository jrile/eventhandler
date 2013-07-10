package eventhandler;

import ehgui.EmailEditor;
import ehgui.EventEditor;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.persistence.EntityManager;
import javax.persistence.Query;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;

public class FirebirdEventMaster {
    // singleton:

    private static FirebirdEventMaster instance = null;

    public static FirebirdEventMaster getInstance() {


        if (instance == null) {
            instance = new FirebirdEventMaster();
        }
        return instance;
    }
    private static String listenHost, listenUser, listenPass, listenDatabase, eventHost, eventUser, eventPass, eventDatabase;
    private static int listenPort, eventPort;
    public EventManager em = new FBEventManager();
    public static Properties config = new Properties();
    public final JFrame parent = new JFrame();
    private Connection connection;

    /**
     * Constructs an event master to handle all of the events and listen for
     * them.
     *
     */
    protected FirebirdEventMaster() {

        config = new Properties();
        try {
            InputStream file = Thread.currentThread().getContextClassLoader().getResourceAsStream("CONFIG.properties");
            config.load(file);
            listenHost = config.getProperty("listenHost", "localhost");
            listenPort = Integer.parseInt(config.getProperty("listenPort", "3050"));
            listenUser = config.getProperty("listenUser", "sysdba");
            listenPass = config.getProperty("listenPass", "masterkey");
            listenDatabase = config.getProperty("listenDatabase", "C:\\EASTCOR.FDB");

            eventHost = config.getProperty("eventHost", "localhost");
            eventPort = Integer.parseInt(config.getProperty("eventPort", "3050"));
            eventUser = config.getProperty("eventUser", "sysdba");
            eventPass = config.getProperty("eventPass", "masterkey");
            eventDatabase = config.getProperty("eventDatabase", "C:\\EVENTS.FDB");
            if (Driver.DEBUGGING) {
                System.out.println("Config file loaded:\nlistenHost=" + listenHost + "\nlistenPort=" + listenPort + "\nlistenUser=" + listenUser + "\nlistenPass=" + listenPass + "\nlistenDatabase=" + listenDatabase);
                System.out.println("\neventHost=" + eventHost + "\neventPort=" + eventPort + "\neventUser=" + eventUser + "\neventPass=" + eventPass + "\neventDatabase=" + eventDatabase);
            }
            
            connection =  DriverManager.getConnection("jdbc:firebirdsql:localhost/3050:c:/EASTCOR.fdb", listenUser, listenPass);
            connection.setAutoCommit(false);

        } catch (IOException ex) {
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE,null,ex);
        }
        try {
            em.setHost(listenHost);
            em.setPort(listenPort);
            em.setUser(listenUser);
            em.setPassword(listenPass);
            em.setDatabase(listenDatabase);
            em.connect();



            EntityManager entityManager = javax.persistence.Persistence.createEntityManagerFactory("events.fdbPU").createEntityManager();
            Query query = entityManager.createQuery("SELECT e FROM Events e");
            List<ehgui.Events> list = org.jdesktop.observablecollections.ObservableCollections.observableList(query.getResultList());
            for (ehgui.Events event : list) {
                em.removeEventListener(event.toString(), event);
                em.addEventListener(event.toString(), event);
            }
            createGUI();
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(parent,
                    "There was an error connecting to the Firebird database. Please make sure the information below is correct and the server is up and running.\n\n\n"
                    + "listenHost=" + listenHost + "\nlistenPort=" + listenPort + "\nlistenUser=" + listenUser + "\nlistenPass=" + listenPass + "\nlistenDatabase=" + listenDatabase,
                    "Database error!",
                    JOptionPane.ERROR_MESSAGE);
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        } catch (AWTException ex) {
            System.out.println("There was an error creating the system tray icon:");
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    
    public Connection getConnection() {
        return connection;
    }
    


    /**
     * Creates a parent frame and a system tray icon with a menu.
     *
     * @throws AWTException If there is an error creating the system tray icon.
     */
    private void createGUI() throws AWTException {
        URL file = Thread.currentThread().getContextClassLoader().getResource("images/firebird.png");
        Image image = new ImageIcon(file).getImage();
        parent.setTitle("Firebird Event Handler");
        parent.setIconImage(image);
        SystemTray systray = SystemTray.getSystemTray();
        PopupMenu menu = new PopupMenu();
        MenuItem eventsMenu = new MenuItem("Edit event calls");
        menu.add(eventsMenu);
        eventsMenu.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                parent.setContentPane(new EventEditor());
                parent.pack();
                parent.setVisible(true);
            }
        });
        MenuItem emails = new MenuItem("Edit email notifications");
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
        icon.setImageAutoSize(true);
        systray.add(icon);
    }
}