package system.delete;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class deleteStudInf {
	static Connection  con = null;
	static Statement stmt = null;
	public static void init(){
		try{
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/studinf", "root", "2271"); 
			System.out.println("Connection is OK!");
			
			stmt = con.createStatement();
			
			//stmt.executeUpdate("INSERT INTO studInf (studName,studID,schoolName) VALUES ('wth0','9120','njust0')");
			stmt.executeUpdate("DELETE from studinf WHERE (studID = '')");
		}catch(Exception e){
			System.out.println("ERROR00 : " + e.getMessage());
		}
	}
	public static void delete(final String studID){
		try{
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/studinf", "root", "2271"); 
			System.out.println("Connection is OK!");
			
			stmt = con.createStatement();
			
			stmt.executeUpdate(String.format("DELETE from studinf WHERE (studID = '%s')", studID));
			System.out.println("Delection is OK!");
		}catch(Exception e){
			System.out.println("ERROR00 : " + e.getMessage());
		}
	}
	public static void main(String[] args){
		//init();
		delete("914");
	}
}
