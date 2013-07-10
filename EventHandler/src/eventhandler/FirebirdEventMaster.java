package eventhandler;

import ehgui.EmailEditor;
import ehgui.EventEditor;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileInputStream;
import java.io.FileOutputStream;
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
import javax.persistence.*;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;

public class FirebirdEventMaster {

    public final static JFrame parent = new JFrame();
    private static Properties config = new Properties();
    private static String listenHost, listenUser, listenPass, listenDatabase, eventHost, eventUser, eventPass, eventDatabase, poReportPath;
    private static int listenPort, eventPort;
    private EventManager em = new FBEventManager();
    private Connection connection;
    private static FirebirdEventMaster instance = null;
    private EntityManagerFactory emf;

    /**
     * Method to return the only instance of the Firebird Event Master. If the
     * firebird event master hasn't been initialized yet (program has just
     * started), initialize it. Return the single instance.
     *
     * @return Single instance of the Firebird event master
     */
    public static FirebirdEventMaster getInstance() {
        if (instance == null) {
            try {
                instance = new FirebirdEventMaster();
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(parent,
                        "There was an error connecting to the Firebird database. Please make sure the information below is correct and the server is up and running.\n\n\n"
                        + "listenHost=" + listenHost + "\nlistenPort=" + listenPort + "\nlistenUser=" + listenUser + "\nlistenPass=" + listenPass + "\nlistenDatabase=" + listenDatabase,
                        "Database error!",
                        JOptionPane.ERROR_MESSAGE);
                System.exit(1);
            }
        }
        return instance;
    }

    /**
     * Constructs an event master to handle all of the events and listen for
     * them.
     *
     */
    protected FirebirdEventMaster() throws SQLException {
        config = new Properties();
        try {
            InputStream file = new FileInputStream("CONFIG.properties");
            createGUI();
            config.load(file);
            loadProperties(config);

        } catch (AWTException ex) {
            // If we get here, the system can not create a system tray
            // Program currently is not functional without GUI.
            System.out.println("There was an error creating the system tray icon:");
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
            System.exit(1);

        } catch (IOException ex) {
            // if we get here, there was an error opening the config file. 
            // create a generic default one.
            System.out.println("Properties file not found... creating default one.");
            Properties defaultProps = new Properties();
            defaultProps.setProperty("listenHost", "localhost");
            defaultProps.setProperty("listenPort", "3050");
            defaultProps.setProperty("listenUser", "sysdba");
            defaultProps.setProperty("listenPass", "masterkey");
            defaultProps.setProperty("listenDatabase", "C:\\listen.fdb");
            defaultProps.setProperty("eventHost", "localhost");
            defaultProps.setProperty("eventPort", "3050");
            defaultProps.setProperty("eventUser", "sysdba");
            defaultProps.setProperty("eventPass", "masterkey");
            defaultProps.setProperty("eventDatabase", "C:\\events.fdb");
            defaultProps.setProperty("mail.smtp.host", "localhost");
            defaultProps.setProperty("mail.smtp.port", "25");
            defaultProps.setProperty("poreportpath", "C:\\Program Files (x86)\\Fishbowl\\server\\reports\\Custom\\POReport.jasper");
            try {
                FileOutputStream out = new FileOutputStream("CONFIG.properties");
                defaultProps.store(out, "Default Configuration For Firebird Event Listener\n\n- Make sure paths are escaped if necessary.\n- For the po report path, make sure it points to the .jasper file.");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(parent,
                        "There was an error writing the default configuration file. Proceeding with default values.",
                        "Config file error!",
                        JOptionPane.ERROR_MESSAGE);
            } finally {
                loadProperties(defaultProps);
            }
        }
    }

