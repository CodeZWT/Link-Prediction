<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%@ page import = "system.insert.*"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'requerstStudInf.jsp' starting page</title>
    
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
    This is my requerstStudInf JSP page. <br>
     <a href = "HTML/Welcome.html">go to home page</a><br>
    
    <%
		//Enumeration<String> headerNames = request.getHeaderNames();
  		//while( headerNames.hasMoreElements() ){
  		//	out.println("--------------------------");
  		//	String headerName = headerNames.nextElement();
  		//	out.println(headerName + "-->" + request.getHeader(headerName) + "<br>");
  		//}
  		//out.println("<hr/>");
	 %>
	 <%
	 	request.setCharacterEncoding("GBK");
	 	String studName = request.getParameter("studName");
	 	String studID = request.getParameter("studID");
	 	String schoolName = request.getParameter("schoolName");
	  %>
	  
	  <font size="5" face="Verdana">
	  <b>The student information insert is succeed;</b><br><br>
	  StudentName = <%= studName%><br>
	  StudentID = <%= studID %><br>
	  SchoolName = <%= schoolName %><br></br>
	  <%!	
	  	insertStudInf work = new insertStudInf();	
	   %>
	  <%	
	  	work.insert(request.getParameter("studName"), request.getParameter("studID"),request.getParameter("schoolName"));
	   %>
	   <b>The student information insert is succeed;</b>
	   <font size="5" face="Verdana">
	   <blockquote>
	   	if you would like to insert more student information,please chick <a href = "HTML/insert.html" >here</a>.
	   </blockquote>
	   </font>
  </body>
</html>
