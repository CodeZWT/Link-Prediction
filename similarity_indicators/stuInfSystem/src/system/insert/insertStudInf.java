package system.insert;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class insertStudInf {
	
	static Connection  con = null;
	static Statement stmt = null;
	public static void init(){
		try{
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/studinf", "root", "2271"); 
			System.out.println("Connection is OK!");
			
			stmt = con.createStatement();
			
			stmt.executeUpdate("INSERT INTO studInf (studName,studID,schoolName) VALUES ('wth0','9120','njust0')");
			
		}catch(Exception e){
			System.out.println("ERROR00 : " + e.getMessage());
		}
	}
	/*
	public static void insert(final String studName,final String studID,final String schoolName){
		try{
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/studInf", "root", "2271"); 
			System.out.println("Connection is OK!");
			
			stmt = con.createStatement();
			
			stmt.executeUpdate(String.format("INSERT INTO studInf (studName,studID,schoolName) VALUES ('%s','%s','%s')",studName,studID,schoolName)) ;
		}catch(Exception e){
			System.out.println("ERROR_INSERT : " + e.getMessage());
		}
	}
	*/
public static void insert(final String studName,final String studID,final String schoolName) {
		
		try{
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/studInf", "root", "2271"); 
			System.out.println("Connection is OK!");
			
			stmt = con.createStatement();
			
			stmt.executeUpdate(String.format("INSERT INTO studInf (studName,studID,schoolName) VALUES ('%s','%s','%s')",studName,studID,schoolName)) ;
		}catch(Exception e){
			System.out.println("ERROR01 : " + e.getMessage());
		}
	}
	public static void main(String[] agrs){
		init();
		insert("wy1","901","nust");
	}
}
