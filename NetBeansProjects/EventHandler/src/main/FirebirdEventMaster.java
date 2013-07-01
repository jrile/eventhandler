package main;

import eventhandler.Driver;
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
import java.util.logging.Level;
import java.util.logging.Logger;
import main.FirebirdEvent;





public class FirebirdEventMaster {
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
	
	ArrayList<FirebirdEvent> events = new ArrayList<FirebirdEvent>();
        
        public FirebirdEventMaster() throws SQLException {
                        readConfig("/home/colgado/NetBeansProjects/EventHandler/src/eventhandler/ehconfig");
                        read();
                        SystemTray systray = SystemTray.getSystemTray();
                        Image image = Toolkit.getDefaultToolkit().getImage("EventHandler/src/eventhandler/firebird.jpeg");
                        PopupMenu menu = new PopupMenu();
                        MenuItem item = new MenuItem("Exit");
                        menu.add(item);
                        item.addActionListener(new ActionListener() {
                            @Override
                            public void actionPerformed(ActionEvent e) {
                                System.exit(0);
                            }
                        });
                        
                        
                        TrayIcon icon = new TrayIcon(image,"Firebird Event Listener", menu);
                    try {
                        systray.add(icon);
                    } catch (AWTException ex) {
                        Logger.getLogger(Driver.class.getName()).log(Level.SEVERE, null, ex);
                    }
        }

	private void read() throws SQLException {
		Connection conn = DriverManager
				.getConnection(
						"jdbc:firebirdsql:"+eventHost+"/"+eventPort+":/"+eventDatabase, eventUser, eventPass);
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
				getEmails.setString(1, event_name);
				ResultSet emails = getEmails.executeQuery();
				ArrayList<String> emailList = new ArrayList<String>();
				while (emails.next()) {
					emailList.add(emails.getString(1));
				}
				events.add(new FirebirdEvent(event_name, emailList,
						email_title, email_text, sender));
			}
		} catch (FBSQLException e) {
			// result set is closed, ignore
		
		} finally {
			stmt.close();
			getEmails.close();
		}
		
		listen();

	}
        
        

	private void listen() throws SQLException {
		EventManager em = new FBEventManager();
		em.setHost(listenHost);
		em.setUser(listenUser);
		em.setPassword(listenPass);
		em.setDatabase(listenDatabase);
		em.connect();
		for (FirebirdEvent event : events) {
			em.addEventListener(event.toString(), event);
		}
	}

	public void addEvent(FirebirdEvent event) {
		events.add(event);
	}

	public boolean removeEvent(String eventname) {
		for (FirebirdEvent event : events) {
			if (event.toString().equals(eventname)) {
				return events.remove(event);
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

}
