from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""
<html>
<title>TCP/IP PROTOCOL</title>
<body>
<table border="2" cellspacing="15" cellpadding="6" bgcolor="yellow">
<caption>TCP/IP PROTOCOL SUITE</caption>
<tr>
<th>S.No</th>
<th>LAYER</th>
<th>PROTOCOLS</th>
</tr> <tr>
<th>1</th>
<td>Application Layer</td>
<td>HTTP,FTP,DNS,Telnet,SSH</td>
</tr>
<tr>
<td>2</td>
<td>Transport Layer</td>
<td>TCP,UDP</td>
</tr>
<tr>
<td>3</td>
<td>Internet Layer</td>
<td>ICMP,IGMP,ARP,IPv4/IPv6</td>
</tr>
<tr>
<td>4</td>
<td>Network Access Layer</td>
<td>MAC/Ethernet,FDDI,Frame Relay</td>
</tr>
</body>
</html>
"""
class myhandler (BaseHTTPRequestHandler):
     def do_GET(self):
        print("request received") 
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()