    /**
     * Loads the configuration properties for the database and mail server. If
     * one or more parameters do not appear in the configuration, they are set
     * to the default value as described in the readme.
     *
     * @param config Properties file that should contain some or all
     * configuration settings.
     * @throws SQLException If there was an error connecting to the "listen"
     * database.
     */
    private void loadProperties(Properties config) throws SQLException {
        listenHost = config.getProperty("listenHost", "localhost");
        listenPort = Integer.parseInt(config.getProperty("listenPort", "3050"));
        listenUser = config.getProperty("listenUser", "sysdba");
        listenPass = config.getProperty("listenPass", "masterkey");
        listenDatabase = config.getProperty("listenDatabase", "C:\\listen.fdb");
        eventHost = config.getProperty("eventHost", "localhost");
        eventPort = Integer.parseInt(config.getProperty("eventPort", "3050"));
        eventUser = config.getProperty("eventUser", "sysdba");
        eventPass = config.getProperty("eventPass", "masterkey");
        eventDatabase = config.getProperty("eventDatabase", "C:\\EVENTS.FDB");
        poReportPath = config.getProperty("poreportpath", "C:\\Program Files (x86)\\Fishbowl\\server\\reports\\Custom\\POReport.jasper");
        if (Driver.DEBUGGING) {
            System.out.println("Config file loaded:\nlistenHost=" + listenHost + "\nlistenPort=" + listenPort + "\nlistenUser=" + listenUser + "\nlistenPass=" + listenPass + "\nlistenDatabase=" + listenDatabase);
            System.out.println("\neventHost=" + eventHost + "\neventPort=" + eventPort + "\neventUser=" + eventUser + "\neventPass=" + eventPass + "\neventDatabase=" + eventDatabase
                    + "\npoReportPath=" + poReportPath + "\nmail.smtp.host=" + config.getProperty("mail.smtp.host") + "\nmail.smtp.port=" + config.getProperty("mail.smtp.port"));
        }
        connection = DriverManager.getConnection("jdbc:firebirdsql:" + listenHost + "/" + listenPort + ":" + listenDatabase, listenUser, listenPass);
        connection.setAutoCommit(false);
        em.setHost(listenHost);
        em.setPort(listenPort);
        em.setUser(listenUser);
        em.setPassword(listenPass);
        em.setDatabase(listenDatabase);
        em.connect();

        Map properties = new HashMap();
        properties.put("javax.persistence.jdbc.url", "jdbc:firebirdsql:" + eventHost + "/" + eventPort + ":" + eventDatabase);
        properties.put("javax.persistence.jdbc.user", eventUser);
        properties.put("javax.persistence.jdbc.password", eventPass);
        properties.put("javax.persistence.jdbc.driver", "org.firebirdsql.jdbc.FBDriver");
        emf = Persistence.createEntityManagerFactory("events.fdbPU", properties);
        listen();
    }

    /**
     * Grabs a new entity manager from the entity manager factory. If there was
     * an error connecting to the event database, displays an error message and
     * quits.
     *
     * @return A newly created EntityManager
     */
    public EntityManager getEntityManager() {
        EntityManager temp = null;
        try {
            temp = emf.createEntityManager();
        } catch (PersistenceException e) {
            JOptionPane.showMessageDialog(parent,
                    "There was an error connecting to the Firebird event database! Please make sure all settings are correct.",
                    "Database error!",
                    JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }
        return temp;
    }

    /**
     *
     * @return The configuration properties file.
     */
    public Properties getConfig() {
        return config;
    }

    /**
     * Selects each event from the events database, iterates through them and
     * adds an event listener for each. If there was an error connecting to the
     * event database, displays an error message and quits.
     */
    public void listen() {
        Query query = getEntityManager().createQuery("SELECT e FROM Events e");
        List<ehgui.Events> list = org.jdesktop.observablecollections.ObservableCollections.observableList(query.getResultList());
        for (ehgui.Events event : list) {
            try {
                em.removeEventListener(event.toString(), event);
                em.addEventListener(event.toString(), event);
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(parent,
                        "There was an error connecting to the Firebird event database! Please make sure all settings are correct.",
                        "Database error!",
                        JOptionPane.ERROR_MESSAGE);
                System.exit(1);
            }
        }
    }

    /**
     * Gets the connection for the "listen" database.
     *
     * @return "listen" database connection.
     */
    public Connection getConnection() {
        return connection;
    }

    public String getPoReportPath() {
        return poReportPath;
    }

    /**
     * Creates a parent frame and a system tray icon with a menu.
     *
     * @throws AWTException If there is an error creating the system tray icon.
     */
    private void createGUI() throws AWTException {
        URL file = Thread.currentThread().getContextClassLoader().getResource("images/firebird.png");
        Image image = new ImageIcon(file).getImage();
        parent.setAlwaysOnTop(true);
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