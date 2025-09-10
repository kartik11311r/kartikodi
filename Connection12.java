package com.giet;

import java.sql.*;
import java.util.Scanner;

public class Connection12 {
    public static final String url = "jdbc:mysql://localhost:3306/jdbc";
    public static final String userName = "root";
    public static final String pwd = "rahul@9861";

    public static void main(String[] args) {
        try {
            // Load driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            Connection con = DriverManager.getConnection(url, userName, pwd);
            System.out.println("Connection established");
            
            Scanner sc = new Scanner(System.in);   
            System.out.print("Enter id: ");
            int id = sc.nextInt();

            // Prepare callable statement
            CallableStatement cst = con.prepareCall("{CALL find(?)}");
            cst.setInt(1, id);

            // Execute stored procedure
            ResultSet rslt = cst.executeQuery();

            boolean found = false;
            while (rslt.next()) {
                found = true;
                System.out.println("ID: " + rslt.getInt("id"));
                System.out.println("Branch: " + rslt.getString("branch"));
                System.out.println("Strength: " + rslt.getInt("strength"));
            }

            if (!found) {
                System.out.println("Result not found for ID: " + id);
            }

            // Close resources
            rslt.close();
            cst.close();
            con.close();
            sc.close();

        } catch (ClassNotFoundException e) {
            System.out.println("MySQL Driver not found: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("SQL Error: " + e.getMessage());
        }
    }
}
















import java.sql.*;
import java.util.Scanner;

public class ConnectionClass {
    public static void main(String[] args) {
        Connection con = null;
        CallableStatement cstmt = null;
        ResultSet rs = null;
        Scanner sc = new Scanner(System.in);

        try {
            // Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish Connection
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/yourDB", "username", "password");
            System.out.println("Connection Established Successfully!");

            // Input ID from user
            System.out.println("Enter id:");
            int id = sc.nextInt();

            // Call stored procedure
            cstmt = con.prepareCall("{CALL collection(?)}");
            cstmt.setInt(1, id);

            rs = cstmt.executeQuery();

            boolean found = false;
            while (rs.next()) {
                found = true;
                System.out.println("id: " + rs.getInt("id"));
                System.out.println("branch: " + rs.getString("branch"));
                System.out.println("strength: " + rs.getInt("strength"));
            }

            if (!found) {
                System.out.println("No records found for id: " + id);
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (cstmt != null) cstmt.close();
                if (con != null) con.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}





package com.giet;
import java.sql.*;
import java.util.Scanner;

public class SqlConnection5 {
    public static void main(String[] args) {
        Connection con = null;
        CallableStatement cst = null;
        ResultSet rslt = null;
        Scanner sc = new Scanner(System.in);

        try {
            // ✅ Load Driver (depends on DB, here for MySQL example)
            Class.forName("com.mysql.cj.jdbc.Driver");

            // ✅ Establish connection
            con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/my_first_db",  // change DB name
                    "root",                            // change username
                    ""                             // change password
            );
   System.out.println("Connection Established Successfully");
     

            System.out.print("Enter Id: ");
            int id = sc.nextInt();

            // ✅ Prepare Callable Statement
            cst = con.prepareCall("{CALL collection(?)}");
            cst.setInt(1, id); // passing id to stored procedure

            // ✅ Execute query
            rslt = cst.executeQuery();

            boolean found = false;
            while (rslt.next()) {
                found = true;
                System.out.println("id: " + rslt.getInt("id"));
                System.out.println("branch: " + rslt.getString("branch"));
                System.out.println("Strength: " + rslt.getInt("strength"));
                System.out.println("---------------------------");
            }

            if (!found) {
                System.out.println("Result Not Found for id: " + id);
            }

        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
        } finally {
            // ✅ Close resources safely
            try {
   
                if (rslt != null) rslt.close();
                if (cst != null) cst.close();
                if (con != null) con.close();
                sc.close();
            } catch (SQLException e) {
                System.out.println("Error closing resources: " + e.getMessage());
            }
        }
    }
}


