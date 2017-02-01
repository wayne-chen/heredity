# requires PyQt5 installed
#
all: errordlg.py startdlg.py parentsdlg.py traitchooserdlg.py mainwindow.py

errordlg.py : errordlg.ui
	pyuic5 errordlg.ui -o errordlg.py 

startdlg.py : startdlg.ui
	pyuic5 startdlg.ui -o startdlg.py 

parentsdlg.py : parentsdlg.ui
	pyuic5 parentsdlg.ui -o parentsdlg.py 

traitchooserdlg.py : traitchooserdlg.ui
	pyuic5 traitchooserdlg.ui -o traitchooserdlg.py 

mainwindow.py : mainwindow.ui
	pyuic5 mainwindow.ui -o mainwindow.py 

		
clean:
	rm errordlg.py
	rm startdlg.py
	rm parentsdlg.py
	rm traitchooserdlg.py
	rm mainwindow.py
