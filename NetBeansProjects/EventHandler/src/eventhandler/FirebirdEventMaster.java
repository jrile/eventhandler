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
import java.sql.SQLException;
import java.util.List;
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

    private EventManager em = new FBEventManager();

    protected FirebirdEventMaster() {

        try {
            em.setHost(listenHost);
            em.setUser(listenUser);
            em.setPassword(listenPass);
            em.setDatabase(listenDatabase);
            em.connect();

            EntityManager entityManager = javax.persistence.Persistence.createEntityManagerFactory("events.fdbPU").createEntityManager();
            Query query = entityManager.createQuery("SELECT e FROM Events e");
            List<ehgui.Events> list = java.beans.Beans.isDesignTime() ? java.util.Collections.emptyList() : org.jdesktop.observablecollections.ObservableCollections.observableList(query.getResultList());
            for (ehgui.Events event : list) {
                listen(event);
            }

            createGUI();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    private void createGUI() {
        final JFrame parent = new JFrame();
        parent.setTitle("Firebird Event Handler");
        SystemTray systray = SystemTray.getSystemTray();
        Image image = new ImageIcon("///home/colgado/NetBeansProjects/EventHandler/src/eventhandler/firebird.png").getImage();
        

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
        try {
            systray.add(icon);
        } catch (AWTException ex) {
            ex.printStackTrace();
        }
    }

    
    public void listen(ehgui.Events event) throws SQLException  {
        em.addEventListener(event.toString(), event);
    }
}
