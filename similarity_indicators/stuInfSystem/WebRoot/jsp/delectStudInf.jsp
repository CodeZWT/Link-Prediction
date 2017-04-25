<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%@ page import = " java.sql.* " %>
<%@ page import = "system.delete.*" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'delectStudInf.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
    This is my delectStduInf JSP page. <br>
    <a href = "HTML/Welcome.html">go to home page</a><br>
    <font size="5" face="Verdana">
    <%
   		String studID = request.getParameter("studID");
     %>
     <%= studID %>
     <% 
     	deleteStudInf delework = new deleteStudInf();
     %>
     <% 
     	delework.delete(request.getParameter("studID"));
     %>
     	<blockquote>
 		   	The student whose ID equal  <%= studID %> has been delete!
    	</blockquote>
    		if you want to delect more stduent information you should chick <a href = "HTML/delete.html">here</a><br> 
     		if you want to see the student information list please chick <a href = "JSP/readStudInf.jsp">here</a>
     </font>
  </body>
</html>
