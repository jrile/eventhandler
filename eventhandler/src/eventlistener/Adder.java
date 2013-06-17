package eventlistener;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Adder {

		public static void main(String[] args) throws SQLException {
			Connection conn = DriverManager.getConnection("jdbc:firebirdsql:localhost/3050:/var/lib/firebird/data/testing.fdb", "SYSDBA", "masterkey");                      
			Statement stmt = conn.createStatement();
			for(int i = 0; i < 5; i++)
				stmt.execute("insert into test (a, b) values (900, 200)");
		
}
}
