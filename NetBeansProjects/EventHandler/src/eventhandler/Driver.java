package eventhandler;

import java.awt.AWTException;
import java.awt.Image;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import main.FirebirdEventMaster;


public class Driver {

	/**
	 * @param args
	 *            Unused.
	 * @throws InterruptedException
	 *             If the user interrupts program, simply print stack and quit.
	 * @throws SQLException
	 *             If there is an error using Firebird.
	 * @throws FileNotFoundException
	 */
	public static void main(String[] args) throws InterruptedException,
			SQLException, FileNotFoundException {
        
		FirebirdEventMaster fem = FirebirdEventMaster.getInstance();
                   fem.toString();
                
                
                    
                    while(true) { }

	}
}