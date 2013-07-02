package eventhandler;

import ehgui.EmailEditor;
import ehgui.EventEditor;
import java.awt.AWTException;
import java.awt.Image;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.sql.SQLException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.persistence.EntityManager;
import javax.persistence.Query;
import javax.swing.ImageIcon;

import org.firebirdsql.event.EventManager;
import org.firebirdsql.event.FBEventManager;
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
    private final String listenHost = "localhost";
    private final int listenPort = 3050;
    private final String listenUser = "sysdba";
    private final String listenPass = "masterkey";
    private final String listenDatabase = "C:\\Users\\jrile\\Downloads\\testing.fdb";
    private EventManager em = new FBEventManager();
    
    public final JFrame parent = new JFrame();

    /**
     * Constructs an event master to handle all of the events and listen for
     * them.
     *
     */
    protected FirebirdEventMaster() {

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
                listen(event);
            }
            createGUI();

        } catch (SQLException ex) {
            System.out.println("There was an error connecting to the firebird database.");
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        } catch (AWTException ex) {
            System.out.println("There was an error creating the system tray icon.");
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    /**
     * Creates a parent frame and a system tray icon with a menu.
     *
     * @throws AWTException If there is an error creating the system tray icon.
     */
    private void createGUI() throws AWTException {
        Image image = new ImageIcon("./firebird.png").getImage();
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

    /**
     * Adds an event name to our event manager so we can listen for it on the
     * database.
     *
     * @param event The event itself.
     */
    public void listen(ehgui.Events event) {
        try {
            em.removeEventListener(event.toString(), event);
            em.addEventListener(event.toString(), event);
        } catch (SQLException ex) {
            System.out.println("There was an error connecting to the firebird database.");
            Logger.getLogger(FirebirdEventMaster.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}